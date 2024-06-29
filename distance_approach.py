import numpy as np
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint
from statsmodels.regression.rolling import RollingOLS
import math

def distance_approach(stocks, start_date,end_date, n=1, money=0):
    df=yf.download(stocks, start=start_date, end=end_date)['Adj Close']
    df.dropna(axis=1, inplace=True)
    
    max_min={}
    for column in df:
        max_min[column]=[max(df[column],default=0),min(df[column],default=0)]
        df[column]=((df[column]-min(df[column],default=0))/(max(df[column],default=0)-min(df[column],default=0)))
    
    
    distances=[]
    covered=[]
    for index, row in df.iterrows():
        for column1 in df:
            for column2 in df:
                if column1!=column2 and (([column1,column2] not in covered) and ([column2,column1] not in covered)):
                    covered.append([column1,column2])
                    sum=0
                    for index, row in df.iterrows():
                        sum+=(row[column1]-row[column2])**2
                    distances.append([sum,column1,column2])
    
    
    pairs=[]
    distances.sort()
    
    i=0
    for i in range(n):
        if(i<len(distances)):
            pairs.append([distances[i][1],distances[i][2]])
    print(pairs)
    for s in pairs:
        s1=df[s[0]]
        s2=df[s[1]]
        spread=s2-s1
        
        sigma_sq=0
        for x in spread:
            sigma_sq+=(x-spread.mean())**2
        sigma_sq=(sigma_sq)/(len(spread)-1)
        volatility=math.sqrt(sigma_sq)
    
        max1=max_min[s[0]][0]
        min1=max_min[s[0]][1]
        max2=max_min[s[1]][0]
        min2=max_min[s[1]][1]
        
        position=1
        count_s1=0
        count_s2=0
        
        for index in range(len(spread)):
            if spread.iloc[index]>spread.mean()+volatility and position==1:
                money=money+((s2.iloc[index])*(max2 - min2) + min2) - (((s1.iloc[index])*(max1 - min1)) + min1)
                count_s1+=1
                count_s2-=1
                position=0
            elif spread.iloc[index]<spread.mean()-volatility and position==0:
                money=money+((s2.iloc[index])*(max2 - min2) + min2) + (((s1.iloc[index])*(max1 - min1)) + min1)
                count_s1-=1
                count_s2+=1
                position=1
        
        money=money + ((count_s2)*((s2.iloc[-1])*(max2 - min2) + min2)) + ((count_s1)*(((s1.iloc[index])*(max1 - min1)) + min1))
    return money
