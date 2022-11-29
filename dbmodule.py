import sqlite3


def updateStatus(status, ip):
    conn = sqlite3.connect("scrap")
    conn.execute(f"UPDATE scrap SET status = '{status}' WHERE ip='{ip}'")
    conn.commit()
    conn.close()

def get():
    IP = []
    HN = []
    stat = []
    conn = sqlite3.connect("scrap")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM scrap ")
    rows = cur.fetchall()
    
    for row in rows:
        # IP.append(row[0])
        # HN.append(row[1])
        # stat.append(row[2])
        IP.append(row)
    
    conn.close()
    # return IP, HN, stat
    # list = []
    # list.append(IP)
    # list.append(HN)
    # list.append(stat)
    print(IP)
    return(IP)
        


get()