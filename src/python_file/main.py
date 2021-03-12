import requests
import sys
import json
import datetime
import logging
import pymysql
import pandas as pd
from collections import defaultdict
import re





class Security:
    exchange=dict()
    exc_cnts=1
    def __init__(self,stock:dict,cursor):
        self.stock=stock
        self.cursor=cursor



    @staticmethod
    def update_exchange(cursor,value:str):
       query="""
       INSERT INTO exchange(name) VALUES (%s)"""
       cursor.execute(query,(value))


    @classmethod
    def from_list(cls,emp:dict,cursor):
        exc_name=emp['exchange']
        if exc_name not in cls.exchange:
            cls.exchange[exc_name]=cls.exc_cnts
            cls.update_exchange(cursor,exc_name)
            cls.exc_cnts+=1

        return cls(emp,cursor)





def merge(path1,path2):
    try:
        data1=pd.read_csv(path1,sep=',',header=0)
        data2=pd.read_csv(path2,sep=',',header=0)
        merged=pd.concat([data1,data2])
    except:
        logging.error("Can't merge the data")
        sys.exit(1)
    return merged.iloc[:10,:]




def main(active_path,delisted_path):
    host="127.0.0.1"
    port=3306
    user="root"
    password="1234"
    database="finance"
    charset="utf8"

    try:
        conn=pymysql.connect(host=host,port=port,user=user,password=password,database=database,charset=charset)
        cursor=conn.cursor()

    except:
        logging.error("Connection to RDS has failed.")


    lines=merge(active_path,delisted_path)
    for line in lines.iterrows():
        if line[1]['assetType']=="ETF":
            continue
        row=line[1][['symbol','name','exchange','status']].to_dict()
        temp=Security.from_list(row,cursor)

    conn.commit()
    cursor.close()





if __name__=="__main__":
    active_path='/home/david/Documents/finance/data/listing_status.csv'
    delisted_path='/home/david/Documents/finance/data/delisted_companies.csv'
    main(active_path,delisted_path)






    # active_list='/home/david/Documents/finance/data/listing_status.csv'
    # delisted_list='/home/david/Documents/finanace/data/delisted_companies.csv'
    # base_url='http://www.alpahvantage.co/query?'
    # key='YIXOQOKYILQ0AOMZ'
    # Security().getData()
