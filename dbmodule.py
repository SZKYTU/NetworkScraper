import sqlite3


def updateStatus(status, ip, hostName):
    conn = sqlite3.connect("scrap")
    conn.execute(f"UPDATE scrap SET status = '{status}' WHERE ip='{ip}'")
    conn.commit()
    conn.close()

def get():
    dbdata = []
    conn = sqlite3.connect("scrap")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM scrap ")
    rows = cur.fetchall()
    
    for row in rows:
        dbdata.append(row)
    conn.close()

    return dbdata
        

