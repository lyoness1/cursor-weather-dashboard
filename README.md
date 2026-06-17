# Cursor Weather Dashboard

A single-page weather dashboard built with Tailwind CSS and the OpenWeatherMap API. Search any city to see current conditions, humidity, and a 5-day forecast. Demo data is shown automatically when no API key is configured.

## Get an OpenWeatherMap API key

1. Create a free account at [openweathermap.org](https://home.openweathermap.org/users/sign_up).
2. Open [API keys](https://home.openweathermap.org/api_keys) in your account.
3. Copy the default key (or create a new one).
4. **Wait for activation** — new keys can take up to 2 hours before they work.
5. (Recommended) Restrict the key by HTTP referrer for local dev: `http://localhost:8080/*`

## Local setup

### 1. Clone and add your key

```bash
git clone https://github.com/lyoness1/cursor-weather-dashboard.git
cd cursor-weather-dashboard
cp .env.example .env
```

Edit `.env` and set your key:

```env
OPENWEATHERMAP_API_KEY=your_key_here
```

`.env` is gitignored and will not be committed.

### 2. Run locally

```bash
python3 scripts/load_env.py && python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

`load_env.py` reads `.env` and writes `config.local.js` (also gitignored). `index.html` loads that file — your key never goes in tracked source code.

### Without `.env`

Open `index.html` directly or skip `load_env.py` — the app uses demo data, or you can paste a key in the **API Configuration** panel (stored in browser `localStorage` only).

> **Note:** This app runs in the browser, so the key is visible in DevTools when making API calls. Restrict it in your OpenWeatherMap account.

## Project structure

```
├── index.html
├── scripts/load_env.py   # .env → config.local.js
├── .env.example
├── .env                  # your key (not committed)
├── config.local.js       # generated locally (not committed)
└── README.md
```
