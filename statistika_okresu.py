from connect import connect

def statistika_okresu():
    cur, conn = connect()
    okres = input("Z jakého okresu chcete statistiky: ")
    sql = "SELECT nazev, pocet_obyvatel, prumerny_vek, pocet_muzi * 1.0 / NULLIF(pocet_zeny, 0) AS pomer  FROM obce_pob WHERE nazev = %s"
    cur.execute(sql, (okres,))
    rows = cur.fetchall()
    for row in rows:
        print(f"Nazev {row[0]}, obyvatele {row[1]}, prumerny vek {row[2]}, prumer muzu a zen {row[3]} ")