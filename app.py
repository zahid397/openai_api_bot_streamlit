"""
OpenAI API Bot Starter — Streamlit App
Dark futuristic theme with Mentor Bot and Innovation Bot.
Run: streamlit run app.py
"""

import streamlit as st
import os
import time
from dotenv import load_dotenv
from mentor_bot import respond as mentor_respond
from innovation_bot import respond as innovation_respond

# ── Load environment ─────────────────────────────────────────
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# ── Page configuration ───────────────────────────────────────
st.set_page_config(
    page_title="OpenAI API Bot Starter",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS — Dark Futuristic Theme ───────────────────────
st.markdown("""
<style>
/* ═══════════════════════════════════════════════════════════
   BASE & BACKGROUND
═══════════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #050714 !important;
    font-family: 'Inter', sans-serif;
}

/* Dot grid background */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-image: radial-gradient(rgba(99, 102, 241, 0.12) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
    z-index: 0;
}

/* Ambient glow blobs */
[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background:
        radial-gradient(ellipse 600px 500px at 20% 40%, rgba(139, 92, 246, 0.08) 0%, transparent 70%),
        radial-gradient(ellipse 500px 400px at 80% 10%, rgba(6, 182, 212, 0.08) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ═══════════════════════════════════════════════════════════
   HIDE STREAMLIT DEFAULTS
═══════════════════════════════════════════════════════════ */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 0.5rem !important;
    max-width: 1300px !important;
}

/* ═══════════════════════════════════════════════════════════
   SIDEBAR
═══════════════════════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: #0d1117 !important;
    border-right: 1px solid rgba(139, 92, 246, 0.2) !important;
}

/* ═══════════════════════════════════════════════════════════
   RADIO BUTTONS (Bot Selector)
═══════════════════════════════════════════════════════════ */
[data-testid="stRadio"] label {
    color: #e2e8f0 !important;
    font-weight: 500;
}
[data-testid="stRadio"] > div {
    gap: 8px;
}

/* ═══════════════════════════════════════════════════════════
   BUTTONS
═══════════════════════════════════════════════════════════ */
.stButton > button {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.15)) !important;
    color: #c4b5fd !important;
    border: 1px solid rgba(139, 92, 246, 0.4) !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 6px 16px !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(139, 92, 246, 0.3)) !important;
    border-color: rgba(139, 92, 246, 0.8) !important;
    color: #fff !important;
    box-shadow: 0 0 16px rgba(139, 92, 246, 0.4) !important;
    transform: translateY(-1px) !important;
}

/* Send button — primary style */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4) !important;
}
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 6px 25px rgba(79, 70, 229, 0.6) !important;
    transform: translateY(-2px) !important;
}

/* ═══════════════════════════════════════════════════════════
   TEXT INPUT & TEXT AREA
═══════════════════════════════════════════════════════════ */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    background: #111827 !important;
    border: 1px solid rgba(99, 102, 241, 0.3) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    caret-color: #8b5cf6;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: rgba(139, 92, 246, 0.7) !important;
    box-shadow: 0 0 12px rgba(139, 92, 246, 0.2) !important;
}
[data-testid="stTextInput"] input::placeholder,
[data-testid="stTextArea"] textarea::placeholder {
    color: #4b5563 !important;
}

/* ═══════════════════════════════════════════════════════════
   SPINNER
═══════════════════════════════════════════════════════════ */
.stSpinner > div {
    border-top-color: #8b5cf6 !important;
}

/* ═══════════════════════════════════════════════════════════
   SELECTBOX / DROPDOWN
═══════════════════════════════════════════════════════════ */
[data-testid="stSelectbox"] > div {
    background: #111827 !important;
    border-color: rgba(99, 102, 241, 0.3) !important;
}

/* ═══════════════════════════════════════════════════════════
   CUSTOM COMPONENT CLASSES
═══════════════════════════════════════════════════════════ */

/* Badge */
.badge-powered {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.4);
    color: #6ee7b7;
    font-size: 11px; font-weight: 600; letter-spacing: 0.05em;
    padding: 4px 12px; border-radius: 20px;
    margin-bottom: 10px; text-transform: uppercase;
}

/* Hero title */
.hero-title {
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 800;
    line-height: 1.1;
    margin: 12px 0 8px;
}
.hero-title .purple { color: #a78bfa; }
.hero-title .white  { color: #ffffff; }

.hero-subtitle {
    font-size: 1.1rem;
    color: #94a3b8;
    font-weight: 400;
    margin-bottom: 28px;
    line-height: 1.6;
}

/* Feature cards */
.feature-card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(55, 65, 81, 0.8);
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 10px;
    display: flex; align-items: center; gap: 14px;
    transition: all 0.2s ease;
    backdrop-filter: blur(8px);
}
.feature-card:hover {
    border-color: rgba(139, 92, 246, 0.5);
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.1);
}
.feature-icon {
    width: 44px; height: 44px;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
}
.feature-text h4 {
    color: #6ee7b7; font-size: 14px;
    font-weight: 600; margin: 0 0 2px;
}
.feature-text p { color: #94a3b8; font-size: 12px; margin: 0; }

/* ── Chat Window ─────────────────────────────────────────── */
.chat-window-wrapper {
    border-radius: 16px;
    padding: 2px;
    background: linear-gradient(135deg, rgba(139,92,246,0.6), rgba(6,182,212,0.4));
    box-shadow: 0 0 40px rgba(139, 92, 246, 0.2), 0 0 80px rgba(6, 182, 212, 0.1);
}
.chat-window {
    background: #0f172a;
    border-radius: 14px;
    overflow: hidden;
}

/* Chat header bar */
.chat-header {
    background: #1e293b;
    padding: 14px 20px;
    display: flex; align-items: center; justify-content: space-between;
    border-bottom: 1px solid rgba(55, 65, 81, 0.6);
}
.chat-header-left { display: flex; align-items: center; gap: 10px; }
.chat-bot-icon {
    width: 34px; height: 34px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
}
.chat-bot-name { color: #e2e8f0; font-size: 15px; font-weight: 600; }
.chat-header-right {
    display: flex; align-items: center; gap: 8px;
    color: #94a3b8; font-size: 13px;
}
.status-dot {
    width: 9px; height: 9px; border-radius: 50%;
    background: #22c55e;
    box-shadow: 0 0 8px rgba(34, 197, 94, 0.6);
    animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 8px rgba(34, 197, 94, 0.6); }
    50%       { box-shadow: 0 0 16px rgba(34, 197, 94, 0.9); }
}

/* Chat messages area */
.chat-messages {
    min-height: 300px; max-height: 400px;
    overflow-y: auto;
    padding: 20px;
    display: flex; flex-direction: column; gap: 16px;
    scrollbar-width: thin;
    scrollbar-color: rgba(139,92,246,0.3) transparent;
}
.chat-messages::-webkit-scrollbar { width: 4px; }
.chat-messages::-webkit-scrollbar-thumb {
    background: rgba(139, 92, 246, 0.4);
    border-radius: 2px;
}

/* Empty state */
.chat-empty {
    text-align: center; padding: 40px 20px;
    color: #4b5563;
}
.chat-empty .big-icon { font-size: 3rem; margin-bottom: 12px; }
.chat-empty p { font-size: 13px; margin: 4px 0; }

/* User message bubble */
.msg-user {
    align-self: flex-end; max-width: 80%;
}
.msg-user .msg-label {
    font-size: 11px; font-weight: 600;
    color: #a5b4fc; margin-bottom: 4px; text-align: right;
}
.msg-user .msg-bubble {
    background: linear-gradient(135deg, #3730a3, #4f46e5);
    color: #e0e7ff;
    padding: 12px 16px;
    border-radius: 14px 14px 4px 14px;
    font-size: 14px; line-height: 1.6;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
}

/* Bot message bubble */
.msg-bot { align-self: flex-start; max-width: 85%; }
.msg-bot-header {
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 8px;
}
.msg-bot-icon {
    width: 28px; height: 28px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border-radius: 7px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; flex-shrink: 0;
}
.msg-bot-name { font-size: 13px; font-weight: 600; color: #e2e8f0; }
.msg-bot .msg-bubble {
    background: #1e293b;
    border: 1px solid rgba(55, 65, 81, 0.8);
    color: #cbd5e1;
    padding: 14px 16px;
    border-radius: 4px 14px 14px 14px;
    font-size: 14px; line-height: 1.7;
}

/* Suggestion chips */
.suggestion-chips {
    display: flex; gap: 8px; padding: 0 20px 12px;
    flex-wrap: wrap;
}
.suggestion-chip {
    background: rgba(30, 41, 59, 0.8);
    border: 1px solid rgba(55, 65, 81, 0.8);
    color: #94a3b8;
    padding: 6px 14px; border-radius: 20px;
    font-size: 12px; cursor: pointer;
    transition: all 0.2s;
    display: inline-flex; align-items: center; gap: 5px;
}
.suggestion-chip:hover {
    border-color: rgba(139, 92, 246, 0.6);
    color: #c4b5fd;
    background: rgba(99, 102, 241, 0.1);
}

/* Chat input area */
.chat-input-area {
    padding: 12px 16px 12px;
    border-top: 1px solid rgba(55, 65, 81, 0.4);
    background: #0f172a;
}

/* Chat footer */
.chat-footer {
    text-align: center;
    padding: 10px;
    color: #374151;
    font-size: 12px;
    border-top: 1px solid rgba(55, 65, 81, 0.3);
}
.chat-footer span { color: #dc2626; }

/* ── Tech Stack Bar ──────────────────────────────────────── */
.tech-stack-bar {
    background: rgba(17, 24, 39, 0.9);
    border: 1px solid rgba(55, 65, 81, 0.6);
    border-radius: 14px;
    padding: 14px 32px;
    display: flex; align-items: center; justify-content: center;
    gap: 40px; margin-top: 24px;
    backdrop-filter: blur(8px);
}
.tech-label {
    color: #6ee7b7; font-size: 14px;
    font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase;
}
.tech-item {
    display: flex; align-items: center; gap: 8px;
    color: #e2e8f0; font-size: 14px; font-weight: 500;
}

/* ── Bot selector styling ────────────────────────────────── */
.bot-selector-label {
    color: #94a3b8; font-size: 12px;
    font-weight: 600; text-transform: uppercase;
    letter-spacing: 0.08em; margin-bottom: 6px;
}

/* ── API Status badge ────────────────────────────────────── */
.api-status-ok {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #6ee7b7; font-size: 11px; font-weight: 600;
    padding: 3px 10px; border-radius: 12px;
}
.api-status-warn {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(245, 158, 11, 0.1);
    border: 1px solid rgba(245, 158, 11, 0.3);
    color: #fcd34d; font-size: 11px; font-weight: 600;
    padding: 3px 10px; border-radius: 12px;
}

/* ── Divider ─────────────────────────────────────────────── */
hr { border-color: rgba(55, 65, 81, 0.4) !important; }
</style>
""", unsafe_allow_html=True)


# ── Session state ────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []          # conversation history
if "bot" not in st.session_state:
    st.session_state.bot = "mentor"         # active bot
if "pending_query" not in st.session_state:
    st.session_state.pending_query = ""     # from chip clicks


# ── Helper functions ─────────────────────────────────────────
def render_chat_history():
    """Render all messages as custom HTML bubbles."""
    if not st.session_state.messages:
        st.markdown("""
        <div class="chat-empty">
            <div class="big-icon">🤖</div>
            <p style="font-size:15px;color:#6b7280;font-weight:500">
                OpenAI Bot is ready
            </p>
            <p>Try a suggestion below or type your own question</p>
        </div>
        """, unsafe_allow_html=True)
        return

    html = ""
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            html += f"""
            <div class="msg-user">
                <div class="msg-label">You</div>
                <div class="msg-bubble">{msg["content"]}</div>
            </div>"""
        else:
            bot_name = "Mentor Bot" if st.session_state.bot == "mentor" else "Innovation Bot"
            # Convert markdown bold/bullets to HTML for display
            content = (msg["content"]
                .replace("**", "<strong>", 1)
                .replace("**", "</strong>", 1))
            # Simple multi-pass replace for bold
            import re
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', msg["content"])
            content = content.replace("\n", "<br>")
            html += f"""
            <div class="msg-bot">
                <div class="msg-bot-header">
                    <div class="msg-bot-icon">🤖</div>
                    <span class="msg-bot-name">{bot_name}</span>
                </div>
                <div class="msg-bubble">{content}</div>
            </div>"""

    st.markdown(f'<div class="chat-messages">{html}</div>', unsafe_allow_html=True)


def get_bot_respond(query: str) -> str:
    """Route to the correct bot."""
    history = st.session_state.messages[-8:]  # last 4 exchanges
    api_key = OPENAI_API_KEY if OPENAI_API_KEY else None

    if st.session_state.bot == "mentor":
        return mentor_respond(query, history, api_key)
    else:
        return innovation_respond(query, history, api_key)


def send_message(query: str):
    """Add user message, get response, update history."""
    if not query.strip():
        return

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": query.strip()
    })

    # Get bot response
    response = get_bot_respond(query.strip())

    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# ════════════════════════════════════════════════════════════
