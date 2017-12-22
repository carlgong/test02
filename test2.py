import numpy as nm
import pandas as pd
import tushare as ts
import datetime
import pymysql
from sqlalchemy import create_engine
df=ts.get_today_all()
# df=ts.get_stock_basics()
# df = ts.get_tick_data('600848', date='2014-12-22')
pymysql.install_as_MySQLdb()
engine = create_engine('mysql://root:123456@lkmj1985.gicp.net:3306/test?charset=utf8')
#conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='test',
# db='mysql')
#追加数据到现有表
# df.to_sql('stock_basics3',engine,if_exists='append')
df['data']=datetime.datetime.now().strftime("%Y%m%d")
df.to_sql('stock_basics3',engine,if_exists='append')





