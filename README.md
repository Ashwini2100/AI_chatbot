# 🤖 AI Chatbot (Flask + Gemini)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/) [![License](https://img.shields.io/badge/License-Free-brightgreen.svg)]() [![Deployment-Ready](https://img.shields.io/badge/Deployment-Ready-blueviolet.svg)]()

> ✨ A **futuristic AI chatbot** powered by **Google Gemini** and **Flask**, featuring a sleek UI with animations, voice input, and dark/light modes.

---

## 📸 Demo Preview
🚀 *Coming Soon!*  
*(Add a GIF or Screenshot here.)*

---

## 📂 Project Structure

```
/your_project_folder
 ├── app.py
 ├── requirements.txt
 ├── /templates
 │    └── index.html
```

---

## ⚙️ Setup Guide

### 1. Clone or Download

```bash
git clone https://github.com/your-username/ai-chatbot-flask-gemini.git
cd ai-chatbot-flask-gemini
```

*(or download ZIP and extract it.)*

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

✅ Installs:
- Flask
- google-generativeai

### 4. Set Up Gemini API Key

Edit `app.py` and replace:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
```

with your **real API key**.

[👉 Get your API Key here](https://ai.google.dev/)

### 5. Run the App

```bash
python app.py
```
Visit:
```
http://127.0.0.1:5000/
```

---

## 🎨 Features

- 🌑 Dark / Light Mode
- 🔊 Typing Sound Effects
- 💬 Real-time Gemini AI Chat
- 📱 Mobile Responsive Design
- 💾 Local Chat History Saving

---

## 🛠 Tech Stack

| Technology    | Description                          |
|---------------|--------------------------------------|
| Python        | Programming Language                 |
| Flask         | Backend Web Framework                |
| HTML/CSS      | Frontend UI                           |
| JavaScript    | Interactivity, Fetch API, Animations  |
| Google Gemini | AI Model for Chatbot Responses        |

---

## 🚀 Deployment

You can deploy it easily on:

- [Render](https://render.com/)
- [Vercel](https://vercel.com/)
- [Railway](https://railway.app/)

(*Want Dockerfile? Ask me!* 🐳)

---

## 📜 License

This project is **free for educational and personal use**.  
Commercial usage needs permission.

---

## ✨ Contributing

Pull Requests are welcome! 🚀  
Suggest new features, fix bugs, or improve the UI!

---

## 💎 FAQ

**Q: "Model not found" error?**  
👉 Check your API key and model name (`gemini-pro`) are correct.

**Q: Can I run it without API Key?**  
👉 No, you need a valid Gemini API Key.

---

## 💬 Contact

- GitHub: [YourUsername](https://github.com/yourusername)
- Email: youremail@example.com

---

# 🌟 Final Message

🚀 Keep building, keep learning!  
💡 The future is for makers like you!

---

# 🏱️ Bonus:

I can generate for you:
- **Dockerfile for Production 🚀**
- **Render Deploy Button**
- **GitHub Action CI/CD Workflow**
