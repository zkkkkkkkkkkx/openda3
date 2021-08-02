# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:11:44 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel('20210801-2300人文素养作答情况.xlsx')
data.columns=['准考证号','姓名','学校','开始答题时间','交卷时间','客户端答题状态','Q1','Q1ans1','Q1ans2','Q2','Q2ans1','Q2ans2','Q2ans3','Q2ans4','Q3','Q3ans1','Q4','Q4ans1','Q4ans2','Q5','Q5ans1','Q5ans2','Q5ans3','Q5ans4','Q5ans5']
#答完未完全退出系统
nat_idx=[]
for i in range(len(data)):
    if pd.isnull(data['交卷时间'].iloc[i]):
        nat_idx.append(i)
data_NaT=data.iloc[nat_idx]
print(len(data_NaT))#21

data=data.drop(nat_idx,axis=0)

sum_finished=len(data)
finish_time=datetime(2021,8,1,0,0,0)
time=pd.to_datetime(data['开始答题时间'])-finish_time
sum_finished_onday=0
flag=[]
for i in range(len(data)):
    if time.iloc[i].days>=0:
        sum_finished_onday=sum_finished_onday+1
        flag.append(i)
#当天完成人数
print(sum_finished_onday)
#合计完成人数
print(sum_finished)


data['总时间'] = pd.to_datetime(data['交卷时间']) - pd.to_datetime(data['开始答题时间'])
time=[]
w_counts=[]
for i in range(len(data)):
    a=data['总时间'].iloc[i].seconds/60
    time.append(a)
    b=len(str(data['Q4ans2'].iloc[i]))
    w_counts.append(b)

data['总时间']=time
data['Q4ans2count']=w_counts

data_onday=data.iloc[flag]

print(data['总时间'].mean())
print(data_onday['总时间'].mean())
def time10(data_onday,name):
    sum010=sum1020=sum2030=sum3040=sum4050=sum5060=sum6070=sum7080=sum8090=sum90100=sum100110=sum110120=0
    count010=count1020=count2030=count3040=count4050=count5060=count6070=count7080=count8090=count90100=count100110=count110120=0
    for i in range(len(data_onday)):
        if 0<=data_onday['总时间'].iloc[i]<=10:
            count010=count010+1
        if 10<data_onday['总时间'].iloc[i]<=20:
            count1020=count1020+1
        if 20<data_onday['总时间'].iloc[i]<=30:
            count2030=count2030+1
        if 30<data_onday['总时间'].iloc[i]<=40:
            count3040=count3040+1
        if 40<data_onday['总时间'].iloc[i]<=50:
            count4050=count4050+1
        if 50<data_onday['总时间'].iloc[i]<=60:
            count5060=count5060+1
        if 60<data_onday['总时间'].iloc[i]<=70:
            count6070=count6070+1
        if 70<data_onday['总时间'].iloc[i]<=80:
            count7080=count7080+1
        if 80<data_onday['总时间'].iloc[i]<=90:
            count8090=count8090+1
        if 90<data_onday['总时间'].iloc[i]<=100:
            count90100=count90100+1
        if 100<data_onday['总时间'].iloc[i]<=110:
            count100110=count100110+1
        if 110<data_onday['总时间'].iloc[i]<=120:
            count110120=count110120+1
    x=['0-10分钟','10-20分钟','20-30分钟','30-40分钟','40-50分钟','50-60分钟','60-70分钟','70-80分钟','80-90分钟','90-100分钟','100-110分钟','110-120分钟']
    y=[count010,count1020,count2030,count3040,count4050,count5060,count6070,count7080,count8090,count90100,count100110,count110120]
    #<=10
    print(y[0])
    #<=20
    print(y[0]+y[1])
    #<=30
    print(y[0]+y[1]+y[2])
    recs=plt.bar(x,y)
    x=[rec.get_x() for rec in recs]#使用列表推导式获取bar的横坐标
    y=[rec.get_height() for rec in recs]#使用列表推导式获取bar的高度
    w=[rec.get_width() for rec in recs]#使用列表推导式获取bar的宽度
    textx=[x+width/2 for x,width in zip(x,w)]#计算标注的横坐标
    result=[plt.text(x,y,str(np.round(y)),size=20,ha = 'center') for x,y in zip(textx,y)]#使用列表推导式标注高度信息
    plt.title(name,size=30)
    plt.ylabel('人数')
    plt.show()
    
    
#time10(data_onday,'8月1日当日每隔10分钟的作答人数图')
#time10(data,'截至目前每隔10分钟的作答人数图')

