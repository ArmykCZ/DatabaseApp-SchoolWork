from vypis_okresu import vypis_okresu
from connect import connect
from obce_v_okrese import obce_v_okrese
from vyhledavani_obce import vyhledavani_obce
from statistika_okresu import statistika_okresu


def menu():
    cur, conn = connect()
    while True:
        try:
            vybrat_menu = int(input(
        """=========================
DEMOGRAFIE ČR
========================z=
1 - Seznam okresů
2 - Obce v okrese
3 - Hledat obec
4 - Statistiky okresu
0 - Konec
> """
    ))

            if vybrat_menu == 1:
                vypis_okresu()
            elif vybrat_menu == 2:
                obce_v_okrese()
            elif vybrat_menu == 3:
                vyhledavani_obce()
            elif vybrat_menu == 4:
                statistika_okresu()
            elif vybrat_menu == 0:
                print("Ukončuji program a přerušuji spojení s databází")
                conn.close()
                cur.close()
                break

        except ValueError:
            print("Zadali jste prázdnou hodnotu nebo písmeno, které není podporováno")
        except KeyboardInterrupt:
            conn.close()
            cur.close()
            print("Vypínám program")