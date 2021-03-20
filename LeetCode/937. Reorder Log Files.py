#!/usr/bin/env python
# coding: utf-8

# In[101]:


# my code

def reorder_log_files(logs):
    # 1) letter-log 인지 digit-log 인지 판별
    dig_logs = []
    let_logs = []
    for log in logs:
        if (log.split(" ")[1].isdigit()):
            dig_logs.append(log)
        else:
            let_logs.append(log)
    print(dig_logs, let_logs)
    # 2) let-log의 identifier과 content로 dict 생성
    let_dict = {}
    for log in let_logs:
        key = log.split(" ")[0]
        value = " ".join(log.split(" ")[1:])
        let_dict[key] = value
    # 3) values 정렬
    print(let_dict)
    keys = list(let_dict.keys())
    values = list(let_dict.values())
    sorted_values = sorted(values)
    # 4) res_logs 생성
    res_logs = []
    multiple_values = []
    for val in sorted_values: 
        count = sorted_values.count(val)
        if (count > 1) & (val not in multiple_values):
            multiple_values.append(val)
            li = []
            for key in keys:
                if let_dict[key] == val:
                    res = " ".join([key, val])
                    li.append(res)
            li.sort()
            print(li)
            res_logs += li
            
        elif (val not in multiple_values):
            key = keys[values.index(val)]
            res = " ".join([key, val])
            res_logs.append(res)
    return res_logs + dig_logs
    


# 내 코드는 식별자가 중복인 것이 있을 때를 다루지 못했다. 
# 그리고, 장황하게 길다.
# sort를 key에 따라 하는 기능이 있다는 것을 몰랐다. 

# ### solution
# - python의 내장형함수인 sort를 사용하자
# - lamda를 사용하자

# In[6]:


from typing import List
def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


# In[7]:


reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])

