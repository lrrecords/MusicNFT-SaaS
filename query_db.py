import sqlite3

conn = sqlite3.connect("music_nft.db")
cursor = conn.cursor()

print("Users:")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

print("\nNFTs:")
cursor.execute("SELECT * FROM nfts")
for row in cursor.fetchall():
    print(row)

print("\nComments:")
cursor.execute("SELECT * FROM comments")
for row in cursor.fetchall():
    print(row)

conn.close()