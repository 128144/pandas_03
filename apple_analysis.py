# -*- coding:utf -*-

import pandas as pd

def quarter_volume():
    date = pd.read_csv('apple.csv', header=0, index_col='Date',parse_dates=True)
    df = date.loc[:,['Volume']]
    idx = pd.date_range(start='20090101',end='20161231')
    df = df.reindex(idx, fill_value=0)
    date_volume = df.resample('Q').sum()
    
    ranking = sorted(date_volume['Volume'])
    second_volume = ranking[-2]
    print(second_volume)
    return second_volume
    

if __name__=='__main__':
    quarter_volume()
    
    
    


