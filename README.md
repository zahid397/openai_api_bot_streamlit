to# 🚀 OpenAI API Bot Starter

> A sleek, dual‑personality AI chatbot built with Streamlit + OpenAI — ready to mentor or innovate.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/OpenAI-API-00ffcc?logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT">
</p>

![Demo Screenshot](assets/demo.png)  
*(Replace with your actual screenshot – see below)*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **Two AI Bots** | **Mentor Bot** – guides you in coding & career. **Innovation Bot** – sparks creative, futuristic ideas. |
| 🎨 **Futuristic UI** | Neon borders, dark dashboard, glow effects, and an optional animated background. |
| ⚡ **Fast & Lightweight** | Built on Streamlit, handles conversations with OpenAI’s GPT‑3.5‑Turbo. |
| 🔒 **Secure** | Your API key stays local – only stored in `.env` or Streamlit secrets. |
| 📱 **Mobile Friendly** | Responsive layout with quick prompts and a scrollable chat container. |
| 🧠 **Context‑Aware** | Remembers conversation history for natural, coherent replies. |

---

## 🧱 Project Structure

```
openai_api_bot_streamlit/
├── app.py                # Main Streamlit app (UI & logic)
├── mentor_bot.py         # Mentor Bot API handler
├── innovation_bot.py     # Innovation Bot API handler
├── .env                  # Environment variables (API key)
└── assets/
    └── background.png    # Optional futuristic background
```

---

## 🛠️ Setup & Run (5 minutes)

### 1️⃣ Clone & enter the project

```bash
git clone https://github.com/yourusername/openai_api_bot_streamlit.git
cd openai_api_bot_streamlit
```

### 2️⃣ Install dependencies

```bash
pip install streamlit openai python-dotenv
```

### 3️⃣ Add your OpenAI API key

Create a `.env` file in the root folder:

```ini
OPENAI_API_KEY=sk-...
```

> **Never commit your `.env` file** – add it to `.gitignore`.

### 4️⃣ (Optional) Add a background image

Place any `background.png` inside the `assets/` folder. The app will automatically use it with a dark overlay.

### 5️⃣ Launch the app

```bash
streamlit run app.py
```

Your default browser will open at `http://localhost:8501` – enjoy! 🎉

---

## 🖥️ How to Use

1. **Select a Bot** – Use the sidebar radio button to choose `Mentor Bot` or `Innovation Bot`.
2. **Type your question** in the text area, or click one of the quick prompts:
   - *Explain AI*
   - *Give me ideas*
   - *Help with code*
3. **Receive a glowing, AI‑powered response** – each answer is styled with neon borders.
4. **Clear chat** anytime using the sidebar button.
5. **Keep the conversation going** – the bot remembers previous messages.

---

## 🌟 Preview (Screenshots)

> *Replace these with your actual screenshots after running the app.*

| Chat Interface | Bot Selector |
|----------------|----------------|
| ![Chat UI](assets/chat.png) | ![Sidebar](assets/sidebar.png) |

*To generate your own screenshots: run the app, press `Cmd+Shift+S` (Mac) or `Win+Shift+S` (Windows), and save them in the `assets/` folder.*

---

## 🧪 Example Conversation

**User:** *Explain quantum computing in simple terms.*

**Mentor Bot:**  
> Quantum computing uses quantum bits, or qubits, which can be in multiple states at once thanks to superposition. This allows quantum computers to solve certain problems much faster than classical computers.

**Innovation Bot:**  
> Imagine a computer that doesn't just switch between 0 and 1, but can be both at the same time – like a coin spinning in the air. That's a qubit. With many spinning coins, you can explore millions of possibilities at once, unlocking new frontiers in medicine, cryptography, and artificial intelligence.

---

## ☁️ Deploy to Streamlit Cloud

1. Push your code to a **GitHub repository**.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. In the **Advanced settings**, add a secret:
   - Key: `OPENAI_API_KEY`
   - Value: `your-api-key`
4. Click **Deploy** – your app will be live in minutes! 🚀

> ⚠️ Do **not** commit your actual API key. Always use secrets on cloud platforms.

---

## 🛡️ Error Handling

- If `OPENAI_API_KEY` is missing → a friendly error message appears in the app.
- If the OpenAI API fails (e.g., rate limit, network issue) → the bot returns a clear error inside the chat.
- Missing background image → gracefully falls back to a solid dark colour.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue for feature suggestions or bug reports.

---

## 📄 License

MIT © [Your Name] – see [LICENSE](LICENSE) file for details.

---

## 💬 Acknowledgements

- [OpenAI](https://openai.com) for the powerful API
- [Streamlit](https://streamlit.io) for making AI apps fun
- FontAwesome & Google Fonts (used indirectly via Streamlit)

---

<p align="center">
  Made with 🛠️, ☕, and a futuristic glow.
</p>
```

---

### 📸 How to Add Real Screenshots

1. Run the app locally.
2. Take screenshots of:
   - The main chat interface (with a sample conversation).
   - The sidebar with bot selection.
3. Save them as `demo.png`, `chat.png`, `sidebar.png` inside the `assets/` folder.
4. Update the markdown image paths accordingly.

