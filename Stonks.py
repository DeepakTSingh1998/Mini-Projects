import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
# Ticker
Ticker_Input = input('What is the Ticker?\n')

# Period 
Period_Input = input('How long is the historical period?\n')


# Input new date
# Input New Date
New_Date = input('What is the projected futre date you want to look at?\n'+
                 'Please use YYYY-MM-DD\n')


# Input Data
Stock = yf.Ticker(Ticker_Input) #Retrieve Stock
Hist = Stock.history(period = Period_Input) # Retrieve Historical 

# Time Series Data Clean up#
Date = Hist.index 
Start_date = str(Date[0])[0:10] #Start Date of Time range
End_date = str(Date[-1])[0:10] #End Date of Time range
Date_index = pd.date_range(Start_date,End_date)

# Create new Dataframe containing 
Stock_Close_Values = ['Free' for x in range(len(Date_index))]
Stock_Index_Close_Values = pd.DataFrame(
    {'Close':Stock_Close_Values},
    index=Date_index)


# Fills in missing Day Close Data
counter = 0
for row in range(0,len(Stock_Index_Close_Values)):
    if str(Stock_Index_Close_Values.index[row])[0:10] == str(Date[counter])[0:10]:
        Stock_Index_Close_Values['Close'][row] = Hist['Close'][counter]
        counter += 1
    else:
        Stock_Index_Close_Values['Close'][row] = Hist['Close'][counter]
        

Stock_Index_Close_Values['Numerical Index'] = range(0,len(Stock_Index_Close_Values))

# Linear Regression
X = Stock_Index_Close_Values['Numerical Index'].reset_index()
del X['index']
Y = Stock_Index_Close_Values['Close'].reset_index()
del Y['index']

reg = LinearRegression().fit(X,Y) 
intercept = reg.intercept_[0]
slope = reg.coef_[0]

# Y_hat function
def Y_hat(X_Values):
    Result = []
    Result = intercept + slope * X_Values
    return Result

# Compute Future date values
Future_Index = pd.date_range(Start_date,New_Date)
Future_Range = range(0,len(Future_Index))
Future_Yhat = Y_hat(Future_Range)
df_Future = pd.DataFrame({'Close':Future_Yhat},index = Future_Index)



# Standardize the data for plotting
def Standardize(df_Y1,df_Y2):
    '''
    df_Y1: Original Stock Data Close prices
    df_Y2: Linaer Regression Data Close prices
    '''
    df_Y_Org = []
    for i in range(0,len(df_Y2)):
        if i >= len(df_Y1):
            df_Y_Org.append(np.nan)
        else:
            df_Y_Org.append(df_Y1['Close'][i])
            
    return df_Y_Org

Y_new = Standardize(Y,Future_Yhat)
df_Y = pd.DataFrame({'Close':Y_new},index=Future_Index)

# Final Plot
Y_plot = Y_hat(X)
plt.plot(df_Y,color='blue')
plt.plot(df_Future,'--',linewidth=2,color='k')
plt.grid(True)
plt.title(Ticker_Input+' Project Price')
plt.ylabel('Price ($)')
plt.xlabel('Date')
plt.gcf().autofmt_xdate()
plt.xlim([df_Y.index[0],df_Y.index[-1]])

# Print Statements
print('The latest close price on '+Ticker_Input+' is $'+str(round(Y['Close'][len(Y)-1],2)))
print('The project price on the '+New_Date+' is $'+str(round(Future_Yhat[-1],2)))
print('The Linear Regression Model has a score of '+str(reg.score(X,Y)))
Percentage_Increase = ((Future_Yhat[-1]-Y['Close'][len(Y)-1])/abs(Y['Close'][len(Y)-1]))*100
print('That is a Percentage Increase of '+str(round(Percentage_Increase,2))+'%')

























