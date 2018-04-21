import quandl
import pandas as pd
import csv
print("Downloading Latest Stock Prices....")
quandl.ApiConfig.api_key = "xL64zZWuQWUzVXjvxCdu"
mydata = quandl.get("NSE/AXISBANK", start_date="2015-01-01", )
dataframe = pd.DataFrame(mydata, columns=['High'])
dataframe.to_csv("AB/AB.csv")
new = dataframe.tail(25)
new.to_csv("AB/AB-Regression.csv")
# i = 1
# with open('Titan/Titan.csv','rt') as csvinput:
#     with open('Titan/Titan-Regression-1.csv', 'wt') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator='\n')
#         reader = csv.reader(csvinput)
#         all = []
#         row = next(reader)
#         for row in reader:
#             row.append(i)
#             i += 1
#             all.append(row)
#
#         writer.writerows(all)
df2 = pd.read_csv("AB/AB-Regression.csv")
df2.to_csv('AB/AB-Regression.csv')
print("Downloaded latest Stock Prices...")
