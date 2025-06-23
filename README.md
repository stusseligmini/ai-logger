# Telegram AI Analyzer

En AI-drevet Telegram-melding analyzer som overvåker grupper for spam, bot-aktivitet og genererer varsler.

## Funksjoner

- 🔍 **Telegram Scraping**: Henter meldinger fra Telegram-grupper
- 🤖 **Bot Detection**: Identifiserer mistenkelig bot-aktivitet
- 📊 **Real-time Dashboard**: Viser analyser og varsler i sanntid
- ⚠️ **Alert System**: Genererer varsler basert på aktivitetsmønstre
- 📈 **Analytics**: Kategoriserer meldinger og beregner risikonivå

## Installasjon

### 1. Klone prosjektet
```bash
git clone <repository-url>
cd ai
```

### 2. Installer avhengigheter
```bash
pip install -r requirements.txt
```

### 3. Sett opp miljøvariabler
Opprett en `.env` fil med følgende innhold:
```env
# Telegram API credentials
TELEGRAM_API_ID=your_api_id_here
TELEGRAM_API_HASH=your_api_hash_here
TELEGRAM_GROUP_URL=https://t.me/your_group_here

# MongoDB connection
MONGO_URI=mongodb://localhost:27017

# Optional: Server settings
HOST=0.0.0.0
PORT=8000
```

### 4. Start MongoDB
```bash
# Installer MongoDB hvis du ikke har det
# Start MongoDB service
```

### 5. Kjør applikasjonen
```bash
uvicorn main:app --reload
```

## Bruk

1. Åpne nettleseren og gå til `http://localhost:8000`
2. Dashboardet vil vise:
   - Risikonivå basert på bot-aktivitet
   - Liste over siste meldinger
   - Varsellogg
   - Live oppdateringer hvert 5. sekund

## API Endepunkter

- `GET /api/latest_messages` - Hent siste meldinger
- `GET /api/alerts` - Hent varsler

## Docker

For å kjøre med Docker:

```bash
docker build -t telegram-ai-analyzer .
docker run -p 8000:8000 --env-file .env telegram-ai-analyzer
```

## Struktur

```
ai/
├── main.py                 # FastAPI app
├── requirements.txt        # Python avhengigheter
├── db/
│   └── database.py        # MongoDB operasjoner
├── routes/
│   └── scraper.py         # API routes
├── scraper/
│   └── telegram_scraper.py # Telegram scraping
├── ai/
│   └── analyzer.py        # AI analyse
├── static/
│   ├── main.js           # Frontend JavaScript
│   └── style.css         # Styling
└── templates/
    └── dashboard.html    # Dashboard template
```

## Sikkerhet

- Bruk miljøvariabler for sensitive data
- Begrens API-tilgang til nødvendige endepunkter
- Overvåk MongoDB-tilgang

## Bidrag

1. Fork prosjektet
2. Opprett en feature branch
3. Commit endringene
4. Push til branchen
5. Opprett en Pull Request 