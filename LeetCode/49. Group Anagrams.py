#!/usr/bin/env python
# coding: utf-8

# ## My code

# ### 처음 시도 

# In[73]:


strs = ["eat","tea","tan","ate","nat","bat"]


# In[74]:


from typing import List
def groupAnagrams(strs: List[str]):
    my_dict = {}

    for string in strs:
        r = []
        for s in string:
            r.append(s)
        r.sort()
        res = ''.join(r)
        my_dict[string] = res

    vals = set(my_dict.values())
    
    result = []
    for val in vals:
        temp = []
        for key in my_dict:
            if my_dict[key] == val:
                temp.append(key)
        result.append(temp)

    return result

groupAnagrams(strs)


# #### test code에서 오류 발생 

# In[76]:


strs = ["",""]


# python sorted()를 사용할 생각을 못 했다. <br>
# 그냥 string에 sorted를 하면 알파벳 순으로 정렬하여 리스트 형식으로 리턴해준다(아래 코드 참고). 이걸 몰라서 이 과정을 일일이 코드로 작성했다..<br> 
# test code에서의 오류는 그냥 딕셔너리의 키 값을 정렬된 문자로 하고 value값을 리스트 형식으로 append해주면 되었다.

# In[75]:


s1 = "ate"
print(sorted(s1))


# ### 최종 수정본

# In[77]:


from typing import List
def groupAnagrams(strs: List[str]):
    my_dict = {}

    for string in strs:
        r = ''.join(sorted(string))
        print(r)
        if r not in my_dict:
            my_dict[r] = [string]
        else:
            my_dict[r].append(string)

    return list(my_dict.values())
groupAnagrams(strs)


# ## Solution

# 문제 접근 방법은 맞았다. sorted()는 문자열도 잘 정렬하며 결과를 리스트 형태로 리턴하는데, 이를 다시 키로 사용하기 위해 join으로 합쳐 이 값을 키로 하는 딕셔너리로 구성한다. 애너그램끼리는 같은 키를 갖게 되고 따라서 여기에 append()하는 형태가 된다. <br>
# 놀랍게도 위 과정을 단 두 줄로 쓸 수 있다!

# In[ ]:


for word in strs:
    anagrams[''.join(sorted(word))].append(word)


# 존재하지 않는 키를 삽힙 할 경우 에러가 나지 않도록 이전 장에서 다룬 collections.difaultdict를 사용하자. 
# anagrams = collections.defaultdict(list)

# In[78]:


from typing import List
import collections

def groupAnagrams(strs: List[str]):
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
groupAnagrams(strs)

