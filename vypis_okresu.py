from connect import connect
def vypis_okresu():
    cur, conn = connect()
    cur.execute("SELECT * FROM obce_pob")
    rows = cur.fetchall()
    for row in rows:
        print(row)
