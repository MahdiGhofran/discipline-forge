"""
Work & Discipline Tracker — Premium Productivity Dashboard
Built with Streamlit · Designed for Mahdi & Daniel
"""

import streamlit as st
import json
import os
import hashlib
from datetime import datetime, date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import calendar
import random

# ─── Configuration ───────────────────────────────────────────────────────────

APP_TITLE = "Discipline Forge"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
START_DATE = date(2026, 2, 17)

USERS = {
    "mahdi": {
        "name": "Mahdi",
        "code_hash": hashlib.sha256("mahdi2026".encode()).hexdigest(),
    },
    "daniel": {
        "name": "Daniel",
        "code_hash": hashlib.sha256("daniel2026".encode()).hexdigest(),
    },
}

QUOTES = [
    "Discipline is the bridge between goals and accomplishment. — Jim Rohn",
    "We are what we repeatedly do. Excellence is not an act, but a habit. — Aristotle",
    "The secret of getting ahead is getting started. — Mark Twain",
    "Success is the sum of small efforts repeated day in and day out. — Robert Collier",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "The pain of discipline is nothing like the pain of disappointment. — Justin Langer",
    "Motivation gets you going, but discipline keeps you growing. — John C. Maxwell",
    "It's not about perfect. It's about effort. — Jillian Michaels",
    "You will never always be motivated. You have to learn to be disciplined. — Unknown",
    "Small disciplines repeated with consistency lead to great achievements. — John C. Maxwell",
    "Hard work beats talent when talent doesn't work hard. — Tim Notke",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Winners embrace hard work. — Lou Holtz",
    "Push yourself, because no one else is going to do it for you. — Unknown",
    "Great things never come from comfort zones. — Unknown",
    "Dream it. Wish it. Do it. — Unknown",
    "Success doesn't just find you. You have to go out and get it. — Unknown",
    "Wake up with determination. Go to bed with satisfaction. — Unknown",
    "Do something today that your future self will thank you for. — Sean Patrick Flanery",
    "The harder you work for something, the greater you'll feel when you achieve it. — Unknown",
    "Don't stop when you're tired. Stop when you're done. — Unknown",
    "Hustle in silence and let your success make the noise. — Unknown",
    "Fall seven times, stand up eight. — Japanese Proverb",
    "Your limitation—it's only your imagination. — Unknown",
    "It always seems impossible until it's done. — Nelson Mandela",
    "Stay hungry. Stay foolish. — Steve Jobs",
    "Believe you can and you're halfway there. — Theodore Roosevelt",
    "Action is the foundational key to all success. — Pablo Picasso",
    "Strive for progress, not perfection. — Unknown",
    "The future depends on what you do today. — Mahatma Gandhi",
]

# ─── Page Config ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Premium Dark Theme CSS ─────────────────────────────────────────────────

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

:root {
    --bg-primary: #0a0a0f;
    --bg-secondary: #12121a;
    --bg-card: #1a1a2e;
    --bg-card-hover: #1f1f35;
    --border-color: #2a2a45;
    --text-primary: #e8e8f0;
    --text-secondary: #9898b0;
    --text-muted: #6868880;
    --accent-primary: #6c5ce7;
    --accent-secondary: #a29bfe;
    --accent-success: #00cec9;
    --accent-warning: #fdcb6e;
    --accent-danger: #ff6b6b;
    --accent-info: #74b9ff;
    --gradient-primary: linear-gradient(135deg, #6c5ce7, #a29bfe);
    --gradient-success: linear-gradient(135deg, #00b894, #00cec9);
    --gradient-danger: linear-gradient(135deg, #e17055, #ff6b6b);
    --gradient-warm: linear-gradient(135deg, #f39c12, #fdcb6e);
    --shadow-card: 0 4px 24px rgba(0,0,0,0.3);
    --shadow-glow: 0 0 30px rgba(108,92,231,0.15);
    --radius: 16px;
    --radius-sm: 10px;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: var(--bg-primary) !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stSidebar"] {
    background: var(--bg-secondary) !important;
    border-right: 1px solid var(--border-color) !important;
}

.stApp {
    background: var(--bg-primary) !important;
}

/* Hide default Streamlit elements */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none !important;}

/* Card Styling */
.metric-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius);
    padding: 24px;
    box-shadow: var(--shadow-card);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
.metric-card:hover {
    border-color: var(--accent-primary);
    box-shadow: var(--shadow-glow);
    transform: translateY(-2px);
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--gradient-primary);
}

.metric-card.success::before { background: var(--gradient-success); }
.metric-card.danger::before { background: var(--gradient-danger); }
.metric-card.warm::before { background: var(--gradient-warm); }

.metric-card .card-icon {
    font-size: 28px;
    margin-bottom: 8px;
}
.metric-card .card-label {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: var(--text-secondary);
    margin-bottom: 6px;
}
.metric-card .card-value {
    font-size: 32px;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1;
    margin-bottom: 4px;
}
.metric-card .card-sub {
    font-size: 13px;
    color: var(--text-secondary);
}

/* Hero Banner */
.hero-banner {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border: 1px solid var(--border-color);
    border-radius: var(--radius);
    padding: 40px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-card);
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(108,92,231,0.15), transparent 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -30%; left: -10%;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(0,206,201,0.1), transparent 70%);
    border-radius: 50%;
}
.hero-banner .hero-greeting {
    font-size: 16px;
    font-weight: 500;
    color: var(--accent-secondary);
    margin-bottom: 4px;
    position: relative;
    z-index: 1;
}
.hero-banner .hero-name {
    font-size: 36px;
    font-weight: 900;
    color: var(--text-primary);
    margin-bottom: 8px;
    position: relative;
    z-index: 1;
}
.hero-banner .hero-quote {
    font-size: 15px;
    font-style: italic;
    color: var(--text-secondary);
    max-width: 600px;
    line-height: 1.6;
    position: relative;
    z-index: 1;
}