def stu_timelast(data_onday,name):
    sum010=sum1020=sum2030=sum3040=sum4050=sum5060=sum6070=sum7080=sum8090=sum90100=sum100110=sum110120=0
    count010=count1020=count2030=count3040=count4050=count5060=count6070=count7080=count8090=count90100=count100110=count110120=0
    for i in range(len(data_onday)):
        if 0<=data_onday['总时间'].iloc[i]<=10:
            count010=count010+1
        if 10<data_onday['总时间'].iloc[i]<=20:
            count1020=count1020+1
        if 20<data_onday['总时间'].iloc[i]<=30:
            count2030=count2030+1
        if 30<data_onday['总时间'].iloc[i]<=40:
            count3040=count3040+1
        if 40<data_onday['总时间'].iloc[i]<=50:
            count4050=count4050+1
        if 50<data_onday['总时间'].iloc[i]<=60:
            count5060=count5060+1
        if 60<data_onday['总时间'].iloc[i]<=70:
            count6070=count6070+1
        if 70<data_onday['总时间'].iloc[i]<=80:
            count7080=count7080+1
        if 80<data_onday['总时间'].iloc[i]<=90:
            count8090=count8090+1
        if 90<data_onday['总时间'].iloc[i]<=100:
            count90100=count90100+1
        if 100<data_onday['总时间'].iloc[i]<=110:
            count100110=count100110+1
        if 110<data_onday['总时间'].iloc[i]<=120:
            count110120=count110120+1
    x=['0-10分钟','10-20分钟','20-30分钟','30-40分钟','40-50分钟','50-60分钟','60-70分钟','70-80分钟','80-90分钟','90-100分钟','100-110分钟','110-120分钟']
    y=[count010,count1020,count2030,count3040,count4050,count5060,count6070,count7080,count8090,count90100,count100110,count110120]
    #<=10
    print(y[0])
    #<=20
    print(y[0]+y[1])
    #<=30
    print(y[0]+y[1]+y[2])
    m=['0-10分钟','10-20分钟','20-30分钟','30-40分钟','40-50分钟','50-60分钟','超过60分钟']
    n_sum=count010+count1020+count2030+count3040+count4050+count5060+count6070+count7080+count8090+count90100+count100110+count110120
    n=[count010/n_sum,count1020/n_sum,count2030/n_sum,count3040/n_sum,count4050/n_sum,count5060/n_sum,count6070/n_sum+count7080/n_sum+count8090/n_sum+count90100/n_sum+count100110/n_sum+count110120/n_sum]
    pic=plt.pie(n,labeldistance = 1.1,autopct = '%3.1f%%')                          
    plt.title(name,size=30)
    plt.legend(m)
    plt.show()
#stu_timelast(data_onday,'8月1日当日总体作答时长分布')
#stu_timelast(data,'截至目前总体作答时长分布')

def time_recording(data):
    sum010=0
    count010=0
    sum1130=0
    count1130=0
    sum3160=0
    count3160=0
    sum6190=0
    count6190=0
    sum91120=0
    count91120=0
    sum120=0
    count120=0
    for i in range(len(data)):
        if 0<=data['总时间'].iloc[i]<=10:
            sum010=sum010+int(data['Q4ans2count'].iloc[i])
            count010+=1
        if 11<=data['总时间'].iloc[i]<=30:
            sum1130=sum1130+int(data['Q4ans2count'].iloc[i])
            count1130+=1
        if 31<=data['总时间'].iloc[i]<=60:
            sum3160=sum3160+int(data['Q4ans2count'].iloc[i])
            count3160+=1
        if 61<=data['总时间'].iloc[i]<=90:
            sum6190=sum6190+int(data['Q4ans2count'].iloc[i])
            count6190+=1
        if 91<=data['总时间'].iloc[i]<=120:
            sum91120=sum91120+int(data['Q4ans2count'].iloc[i])
            count91120+=1
        if data['总时间'].iloc[i]>120:
            sum120=sum120+int(data['Q4ans2count'].iloc[i])
            count120+=1
    res010=round(sum010/count010,2)
    res1130=round(sum1130/count1130,2)
    res3160=round(sum3160/count3160,2)
    res6190=round(sum6190/count6190,2)
    res91120=round(sum91120/count91120,2)
    res120=round(sum120/count120,2)
    sns.set(style="white", context="notebook")
    sns.set_style('whitegrid', {'font.sans-serif':['simhei','Arial']})
    y=[res010,res1130,res3160,res6190,res91120,res120]
    x=['0-10分钟','11-30分钟','31-60分钟','61-90分钟','91-120分钟','120+分钟']
    recs=plt.bar(x,y)
    x=[rec.get_x() for rec in recs]#使用列表推导式获取bar的横坐标
    y=[rec.get_height() for rec in recs]#使用列表推导式获取bar的高度
    w=[rec.get_width() for rec in recs]#使用列表推导式获取bar的宽度
    textx=[x+width/2 for x,width in zip(x,w)]#计算标注的横坐标
    result=[plt.text(x,y,str(np.round(y)),size=20,ha = 'center') for x,y in zip(textx,y)]#使用列表推导式标注高度信息
    plt.title('学生作答时长与小作文字数的分布情况',size=30)
    plt.ylabel('字符数')
    plt.show()
time_recording(data)   
def school_count(data):
    schools=data['学校'].unique()
    num10=[]
    num_sum=[]
    per=[]
    for idx in schools:
        temp_data=data[data['学校'].isin([idx])]
        sum=0
        for j in range(len(temp_data)):
            if temp_data['总时间'].iloc[j]<10:
                sum=sum+1
        num10.append(sum)
        num_sum.append(len(temp_data))
        per.append(round(sum/len(temp_data),2))
    print(schools)
    print(num10)
    print(num_sum)
    print(per)
school_count(data)
school_count(data_onday)
            

