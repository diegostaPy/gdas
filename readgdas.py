#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ARLreader as Ar
#import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
import os.path
from os import path
from ftplib import FTP


# #ftp://arlftp.arlhq.noaa.gov/pub/archives/gdas1

# In[2]:


dt = datetime.datetime(2021, 7, 6)
end = datetime.datetime(2021, 7, 12)
step = datetime.timedelta(hours=1)
dates= []
while dt <= end:
    dates.append(dt)
    dt += step


# In[3]:






test = datetime.datetime(2021, 7, 1,0,0)
print(test)

# In[26]:


print(Ar.fname_from_date(test))


# In[13]:


Teff=[]
Tg=[]
Pg=[]
for date in dates:
    print(date)
    
    filename=Ar.fname_from_date(date)
    if(not(path.exists('datos/'+filename))):
        ftp = FTP('arlftp.arlhq.noaa.gov')
        ftp.login() 
        ftp.cwd('/pub/archives/gdas1') 
        with open('datos/'+filename, 'wb') as fp:
            ftp.retrbinary('RETR '+filename, fp.write)
        ftp.quit()   
#    profile, sfcdata, indexinfo, ind = Ar.reader('datos/'+filename).load_profile(date.day, date.hour, (16.75973,-93.11308),sfc=True, flag_interp=True)
    profile, sfcdata, indexinfo, ind = Ar.reader('datos/'+filename).load_profile(date.day, date.hour, ( -25.331270,-57.516597),sfc=True, flag_interp=True)
  
   
    T=profile['TEMP']#- 273.15
    P=profile['PRSS']    
    H=profile['HGTS']
    Ts=sfcdata['TMPS']    
    Ps=sfcdata['PRSS']

    Wun=-np.diff(np.hstack((P,0)))/P[0]
    Teff.append(np.sum(Wun*T))
    Tg.append(Ts)
    Pg.append(Ps)
    


# In[12]:


dataTeff = pd.DataFrame(list(zip( dates, Teff,Tg,Pg)), 
               columns =['date', 'teff', 'ts', 'ps']) 


# In[1]:


#dataTeff.to_csv("teffPyjulio6a8.csv")


# In[14]:


dataTeff.tail()


# In[ ]:





# In[ ]:




