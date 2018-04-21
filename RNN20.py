#on 'k day input, model predicts 'k+1' day output
#Imprting preprocessing libraries
import sys
import os
from tkinter import *
from sklearn import linear_model
import csv
import numpy as np
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from textblob import TextBlob


training_set=pd.read_csv("AB\AB.csv")   #reading csv file
training_set.head()			   #print first five rows

training_set1=training_set.iloc[:,1:2] 	   #selecting the second column
training_set1.head()			   #print first five rows
training_set1=training_set1.values	   #converting to 2d array
training_set1				   #print the whole data

sc = MinMaxScaler()			   #scaling using normalisation
training_set1 = sc.fit_transform(training_set1)

xtrain=training_set1[700:794]		   #input values of rows [2600-2694]
ytrain=training_set1[700:794]		   #input values of rows [2600-2694]

today=pd.DataFrame(xtrain[0:5])		   #taking first file elements of the row from xtrain
tomorrow=pd.DataFrame(ytrain[0:5])         #taking first file elements of the row from ytrain
ex= pd.concat([today,tomorrow],axis=1)	   #concat two columns
ex.columns=(['today','tomorrow'])

# Reshaping into required shape for Keras
xtrain = np.reshape(xtrain, (94, 1, 1))

#importing keras and its packages

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM


regressor=Sequential()			#initialize the RNN

regressor.add(LSTM(units=4,activation='sigmoid',input_shape=(None,1)))			#adding input layer and the LSTM layer

regressor.add(Dense(units=1))		#ading output layers

regressor.compile(optimizer='adam',loss='mean_squared_error') 		#compiling the RNN

regressor.fit(xtrain,ytrain,batch_size=32,epochs=2700)		#fitting the RNN to the training set




# Reading CSV file into test set
training_set.head()
test_set = training_set.tail(25)
test_set.head()


real_stock_price = test_set.iloc[:,1:2]		#selecting the second column

real_stock_price = real_stock_price.values	#converting to 2D array

#getting the predicted  value via Neural Networks
inputs = real_stock_price
inputs = sc.transform(inputs)
inputs = np.reshape(inputs, (25, 1, 1)) #input no of days to predict , for eg. here it is 8
predicted_stock_price = regressor.predict(inputs)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# plt.plot(real_stock_price, color = 'red', label = 'Real Stock Price')
# plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Stock Price')
# plt.title('Stock Price Prediction')
# plt.xlabel('Days')
# plt.ylabel('Stock Price')
# plt.legend()
# plt.show()


#ARMA
dates = []
prices = []

def get_data(filename):
	with open(filename) as csvfile:
		csvFileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		next(csvFileReader) #skipping column names
		for row in csvFileReader:
				dates.append(int(row[0]))
				prices.append(float(row[2]))
	return

def show_plot(dates,prices):
	linear_mod = linear_model.LinearRegression()
	dates = np.reshape(dates,(len(dates),1)) # converting to matrix of n X 1
	prices = np.reshape(prices,(len(prices),1))
	linear_mod.fit(dates,prices) #fitting the data points in the model
	# plt.scatter(dates,prices,color='yellow') #plotting the initial datapoints
	# plt.plot(dates,linear_mod.predict(dates),color='blue',linewidth=3) #plotting the line made by linear regression
	# plt.show()
	return

def predict_price(dates,prices,x):
	linear_mod = linear_model.LinearRegression() #defining the linear regression model
	dates = np.reshape(dates,(len(dates),1)) # converting to matrix of n X 1
	prices = np.reshape(prices,(len(prices),1))
	linear_mod.fit(dates,prices) #fitting the data points in the model
	predicted_price =linear_mod.predict(x)
	return predicted_price[0][0],linear_mod.coef_[0][0] ,linear_mod.intercept_[0]

get_data("AB\AB-Regression.csv") # calling get_data method by passing the csv file to it



#image of the plot will be generated. Save it if you want and then Close it to continue the execution of the below code.

predicted_price, coefficient, constant = predict_price(dates,prices,26)

#NLP
file = open("AB/AxisBank_tweets.txt","r");
t = file.read();
bobo = TextBlob(t)

if bobo.sentiment.polarity == -1:
    Message=" Highly neagtive , not advisable to invest!!"
elif bobo.sentiment.polarity >-1.0 and bobo.sentiment.polarity<-0.5 :
    Message= " Neagtive , not advisable to invest"
elif bobo.sentiment.polarity >-0.5 and bobo.sentiment.polarity<0.0 :
    Message= " Slightly Negative,  invest with precautionary measures"
elif bobo.sentiment.polarity == 0:
	    Message= " Neutral outlook , invest with precautionary measures"
elif bobo.sentiment.polarity > 0 and bobo.sentiment.polarity<=0.5 :
    Message= " Slightly Positive, invest with precautionary measures"
elif bobo.sentiment.polarity >0.0 and bobo.sentiment.polarity< 1.0 :
    Message=" Positive outlook, safe investment option"
else:
    Message=" Highly Positive, excellent for investing!"

def updater():
    os.system('python Tweet_Dumper0.py')
    os.system('python Stock_Dumper0.py')

#
#printing to GUI label
root = Tk()
w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
# root.geometry("{0}x{1}+0+0".format(w,h))
root.title("AxisBank Stock Price Prediction and Sentiment Analysis")
container1 = Frame(root, bg = "#7BABEB")
container1.pack( fill = "both")
container = Frame(root, bg = "#EEF3F7")
container.pack(expand = True, fill = "both")
PP =((predicted_stock_price[24])+(predicted_price))/2
Label(container, text="Tomorrow's Predicted High Price for the Axis Bank stock in INR",font=("Times", "15","bold"),bg = "#EEF3F7",fg="#737373").pack(fill='x')
if(PP>real_stock_price[24]):
	Label(container, text=PP, font=("Times", "15","bold"), fg="green",bg = "#EEF3F7").pack(fill='x')
else:
	Label(container, text=PP, font=("Times", "15","bold"), fg="red",bg = "#EEF3F7" ).pack(fill='x')


f = Figure(figsize=(10,5), dpi=100)
a = f.add_subplot(111)
a.plot(real_stock_price, color = 'red', label = 'Real Stock Price')
a.plot(predicted_stock_price, color = 'blue', label = 'Predicted Stock Price')
# a.title('Stock Price Prediction')
a.set_xlabel('Days')
a.set_ylabel('Stock Price')
a.legend()
canvas = FigureCanvasTkAgg(f, container)
canvas.draw()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
# toolbar = NavigationToolbar2TkAgg(canvas, container)
# toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

Label(container, text="Company Sentiment Analysis",font=("Times", "15","bold"),bg = "#EEF3F7",fg="#737373").pack(fill='x')
Label(container, text="Sentiment Score", font=("Times", "15","bold"),bg = "#EEF3F7",fg="#737373").pack(fill='x')
if(bobo.sentiment.polarity > 0 ):
	Label(container, text=(bobo.sentiment.polarity), font=("Times", "15","bold"),fg = "green",bg = "#EEF3F7").pack(fill='x')
else:
	Label(container, text=(bobo.sentiment.polarity), font=("Times", "15","bold"),fg = "red",bg = "#EEF3F7").pack(fill='x')

Label(container, text=(Message),bg = "#EEF3F7",fg="#737373",font=("Times", "15","bold")).pack(fill='x')
Predict_Titan = Button(container,text="Update Tweets and Stock Value's Database", command=updater,fg="black",bg ="#FFC300",font=("Times", "15","bold")).pack(fill='x')
mainloop()
