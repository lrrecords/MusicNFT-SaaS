from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from web3 import Web3
import httpx
import requests
import sqlite3
from typing import List
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = HTTPBearer()

PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_KEY = os.getenv("PINATA_SECRET_KEY")
POLYGON_RPC_URL = os.getenv("POLYGON_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
SECRET_KEY = os.getenv("SECRET_KEY")

# w3 = Web3(Web3.HTTPProvider(POLYGON_RPC_URL))

conn = sqlite3.connect("music_nft.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT, wallet_address TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS nfts (id INTEGER PRIMARY KEY, token_id INTEGER, artist_id INTEGER, ipfs_url TEXT, metadata TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, nft_id INTEGER, user_id INTEGER, content TEXT)''')
conn.commit()

class User(BaseModel):
    email: str
    password: str
    wallet_address: str

class TokenRequest(BaseModel):
    email: str
    password: str

class NFTCreate(BaseModel):
    title: str
    genre: str
    royalties: List[dict]

class Comment(BaseModel):
    nft_id: int
    content: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(email: str):
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    if user:
        return {"id": user[0], "email": user[1], "password": user[2], "wallet_address": user[3]}
    return None

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user(email)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/register")
async def register(user: User):
    hashed_password = pwd_context.hash(user.password)
    cursor.execute("INSERT INTO users (email, password, wallet_address) VALUES (?, ?, ?)",
                   (user.email, hashed_password, user.wallet_address))
    conn.commit()
    return {"message": "User registered"}

@app.post("/token")
async def login(form_data: TokenRequest):
    user = get_user(form_data.email)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": form_data.email}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

@app.post("/nfts")
async def create_nft(nft: str, file: UploadFile = File(...), user: dict = Depends(get_current_user)):
    try:
        nft_data = json.loads(nft)
        nft_model = NFTCreate(**nft_data)
    except (json.JSONDecodeError, ValueError):
        raise HTTPException(status_code=422, detail="Invalid NFT JSON")
    file_content = await file.read()
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {"pinata_api_key": PINATA_API_KEY, "pinata_secret_api_key": PINATA_SECRET_KEY}
    files = {"file": (file.filename, file_content)}
    response = requests.post(url, headers=headers, files=files)
    response.raise_for_status()
    ipfs_hash = response.json()["IpfsHash"]
    ipfs_url = f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"
    cursor.execute("INSERT INTO nfts (token_id, artist_id, ipfs_url, metadata) VALUES (?, ?, ?, ?)",
                   (0, user["id"], ipfs_url, str(nft_model.dict())))
    conn.commit()
    return {"token_id": 0, "ipfs_url": ipfs_url}

@app.get("/dashboard")
async def get_dashboard(user: dict = Depends(get_current_user)):
    cursor.execute("SELECT * FROM nfts WHERE artist_id = ?", (user["id"],))
    nfts = cursor.fetchall()
    return [{"token_id": nft[1], "ipfs_url": nft[3], "metadata": nft[4]} for nft in nfts]

@app.get("/marketplace")
async def get_marketplace(genre: str = None):
    query = "SELECT * FROM nfts"
    params = []
    if genre:
        query += " WHERE metadata LIKE ?"
        params.append(f'%{genre}%')
    cursor.execute(query, params)
    nfts = cursor.fetchall()
    return [{"token_id": nft[1], "ipfs_url": nft[3], "metadata": nft[4]} for nft in nfts]

@app.post("/comments")
async def post_comment(comment: Comment, user: dict = Depends(get_current_user)):
    cursor.execute("INSERT INTO comments (nft_id, user_id, content) VALUES (?, ?, ?)",
                   (comment.nft_id, user["id"], comment.content))
    conn.commit()
    return {"message": "Comment posted"}

@app.get("/comments/{nft_id}")
async def get_comments(nft_id: int):
    cursor.execute("SELECT * FROM comments WHERE nft_id = ?", (nft_id,))
    comments = cursor.fetchall()
    return [{"user_id": c[1], "content": c[2]} for c in comments]

@app.post("/share")
async def share_nft(token_id: int, platform: str, user: dict = Depends(get_current_user)):
    cursor.execute("SELECT * FROM nfts WHERE token_id = ? AND artist_id = ?", (token_id, user["id"]))
    nft = cursor.fetchone()
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    share_url = f"https://yourapp.com/nft/{token_id}"
    return {"message": f"NFT shared on {platform}", "url": share_url}