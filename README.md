# Know Your Prospect

![Know Your Prospect](assets/cover.png)

An interactive learning experience for cold-call prep: drill **who** you're calling — what each Copado prospect cares about, how the work hits their role, what makes them take a meeting — and practice your judgment under pressure.

Built on **29 buyer personas** across **4 altitudes** (doer → manager → technical authority → executive), spanning the Salesforce ecosystem and Copado's positioning (DevOps pipelines, robotic testing, governance, AI/Agentforce).

---

## Run it

No build tools, no server. Just open the app:

```
open index.html      # macOS
```

Or double-click `index.html`. It runs fully offline in any modern browser. Your progress (spaced-repetition schedules, scores, custom personas) is saved in the browser's local storage on your machine.

---

## What's inside

Six practice modes, all driven by the persona data:

| Mode | What it trains |
|------|----------------|
| 🃏 **Flashcards** | Spaced repetition on the facts — missed cards resurface sooner. |
| ✅ **Quiz + confidence** | Multiple choice; being *confidently wrong* costs more than admitting doubt. |
| 🎭 **Scenarios** | Branching role-play — each move advances, stalls, or kills the call. |
| 🕵️ **Guess Who** | A prospect quote fires; name the persona. |
| 🛡️ **Objection volley** | Objections come at you; recall the response, self-rate. |
| 📇 **Persona library** | The full dossier on any prospect, any time. |

Plus a **mastery-by-dimension** dashboard so you can see where you're sharp and where you're weak.

---

## Data model — the single source of truth

Everything lives in **`data/prospect-intelligence.json`**. The app reads from it; nothing is hard-coded in the UI. Each persona carries:

- An **altitude** (`doer` / `manager` / `technical-authority` / `exec`) — this teaches you to shift your pitch by who you're talking to.
- **7 dimensions** — `cares`, `roleImpact`, `discoveryQuestions`, `salesforceReality`, `copadoImpact`, `competingPriorities`, `meetingTrigger` — each with a summary + sharp points.
- A **quiz block** generated from those dimensions: `flashcards`, `mcq` (each tagged to a dimension), `scenarios` (branching, with `advances`/`stalls`/`kills` outcomes), `objections`, and a `quote` for the reverse "guess the persona" game.

Because every quiz item is tagged to a dimension, the app scores you *per dimension*, not as one blob.

### Editing the data

1. Edit `data/prospect-intelligence.json`.
2. Rebuild the app: `python3 build/build.py` (re-embeds the data into `index.html`).

The app also has an in-browser **"+ Add persona"** importer: paste a filled template (a friendly labeled format — copy the blank from inside the app), and the persona is live immediately and saved locally. Use **"Export all personas (JSON)"** in the app to pull your additions back out and commit them to `data/prospect-intelligence.json`.

---

## Repo layout

```
know-your-prospect/
├── index.html                      # the app (data embedded, ready to open)
├── data/
│   └── prospect-intelligence.json  # SOURCE OF TRUTH — 29 personas
├── build/
│   ├── template.html               # app shell with a __SEED__ placeholder
│   └── build.py                    # injects the JSON into the template -> index.html
├── assets/
│   ├── cover.png                   # project visual (also the GitHub social preview)
│   └── design-philosophy.md        # "Quiet Telemetry" — the visual philosophy behind the cover
├── .gitignore
└── README.md
```

> **Set the cover as your repo's social preview:** GitHub → repo **Settings → General → Social preview → Upload** `assets/cover.png`.

---

## Notes

- The app is intentionally one self-contained file so it works from disk with zero setup. `build.py` only matters when you change the data.
- Persona content reflects Copado's Salesforce DevOps positioning and is meant as a sales-enablement training aid, not official product documentation.
