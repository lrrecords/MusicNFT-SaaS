# EasyFunnels Integration Guide for LR Records Music NFT Platform

This guide specifically covers how to integrate your Music NFT platform into your existing lrrecords.com.au website hosted on EasyFunnels.

## 🎯 Integration Options

### Option 1: Iframe Embed (Recommended - Easiest)

This is the simplest way to embed your Music NFT platform into any EasyFunnels page.

#### Step 1: Deploy Your Backend
1. Deploy the Flask backend (`MusicNFTSaaS`) to a cloud provider:
   - **Heroku** (easiest): `git push heroku main`
   - **Railway**: Connect GitHub repo
   - **DigitalOcean App Platform**: Upload code
   - **AWS/Google Cloud**: Use their app services

#### Step 2: Get Your App URL
After deployment, you'll get a URL like:
- `https://your-app-name.herokuapp.com`
- `https://your-app.railway.app`
- `https://your-app.ondigitalocean.app`

#### Step 3: Add to EasyFunnels
In your EasyFunnels page editor:

```html
<!-- Full Page Embed -->
<iframe 
  src="https://your-deployed-app.com" 
  width="100%" 
  height="900px" 
  frameborder="0"
  style="
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    background: #000;
  ">
</iframe>

<!-- Section Embed -->
<div style="padding: 20px; background: #000;">
  <iframe 
    src="https://your-deployed-app.com" 
    width="100%" 
    height="600px" 
    frameborder="0"
    style="border-radius: 8px;">
  </iframe>
</div>
```

### Option 2: Direct File Integration

If you want tighter integration with your EasyFunnels site:

#### Step 1: Extract Frontend Files
From `MusicNFTFrontend/dist/`:
- `index.html` - Main HTML
- `assets/` folder - CSS and JavaScript files

#### Step 2: Modify for EasyFunnels
1. **Update API endpoints** in the JavaScript files to point to your deployed backend
2. **Integrate styling** with your existing EasyFunnels theme
3. **Upload files** to EasyFunnels custom code sections

#### Step 3: Custom Code Integration
In EasyFunnels, add to your page:

```html
<!-- In the <head> section -->
<link rel="stylesheet" href="path/to/your/assets/index-DJb3JbMz.css">

<!-- In the <body> section -->
<div id="music-nft-app"></div>
<script src="path/to/your/assets/index-jfyiTOQ-.js"></script>
```

## 🚀 Quick Deploy Solutions

### Heroku Deployment (Recommended)

1. **Install Heroku CLI**
2. **Create Heroku app:**
   ```bash
   cd MusicNFTSaaS
   heroku create your-app-name
   ```

3. **Add environment variables:**
   ```bash
   heroku config:set PRIVATE_KEY=your_private_key
   heroku config:set CONTRACT_ADDRESS=0x1c6D8D2C85d65b20413532a2b464b59f0CEA07d8
   ```

4. **Deploy:**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

5. **Your app will be live at:** `https://your-app-name.herokuapp.com`

### Railway Deployment

1. **Connect GitHub repo** to Railway
2. **Set environment variables** in Railway dashboard
3. **Deploy automatically** on git push

## 🎨 Styling Integration

### Match Your EasyFunnels Theme

Update the CSS variables in `MusicNFTFrontend/src/App.css`:

```css
:root {
  /* Match your lrrecords.com.au colors */
  --color-primary: #your-primary-color;
  --color-secondary: #your-secondary-color;
  --color-accent: #your-accent-color;
  
  /* Keep the music theme */
  --color-gold: #FFD700;
  --color-teal: #14B8A6;
  --color-dark: #0F0F0F;
}
```

### Custom Branding

Replace in `MusicNFTFrontend/src/App.jsx`:

```jsx
// Update header section
<div className="flex items-center space-x-3">
  <img src="/your-logo.png" alt="LR Records" className="w-10 h-10" />
  <div>
    <h1 className="text-2xl font-bold text-white">LRRecords</h1>
    <p className="text-teal-400 text-sm">Music NFT Platform</p>
  </div>
</div>
```

## 📱 Mobile Optimization

The app is already mobile-responsive, but for EasyFunnels integration:

