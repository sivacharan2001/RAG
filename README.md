# 🦜 Chat with SQL DB using LangChain + Groq + Streamlit

This project allows you to interact with SQL databases (SQLite or MySQL) in natural language using a powerful **LLM (Qwen3-32B via Groq)** and **LangChain's SQL agent** — all within an intuitive **Streamlit interface**.

---

## 🚀 Features

- 💬 Chat-based SQL agent using LangChain
- 🧠 Backed by `qwen/qwen3-32b` model from [Groq](https://groq.com/)
- ⚙️ Supports **SQLite3 (`student.db`)** or your own **MySQL** instance
- 📊 Execute natural language queries and get SQL-powered responses
- 🧼 Reset conversation at any time
- 🔒 Secure integration using `.env` or sidebar entry for API keys

---

## 📦 Requirements

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Or manually install core packages:

```bash
pip install streamlit langchain sqlalchemy langchain-groq pymysql
```

---

## 🔑 Setup

1. **Groq API Key**  
   Sign up at [groq.com](https://console.groq.com/) to get your API key.

2. **Environment Variables** (Optional)
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **SQLite (Default Option)**  
   Ensure the file `student.db` exists in the root folder with a valid schema. Example schema:
   ```sql
   CREATE TABLE STUDENT (
       name TEXT,
       course TEXT,
       grade TEXT,
       score INTEGER
   );
   ```

4. **MySQL (Optional)**  
   Select **MySQL** from the sidebar and fill in:
   - Host
   - User
   - Password
   - Database Name

---

## 🧪 Running the App

```bash
streamlit run app.py
```

Once the app launches:
- Select your database type (SQLite or MySQL)
- Enter your Groq API key
- Start chatting with your database!

---

## 🧠 Powered By

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq LPU Inference](https://groq.com/)
- [Streamlit](https://streamlit.io/)
- [Qwen3-32B Model](https://huggingface.co/Qwen/Qwen1.5-32B)

---

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit application
├── student.db          # Sample SQLite database
├── .env                # API key storage (optional)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ✅ Example Prompts

- "Show all students with grade A"
- "What is the average score in Data Science?"
- "List top 3 students in descending order of scores"

---

## 🔒 Security Notes

- API keys are entered through the sidebar or `.env` file — never hard-code them.
- Avoid pushing `.env` and `venv/` by using a `.gitignore`.

---

## 🙌 Author

Made with ❤️ using LangChain + Groq.  
Feel free to contribute or raise issues.

---