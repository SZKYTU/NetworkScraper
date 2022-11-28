from fractions import Fraction
from config import IP
from pythonping import ping
from dbmodule import update


def ipCheck():
    for ip in IP:
        pingComand = ping(ip, count=1,verbose=True)
        string = str(pingComand)
        
        if "out" in string:
            update(1, ip)
        else:
            update(0, ip)


print(ipCheck())