from pythonping import ping

from config import IP
from dbmodule import updateStatus

import os


def ipCheck():
    for ip in IP:
        pingComand = ping(ip, count=1,verbose=True)
        string = str(pingComand)
        
        if "out" in string:
            updateStatus(1, ip)
        else:
            updateStatus(0, ip)

# def HNCheck():
#     for ip in IP:
#         askDomain = os.system(f'cmd /k "nbtstat -a {ip}"')
#         print(askDomain)



ipCheck()