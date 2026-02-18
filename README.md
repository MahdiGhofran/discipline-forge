<div align="center">

# Discipline Forge

### Your Premium Productivity Command Center

*Track habits. Build discipline. Achieve greatness.*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-6c5ce7.svg)](LICENSE)

---

</div>

## Overview

**Discipline Forge** is a premium, gamified productivity dashboard designed for two-person accountability partnerships. Built with Streamlit, it combines habit tracking, task management, self-assessment, and a penalty system into a single motivating interface.

The app is designed around a core philosophy: **consistency beats intensity**. Every feature is built to reinforce daily discipline through visual feedback, streak tracking, progressive penalties, and long-term milestone rewards.

---

## Features

### Authentication & Multi-User Support
- Two dedicated user profiles with private access codes
- Fully separated data storage per user
- Session-based authentication with secure SHA-256 hashed passwords

### Wake-Up Time Tracker
- Log daily wake-up times with a single tap
- Consecutive day streak counter with visual fire badge
- 7-day history at a glance
- Consistency indicator to track morning routine stability

### Three Daily Jobs
- Define exactly 3 main tasks each day
- Mark tasks as complete with instant visual feedback
- Real-time completion percentage with progress ring
- Weekly and monthly progress bars to track trends

### Daily Performance Assessment
- **6-dimension evaluation system** that replaces subjective self-rating:
  - Focus & Concentration
  - Energy & Physical State
  - Self-Discipline & Willpower
  - Time Management
  - Quality of Work
  - Learning & Growth
- 4-point scale per dimension (total: 24 points, normalized to 10)
- Auto-calculated performance score with letter grade (A–D)
- Radar chart visualization of daily strengths and weaknesses
- Historical score trend chart over time

### Penalty System (Gamified Discipline Engine)
- Base penalty: **50 Toman**
- Progressive increase per failure within each month:
  - 1st failure → 50 T
  - 2nd failure → 100 T
  - 3rd failure → 150 T
  - *...continues incrementing by +50 per failure*
- Monthly penalty accumulator with real-time display
- Auto-resets on the first of each month
- Visual penalty schedule showing current position

### Instagram Limitation Tracker
- **Daily limit: 45 minutes**
- Quick selection from predefined usage ranges (no manual typing)
- Real-time violation detection:
  - Within limit → green confirmation
  - Over limit → automatic penalty applied
- Usage percentage ring showing proximity to limit
- Color-coded weekly bar chart with limit line overlay

### Long-Term Motivation Roadmap
Two milestone-driven phases over 12 months:

| Phase | Duration | Reward | Focus |
|-------|----------|--------|-------|
| **Phase 1** | Months 1–6 | Sightseeing Trip | Personal discipline & habit building |
| **Phase 2** | Months 7–12 | Travel Reward | Business launch & skill development |

- Countdown timers for each phase
- Progress bars based on elapsed time
- Milestone checklists that persist across sessions

### Achievement Badges
Dynamic badges earned through consistency:
- **Early Riser** — 3+ day wake-up streak
- **Week Warrior** — 7+ day wake-up streak
- **Month Master** — 30+ day wake-up streak
- **Task Crusher** — 80%+ monthly task completion
- **Perfect Score** — 100% task completion
- **Digital Discipline** — Zero Instagram violations
- **High Performer** — Average assessment score above 8
- **Clean Record** — No penalties this month

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | [Streamlit](https://streamlit.io) |
| Charts | [Plotly](https://plotly.com/python/) |
| Data Storage | JSON (file-based, per-user) |
| Styling | Custom CSS with Inter font |
| Language | Python 3.10+ |

---

## Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/MahdiGhofran/discipline-forge.git
cd discipline-forge

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

### Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository, branch `main`, file `app.py`
5. Click **Deploy**

Your app will be live at `https://your-app-name.streamlit.app`

---

## Default Access Codes

| User | Access Code |
|------|-------------|
| Mahdi | `mahdi2026` |
| Daniel | `daniel2026` |

> To change access codes, update the `USERS` dictionary in `app.py` with new SHA-256 hashes.

---

## Project Structure

```
discipline-forge/
├── app.py                  # Main application (all features)
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit theme & server config
├── .gitignore              # Excludes data/ and cache files
├── README.md               # This file
└── data/                   # Auto-created, stores user JSON files
    ├── mahdi_data.json     # Mahdi's data (gitignored)
    └── daniel_data.json    # Daniel's data (gitignored)
```

---

## Design Philosophy

- **Dark Theme** — Soft dark palette with purple, teal, and gold accents to reduce eye strain and feel premium
- **Zero Clutter** — Tab-based navigation keeps the dashboard clean and focused
- **Gamification** — Streaks, badges, penalties, and progress rings create positive feedback loops
- **Accountability** — Two-user system with shared penalty rules builds mutual accountability
- **Psychology-Driven** — Daily rotating motivational quotes and visual progress reinforce habit formation

---

## Data Persistence

User data is stored as JSON files in the `data/` directory. On Streamlit Cloud, this data persists during the app's active lifecycle but may reset on reboot. For permanent cloud storage, consider integrating:
- Google Sheets API
- Supabase
- Firebase Realtime Database

---

<div align="center">

**Built for Champions** · Stay consistent. Stay hungry. Stay disciplined.

</div>
