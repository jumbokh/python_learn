
# coding: utf-8

# In[1]:


# _*_ coding: utf-8 _*_
# program ex11-2.py 
from firebase import firebase

db_url = "https://studypython-63565.firebaseio.com"
fdb = firebase.FirebaseApplication(db_url, None)
users = fdb.get('/user', None)
print("資料庫中找到以下的使用者")
for key in users:
    print(users[key]['name'])