```html
<!-- Mobile-optimized iframe -->
<div style="position: relative; width: 100%; overflow: hidden;">
  <iframe 
    src="https://your-app.com" 
    style="
      width: 100%; 
      height: 80vh; 
      min-height: 600px;
      border: none;
      border-radius: 10px;
    ">
  </iframe>
</div>
```

## 🔧 Configuration for EasyFunnels

### Environment Setup

Create a production configuration:

**MusicNFTSaaS/config.py:**
```python
import os

class Config:
    # Your deployed backend URL
    API_BASE_URL = os.environ.get('API_BASE_URL', 'https://your-app.herokuapp.com')
    
    # CORS settings for EasyFunnels
    CORS_ORIGINS = [
        'https://lrrecords.com.au',
        'https://*.easyfunnels.com',
        'https://your-custom-domain.com'
    ]
    
    # Contract settings
    CONTRACT_ADDRESS = '0x1c6D8D2C85d65b20413532a2b464b59f0CEA07d8'
    NETWORK = 'Polygon Amoy'
```

### CORS Configuration

Update `MusicNFTSaaS/src/main.py`:

```python
from flask_cors import CORS

# Allow your EasyFunnels domain
CORS(app, origins=[
    'https://lrrecords.com.au',
    'https://*.easyfunnels.com'
])
```

## 🎵 Page Integration Examples

### Landing Page Integration

```html
<!-- Hero section with embedded app -->
<section style="background: linear-gradient(135deg, #000, #1F2937); padding: 60px 20px;">
  <div style="max-width: 1200px; margin: 0 auto;">
    <h1 style="color: white; text-align: center; font-size: 3rem; margin-bottom: 20px;">
      Welcome to LR Records NFT Platform
    </h1>
    <p style="color: #14B8A6; text-align: center; font-size: 1.2rem; margin-bottom: 40px;">
      Mint, collect, and trade music NFTs
    </p>
    
    <!-- Embedded Music NFT App -->
    <iframe 
      src="https://your-app.herokuapp.com" 
      width="100%" 
      height="800px" 
      frameborder="0"
      style="border-radius: 15px; box-shadow: 0 20px 40px rgba(20, 184, 166, 0.2);">
    </iframe>
  </div>
</section>
```

### Dedicated NFT Page

Create a new page in EasyFunnels called "Music NFTs" and embed the full app:

```html
<!DOCTYPE html>
<html>
<head>
    <title>LR Records - Music NFTs</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; padding: 0; background: #000; }
        .nft-container { width: 100%; height: 100vh; }
    </style>
</head>
<body>
    <div class="nft-container">
        <iframe 
            src="https://your-app.herokuapp.com" 
            width="100%" 
            height="100%" 
            frameborder="0">
        </iframe>
    </div>
</body>
</html>
```

## 🔗 Navigation Integration

Add to your EasyFunnels navigation menu:

```html
<a href="/music-nfts" style="color: #14B8A6; font-weight: bold;">
    🎵 Music NFTs
</a>
```

## 📊 Analytics Integration

Track usage in your EasyFunnels analytics:

```html
<!-- Add to your iframe page -->
<script>
  // Track NFT page views
  gtag('event', 'page_view', {
    page_title: 'Music NFT Platform',
    page_location: window.location.href
  });
</script>
```

## 🚨 Troubleshooting

### Common Issues:

1. **CORS Errors**: Add your EasyFunnels domain to CORS settings
2. **Mobile Display**: Use responsive iframe CSS
3. **Loading Speed**: Optimize images and enable gzip compression
4. **SSL Issues**: Ensure both your app and EasyFunnels use HTTPS

### Testing Checklist:

- [ ] App loads in iframe on desktop
- [ ] App loads in iframe on mobile
- [ ] All API calls work from EasyFunnels domain
- [ ] Styling matches your brand
- [ ] Navigation works properly

## 🎯 Next Steps

1. **Deploy backend** to your preferred hosting
2. **Test integration** on a staging EasyFunnels page
3. **Customize branding** to match lrrecords.com.au
4. **Add to main navigation** once tested
5. **Monitor performance** and user engagement

---

**Your Music NFT platform is ready to integrate with lrrecords.com.au! 🎵**

