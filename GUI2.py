import sys
import os
from tkinter import *
import datetime

now = datetime.datetime.now()

def titan():
    os.system('python RNN2.py')
def ab():
    os.system('python RNN20.py')
def Inox():
    os.system('python RNN200.py')

window= Tk()
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("{0}x{1}+0+0".format(w,h))
window.title('Stock Prediction using ARMA')
container1 = Frame(window, bg = "#7BABEB")
container1.pack( fill = "both")
Label1 = Label(container1, text="Precision Stocks", font=("Times", "26","bold"), bg="#7BABEB" , fg="#FCFCFE" ,width=w)
Label1.pack(fill='x',anchor="center")
container = Frame(window, bg = "#EEF3F7")
container.pack(expand = True, fill = "both")
Label(container, text="Date Today", font=("Times", "16","bold"),bg = "#EEF3F7",fg="#737373").pack( fill='x')
Label(container, text=(now.strftime("%Y-%m-%d")), font=("Times", "16","bold"),bg = "#EEF3F7",fg="#737373").pack(fill='x')
Label(container, text="Click the Company button for Predicitng Price and Sentiment Analysis",font=("Times", "16","bold"),bg = "#EEF3F7",fg="#737373").pack(fill='x')
Predict_Titan = Button(container,text="Titan", command=titan,fg="black",bg ="#f7e7bb", font=("Times", "16","bold")).pack(fill='x')
Predict_AB = Button(container,text="Axis Bank", command=ab,fg="black",bg ="#f7e7bb", font=("Times", "16","bold")).pack(fill='x')
Predict_Mahindra = Button(container,text="Inox Lesiure", command=Inox,fg="black",bg ="#f7e7bb", font=("Times", "16","bold")).pack(fill='x')

window.mainloop()