/* Section Headers */
.section-header {
    font-size: 22px;
    font-weight: 700;
    color: var(--text-primary);
    margin: 36px 0 20px 0;
    padding-bottom: 12px;
    border-bottom: 2px solid var(--border-color);
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Badge Styles */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}
.badge-success {
    background: rgba(0,206,201,0.15);
    color: var(--accent-success);
    border: 1px solid rgba(0,206,201,0.3);
}
.badge-danger {
    background: rgba(255,107,107,0.15);
    color: var(--accent-danger);
    border: 1px solid rgba(255,107,107,0.3);
}
.badge-primary {
    background: rgba(108,92,231,0.15);
    color: var(--accent-secondary);
    border: 1px solid rgba(108,92,231,0.3);
}
.badge-warning {
    background: rgba(253,203,110,0.15);
    color: var(--accent-warning);
    border: 1px solid rgba(253,203,110,0.3);
}

/* Progress Bar */
.progress-container {
    background: var(--bg-secondary);
    border-radius: 10px;
    height: 14px;
    overflow: hidden;
    margin: 8px 0;
    border: 1px solid var(--border-color);
}
.progress-fill {
    height: 100%;
    border-radius: 10px;
    transition: width 0.6s ease;
}
.progress-fill.primary { background: var(--gradient-primary); }
.progress-fill.success { background: var(--gradient-success); }
.progress-fill.danger { background: var(--gradient-danger); }
.progress-fill.warm { background: var(--gradient-warm); }

/* Task item */
.task-item {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    padding: 16px 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.task-item.done {
    border-color: rgba(0,206,201,0.3);
    background: rgba(0,206,201,0.05);
}
.task-item .task-status {
    width: 24px; height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
}
.task-status.complete {
    background: var(--accent-success);
    color: #fff;
}
.task-status.incomplete {
    background: var(--bg-secondary);
    border: 2px solid var(--border-color);
}

/* Streak fire */
.streak-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(243,156,18,0.2), rgba(253,203,110,0.1));
    border: 1px solid rgba(243,156,18,0.3);
    padding: 10px 20px;
    border-radius: 30px;
    font-size: 18px;
    font-weight: 700;
    color: var(--accent-warning);
}

/* Penalty display */
.penalty-amount {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(135deg, #e17055, #ff6b6b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Phase card */
.phase-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius);
    padding: 28px;
    box-shadow: var(--shadow-card);
    position: relative;
    overflow: hidden;
}
.phase-card.active {
    border-color: var(--accent-primary);
    box-shadow: var(--shadow-glow);
}
.phase-card .phase-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--accent-secondary);
    margin-bottom: 8px;
}
.phase-card .phase-title {
    font-size: 20px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 6px;
}
.phase-card .phase-desc {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 16px;
}

/* Login page */
.login-container {
    max-width: 420px;
    margin: 80px auto;
    text-align: center;
}
.login-title {
    font-size: 42px;
    font-weight: 900;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
}
.login-subtitle {
    font-size: 16px;
    color: var(--text-secondary);
    margin-bottom: 40px;
}

/* Streamlit widget overrides */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stTimeInput > div > div > input,
.stSelectbox > div > div,
.stTextArea > div > div > textarea {
    background-color: var(--bg-card) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: var(--radius-sm) !important;
    font-family: 'Inter', sans-serif !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--accent-primary) !important;
    box-shadow: 0 0 0 2px rgba(108,92,231,0.2) !important;
}

div[data-testid="stFormSubmitButton"] > button,
.stButton > button {
    background: var(--gradient-primary) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    padding: 10px 28px !important;
    transition: all 0.3s ease !important;
    letter-spacing: 0.3px;
}

