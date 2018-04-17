import sys
import os
import tkinter as tk


def StartTask():
    os.system('python GUI2.py')

def Tutorial():
    os.system('E:\Movies\The.Hitmans.Bodyguard.2017.HDRip.XviD.AC3-EVO\sample.avi')

root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(w,h))
root.title('Stock Prediction using ARMA')
container = tk.Frame(root, bg = "#7BABEB")
container.pack( fill = "both")
Label1 = tk.Label(container, text="Introduction To Precision Stocks", font=("Times", "26","bold"), bg="#7BABEB" , fg="#FCFCFE" ,width=w)
Label1.pack(fill='x',anchor="center")
container1 = tk.Frame(root, bg = "#EEF3F7")
container1.pack(expand = True, fill = "both")
Label2 = tk.Label(container1, text="About the app:", font=("Times", "16","bold"), bg="#EEF3F7" , fg="#737373", anchor='w')
Label2.pack(fill='x')
root.update()
width1 = container.winfo_width()
Label3 = tk.Label(container1, text="The application is stock price prediction tool which uses RNN (Recurrent Neural Network) and ARMA (Autoregressive – moving - average) to predict a price of the stock of the next day. The application also features the sentiment analysis on the company based on the tweets on the company.The sentiment is a important indicator as to where the stock price will be heading.", font=("Times", "14"), bg="#EEF3F7" , fg="#a6a6a6", wraplength=width1,justify=tk.CENTER)
Label3.pack(fill='x')
Label5 = tk.Label(container1, text="How to use:", font=("Times", "16","bold"), bg="#EEF3F7" , fg="#737373", anchor='w')
Label5.pack(fill='x')
Label4 = tk.Label(container1, text="The application is stock price prediction tool which uses RNN (Recurrent Neural Network) and ARMA (Autoregressive – moving - average) to predict a price of the stock of the next day. The application also features the sentiment analysis on the company based on the tweets on the company.The sentiment is a important indicator as to where the stock price will be heading.", font=("Times", "14"), bg="#EEF3F7" , fg="#a6a6a6", wraplength=width1,justify=tk.CENTER)
Label4.pack(fill='x')
Tutor = tk.Button(container1, text ="Tutorial Video",font=("Times", "16","bold"), command=Tutorial, bg ="#f7e7bb", fg="black", relief='groove' ,width='30' )
Tutor.pack()
Label6 = tk.Label(container1, text="Terms and Condition:", font=("Times", "16","bold"), bg="#EEF3F7" , fg="#737373", anchor='w')
Label6.pack(fill='x')
Label7 = tk.Label(container1, text="The application is stock price prediction tool which uses RNN (Recurrent Neural Network) and ARMA (Autoregressive – moving - average) to predict a price of the stock of the next day. The application also features the sentiment analysis on the company based on the tweets on the company.The sentiment is a important indicator as to where the stock price will be heading.", font=("Times", "14"), bg="#EEF3F7" , fg="#a6a6a6", wraplength=width1,justify=tk.CENTER)
Label7.pack(fill='x')
Tutor.update()
StartButton = tk.Button(container1, text ="Get Started", font=("Times", "16","bold"),command=StartTask, bg ="#f7e7bb", fg="black", relief='groove' , width='30')
StartButton.pack()

root.mainloop()
