from fractions import Fraction
from pythonping import ping


IP = ["10.10.0.1","10.10.0.2","10.10.0.13","8.8.8.8"]


def ipCheck():
    FREEIP = []
    BLOCKIP = []
    for ip in IP:
        pingComand = ping(ip, count=1,verbose=True)
        string = str(pingComand)
        
        if "out" in string:
            FREEIP.append(ip)
        else:
            BLOCKIP.append(ip)
    return FREEIP, BLOCKIP


print(ipCheck())