# MAIN LAYOUT
# ════════════════════════════════════════════════════════════

# ── Top badge + header ───────────────────────────────────────
col_badge, col_logo = st.columns([3, 1])
with col_badge:
    st.markdown("""
    <div class="badge-powered">
        🤖 Powered by OpenAI API
    </div>
    """, unsafe_allow_html=True)

# ── Two-column main layout ───────────────────────────────────
left_col, right_col = st.columns([1.05, 1.2], gap="large")

# ════════════════════════════════════════════════════════════
# LEFT COLUMN — Features / Marketing
# ════════════════════════════════════════════════════════════
with left_col:
    st.markdown("""
    <div class="hero-title">
        <span class="purple">OpenAI</span> <span class="white">API Bot</span><br>
        <span class="white">Starter</span>
    </div>
    <div class="hero-subtitle">
        A Simple, Powerful AI Chatbot<br>Built for Developers
    </div>
    """, unsafe_allow_html=True)

    # API status
    if OPENAI_API_KEY:
        st.markdown(
            '<span class="api-status-ok">● API Connected — Full AI Mode</span>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<span class="api-status-warn">⚡ Rule-Based Mode — Add API key for full AI</span>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature cards
    features = [
        ("💬", "AI-Powered Conversations",
         "Smart, context-aware responses", "#22d3ee"),
        ("⟨/⟩", "Developer Friendly",
         "Clean, minimal, and easy to extend", "#22d3ee"),
        ("⚡", "Fast & Lightweight",
         "Built with Python & OpenAI API", "#4ade80"),
        ("🛡️", "Secure & Private",
         "Your API key stays in your control", "#a78bfa"),
    ]

    for icon, title, desc, _ in features:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-text">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Bot selector
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="bot-selector-label">Choose Your Bot</div>',
                unsafe_allow_html=True)

    bot_choice = st.radio(
        "",
        options=["🎓 Mentor Bot", "💡 Innovation Bot"],
        index=0 if st.session_state.bot == "mentor" else 1,
        horizontal=True,
        label_visibility="collapsed",
    )
    st.session_state.bot = "mentor" if "Mentor" in bot_choice else "innovation"

    # Clear chat button
    if st.session_state.messages:
        if st.button("🗑️ Clear Chat", key="clear_btn"):
            st.session_state.messages = []
            st.rerun()


