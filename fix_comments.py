import sqlite3
conn = sqlite3.connect("music_nft.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM comments WHERE nft_id = 1")
conn.commit()
conn.close()
print("Removed invalid comments")