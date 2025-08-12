import sqlite3

conn = sqlite3.connect("music_nft.db")
cursor = conn.cursor()
print("Users:")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)
conn.close()