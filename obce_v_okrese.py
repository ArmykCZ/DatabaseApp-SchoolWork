from connect import connect
def obce_v_okrese():
    okres = input("Zadej kód okresu: ")
    cur, conn = connect()
    sql = "SELECT nazev, pocet_obyvatel, prumerny_vek FROM obce_pob WHERE id_okres = %s"
    cur.execute(sql, (okres,))
    rows = cur.fetchall()
    for row in rows:
        print(f"Název obce: {row[0]}, Počet obyvatel: {row[1]}, Průměrný věk: {row[2]}")
