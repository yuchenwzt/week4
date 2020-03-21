from list_attr_cloth_txt import list_read
import numpy as np
import pandas as pd
import csv

filename="I:\DeepFashion\Category and Attribute Prediction Benchmark\Anno\list_attr_cloth.txt"
filename2='data2.csv'

def transform():
    with open('data2.csv', 'r') as f:
        reader = csv.reader(f)
        content=list(reader)

    content_eff=[]
    for i in range(len(content)):
        if content[i][2]!='[]':
            content_eff.append(content[i])

    b = [i[2] for i in content_eff]

    for i in range(len(b)):
        b[i] = b[i].replace("[", "")
        b[i] = b[i].replace("]", "")
        b[i] = b[i].replace(" ", "")
        b[i] = b[i].split(',')

    #print(b)
    print(b[0])

    a = [i[1] for i in content_eff]
    print(a[0])
    #print(len(a))
    #print(len(b))
    #print(a)
    return a,b

def create_attr(b,list_content):
    att=[]
    for i in range(len(b)):
        temp_att=[]
        for j in range(len(b[i])):
            temp=int(b[i][j])-1
            #print(temp)
            #print(list_content[temp])
            temp_att.append(list_content[temp][0])
        att.append(temp_att)



    #print(att)
    return att

def to_num(a,att,dic):

    att_=[]
    for i in range(len(a)):
        temp=[a[i],att[i]]
        att_.append(temp)
    test = pd.DataFrame(data=att_)
    #test.to_csv('data_att.csv', encoding='gbk')

    for i in range(len(att)):
        for j in range(len(att[i])):
            att[i][j]=dic.get(att[i][j])
    #print(att)

    num=[]
    for i in range(len(a)):
        temp=[a[i],att[i]]
        num.append(temp)

    #print(num)

    test = pd.DataFrame(data=num)
    #test.to_csv('data_num.csv', encoding='gbk')

if __name__ == '__main__':
    dic,list_content=list_read(filename)
    a,b=transform()
    att=create_attr(b,list_content)
    to_num(a,att,dic)
