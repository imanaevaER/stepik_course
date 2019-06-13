#!/usr/bin/env python
# coding: utf-8

# **3.1 Функции №1**

# In[1]:


def f(x):
    if x<=(-2):
        return 1-(x+2)**2
    elif x>2:
        return (x-2)**2+1
    else:
        return -x/2


# **3.1 Функции №2**

# In[2]:


def modify_list(l):
    n = len(l)
    i=0
    while i < n:
        if l[i]%2==0:
            l[i]=int(l[i]/2)
            i+=1
        else:
            del l[i]
            n-=1


# In[ ]:





# **3.2 Словари №1**

# In[3]:


def update_dictionary(d, key, value):
    
    if key in d:
        d[key] += [value]
    elif key*2 in d:
        d[key*2] += [value]
    else:
        d[2*key]=[value]


# **3.2 Словари №2**

# In[4]:


s = input().lower().split()
m = list(set(s))
for j in range(len(m)):
    count=0
    for i in range(len(s)):
        if m[j]==s[i]:
            count+=1
            i+=1
        else:
            i+=1
    print(m[j], count)
    j+=1


# **3.2 Словари №3**

# In[ ]:


d={}
k=[]
n = int(input())
for i in range(n):
    x = int(input())
    k.append(x)
for j in range (len(k)):
    key=k[j]
    if key in d:
        print(d[key])
    else:
        p = k[j]
        d[key]=f(p)
        print(d.get(key))


# In[ ]:





# **3.4 Файловый ввод/вывод №1**

# In[ ]:


import requests
with open('dataset_3378_2.txt') as inf:
    for line in inf:
        line = line.strip()
url = line
r = requests.get(url)   
ouf = open('file3.txt', 'w')
ouf.write(str(len(r.text.splitlines())))
ouf.close()


# **3.4 Файловый ввод/вывод №2**

# In[ ]:


with open('dataset_3378_3.txt') as inf:
    for line in inf:
        line = line.strip()
url = line
r = requests.get(url)
while r.text.find('We')!=0: 
    t=url.rfind('/')
    url=url.replace(url[t+1:len(url)],r.text)
    r = requests.get(url)
ouf = open('file4.txt', 'w')
ouf.write(r.text)
ouf.close()


# **3.4 Файловый ввод/вывод №3**

# In[ ]:


mt = 0
f = 0
r = 0
c = 0
ouf = open('file6.txt', 'w')
with open('dataset_3363_4_4.txt') as inf:
    for line in inf:
        line = line.strip()
        m = [i for i in line.split(';')]
        s = 0
        c += 1
        mt += int(m[1])
        f += int(m[2])
        r += int(m[3])
        for j in range(1,len(m)):
            s +=int(m[j])
        ouf.write(str(s/(len(m)-1))+'\n')
ouf.write(str(mt/c)+' '+str(f/c)+' '+str(r/c))
ouf.close()


# In[ ]:





# **3.5 Модули, подключение модулей №1**

# In[ ]:


import math
r=float(input())
print(2*math.pi*r)


# **3.5 Модули, подключение модулей №2**

# In[ ]:


import sys
s=''
for i in range(1, len(sys.argv)):
    s = s + sys.argv[i]+' '
print(s, end=' ')


# In[ ]:





# **3.6 Установка дополнительных модулей №1**

# In[ ]:


import requests
with open('dataset_3378_2.txt') as inf:
    for line in inf:
        line = line.strip()
url = line
r = requests.get(url)   
ouf = open('file3.txt', 'w')
ouf.write(str(len(r.text.splitlines())))
ouf.close()


# **3.6 Установка дополнительных модулей №2**

# In[ ]:


with open('dataset_3378_3.txt') as inf:
    for line in inf:
        line = line.strip()
url = line
r = requests.get(url)
while r.text.find('We')!=0: 
    t=url.rfind('/')
    url=url.replace(url[t+1:len(url)],r.text)
    r = requests.get(url)
ouf = open('file4.txt', 'w')
ouf.write(r.text)
ouf.close()


# In[ ]:





# **3.7 Задачи по материалам недели №1**

# In[ ]:


n = int(input())
x_list = [input().split(';') for x in range(n)]
vs = [x[0] for x in x_list]
vs1 = [x[2] for x in x_list]
vs2=vs
for x in vs1:
    if x not in vs2:
        vs2.append(x)
count1=dict.fromkeys(vs2,0)
wins=dict.fromkeys(vs2,0)
lose=dict.fromkeys(vs2,0)
nich=dict.fromkeys(vs2,0)
all1=dict.fromkeys(vs2,0)
for kom1, gol1, kom2, gol2 in x_list:
    count1[kom1] += 1
    count1[kom2] += 1
    if int(gol1) > int(gol2):
        wins[kom1] += 1
        all1[kom1] += 3
        lose[kom2] += 1
    elif int(gol1) < int(gol2):
        wins[kom2] += 1
        all1[kom2] += 3
        lose[kom1] += 1
    elif int(gol1) == int(gol2):
        nich[kom1] += 1
        all1[kom1] += 1
        nich[kom2] += 1
        all1[kom2] += 1
for i in count1.keys():
    print(i, end='')
    print(':', end='')
    print(count1[i],wins[i],nich[i],lose[i],all1[i])


# **3.7 Задачи по материалам недели №2**

# In[ ]:


s = input()
s_1 = input()
d = dict(zip(s,s_1))
d_1 = dict(zip(s_1,s))
new = input()
new_1 = input()

for i in new:
    print(d[i], end='')
print(sep='\n')
for i in new_1:
    print(d_1[i], end='')


# **3.7 Задачи по материалам недели №3**

# In[ ]:


n = int(input())
d = [input().lower() for i in range(n)]
n = int(input())
words = []
for i in range(n):
    s = input().split(' ')
    for word in s:
        words.append(word)
words = list(set(words))
for i in words:
    if d.count(i.lower()) == 0:
        print(i.lower(), sep='\n')


# **3.7 Задачи по материалам недели №4**

# In[ ]:


n = int(input())
y = 0
x = 0
for i in range(n):
    s=str(input()).split()
    if s[0] == 'север':
        y += int(s[1])
    elif s[0] =='запад':
        x -= int(s[1])
    else:
        if s[0] == 'юг':
            y -= int(s[1])
        elif s[0] =='восток':
            x += int(s[1])
print(x,y)


# **3.7 Задачи по материалам недели №5**

# In[ ]:


ouf = open('file7.txt', 'w')
with open('dataset_3380_5_3.txt') as inf:
    s = []
    d = {}
    for l in inf:
        s.append(l.strip('\n').split('\t'))
    print(s)
    for c in s:
        if int(c[0]) in d:
            d[int(c[0])].append(int(c[2]))
        else:
            d[int(c[0])] = [int(c[2])]
    for i in sorted(d.keys()):
        print(i, '', sum(d[i]) / len(d[i]))


# In[ ]:





# In[ ]:





# In[ ]:




