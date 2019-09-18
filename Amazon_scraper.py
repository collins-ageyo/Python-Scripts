#!/usr/bin/env python
# coding: utf-8

# In[35]:


import requests
from bs4 import BeautifulSoup
import smtplib


# In[36]:


URL ="https://www.ebay.com/itm/SONY-VAIO-Duo-13-Convertible-13-3-Ultrabook-i7-4650U-512GB-SSD-8GB-RAM/183946163632?hash=item2ad40bb5b0:g:hY0AAOSw2XhddeiN"


# In[37]:


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


# In[38]:


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="itemTitle").get_text().strip()
    price = soup.find(id="prcIsum").get_text()
    price = soup.find(id="prcIsum").get_text()
    converted_price = price[4:10]float("converted_price".replace(',',''))
    if (converted_price <600):
        send_mail

# In[43]:


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.ehlo()
    server.login('email', 'nxwuzkvbvtllzyyz')
    
    subject ="Price for Sony Vaio Duo 13 Reduced"
    body = 'Check this link: https://www.ebay.com/itm/SONY-VAIO-Duo-13-Convertible-13-3-Ultrabook-i7-4650U-512GB-SSD-8GB-RAM/183946163632?hash=item2ad40bb5b0:g:hY0AAOSw2XhddeiN'
    msg = f"Subject: {Subject}\n\n{body}"
    
    serve.send_email('from_email',
                     'to_email',
                    msg
                    )
    print ("Email Has Been Sent")
    
    server.quit()

check_price()




