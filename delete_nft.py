import sqlite3
conn = sqlite3.connect("music_nft.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM nfts WHERE id = 2")
conn.commit()
conn.close()
print("Deleted NFT ID 2")