div[data-testid="stFormSubmitButton"] > button:hover,
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(108,92,231,0.4) !important;
}

.stCheckbox label span {
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

.stSlider > div > div > div {
    color: var(--accent-primary) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: var(--bg-secondary);
    padding: 6px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-color);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    color: var(--text-secondary) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    padding: 8px 20px !important;
}
.stTabs [aria-selected="true"] {
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-color) !important;
}
.stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* Metric override */
[data-testid="stMetric"] {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    padding: 16px;
}
[data-testid="stMetricLabel"] {
    color: var(--text-secondary) !important;
}
[data-testid="stMetricValue"] {
    color: var(--text-primary) !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

/* Divider */
hr {
    border-color: var(--border-color) !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-track {
    background: var(--bg-primary);
}
::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: 3px;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-banner { padding: 24px; }
    .hero-banner .hero-name { font-size: 28px; }
    .metric-card .card-value { font-size: 24px; }
    .penalty-amount { font-size: 32px; }
}
</style>
""",
    unsafe_allow_html=True,
)


# ─── Data Persistence Layer ─────────────────────────────────────────────────


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def get_user_file(username: str) -> str:
    ensure_data_dir()
    return os.path.join(DATA_DIR, f"{username}_data.json")


def load_user_data(username: str) -> dict:
    filepath = get_user_file(username)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "wake_up": {},
        "tasks": {},
        "reports": {},
        "instagram": {},
        "penalties": {},
        "milestones": {
            "phase1": {},
            "phase2": {},
        },
    }


def save_user_data(username: str, data: dict):
    filepath = get_user_file(username)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ─── Helper Functions ────────────────────────────────────────────────────────


def get_today() -> str:
    return date.today().isoformat()


def get_month_key() -> str:
    return date.today().strftime("%Y-%m")


def get_week_key() -> str:
    today = date.today()
    start = today - timedelta(days=today.weekday())
    return start.isoformat()


def calculate_streak(data: dict, key: str, check_fn) -> int:
    """Calculate consecutive day streak backwards from yesterday."""
    streak = 0
    check_date = date.today() - timedelta(days=1)
    while True:
        ds = check_date.isoformat()
        if ds in data.get(key, {}) and check_fn(data[key][ds]):
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break
    # Check today too
    today_s = get_today()
    if today_s in data.get(key, {}) and check_fn(data[key][today_s]):
        streak += 1
    return streak


def get_month_failures(data: dict) -> int:
    """Count total failures in current month across all penalty categories."""
    month_key = get_month_key()
    penalties = data.get("penalties", {}).get(month_key, {})
    return penalties.get("failure_count", 0)


def add_penalty(data: dict) -> dict:
    """Add a penalty increment and return updated data."""
    month_key = get_month_key()
    if month_key not in data.get("penalties", {}):
        data.setdefault("penalties", {})[month_key] = {
            "failure_count": 0,
            "total_penalty": 0,
            "failures": [],
        }
    p = data["penalties"][month_key]
    p["failure_count"] += 1
    increment = p["failure_count"] * 50
    p["total_penalty"] += increment
    return data


def get_penalty_info(data: dict) -> dict:
    month_key = get_month_key()
    return data.get("penalties", {}).get(
        month_key, {"failure_count": 0, "total_penalty": 0, "failures": []}
    )


def get_daily_quote() -> str:
    day_of_year = date.today().timetuple().tm_yday
    return QUOTES[day_of_year % len(QUOTES)]


def make_progress_ring(value: float, label: str, color: str = "#6c5ce7", size: int = 160):
    fig = go.Figure()
    fig.add_trace(go.Pie(
        values=[value, 100 - value],
        hole=0.78,
        marker=dict(colors=[color, "rgba(42,42,69,0.5)"], line=dict(width=0)),
        textinfo="none",
        hoverinfo="none",
        direction="clockwise",
        sort=False,
    ))
    fig.update_layout(
        showlegend=False,
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=size,
        width=size,
        annotations=[
            dict(
                text=f"<b>{value:.0f}%</b><br><span style='font-size:11px;color:#9898b0'>{label}</span>",
                showarrow=False,
                font=dict(size=18, color="#e8e8f0", family="Inter"),
            )
        ],
    )
    return fig


def make_line_chart(dates_list, values, title, color="#6c5ce7", y_label=""):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates_list,
        y=values,
        mode="lines+markers",
        line=dict(color=color, width=3, shape="spline"),
        marker=dict(size=8, color=color, line=dict(width=2, color="#1a1a2e")),
        fill="tozeroy",
        fillcolor=f"rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.1)",
    ))
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#e8e8f0", family="Inter")),
        xaxis=dict(
            gridcolor="rgba(42,42,69,0.5)",
            color="#9898b0",
            tickfont=dict(family="Inter"),
        ),
        yaxis=dict(
            title=y_label,
            gridcolor="rgba(42,42,69,0.5)",
            color="#9898b0",
            tickfont=dict(family="Inter"),
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=300,
        margin=dict(t=50, b=40, l=50, r=20),
        hovermode="x unified",
    )
    return fig


def make_bar_chart(labels, values, title, color="#6c5ce7"):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=labels,
        y=values,
        marker=dict(
            color=color,
            cornerradius=6,
        ),
    ))
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#e8e8f0", family="Inter")),
        xaxis=dict(gridcolor="rgba(42,42,69,0.5)", color="#9898b0", tickfont=dict(family="Inter")),
        yaxis=dict(gridcolor="rgba(42,42,69,0.5)", color="#9898b0", tickfont=dict(family="Inter")),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=300,
        margin=dict(t=50, b=40, l=50, r=20),
    )
    return fig


# ─── Authentication ──────────────────────────────────────────────────────────


def show_login():
    st.markdown(
        """
    <div class="login-container">
        <div style="font-size:56px; margin-bottom:16px;">🔥</div>
        <div class="login-title">Discipline Forge</div>
        <div class="login-subtitle">Your premium productivity command center.<br>
        Track habits. Build discipline. Achieve greatness.</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        with st.form("login_form"):
            username = st.selectbox(
                "Select your profile",
                options=["", "Mahdi", "Daniel"],
                index=0,
            )
            code = st.text_input("Enter your access code", type="password")
            submitted = st.form_submit_button("Unlock Dashboard", use_container_width=True)

            if submitted:
                if not username:
                    st.error("Please select your name.")
                    return
                uname = username.lower()
                code_hash = hashlib.sha256(code.encode()).hexdigest()
                if uname in USERS and USERS[uname]["code_hash"] == code_hash:
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = uname
                    st.session_state["display_name"] = USERS[uname]["name"]
                    st.rerun()
                else:
                    st.error("Invalid access code. Try again.")


# ─── Dashboard Components ───────────────────────────────────────────────────


def render_hero(name: str):
    quote = get_daily_quote()
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    st.markdown(
        f"""
    <div class="hero-banner">
        <div class="hero-greeting">{greeting}</div>
        <div class="hero-name">{name} 🔥</div>
        <div class="hero-quote">"{quote}"</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_overview_cards(data: dict):
    today = get_today()

    # Wake-up streak
    wake_streak = calculate_streak(data, "wake_up", lambda x: x.get("logged", False))

    # Today's task completion
    today_tasks = data.get("tasks", {}).get(today, {})
    tasks_defined = today_tasks.get("items", [])
    tasks_done = sum(1 for t in tasks_defined if t.get("done", False))
    tasks_total = len(tasks_defined)
    task_pct = (tasks_done / tasks_total * 100) if tasks_total > 0 else 0

    # Monthly penalty
    penalty_info = get_penalty_info(data)

    # Instagram today
    ig_today = data.get("instagram", {}).get(today, {}).get("minutes", 0)
    ig_ok = ig_today <= 45

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
        <div class="metric-card success">
            <div class="card-icon">⏰</div>
            <div class="card-label">Wake-Up Streak</div>
            <div class="card-value">{wake_streak} days</div>
            <div class="card-sub">Consistency builds champions</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        pct_class = "success" if task_pct >= 80 else ("warm" if task_pct >= 50 else "danger")
        st.markdown(
            f"""
        <div class="metric-card {pct_class}">
            <div class="card-icon">✅</div>
            <div class="card-label">Today's Tasks</div>
            <div class="card-value">{tasks_done}/{tasks_total}</div>
            <div class="card-sub">{task_pct:.0f}% completed</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
        <div class="metric-card danger">
            <div class="card-icon">💰</div>
            <div class="card-label">Monthly Penalty</div>
            <div class="card-value">{penalty_info['total_penalty']:,} T</div>
            <div class="card-sub">{penalty_info['failure_count']} failures this month</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c4:
        ig_class = "success" if ig_ok else "danger"
        st.markdown(
            f"""
        <div class="metric-card {ig_class}">
            <div class="card-icon">📱</div>
            <div class="card-label">Instagram Today</div>
            <div class="card-value">{ig_today} min</div>
            <div class="card-sub">{'Within limit ✓' if ig_ok else 'Over limit ✗'}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )


def render_wakeup_section(data: dict, username: str):
    st.markdown(
        '<div class="section-header">⏰ Wake-Up Time Tracker</div>',
        unsafe_allow_html=True,
    )

    today = get_today()
    today_wake = data.get("wake_up", {}).get(today, {})

    col1, col2 = st.columns([2, 1])

    with col1:
        with st.form("wakeup_form"):
            st.markdown("**Log today's wake-up time**")
            wake_time = st.time_input(
                "What time did you wake up?",
                value=None,
            )
            wake_submit = st.form_submit_button("Log Wake-Up", use_container_width=True)

            if wake_submit and wake_time:
                data.setdefault("wake_up", {})[today] = {
                    "time": wake_time.strftime("%H:%M"),
                    "logged": True,
                }
                save_user_data(username, data)
                st.success(f"Wake-up logged: {wake_time.strftime('%H:%M')}")
                st.rerun()

        if today_wake.get("logged"):
            st.markdown(
                f"""<div class="badge badge-success">✓ Today logged: {today_wake.get('time', 'N/A')}</div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="badge badge-warning">⏳ Not logged yet today</div>',
                unsafe_allow_html=True,
            )

    with col2:
        streak = calculate_streak(data, "wake_up", lambda x: x.get("logged", False))
        st.markdown(
            f'<div class="streak-badge">🔥 {streak} Day Streak</div>',
            unsafe_allow_html=True,
        )

        # Show last 7 days
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Last 7 days:**")
        for i in range(6, -1, -1):
            d = (date.today() - timedelta(days=i)).isoformat()
            entry = data.get("wake_up", {}).get(d, {})
            day_label = (date.today() - timedelta(days=i)).strftime("%a %d")
            if entry.get("logged"):
                st.markdown(f"<span style='color:#00cec9'>✓</span> {day_label} — {entry.get('time', '')}", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color:#ff6b6b'>✗</span> {day_label} — Not logged", unsafe_allow_html=True)


def render_tasks_section(data: dict, username: str):
    st.markdown(
        '<div class="section-header">📋 Three Main Daily Jobs</div>',
        unsafe_allow_html=True,
    )

    today = get_today()
    today_tasks = data.get("tasks", {}).get(today, {"items": []})
    items = today_tasks.get("items", [])

    # Ensure exactly 3 task slots
    while len(items) < 3:
        items.append({"text": "", "done": False})

    col_input, col_progress = st.columns([2, 1])

    with col_input:
        with st.form("tasks_form"):
            st.markdown("**Define and track your 3 main tasks:**")
            new_items = []
            for i in range(3):
                tc1, tc2 = st.columns([4, 1])
                with tc1:
                    text = st.text_input(
                        f"Task {i+1}",
                        value=items[i].get("text", ""),
                        key=f"task_text_{i}",
                        placeholder=f"Enter task {i+1}...",
                    )
                with tc2:
                    done = st.checkbox(
                        "Done",
                        value=items[i].get("done", False),
                        key=f"task_done_{i}",
                    )
                new_items.append({"text": text, "done": done})

            if st.form_submit_button("Save Tasks", use_container_width=True):
                data.setdefault("tasks", {})[today] = {"items": new_items}
                save_user_data(username, data)
                st.success("Tasks saved!")
                st.rerun()

    with col_progress:
        tasks_done = sum(1 for t in items if t.get("done"))
        pct = (tasks_done / 3) * 100 if items else 0
        fig = make_progress_ring(pct, "Today", "#00cec9" if pct >= 80 else ("#fdcb6e" if pct >= 50 else "#ff6b6b"))
        st.plotly_chart(fig, use_container_width=False, config={"displayModeBar": False})

        # Weekly progress
        week_tasks_done = 0
        week_tasks_total = 0
        for i in range(7):
            d = (date.today() - timedelta(days=i)).isoformat()
            day_tasks = data.get("tasks", {}).get(d, {}).get("items", [])
            week_tasks_total += len(day_tasks)
            week_tasks_done += sum(1 for t in day_tasks if t.get("done"))

        week_pct = (week_tasks_done / week_tasks_total * 100) if week_tasks_total > 0 else 0

        st.markdown(f"**Weekly:** {week_tasks_done}/{week_tasks_total}")
        fill_class = "success" if week_pct >= 70 else ("warm" if week_pct >= 40 else "danger")
        st.markdown(
            f"""<div class="progress-container"><div class="progress-fill {fill_class}" style="width:{week_pct}%"></div></div>""",
            unsafe_allow_html=True,
        )

        # Monthly progress
        month_tasks_done = 0
        month_tasks_total = 0
        for key, val in data.get("tasks", {}).items():
            if key.startswith(get_month_key()):
                day_items = val.get("items", [])
                month_tasks_total += len(day_items)
                month_tasks_done += sum(1 for t in day_items if t.get("done"))

        month_pct = (month_tasks_done / month_tasks_total * 100) if month_tasks_total > 0 else 0
        st.markdown(f"**Monthly:** {month_tasks_done}/{month_tasks_total}")
        fill_class = "success" if month_pct >= 70 else ("warm" if month_pct >= 40 else "danger")
        st.markdown(
            f"""<div class="progress-container"><div class="progress-fill {fill_class}" style="width:{month_pct}%"></div></div>""",
            unsafe_allow_html=True,
        )


def render_report_section(data: dict, username: str):
    st.markdown(
        '<div class="section-header">📝 Daily Report</div>',
        unsafe_allow_html=True,
    )

    today = get_today()
    today_report = data.get("reports", {}).get(today, {})

    col1, col2 = st.columns([2, 1])

    with col1:
        with st.form("report_form"):
            st.markdown("**End-of-day performance summary**")
            summary = st.text_area(
                "How was your day? What did you accomplish?",
                value=today_report.get("summary", ""),
                height=120,
                placeholder="Write a brief summary of your performance today...",
            )
            rating = st.slider(
                "Self-Rating (1–10)",
                min_value=1,
                max_value=10,
                value=today_report.get("rating", 5),
            )

            if st.form_submit_button("Submit Report", use_container_width=True):
                data.setdefault("reports", {})[today] = {
                    "summary": summary,
                    "rating": rating,
                    "submitted_at": datetime.now().strftime("%H:%M"),
                }
                save_user_data(username, data)
                st.success("Report submitted!")
                st.rerun()

    with col2:
        if today_report:
            st.markdown(
                f"""<div class="badge badge-success">✓ Report submitted at {today_report.get('submitted_at', '')}</div>""",
                unsafe_allow_html=True,
            )
            st.markdown(f"**Rating:** {'⭐' * today_report.get('rating', 0)}")
        else:
            st.markdown(
                '<div class="badge badge-warning">⏳ Not submitted yet</div>',
                unsafe_allow_html=True,
            )

    # Rating chart over time
    reports = data.get("reports", {})
    if len(reports) > 1:
        sorted_dates = sorted(reports.keys())[-30:]
        dates_list = sorted_dates
        ratings = [reports[d].get("rating", 0) for d in sorted_dates]
        fig = make_line_chart(dates_list, ratings, "Self-Rating Over Time", "#a29bfe", "Rating")
        fig.update_yaxes(range=[0, 10.5])
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def render_penalty_section(data: dict, username: str):
    st.markdown(
        '<div class="section-header">⚖️ Penalty System</div>',
        unsafe_allow_html=True,
    )

    penalty_info = get_penalty_info(data)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown(
            f"""
        <div class="metric-card danger">
            <div class="card-label">Accumulated Penalty</div>
            <div class="penalty-amount">{penalty_info['total_penalty']:,} T</div>
            <div class="card-sub">This month</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="metric-card warm">
            <div class="card-icon">📊</div>
            <div class="card-label">Failure Count</div>
            <div class="card-value">{penalty_info['failure_count']}</div>
            <div class="card-sub">Next penalty: {(penalty_info['failure_count'] + 1) * 50} T</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="card-icon">📅</div>
            <div class="card-label">Current Month</div>
            <div class="card-value">{date.today().strftime('%B')}</div>
            <div class="card-sub">Resets on the 1st</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("**Penalty Progression Schedule:**")
    prog_data = []
    for i in range(1, 8):
        amount = i * 50
        cum = sum(j * 50 for j in range(1, i + 1))
        is_current = i == penalty_info['failure_count']
        marker = " ← You are here" if is_current else ""
        prog_data.append(f"{'🔴' if i <= penalty_info['failure_count'] else '⚪'} Failure #{i}: **{amount} T** (cumulative: {cum} T){marker}")

    for line in prog_data:
        st.markdown(line)


def render_instagram_section(data: dict, username: str):
    st.markdown(
        '<div class="section-header">📱 Instagram Limitation Tracker</div>',
        unsafe_allow_html=True,
    )

    today = get_today()
    today_ig = data.get("instagram", {}).get(today, {})

    col1, col2 = st.columns([2, 1])

    with col1:
        with st.form("ig_form"):
            st.markdown("**Log your Instagram usage (limit: 45 minutes)**")
            minutes = st.number_input(
                "Minutes used today",
                min_value=0,
                max_value=600,
                value=today_ig.get("minutes", 0),
                step=5,
            )

            if st.form_submit_button("Log Usage", use_container_width=True):
                was_violation = today_ig.get("violation", False)
                is_violation = minutes > 45
                data.setdefault("instagram", {})[today] = {
                    "minutes": minutes,
                    "violation": is_violation,
                }

                if is_violation and not was_violation:
                    data = add_penalty(data)
                    st.warning(f"⚠️ You exceeded the 45-minute limit! Penalty added.")

                save_user_data(username, data)
                st.success(f"Instagram usage logged: {minutes} minutes")
                st.rerun()

    with col2:
        minutes_val = today_ig.get("minutes", 0)
        usage_pct = min((minutes_val / 45) * 100, 100)
        color = "#00cec9" if minutes_val <= 45 else "#ff6b6b"
        fig = make_progress_ring(usage_pct, "of limit", color)
        st.plotly_chart(fig, use_container_width=False, config={"displayModeBar": False})

    # Weekly chart
    week_dates = []
    week_minutes = []
    for i in range(6, -1, -1):
        d = (date.today() - timedelta(days=i)).isoformat()
        day_label = (date.today() - timedelta(days=i)).strftime("%a")
        week_dates.append(day_label)
        week_minutes.append(data.get("instagram", {}).get(d, {}).get("minutes", 0))

    fig = make_bar_chart(week_dates, week_minutes, "Weekly Instagram Usage (minutes)", "#a29bfe")
    fig.add_hline(y=45, line_dash="dash", line_color="#ff6b6b", annotation_text="45 min limit")
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def render_roadmap_section(data: dict, username: str):
    st.markdown(
        '<div class="section-header">🗺️ Long-Term Motivation Roadmap</div>',
        unsafe_allow_html=True,
    )

    days_since_start = (date.today() - START_DATE).days
    phase1_end = START_DATE + timedelta(days=180)
    phase2_end = START_DATE + timedelta(days=365)

    col1, col2 = st.columns(2)

    with col1:
        days_to_p1 = max(0, (phase1_end - date.today()).days)
        p1_progress = min(100, (days_since_start / 180) * 100) if days_since_start >= 0 else 0
        is_active_p1 = days_since_start < 180
        active_class = "active" if is_active_p1 else ""

        st.markdown(
            f"""
        <div class="phase-card {active_class}">
            <div class="phase-label">Phase 1 — First 6 Months</div>
            <div class="phase-title">Personal Discipline + Sightseeing Reward 🏔️</div>
            <div class="phase-desc">Build rock-solid habits, track consistency, and earn your sightseeing trip reward.</div>
            <div style="margin-bottom:8px;">
                <span style="color:#9898b0; font-size:13px;">Progress</span>
                <span style="float:right; color:#a29bfe; font-weight:700;">{p1_progress:.0f}%</span>
            </div>
            <div class="progress-container">
                <div class="progress-fill primary" style="width:{p1_progress}%"></div>
            </div>
            <div style="margin-top:12px; font-size:14px; color:#fdcb6e; font-weight:600;">
                ⏳ {days_to_p1} days remaining
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Phase 1 milestones
        p1_milestones = data.get("milestones", {}).get("phase1", {})
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Phase 1 Milestones:**")
        p1_items = [
            ("consistent_wakeup", "30-day consistent wake-up streak"),
            ("tasks_mastery", "80%+ monthly task completion"),
            ("ig_control", "Instagram under control for 30 days"),
            ("self_rating_7", "Average self-rating above 7"),
        ]
        changed = False
        for key, label in p1_items:
            val = st.checkbox(label, value=p1_milestones.get(key, False), key=f"p1_{key}")
            if val != p1_milestones.get(key, False):
                data.setdefault("milestones", {}).setdefault("phase1", {})[key] = val
                changed = True
        if changed:
            save_user_data(username, data)

    with col2:
        days_to_p2 = max(0, (phase2_end - date.today()).days)
        p2_days_elapsed = max(0, days_since_start - 180)
        p2_progress = min(100, (p2_days_elapsed / 180) * 100) if p2_days_elapsed > 0 else 0
        is_active_p2 = 180 <= days_since_start < 365
        active_class = "active" if is_active_p2 else ""

        st.markdown(
            f"""
        <div class="phase-card {active_class}">
            <div class="phase-label">Phase 2 — Second 6 Months</div>
            <div class="phase-title">Travel Reward + Business Launch 🚀</div>
            <div class="phase-desc">Level up with business preparation, revenue tracking, and earn your travel reward.</div>
            <div style="margin-bottom:8px;">
                <span style="color:#9898b0; font-size:13px;">Progress</span>
                <span style="float:right; color:#00cec9; font-weight:700;">{p2_progress:.0f}%</span>
            </div>
            <div class="progress-container">
                <div class="progress-fill success" style="width:{p2_progress}%"></div>
            </div>
            <div style="margin-top:12px; font-size:14px; color:#fdcb6e; font-weight:600;">
                ⏳ {days_to_p2} days remaining
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Phase 2 milestones
        p2_milestones = data.get("milestones", {}).get("phase2", {})
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Phase 2 Milestones:**")
        p2_items = [
            ("start_business", "Start business"),
            ("first_revenue", "First revenue earned"),
            ("skill_dev_1", "Complete first skill course"),
            ("skill_dev_2", "Complete second skill course"),
            ("travel_earned", "Travel reward earned"),
        ]
        changed2 = False
        for key, label in p2_items:
            val = st.checkbox(label, value=p2_milestones.get(key, False), key=f"p2_{key}")
            if val != p2_milestones.get(key, False):
                data.setdefault("milestones", {}).setdefault("phase2", {})[key] = val
                changed2 = True
        if changed2:
            save_user_data(username, data)


def render_streak_badges(data: dict):
    st.markdown(
        '<div class="section-header">🏅 Achievement Badges</div>',
        unsafe_allow_html=True,
    )

    wake_streak = calculate_streak(data, "wake_up", lambda x: x.get("logged", False))

    # Task completion rate this month
    month_done = 0
    month_total = 0
    for key, val in data.get("tasks", {}).items():
        if key.startswith(get_month_key()):
            items = val.get("items", [])
            month_total += len(items)
            month_done += sum(1 for t in items if t.get("done"))

    month_rate = (month_done / month_total * 100) if month_total > 0 else 0

    # Instagram discipline
    ig_violations = sum(
        1
        for k, v in data.get("instagram", {}).items()
        if k.startswith(get_month_key()) and v.get("violation", False)
    )

    # Avg rating
    month_ratings = [
        v.get("rating", 0)
        for k, v in data.get("reports", {}).items()
        if k.startswith(get_month_key()) and v.get("rating", 0) > 0
    ]
    avg_rating = sum(month_ratings) / len(month_ratings) if month_ratings else 0

    badges = []
    if wake_streak >= 3:
        badges.append(("🌅", "Early Riser", f"{wake_streak}-day streak"))
    if wake_streak >= 7:
        badges.append(("🔥", "Week Warrior", "7+ day wake-up streak"))
    if wake_streak >= 30:
        badges.append(("👑", "Month Master", "30+ day wake-up streak"))
    if month_rate >= 80:
        badges.append(("⚡", "Task Crusher", f"{month_rate:.0f}% completion"))
    if month_rate >= 100 and month_total > 0:
        badges.append(("💎", "Perfect Score", "100% task completion"))
    if ig_violations == 0 and len(data.get("instagram", {})) > 0:
        badges.append(("🛡️", "Digital Discipline", "No IG violations"))
    if avg_rating >= 8:
        badges.append(("🌟", "High Performer", f"Avg rating: {avg_rating:.1f}"))
    if get_penalty_info(data)["failure_count"] == 0:
        badges.append(("✨", "Clean Record", "No penalties this month"))

    if not badges:
        badges.append(("🎯", "Getting Started", "Keep going to earn badges!"))

    cols = st.columns(min(len(badges), 4))
    for i, (icon, title, desc) in enumerate(badges):
        with cols[i % len(cols)]:
            st.markdown(
                f"""
            <div class="metric-card" style="text-align:center; padding:20px;">
                <div style="font-size:36px; margin-bottom:8px;">{icon}</div>
                <div style="font-size:14px; font-weight:700; color:var(--text-primary); margin-bottom:4px;">{title}</div>
                <div style="font-size:12px; color:var(--text-secondary);">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )


# ─── Main Dashboard ─────────────────────────────────────────────────────────


def render_dashboard():
    username = st.session_state["username"]
    display_name = st.session_state["display_name"]
    data = load_user_data(username)

    # Top bar with logout
    top1, top2 = st.columns([6, 1])
    with top2:
        if st.button("Logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    # Hero
    render_hero(display_name)

    # Overview cards
    render_overview_cards(data)

    st.markdown("<br>", unsafe_allow_html=True)

    # Tabs for main sections
    tab_wake, tab_tasks, tab_report, tab_penalty, tab_ig, tab_roadmap, tab_badges = st.tabs([
        "⏰ Wake-Up",
        "📋 Daily Tasks",
        "📝 Report",
        "⚖️ Penalties",
        "📱 Instagram",
        "🗺️ Roadmap",
        "🏅 Badges",
    ])

    with tab_wake:
        render_wakeup_section(data, username)

    with tab_tasks:
        render_tasks_section(data, username)

    with tab_report:
        render_report_section(data, username)

    with tab_penalty:
        render_penalty_section(data, username)

    with tab_ig:
        render_instagram_section(data, username)

    with tab_roadmap:
        render_roadmap_section(data, username)

    with tab_badges:
        # Reload data in case milestones changed
        data = load_user_data(username)
        render_streak_badges(data)

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        """
    <div style="text-align:center; padding:24px; color:var(--text-muted); font-size:12px; border-top:1px solid var(--border-color);">
        Discipline Forge — Built for Champions 🔥<br>
        <span style="color:var(--text-secondary);">Stay consistent. Stay hungry. Stay disciplined.</span>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ─── App Entry Point ────────────────────────────────────────────────────────


def main():
    if st.session_state.get("authenticated"):
        render_dashboard()
    else:
        show_login()


if __name__ == "__main__":
    main()
