# RuDoEu — Financial Dashboard

> **Ru**pee · **Do**llar · **Eu**ro — A real-time financial dashboard built for NRIs living in Europe.

🌐 **Live:** [https://rudoeu.com](https://rudoeu.com)

---

## Overview

RuDoEu is a single-file, client-side financial dashboard that brings together Indian, US, and European market data in one place — designed specifically for NRIs who need to track all three financial worlds simultaneously.

Built as a personal project by an embedded systems engineer, it demonstrates front-end development, REST API integration, and real-time data handling — all in a zero-dependency, single HTML file.

---

## Features

### 📊 Market Coverage
| Region | Markets Covered |
|---|---|
| 🇮🇳 **India** | Sensex, Nifty, BSE/NSE data, RBI rates, INR/EUR/USD FX |
| 🇪🇺 **Europe** | ECB rates, European indices, EUR/USD, defence & energy stocks |
| 🇺🇸 **USA** | S&P 500, Fed rate, USD indices, major US equities |

### 📰 News Feed
- Financial news filtered by region — India (6), Europe (5), USA (6)
- All 17 headlines view
- Powered by Marketaux API (user-supplied key, stored locally)

### 💹 Dashboard Panels
- Live market status indicators (Open / Closed)
- FX rate ticker
- Sector performance heatmap
- Banking & Investment Hub
- Scrolling breaking news ticker

---

## Tech Stack

| Layer | Technology | Language | Lines of Code |
|---|---|---|---|
| **Frontend – HTML** | HTML5 (structure, layout, components) | HTML | ~292 |
| **Frontend – CSS** | CSS3 (variables, animations, responsive) | CSS | ~178 |
| **Frontend – JS** | Vanilla JavaScript (data, logic, UI) | JavaScript | ~925 |
| **Backend** | GitHub Actions (Python script — auto news fetch every 6h) | Python | ~120 |
| **Data / APIs** | RSS Feeds (server-side) · open.er-api.com · Marketaux API | REST / JSON | — |
| **Hosting** | GitHub Pages *(initially on Netlify)* | — | — |
| **Dependencies** | Zero — single self-contained HTML file | — | **1,727 total** |


## Setup & Usage

### Option 1 — Just open it
Visit [rudoeu.com](https://rudoeu.com) — no installation needed.

### Option 2 — Run locally
```bash
git clone https://github.com/kamalkadakara/RuDoEu
cd RuDoEu
# Open index.html directly in your browser
open index.html
```

#
## Project Structure

```
RuDoEu/
├── index.html          # Complete single-file app (HTML + CSS + JS)
├── README.md
└── .gitignore
```

---

## Design Decisions

- **Single file architecture** — zero build step, zero dependencies, easy to audit and deploy
- **Client-side only** — no backend, no server costs, no data storage
- **API key via localStorage + prompt** — keeps keys out of source code entirely
- **GitHub Pages deployment** — auto-deploys on every push to main branch

---

## Screenshots

> Dashboard showing Indian, European, and US market panels with live news feed.
> *(Add screenshots here)*

---

## Roadmap

- [ ] Premium membership tier with additional data feeds
- [ ] Saved watchlist (localStorage)
- [ ] INR/EUR/USD calculator widget
- [ ] Mobile-optimised layout
- [ ] Dark / light theme toggle

---

## Author

**Kamal Kadakara**
Embedded Systems & Functional Safety Engineer | Wolfsburg, Germany

- 🔗 [LinkedIn](https://linkedin.com/in/kamalkadakara)
- 💻 [GitHub](https://github.com/kamalkadakara)
- 🌐 [rudoeu.com](https://rudoeu.com)

---

## Disclaimer

This dashboard is for **informational purposes only**. It does not constitute financial advice. Market data may be delayed. Always verify with official sources before making financial decisions.

---

## License

MIT License — free to use, modify, and distribute with attribution.
