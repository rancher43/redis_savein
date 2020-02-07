# python -m idlelib
import redis
import pandas as pd
import numpy as np

redis_con = redis.Redis(db=0)
df = pd.read_csv("/home/ds/tamrin/04-Pandas/titanic.csv")

tit_dic = {}
for ind, row in df.iterrows():
    t1 = row[0:3]
    t2 = row[4:]
    value = t1.append(t2)
    tit_dic[row[3]] = value

for h_id, val in tit_dic.items():
	dic = val.to_dict()
	redis_con.hmset(h_id, dic)

print('DB size:', redis_con.dbsize())
# redis_con.hgetall('Heikkinen, Miss. Laina')
redis_con.close()
