# LRRecords - Music NFT Platform

A complete full-stack Music NFT SaaS application built for musicians, producers, and fans. This platform allows artists to mint their music as NFTs on the Polygon blockchain and provides fans with a beautiful interface to discover and collect music NFTs.


## 📁 Project Structure

```
MusicNFT_Complete_Package/
├── MusicNFTContract/          # Smart Contract (Solidity)
│   ├── contracts/
│   │   └── MusicNFT.sol      # Main NFT contract
│   ├── scripts/
│   │   └── deploy.js         # Deployment script
│   ├── hardhat.config.js     # Hardhat configuration
│   └── package.json          # Node.js dependencies
├── MusicNFTSaaS/             # Backend API (Flask/Python)
│   ├── src/
│   │   ├── routes/
│   │   │   ├── nft.py       # NFT API endpoints
│   │   │   └── user.py      # User management
│   │   ├── static/          # Built frontend files
│   │   └── main.py          # Flask app entry point
│   ├── venv/                # Python virtual environment
│   └── requirements.txt     # Python dependencies
├── MusicNFTFrontend/         # Frontend (React)
│   ├── src/
│   │   ├── App.jsx          # Main React component
│   │   ├── App.css          # Custom styling
│   │   └── components/      # UI components
│   ├── dist/                # Built production files
│   └── package.json         # Node.js dependencies
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites
- Node.js (v18+)
- Python (v3.8+)
- Git

### 1. Smart Contract Deployment

```bash
cd MusicNFTContract
npm install
npx hardhat compile
npx hardhat run scripts/deploy.js --network polygonAmoy
```

### 2. Backend Setup

```bash
cd MusicNFTSaaS
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

### 3. Frontend Development

```bash
cd MusicNFTFrontend
pnpm install  # or npm install
pnpm run dev  # or npm run dev
```

### 4. Production Build

```bash
cd MusicNFTFrontend
pnpm run build
cp -r dist/* ../MusicNFTSaaS/src/static/
```

## 🌐 Deployment Options

### Option 1: Standalone Hosting
Deploy the complete Flask app to any hosting provider (Heroku, DigitalOcean, AWS, etc.)

### Option 2: EasyFunnels Integration (Recommended for lrrecords.com.au)

#### Method A: Iframe Embed
```html
<iframe 
  src="https://your-deployed-app.com" 
  width="100%" 
  height="800px" 
  frameborder="0"
  style="border-radius: 10px;">
</iframe>
```

#### Method B: Direct Integration
1. Export the built frontend files from `MusicNFTFrontend/dist/`
2. Upload to your EasyFunnels hosting
3. Set up API proxy to your backend server

### Option 3: Vercel + Railway
- **Frontend**: Deploy to Vercel
- **Backend**: Deploy to Railway
- **Database**: Use Railway PostgreSQL

## 🔧 Configuration

### Environment Variables

Create `.env` files in both backend and contract directories:

**MusicNFTContract/.env:**
```
PRIVATE_KEY=your_wallet_private_key
ETHERSCAN_API_KEY=your_polygonscan_api_key
```

**MusicNFTSaaS/.env:**
```
PRIVATE_KEY=your_wallet_private_key
CONTRACT_ADDRESS=0x1c6D8D2C85d65b20413532a2b464b59f0CEA07d8
RPC_URL=https://rpc-amoy.polygon.technology
```

### Contract Information
- **Deployed Contract:** `0x1c6D8D2C85d65b20413532a2b464b59f0CEA07d8`
- **Network:** Polygon Amoy Testnet
- **Owner:** `0xf05fA0FcEBeE75d691aFa714EbC7ca19Ef2254E2`

## 🎨 Design System

### Color Palette
- **Primary Black:** `#000000`
- **Teal:** `#14B8A6`
- **Gold:** `#FFD700`
- **Dark Gray:** `#1F2937`

### Features
- Responsive design (mobile-first)
- Dark theme with neon accents
- Smooth animations and transitions
- Web3 wallet integration ready
- Music-themed UI elements

## 🔗 API Endpoints

### Backend API Routes

**Base URL:** `/api/nft/`

- `GET /contract-info` - Get contract details
- `POST /mint` - Mint new NFT
- `GET /tokens` - List all tokens
- `GET /user-tokens/<address>` - Get user's tokens

### Example API Usage

```javascript
// Mint NFT
const response = await fetch('/api/nft/mint', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    recipient_address: '0x...'
  })
});

// Get contract info
const info = await fetch('/api/nft/contract-info');
const data = await info.json();
```

## 🛠 Customization

### Branding
1. Update colors in `MusicNFTFrontend/src/App.css`
2. Replace logo and favicon in `MusicNFTFrontend/public/`
3. Modify text content in `MusicNFTFrontend/src/App.jsx`

### Features
1. Add new API endpoints in `MusicNFTSaaS/src/routes/`
2. Create new React components in `MusicNFTFrontend/src/components/`
3. Extend smart contract functionality in `MusicNFTContract/contracts/`

## 🚀 Production Deployment

### For lrrecords.com.au Integration

1. **Build the frontend:**
   ```bash
   cd MusicNFTFrontend
   pnpm run build
   ```

2. **Deploy backend to cloud provider**
3. **Update frontend API endpoints to point to your backend**
4. **Embed in EasyFunnels using iframe or direct integration**

### Deployment Checklist
- [ ] Update contract address in backend
- [ ] Set production environment variables
- [ ] Configure CORS for your domain
- [ ] Test all functionality
- [ ] Set up SSL certificate
- [ ] Configure domain/subdomain

## 🔐 Security Notes

- Never commit private keys to version control
- Use environment variables for sensitive data
- Implement rate limiting for API endpoints
- Validate all user inputs
- Use HTTPS in production

## 🎯 Next Steps

### Phase 2 Features
1. **User Authentication** - MetaMask wallet connection
2. **File Upload** - IPFS integration for music files
3. **Marketplace** - Buy/sell functionality
4. **Royalties** - Artist revenue tracking
5. **Social Features** - Comments, likes, sharing

### Integration Ideas
1. **Spotify Integration** - Import artist data
2. **Payment Gateway** - Fiat currency support
3. **Analytics Dashboard** - Detailed metrics
4. **Mobile App** - React Native version

## 📞 Support

For questions or support:
- **Website:** lrrecords.com.au
- **Contract:** `0x1c6D8D2C85d65b20413532a2b464b59f0CEA07d8`
- **Network:** Polygon Amoy Testnet

## 📄 License

This project is created for LR Records. All rights reserved.

---

**Built with ❤️ for the music community**

