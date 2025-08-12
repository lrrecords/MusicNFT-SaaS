import sqlite3

conn = sqlite3.connect("music_nft.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE id > 1")
conn.commit()
print("Kept user ID 1, deleted others")
conn.close()