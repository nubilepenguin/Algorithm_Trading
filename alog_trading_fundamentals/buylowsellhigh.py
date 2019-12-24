# loading the class data from the package pandas_datareader
from pandas_datareader import data
# First day
start_date = '2014-01-01'
# Last day
end_date = '2018-01-01'
# Call the function DataReader from class data
goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)
print(goog_data.head())
import pandas as pd
import numpy as np

goog_data_singal = pd.DataFrame(index=goog_data.index)
goog_data_singal['price'] = goog_data['Adj Close']
goog_data_singal['daily_difference'] = goog_data_singal['price'].diff()
goog_data_singal['signal'] = 0.0
goog_data_singal['signal'] = np.where(goog_data_singal['daily_difference'][:] > 0, 1.0, 0.0)
goog_data_singal['positions'] = goog_data_singal['signal'].diff()

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'serif'
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
goog_data_singal['price'].plot(ax=ax1, color='r', lw=2.0)
ax1.plot(goog_data_singal.loc[goog_data_singal.positions==1.0].index,
         goog_data_singal.price[goog_data_singal.positions==1.0],
         '^', markersize=5, color='g')
ax1.plot(goog_data_singal.loc[goog_data_singal.positions == -1.0].index,
         goog_data_singal.price[goog_data_singal.positions == -1.0],
         'v', markersize=5, color='b')
plt.show()

# Set the initial capital
initial_capital = float(1000.0)
positions = pd.DataFrame(index=goog_data_singal.index).fillna(0.0)
portfolio = pd.DataFrame(index=goog_data_singal.index).fillna(0.0)
positions['GOOG'] = goog_data_singal['signal']
portfolio['positions'] = (positions.multiply(goog_data_singal['price'],
                                            axis=0))
portfolio['cash'] = initial_capital - (positions.diff().multiply(goog_data_singal['price'], axis=0)).cumsum()
portfolio['total'] = portfolio['positions'] + portfolio['cash']
portfolio.plot()
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')
portfolio['total'].plot(ax=ax1, lw=2.)
ax1.plot(portfolio.loc[goog_data_singal.positions == 1.0].index,portfolio.total[goog_data_singal.positions == 1.0],'^', markersize=10, color='m')
ax1.plot(portfolio.loc[goog_data_singal.positions == -1.0].index,portfolio.total[goog_data_singal.positions == -1.0],'v', markersize=10, color='k')
plt.show()
