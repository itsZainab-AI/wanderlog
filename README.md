# Wanderlog — Your AI Travel Buddy

**Live demo → [wanderlog-u89f.onrender.com](https://wanderlog-u89f.onrender.com/)**

*(hosted on Render's free tier — if it's been idle a while, the first load can take 30–50 seconds to wake up. Worth the wait.)*

An AI-powered travel itinerary planner that generates real, destination-specific day-by-day trip plans — not generic "visit a museum" filler — and presents them with an editorial, human-touch design instead of a typical AI-dashboard look.

## What it does

- **Generates a full itinerary** from your destination, trip length, pace, budget, and interests — real named places, not categories
- **Editable on the fly** — regenerate a single day, swap an activity, or adjust the pace without starting over
- **Chat with your trip** — a built-in travel buddy that knows your itinerary and answers questions about it
- **Local tips baked into every day** — not just a list of attractions, but the kind of detail a well-traveled friend would mention

## Tech stack

- **Backend:** FastAPI (Python) + SQLAlchemy
- **AI:** Google Gemini API — `gemini-3.6-flash` for itinerary generation, `gemini-3.5-flash-lite` for chat
- **Frontend:** Vanilla HTML/CSS/JS, served directly by the FastAPI backend
- **Deployment:** Render

## Running it locally

```bash
git clone https://github.com/itsZainab-AI/wanderlog.git
cd wanderlog/backend

python -m venv venv
venv\Scripts\Activate.ps1   # Windows PowerShell
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file in `backend/` with:
```
GOOGLE_API_KEY=your-gemini-api-key-here
```
(get a free key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey))

Then run:
```bash
uvicorn main:app --reload --port 8000
```
Visit `http://localhost:8000`.

## Project structure

```
wanderlog/
├── backend/
│   ├── main.py           # FastAPI app, itinerary + chat generation
│   ├── requirements.txt
│   └── ...
└── frontend/
    └── index.html         # Single-page app UI
```

---

Built by [Zainab](https://github.com/itsZainab-AI) —  AI/ML student.