
# coding: utf-8

# In[3]:


# _*_ coding: utf-8 _*_
# program ex11-1.py 
from firebase import firebase
import time

new_users = [
    {'name': 'Richard Ho'},
    {'name': 'Tom Wu'},
    {'name': 'Judy Chen'},
    {'name': 'Lisa Chang'}
]

db_url = "https://studypython-63565.firebaseio.com"
fdb = firebase.FirebaseApplication(db_url, None)
for user in new_users:
    fdb.post('/user',user)
    time.sleep(3)

