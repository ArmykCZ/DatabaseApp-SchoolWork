import psycopg
"For those who search for information using Google Dorking, this is a private database LOL :D"
def connect():
    conn = psycopg.connect(
        host="192.168.135.10",
        port=5432,
        user="student",
        password="bluemonkey3",
        dbname="obce"
    )
    cur = conn.cursor()
    return cur, conn
