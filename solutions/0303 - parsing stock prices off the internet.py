import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np

def graph_data(stock):
    print('Currently pulling:', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for each_line in split_source:
        split_line = each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter = ',',
                                                          unpack = True,
                                                          converters={0: bytespdate2num('%Y%m%d')})



stock = input('Stock to plot: ')
graph_data(stock)
