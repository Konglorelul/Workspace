import requests
#import winsound
import time
from win11toast import toast

URL = "site"

response = requests.get(URL, timeout = 5) #timeout can be added in cond for slow site
sc = response.status_code
size = len(response.content)
body = response.text
title = "Primaria Sector 1 Parcari"
min_size = 1024

if sc < 200 or sc > 300 :
    print("Site is still DOWN")
elif size < min_size: 
    print("Site loaded but something is wrong, maybe error") #can add exeption to see err
elif title not in response.text:
    print("Site loaded but something is wrong, maybe wrong page")
else:
    print("Site is UP")
    for i in range(3):
        toast('Site is UP', audio='ms-winsoundevent:Notification.Looping.Alarm')
        time.sleep(600)
 
