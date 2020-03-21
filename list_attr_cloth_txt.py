#fr = open("I:\DeepFashion\Category and Attribute Prediction Benchmark\Anno\list_attr_cloth.txt",'r+')
from numpy import *
import numpy as np
import pandas as pd

filename="I:\DeepFashion\Category and Attribute Prediction Benchmark\Anno\list_attr_cloth.txt"
filename2="I:\DeepFashion\Category and Attribute Prediction Benchmark\Anno\list_attr_img.txt"
content_new=[]

dic={}

def list_read(filename):
    # Try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]

    file.close()

    for i in range(len(content)):
        content[i] = content[i].replace(" ","")

    del content[0]
    del content[0]
    global list_content
    list_content=[]
    for i in range(len(content)):
        for j in range(len(content[i])):
            if (content[i])[j].isdigit()==True:
                str1=(content[i])[0:j]
                str2=(content[i])[j]
                item=[str1,str2]
                list_content.append(item)

    list_content=list(list_content)

    test = pd.DataFrame(data=list_content)
    #test.to_csv('data_attr_list.csv', encoding='gbk')

    for i in range(len(list_content)):
        dic[list_content[i][0]]=list_content[i][1]
    #将所有attribute换成字典的形式
    #print(list_content)
    return dic,list_content

def table_read(filename):
    # Try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename, 'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]

    file.close()

#处理矩阵的数据
    #将字符串分开
    for i in range(len(content)):
        a=content[i][0:70]
        b=content[i][70:]
        content[i]=[a,b]

    del content[0]
    del content[0]

    for i in range(len(content)):
        content[i][0]=content[i][0].strip()
        content[i][1]=content[i][1].strip()

    #print(content)
    #将矩阵分开
    b = [i[1] for i in content]

    for i in range(len(b)):
        b[i] =b[i].split(' ')
        for item in b[i]:
            if item != '1' and item != '-1':
                # print('other item in b[' + str(i) + ']:' + str(item))
                b[i].remove(item)

    '''  #print('len(b['+str(i)+']):' + str(len(b[i])))
        # print('-1 in b['+str(i)+']:' + str(b[i].count('-1')))
        # print('1 in b['+str(i)+']:' + str(b[i].count('1')))
       for item in b[i]:
            if item != '1' and item != '-1':
                print('other item in b['+str(i)+']:'+str(item))'''
    # print('b: ' + str(b[0]))
    # print('-1 in b[0]:' + str(b[0].count('-1')))
    # print('1 in b[0]:' + str(b[0].count('1')))
    # print('b[0]1002: ' + str(b[0]))
    # print('b[1]1004: ' + str(b[1]))
    #print(b[0])
    # print('len(content):'+str(len(content)))
    #print('len(content):'+str(len(content)))
    # print(b[5793])

    #根据矩阵找到合适的位置数字
    new_index=[]
    for i in range(len(b)):
        temp = []
        for j in range(len(b[i])):
            if b[i][j]=='1':
                temp.append(j)
        new_index.append(temp)

    #print(new_index)

    for i in range(len(content)):
        content[i][1]=new_index[i]

    test = pd.DataFrame(data=content)  # 数据有三列，列名分别为one,two,three
    test.to_csv('data2.csv', encoding='gbk')


"""   #将数字转换为第一个list中的attr名称
    for i in range (len(new_index)):
        for j in range(len(new_index[i])):
            print(list_content[int(new_index[i][j])][0])


    
    #for i in range (len(b)):
     temp=b[i].find('1')
        lb=list(b[i])
        lb.insert(temp,' ')
        b[i]=lb


    #print(content)

   del(content[0])
    del(content[0])

    content_table=[x[0] for x in content]

    content_table=list(set(content_table))

    np.array(content_table)
    for i in range(len(content_table)):
        content_new.append(content_table[i])

    for i in range(len(content_new)):
        content_new[i] = content_new[i].split('_')

    #print(content_new)
    #print(len(content_table))
    #print(temp)
    return content_new
    

def getvalue(content,dic):
    for i in range(len(content)):
        for j in range(len(content[i])):
            (content[i])[j]=((content[i])[j]).lower()
            content[i][j] = content[i][j].replace(" ", "")

    for i in range(len(content)):
        print(content[i])
        for j in range(len(content[i])):
            a = (content[i][j])
            print(dic.get(a))"""


if __name__ == '__main__':
    list_read(filename)
    #table_read(filename2)
    #getvalue(content_new,dic)