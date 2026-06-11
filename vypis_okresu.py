from connect import connect
def vypis_okresu():
    cur, conn = connect()
    cur.execute("SELECT * FROM obce_pob")
    rows = cur.fetchall()
    for row in rows:
        print(f"ID okresu: {row[0]}, ID obce: {row[1]}, název: {row[2]}, počet obyvatel: {row[3]}, počet můžů: {row[4]}, počet žen: {row[5]}, průměrný věk: {row[6]}, průměrný věk mužů: {row[7]}, průměrný věk žen: {row[8]}")