# ════════════════════════════════════════════════════════════
# RIGHT COLUMN — Chat Interface
# ════════════════════════════════════════════════════════════
with right_col:
    bot_name = "Mentor Bot" if st.session_state.bot == "mentor" else "Innovation Bot"
    bot_icon = "🎓" if st.session_state.bot == "mentor" else "💡"

    # ── Chat window wrapper with gradient border ──────────────
    st.markdown('<div class="chat-window-wrapper"><div class="chat-window">',
                unsafe_allow_html=True)

    # Chat header
    st.markdown(f"""
    <div class="chat-header">
        <div class="chat-header-left">
            <div class="chat-bot-icon">{bot_icon}</div>
            <span class="chat-bot-name">{bot_name}</span>
        </div>
        <div class="chat-header-right">
            🌙 Dark Mode
            <div class="status-dot"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Messages area
    render_chat_history()

    # ── Suggestion chips ──────────────────────────────────────
    if st.session_state.bot == "mentor":
        suggestions = [
            ("🔍", "Explain AI"),
            ("🐍", "Python roadmap"),
            ("💼", "Career tips"),
            ("🛠️", "Help with code"),
        ]
    else:
        suggestions = [
            ("💡", "Give me ideas"),
            ("🚀", "Startup advice"),
            ("🔮", "Future trends"),
            ("🧠", "Brainstorm with me"),
        ]

    # Render chip labels as HTML (visual only)
    chips_html = '<div class="suggestion-chips">'
    for icon, label in suggestions:
        chips_html += f'<span class="suggestion-chip">{icon} {label}</span>'
    chips_html += '</div>'
    st.markdown(chips_html, unsafe_allow_html=True)

    # ── Functional chip buttons ───────────────────────────────
    chip_cols = st.columns(len(suggestions))
    for i, (icon, label) in enumerate(suggestions):
        with chip_cols[i]:
            btn_key = f"chip_{i}_{st.session_state.bot}"
            if st.button(f"{icon} {label}", key=btn_key,
                        use_container_width=True):
                st.session_state.pending_query = label
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)  # close chat-window

    # ── Input form ────────────────────────────────────────────
    with st.form(key="chat_form", clear_on_submit=True):
        input_col, btn_col = st.columns([6, 1])
        with input_col:
            user_input = st.text_input(
                "",
                placeholder="Type your message…",
                key="chat_input",
                label_visibility="collapsed",
                value=st.session_state.get("pending_query", ""),
            )
        with btn_col:
            submitted = st.form_submit_button("➤", use_container_width=True)

    # Reset pending query after populating input
    if st.session_state.pending_query:
        query_to_send = st.session_state.pending_query
        st.session_state.pending_query = ""
        with st.spinner("🤖 Thinking…"):
            time.sleep(0.4)  # brief delay for UX
            send_message(query_to_send)
        st.rerun()

    # Process form submission
    if submitted and user_input.strip():
        with st.spinner("🤖 Thinking…"):
            time.sleep(0.3)
            send_message(user_input.strip())
        st.rerun()

    # Chat footer
    st.markdown("""
    <div class="chat-footer">
        Built with <span>♥</span> and OpenAI
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # close wrapper


# ════════════════════════════════════════════════════════════
# TECH STACK BAR — Full Width
# ════════════════════════════════════════════════════════════
st.markdown("""
<div class="tech-stack-bar">
    <span class="tech-label">Tech Stack</span>
    <div class="tech-item">🐍 Python</div>
    <div class="tech-item">🤖 OpenAI API</div>
    <div class="tech-item">⚡ Streamlit</div>
    <div class="tech-item">🧠 Rule-Based AI</div>
</div>
""", unsafe_allow_html=True)
