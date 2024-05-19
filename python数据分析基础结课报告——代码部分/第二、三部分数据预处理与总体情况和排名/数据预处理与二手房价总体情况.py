#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd  #导入库
import numpy as np
hanyang=pd.read_excel(r'C:\Users\linda\Desktop\汉阳区二手房.xlsx')  #打开数据表格
hanyang['单价'] = hanyang['单价'].str.replace(',', '').astype(float)  #将单价列所有逗号替换为空字符串，所有值转换为浮点数
price_above18000=(hanyang['单价']>=18000).sum()  #筛选单价大于等于18000的房子个数
print(f"单价大于等于18000的个数是: {price_above18000}")


# In[42]:


price_between15000and18000=((hanyang['单价']>=15000)&(hanyang['单价']<18000)).sum()  #筛选单价在15000和18000之间的房子个数
print(f"单价在15000和18000之间的个数是: {price_between15000and18000}")


# In[43]:


price_between10000and15000=((hanyang['单价']>=10000)&(hanyang['单价']<15000)).sum()  #筛选单价在10000和15000之间的房子个数
print(f"单价在10000和15000之间的个数是: {price_between10000and15000}")


# In[44]:


price_between5000and10000=((hanyang['单价']>=5000)&(hanyang['单价']<10000)).sum()  #筛选单价在5000和10000之间的房子个数
print(f"单价在5000和10000之间的个数是: {price_between5000and10000}")


# In[45]:


price_below5000=(hanyang['单价']<5000).sum()  #筛选单价小于5000的房子个数
print(f"单价小于5000的个数是: {price_below5000}")


# In[49]:


import matplotlib.pyplot as plt
from pylab import * 
mpl.rcParams['font.sans-serif']=['SimHei']
total_price=(hanyang['单价']>0).sum()  #计算一共有多少房子
total_price


# In[50]:


#计算每个单价区间的房子个数占房子总数的百分比
above18000=100*price_above18000/total_price 
between15000and18000=100*price_between15000and18000/total_price
between10000and15000=100*price_between10000and15000/total_price
between5000and10000=100*price_between5000and10000/total_price
below5000=100*price_below5000/total_price

sizes=[above18000,between15000and18000,between10000and15000,between5000and10000,below5000]
labels=['单价大于等于18000','单价在15000和18000之间','单价在10000和15000之间','单价在5000和10000之间','单价小于5000']

#画饼状图
plt.figure(figsize=(16,9))
explode = [0, 0, 0, 0, 0]    
plt.pie(sizes, autopct='%.2f%%', labels=labels, explode=explode)  
plt.axis('equal')  # 设置轴相等以确保饼图是圆形的  
plt.title('不同价格区间二手房占比')  

# 保存图形为PDF文件  
plt.savefig(r'C:\Users\linda\Desktop\饼图.pdf')  

plt.show()


# In[ ]:





# In[ ]:




