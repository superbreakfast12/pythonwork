#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd #导入库
import numpy as np
lianjia=pd.read_excel(r'C:\Users\linda\Desktop\汉阳区二手房.xlsx')  #打开“汉阳区二手房”数据表格
lianjia['标题'] = lianjia['标题'].str.replace(',', '')  #将标题列所有逗号替换为空字符串
lianjia['标题'] = pd.to_numeric(lianjia['标题'], errors='coerce')  #将标题列所有值转换为数字，若遇到不能转换的值则转换为NaN

FF=lianjia.loc[(lianjia['区域']=='七里庙')].copy()  #筛选出区域为七里庙的数据信息，命名为FF
print(lianjia.loc[(lianjia['区域']=='七里庙')].copy())  #显示数据

FF.to_excel(r'C:\Users\linda\Desktop\FF.xlsx')  #保存至桌面

qilimiao=pd.read_excel(r'C:\Users\linda\Desktop\FF.xlsx')  #打开“七里庙”数据表格

qilimiao['单价'] = qilimiao['单价'].str.replace(',', '').astype(float)  #将单价列所有逗号替换为空字符串，所有值转换为浮点数
avg = qilimiao['单价'].mean()  #计算七里庙的房子单价平均值
print(avg)  #显示平均值


# In[54]:


FF=lianjia.loc[(lianjia['区域']=='四新')]  #筛选出区域为四新的数据信息，命名为FF
print(lianjia.loc[(lianjia['区域']=='四新')])  #显示数据

FF['单价'] = FF['单价'].str.replace(',', '').astype(float)  #将单价列所有逗号替换为空字符串，所有值转换为浮点数
avg = FF['单价'].mean()  #计算四新的房子单价平均值
print(avg)  #显示平均值


# In[55]:


FF=lianjia.loc[(lianjia['区域']=='王家湾')]  #筛选出区域为王家湾的数据信息，命名为FF
print(lianjia.loc[(lianjia['区域']=='王家湾')])  #显示数据

FF['单价'] = FF['单价'].str.replace(',', '').astype(float)  #将单价列所有逗号替换为空字符串，所有值转换为浮点数
avg = FF['单价'].mean()  #计算王家湾的房子单价平均值
print(avg)  #显示平均值


# In[56]:


FF=lianjia.loc[(lianjia['区域']=='钟家村')]  #筛选出区域为钟家村的数据信息，命名为FF
print(lianjia.loc[(lianjia['区域']=='钟家村')])  #显示数据

FF['单价'] = FF['单价'].str.replace(',', '').astype(float)  #将单价列所有逗号替换为空字符串，所有值转换为浮点数
avg = FF['单价'].mean()  #计算钟家村的房子单价平均值
print(avg)  #显示平均值


# In[63]:



data = {  
    '区域': ['七里庙', '四新', '王家湾', '钟家村'],  
    '平均单价': [13396, 11982, 9905, 12234]  
}  
  
area = pd.DataFrame(data)  #将数据转换为DataFrame
  
# 使用 rank 方法对 '平均单价' 列进行排名  
area['排名'] = area['平均单价'].rank(ascending=False, method='first')  
  
print(area)  #显示数据


# In[ ]:





# In[ ]:





# In[ ]:




