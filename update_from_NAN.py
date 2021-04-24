# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:17:08 2021

@author: Raza_Jutt
"""
import time
import csv
import pandas as pd
import os
from blockchain import blockexplorer

def funtion(file,n):
    with open(file, 'a') as g:
        writer = csv.writer(g)
        pre_block = ""
        #new_row = 0, 0, 0 ,0 ,0
        #writer.writerow(new_row)
        for i in range(n,n+5000):
            print(i)
            try :
                block = blockexplorer.get_block(str(i))
                new_row = i, block.hash, str(block.transactions) , pre_block ,block.nonce
                writer.writerow(new_row)
                pre_block = str(block.hash)
            except:
                print("Stuck >>>>>>>  waiting")
                time.sleep(60)
                i = i-1
            
data = pd.read_csv('C:/Users/Raza Jutt/Desktop/3.csv')
data = data.dropna()
#print(data)
data.to_csv("up.csv",header=["Height", "Hash", "Transcations","Previous_Hash","Nonce"], index=False)
#os.remove('BitCoin_Chain.csv')
# 679487


#funtion('58986-60000.csv',6585)