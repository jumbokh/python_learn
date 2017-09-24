
# coding: utf-8

# In[2]:


# ex7-4.py
stock = {'book':10, 'pen':3, 'earser':6, 'ruler':2}

for key, value in stock.items():
    if value < 5:
        print("({},{})".format(key, value))

