# 🛡️ Pramod Jadhav — AI SOC Portfolio

> Production-ready AI-powered portfolio website for an AI SOC Analyst / Cybersecurity ML Engineer.

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **Cyber Noir UI** | Dark theme, grid background, glow effects, JetBrains Mono typography |
| ⚡ **Typing Animation** | Auto-cycles 5 role titles |
| 📊 **Animated Skill Bars** | Triggered by scroll intersection observer |
| 🔴 **Live AI Demo** | 6-parameter threat scoring engine with real-time risk score |
| 🤖 **AI Chatbot** | Claude-powered assistant with SOC/cybersecurity system prompt |
| 🌙 **Dark/Light Mode** | Full CSS variable theming |
| 📱 **Mobile Responsive** | CSS Grid + Flexbox, hamburger menu |
| 🔒 **Secure Backend** | Helmet, CORS, rate limiting, env variables |

---

## 📁 Folder Structure

```
pramod-portfolio/
├── pramod_jadhav_portfolio.html   ← Single-file frontend (deploy directly)
├── README.md
└── backend/
    ├── server.js                  ← Express entry point
    ├── package.json
    ├── .env                       ← (create this — DO NOT commit)
    ├── routes/
    │   └── chat.js
    └── controllers/
        └── chatController.js
```

---

## 🚀 Quick Start

### Frontend Only (Simplest)

The `pramod_jadhav_portfolio.html` file works standalone.

1. Open in any browser — all features work without a backend
2. For the chatbot: enter your Claude API key in the key input on the chat section
3. Your key is stored only in `sessionStorage` (never sent anywhere else)

### With Backend (Recommended for Production)

**1. Install backend dependencies:**
```bash
cd backend
npm install
```

**2. Create `.env` file:**
```env
ANTHROPIC_API_KEY=sk-ant-api03-YOUR_KEY_HERE
FRONTEND_URL=https://your-portfolio.netlify.app
PORT=3001
```

**3. Run locally:**
```bash
npm run dev
```

**4. Update frontend chatbot URL:**
In `pramod_jadhav_portfolio.html`, find the `callAPI` function and replace:
```javascript
// Replace direct API call with:
const resp = await fetch('https://your-backend.onrender.com/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ messages: chatHistory })
});
const d = await resp.json();
return d.reply;
```

---

## 🌐 Deployment

### Frontend → Netlify (Free)

1. Go to [netlify.com](https://netlify.com) → Sign up → "Add new site"
2. Choose **"Deploy manually"**
3. Drag and drop `pramod_jadhav_portfolio.html` into the deploy box
4. Done! You get a URL like `pramod-jadhav.netlify.app`

**Custom Domain:**
- Netlify Dashboard → Domain Management → Add custom domain
- Update your domain registrar DNS: CNAME `www` → `pramod-jadhav.netlify.app`
- HTTPS is automatic via Let's Encrypt

### Backend → Render (Free)

1. Push your `backend/` folder to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Settings:
   - Build Command: `npm install`
   - Start Command: `npm start`
   - Environment: `Node`
5. Add environment variables:
   - `ANTHROPIC_API_KEY` = your key
   - `FRONTEND_URL` = your Netlify URL
6. Deploy — you get a URL like `pramod-api.onrender.com`

---

## 🔑 Getting a Claude API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up for free
3. API Keys → Create Key
4. Free tier includes $5 credit (~500+ chatbot conversations)

---

## 🎯 Customization Checklist

- [ ] Replace `your@email.com` with real email
- [ ] Update GitHub and LinkedIn URLs
- [ ] Add real resume PDF — update `href` on resume buttons
- [ ] Add your photo — update the hero avatar emoji or `<img>` tag
- [ ] Update phone number in contact section
- [ ] Add your actual degree in About timeline
- [ ] Update GitHub links on project cards

---

## 🛠️ Tech Stack

**Frontend:** Pure HTML5, CSS3 (custom design system), Vanilla JS  
**AI:** Anthropic Claude API (claude-sonnet-4-20250514)  
**Backend:** Node.js, Express, Helmet, express-rate-limit  
**Fonts:** JetBrains Mono, Syne (Google Fonts)  
**Deployment:** Netlify (frontend) + Render (backend)  

---

## 📄 License

MIT — use freely, attribution appreciated.

---

*Built to demonstrate the rare combination of deep SOC operations expertise and modern AI/ML engineering.*
