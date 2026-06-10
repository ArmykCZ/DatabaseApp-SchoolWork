from connect import connect

def vyhledavani_obce():
    cur, conn = connect()
    nazev = input("Zadej název obce: ")
    sql = "SELECT nazev FROM obce_pob WHERE nazev LIKE %s"
    cur.execute(sql, (f"%{nazev}%",))
    rows = cur.fetchall()
    for row in rows:
        print(f"Nazev: {row[0]}")
