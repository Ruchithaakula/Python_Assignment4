#!/usr/bin/env python
# coding: utf-8

# In[8]:


num=input("enter the number")
try:
        temp=int(num)
        rev=0
        num1=int(num)
        while(num1>0):
            r=num1%10
            rev=rev*10+r
            num1=num1//10
        if temp==rev:
            print("the number is palindrome")
        else:
            print("the number is not aq palindrome")
            
except ValueError:
       print("the input is not proper")


# In[ ]:




