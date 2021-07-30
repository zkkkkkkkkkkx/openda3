# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:07:58 2021

@author: Administrator
"""

import os 
import re
import pandas as pd
from PIL import Image
import numpy as np
file_dir='E:\openct\草图作答300人'
Task_name=[]
ID=[]
Path=[]
N=[]
X=[]
Xs=[]
num=-888
Num=[]
for root,dirs,files in os.walk(file_dir):
    for i in range(len(files)):
        path='E:\草图作答300人'+'\\'+files[i]
        Path.append(path)
        Id=re.findall(r'(?<=草图\-)\d*',files[i])
        ID.append(Id[0])
        name=re.findall(r'(?<=题目\d\.\s).*(?=\s\-)',files[i])
        #if name=='场景三：赏文物（二）':
        Task_name.append(31)
        N.append('N')
        X.append('*')
        Xs.append('*|')
        Num.append(num)
        num-=1
    data={'默认值N':N,'准考证号':ID,'题号':Task_name,'默认值N':N,'默认值0':np.linspace(0,0,len(files)),'图像路径':path,'默认值-888':Num,'默认值3':Xs,'默认值':X}
    df=pd.DataFrame(data)
    df.to_excel('pic.xls')
