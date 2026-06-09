---

**File — 2** `innovation_bot.py`

```python
"""
Innovation Bot — Brainstorming, ideas, and creative problem-solving.
Uses OpenAI API if key is available, else rule-based fallback.
"""

import os
import random

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# ── System prompt ─────────────────────────────────────────────
INNOVATION_SYSTEM_PROMPT = """You are an Innovation Catalyst — a creative thinker who helps people generate bold ideas.
You use frameworks like Design Thinking, First Principles, SCAMPER, and Jobs-to-be-Done.
Be energetic, expansive, and inspire BIG thinking.
Give specific, actionable ideas — never vague generalities.
Format responses with bullet points and bold key concepts.
Keep responses focused and under 200 words."""

# ── Rule-based knowledge base ────────────────────────────────
RULES = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "howdy", "greetings", "sup"],
        "responses": [
            "💡 **Welcome to Innovation Bot!**\n\nI help you think bigger. Ask me about:\n- 🚀 Startup ideas\n- 🧠 Brainstorming techniques\n- 🔮 Tech trends & the future\n- 🎯 Problem-solving frameworks\n- 💥 Disrupting any industry\n\nWhat's the bold idea you're working on?",
        ]
    },
    "idea": {
        "keywords": ["idea", "brainstorm", "think", "generate", "suggest", "concept", "notion"],
        "responses": [
            """💡 **SCAMPER Brainstorming Framework:**

Use this on any existing product or idea:

- **S**ubstitute → What if you replaced [component] with AI?
- **C**ombine → Merge two unrelated industries
- **A**dapt → Apply solution from nature/biology
- **M**odify → Make it 10x smaller/bigger/faster
- **P**ut to other uses → Who else needs this?
- **E**liminate → What if you removed the main feature?
- **R**everse → What if users became the product creators?

🎯 **Exercise:** Pick an industry you know. Apply each letter. You'll generate 7 ideas in 10 minutes.""",
        ]
    },
    "startup": {
        "keywords": ["startup", "business", "venture", "company", "entrepreneur", "founder", "launch", "mvp", "product"],
        "responses": [
            """🚀 **Startup Idea Validation Framework:**

**Step 1: Problem First**
- Talk to 20 potential customers before writing code
- Look for problems people pay to solve right now

**Step 2: Test the Simplest Version**
- Notion doc as MVP: describe the product, collect emails
- Manual service before building automation
- Landing page → measure sign-up rate

**Step 3: Distribution > Product**
- How will the first 100 users find you?
- Content, community, cold outreach, or partnerships?

**Hot Spaces Right Now:**
- AI tools for niche industries (legal, medical, education)
- B2B automation for SMBs
- Climate/sustainability tech
- Developer productivity tools

💥 *The best startups solve a problem the founder personally experienced.*""",
        ]
    },
    "ai": {
        "keywords": ["ai", "artificial intelligence", "llm", "gpt", "machine learning", "chatbot", "automation", "openai"],
        "responses": [
            """🤖 **AI Innovation Opportunities in 2024–2025:**

**Underserved Niches:**
- AI legal document drafting for freelancers
- Personalized learning paths for trade skills
- AI-powered audit/compliance for SMBs
- Voice AI for elderly care
- Code review bot for junior developers

**High-Leverage AI Applications:**
1. **RAG systems** → Make any document searchable + queryable
2. **AI agents** → Automate multi-step workflows
3. **Multimodal apps** → Combine text, image, audio input
4. **AI + IoT** → Smart physical products

**Build Fast Strategy:**
- Use OpenAI API (no ML required)
- Deploy on Vercel/Railway for free
- Validate with 10 beta users in week 1

💡 *AI gives solo developers 10x leverage. One person can now build what took a team.*""",
        ]
    },
    "problem": {
        "keywords": ["problem", "solve", "challenge", "fix", "improve", "better", "solution", "pain point", "issue"],
        "responses": [
            """🎯 **First Principles Problem Solving:**

**The 5-Why Method:**
1. State the problem
2. Ask "why does this happen?" → Answer
3. Ask "why?" again → Deeper cause
4. Repeat 5 times → Find the ROOT cause
5. Solve the root, not the symptom

**Design Thinking Process:**
1. **Empathize** → Interview people who have the problem
2. **Define** → "How might we [do X] so that [person] can [achieve Y]?"
3. **Ideate** → Generate 20 ideas (no judgment!)
4. **Prototype** → Build the simplest version in 1 day
5. **Test** → Show 5 real users, observe without explaining

🔥 **Contrarian thinking:** Ask "What if the opposite were true?" — Many innovations come from reversing assumptions.""",
        ]
    },
    "trend": {
        "keywords": ["trend", "future", "emerging", "next", "2024", "2025", "technology", "coming", "innovation"],
        "responses": [
            """🔮 **Tech Trends Shaping 2025:**

**AI-Native Applications**
- Every app will have AI built-in, not bolted on
- Agentic systems that take multi-step actions

**Developer Tools Revolution**
- AI pair programming becomes standard
- No-code + AI = anyone can ship software

**Spatial & Physical Computing**
- AR glasses becoming practical
- Robots + LLMs = real-world AI agents

**Decentralization Continues**
- Local LLMs (run on your laptop)
- Edge computing for privacy

**What to Build Now:**
Pick any traditional software category (spreadsheets, CRM, analytics) and rebuild it with AI as the core interaction layer.

💡 *"The best time to plant a tree was 20 years ago. The second best time is now." — Build something in these spaces immediately.*""",
        ]
    },
    "product": {
        "keywords": ["product", "app", "tool", "software", "platform", "saas", "feature", "design", "ux", "user"],
        "responses": [
            """🎨 **Product Innovation Principles:**

**Jobs-to-be-Done Framework:**
People don't buy products — they hire them to do a job.
Ask: "What job is the user trying to accomplish?"

**The 3 Moats for Software Products:**
1. **Network effects** → More users = more valuable (Slack, GitHub)
2. **Data flywheel** → More usage = smarter AI = better product
3. **Workflow lock-in** → Deeply embedded in daily processes

**10x Better Rule:**
Your product needs to be 10x better (not just 10% better) than alternatives to win market share.

**Quick Differentiation Tactics:**
- Dramatically better UX (usually under-valued)
- Target a segment competitors ignore
- Price 80% cheaper with good-enough features (disruptive)
- Make the expert-level experience accessible to beginners

💥 *The best products feel like magic the first time you use them.*""",
        ]
    }
}

def _rule_response(query: str) -> str:
    """Keyword matching fallback classifier."""
    q = query.lower()
    for category, data in RULES.items():
        if any(kw in q for kw in data["keywords"]):
            return random.choice(data["responses"])

    return f"""💥 **Innovation Thinking for: "{query}"**

Let me apply creative frameworks to your question:

**First Principles Approach:**
1. What assumptions are you making about this?
2. Which of those assumptions could be wrong?
3. If you stripped everything away, what's the core truth?

**The "10x" Challenge:**
Not "how can I improve this by 10%?" but "how could this be 10x better?"

**Random Stimulus Technique:**
Think of a random word: 🦁 **LION**
How could lion-like qualities (bold, patient, powerful) apply to: "{query[:30]}..."?

Sometimes the most creative solutions come from forcing unlikely connections.

💡 Want a more targeted response? Add context: e.g., "Innovation ideas for sustainable food delivery in Southeast Asia" unlocks much richer answers.

_Running in **Rule-Based Mode** — add your OpenAI API key in `.env` for dynamic AI-powered responses._"""


def respond(query: str, history: list, api_key: str = None) -> str:
    """
    Main response function.
    Falls back gracefully if OpenAI is unavailable.
    """
    if api_key and OPENAI_AVAILABLE:
        try:
            client = OpenAI(api_key=api_key)
            messages = [{"role": "system", "content": INNOVATION_SYSTEM_PROMPT}]

            for msg in history[-6:]:
                messages.append({"role": msg["role"], "content": msg["content"]})

            messages.append({"role": "user", "content": query})

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=700,
                temperature=0.9,  # higher creativity for innovation
            )
            return completion.choices[0].message.content

        except Exception as e:
            fallback = _rule_response(query)
            return f"⚠️ **API Notice:** {str(e)}\n\n---\n\n{fallback}"

    return _rule_response(query)
