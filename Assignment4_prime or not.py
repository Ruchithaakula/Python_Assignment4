#!/usr/bin/env python
# coding: utf-8

# In[14]:


number = int(input("Enter any number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# In[ ]:





# In[ ]:




