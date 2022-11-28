import sqlite3


def updateStatus(status, ip):
    conn = sqlite3.connect("scrap")
    conn.execute(f"UPDATE scrap SET status = '{status}' WHERE ip='{ip}'")
    conn.commit()
    conn.close()