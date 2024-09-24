#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip3
import sasctl
from sasctl import Session
from sasctl import publish_model
from sasctl.services import model_repository as mr 


# In[4]:


session = Session('https://sit.woodpecker.com','akash','akash@2024',verify_ssl = False)


# In[2]:




# In[5]:


model = mr.get_model('logreg')
publish_model(model,'maslocal')

