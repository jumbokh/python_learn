
# coding: utf-8

# In[1]:


# ex7-7.py

for i in range(2,9):
    if(i!=2 and i!=6): continue
    for j in range(1,10):
        for k in range(i,i+5):
           print("{}x{}={:>2}    ".format(k, j, k*j), end="")
        print()
    print()

