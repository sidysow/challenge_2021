#%%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from download import download
import statsmodels.api as sm


#%%
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv "
path_target = "./Bike_Totems_Montpellier.csv"
download(url, path_target, replace=True)  

#%%
data_dfraw = pd.read_csv("Bike_Totems_Montpellier.csv")

#%%
data_dfraw=data_dfraw.rename(columns = {'Heure / Time': 'HT'})
#%%
data_dfraw1=data_dfraw[(data_dfraw.HT > '00:00') & (data_dfraw.HT< '09:01')].tail(30)


# %%
data_df= data_dfraw1.drop(['Remarque','Unnamed: 4'], inplace=False, axis=1)


# %%
data_df = data_df.dropna()

#%%

standard_time  = pd.to_datetime(data_df['Date'] +
                               ' ' + data_df['HT'],
                               format='%d/%m/%Y %H:%M:%S')

# Where d = day, m=month, Y=year, H=hour, M=minutes
standard_time 


#%%

# create correct timing format in the dataframe
#%%
data_df['DateTime'] = standard_time


#%%
# remove useles columns
del data_df['Date']
del data_df['HT']


# %%

data_ts = data_df.set_index(['DateTime'])


# %%

#V1J = Vélos depuis le 1er janvier / Grand total
#VCJ = Vélos ce jour / Today's total
#%%
data_ts.columns = ['V1J','VCJ']
del data_ts['V1J']
data_ts.describe()








# %%

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    #rolmean = pd.rolling_mean(timeseries, window=12)
    rolmean = pd.Series(timeseries).rolling(window=12).mean()

    #rolstd = pd.rolling_std(timeseries, window=12)#Plot rolling statistics:
    rolstd = pd.Series(timeseries).rolling(window=12).std()

    plt.plot(timeseries, color='blue',label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

# %%
test_stationarity(data_ts['VCJ'])

# %%
from statsmodels.tsa.arima_model import ARIMA
#%%
fig = plt.figure(figsize=(10,8))
model = ARIMA(data_ts['VCJ'], order=(0,1,2)) 
ax = plt.gca()
results = model.fit()
plt.plot(data_ts['VCJ'], color='green')
plt.plot(results.fittedvalues, color='red')
ax.legend(['bike', 'Forecast'])
#%%

print(results)
# %%
fig = plt.figure(figsize=(20,8))
num_points = len(data_ts['VCJ'])
x = results.predict(start=(1350), end=(1376), dynamic=False)

plt.plot(data_ts['VCJ'][:1377])
plt.plot(x, color='r')
# %%
#%%







