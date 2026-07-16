# 🤖 Support Ticket Triage Agent

An AI-powered Support Ticket Triage Agent built using **FastAPI**, **Groq Llama 3**, **Python**, and **Bootstrap**.

The application automatically analyzes incoming support tickets, classifies them into categories, predicts urgency, assigns the appropriate support team, provides a confidence score, detects sentiment, generates AI summaries, and supports batch CSV processing.

---

# 🚀 Features

- AI-powered ticket classification
- Urgency prediction (High / Medium / Low)
- Automatic team routing
- Confidence score for every prediction
- AI-generated summary and reasoning
- Sentiment detection
- Human review recommendation for uncertain cases
- Batch CSV ticket processing
- Dashboard analytics
- Recent ticket history
- CSV download

---

# 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- FastAPI
- Jinja2

### AI
- Groq API
- Llama 3.3 70B Versatile

### Data Processing
- Pandas
- CSV

---

# 📂 Project Structure

```
support-ticket-triage-agent/
│
├── app.py
├── agent.py
├── analytics.py
├── services.py
├── utils.py
├── prompts.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── data/
│   ├── sample_tickets.csv
│   └── results.csv
│
├── screenshots/
│   ├── dashboard.png
│   ├── single-analysis.png
│   └── batch-upload.png
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Srinivas25052004/support-ticket-triage-agent.git
```

Navigate to the project

```bash
cd support-ticket-triage-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application

```bash
python -m uvicorn app:app --reload
```

Open the application

```
http://127.0.0.1:8000
```

---

# 📥 Sample Input

A sample dataset is included in:

```
data/sample_tickets.csv
```

The file contains realistic customer support tickets covering:

- Authentication
- Billing
- Technical
- Account
- Feature Request
- General

---

# 📤 Sample Output

Processed routing decisions are generated in:

```
data/results.csv
```

Each output contains:

- Category
- Urgency
- Assigned Team
- Confidence Score
- AI Summary
- Sentiment
- Human Review Recommendation

---

# 🖼 Screenshots

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Single Ticket Analysis

![Single Ticket Analysis](screenshots/single-analysis.png)

## Batch CSV Processing

![Batch CSV Processing](screenshots/batch-upload.png)

---

# 🎯 Decision Boundary

The agent predicts a confidence score for every ticket.

- Tickets with high confidence are automatically routed to the predicted support team.
- Tickets with low confidence or ambiguous content are flagged for **Human Review**.
- Routing decisions are based on the predicted category:

| Category | Assigned Team |
|----------|---------------|
| Authentication | Identity Team |
| Billing | Billing Team |
| Technical | Technical Team |
| General | Support Team |
| Feature Request | Product Team |

---

# 📊 AI Output

For every support ticket, the agent predicts:

- Ticket Category
- Urgency
- Assigned Team
- Confidence Score
- AI Summary
- Sentiment
- Human Review Recommendation

---

# ⚖ Tradeoffs

This implementation was designed to be simple, modular, and easy to evaluate.

Design choices:

- FastAPI for lightweight REST application development.
- Groq Llama 3.3 70B for fast and accurate ticket classification.
- CSV storage instead of a database to simplify deployment and review.
- Modular architecture separating AI logic, analytics, services, and utilities.

With more development time, the following improvements could be added:

- Database integration (SQLite/PostgreSQL)
- Interactive analytics charts
- User authentication
- Docker deployment
- Asynchronous batch processing
- Email/Helpdesk integration

---

# 👨‍💻 Author

**Srinivasa H N**

Bachelor of Engineering (Artificial Intelligence & Machine Learning)

---

# Assessment Deliverables

This repository includes:

- ✅ Runnable FastAPI application
- ✅ Public source code
- ✅ Setup instructions
- ✅ Sample support tickets
- ✅ Sample routing output
- ✅ Decision boundary explanation
- ✅ Tradeoff notes
- ✅ Screenshots demonstrating the application
