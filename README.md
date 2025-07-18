# 🤖 GitHub PR Assistant using Webhooks + Gemini + FastAPI

This project is an AI-powered assistant that listens to pull requests (PRs) via GitHub webhooks, uses **Gemini (Google Generative AI)** to analyze PR content, and **automatically adds review comments** back to the PR with suggestions or summaries.

---

## 🚀 Features

- 🪝 **GitHub Webhook Listener** – built with FastAPI to receive PR events in real-time.
- 🧠 **AI-Powered Analysis** – integrates with Gemini to analyze PR body and generate smart suggestions.
- 💬 **Automated GitHub Comments** – posts Gemini’s suggestions as comments on the pull request itself.

---

## 🛠️ Tech Stack

- **FastAPI** – Web server to handle webhook requests.
- **PyGithub** – Interact with the GitHub API.
- **Gemini / Google Generative AI** – AI model used to analyze the pull request.
- **Ngrok (optional)** – Used for local development to expose your webhook to GitHub.

---

## 📦 Requirements

- Python 3.9+
- Install dependencies:

```bash
pip install fastapi uvicorn python-dotenv PyGithub google-generativeai
```

---

## 🔧 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/github-pr-assistant.git
cd github-pr-assistant
```

### 2. Create Environment File

```env
# .env
GITHUB_TOKEN=ghp_YourGitHubTokenHere
GEMINI_API_KEY=Your_Gemini_API_Key
```

> 🔐 Make sure your GitHub token has `repo` access.  
> 💡 Gemini API key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

### 3. Run FastAPI Server

```bash
uvicorn main:app --reload
```

### 4. (Optional) Use Ngrok

```bash
ngrok http 8000
```

Use the ngrok URL as the webhook target.

---

## 🔁 Set Up GitHub Webhook

- Go to your repo → Settings → Webhooks → Add Webhook
- **Payload URL**: `https://your-ngrok-url/webhook`
- **Content type**: `application/json`
- **Events to trigger**: Just the `Pull request` event

---

## ⚙️ How It Works

1. A developer **opens or updates a pull request**.
2. GitHub sends a **webhook payload** to your server.
3. The FastAPI endpoint:
   - Validates the request
   - Extracts PR title and body
   - Sends the PR content to **Gemini**
   - Receives AI-generated suggestions
   - Posts those as a **comment** on the same PR

---

## 💻 Webhook Listener Logic (Simplified)

```python
@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    event_type = request.headers.get('x-github-event')

    if event_type == "pull_request":
        action = payload.get("action")
        if action in ["opened", "synchronize"]:
            repo_full_name = payload["repository"]["full_name"]
            pr_number = payload["pull_request"]["number"]
            pr_body = payload["pull_request"]["body"]

            # Send to Gemini & post response to GitHub
```

---

## 🧠 Prompt Used for Gemini

```text
You are a code reviewer. Give suggestions to improve the code or documentation based on the following pull request body:

---

<Insert PR Body Here>
```

---

## ✅ Example Output

> 🤖 **AI Review Suggestion**  
> Based on the PR description, consider improving test coverage and documenting the API endpoints. You can also use more specific variable names for readability.

---

## 🧪 Testing

- Make a PR on the GitHub repo you’ve connected.
- Watch the console logs and PR comment section.
- Check for:
  - Webhook received
  - Gemini suggestion returned
  - Comment added on PR

---

## 📁 Folder Structure

```bash
.
├── main.py           # FastAPI app and webhook logic
├── .env              # GitHub + Gemini API keys
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 📜 License

MIT License. Free to use and adapt.

---

## 🤝 Contributions

Pull requests and feedback are welcome! Let’s make AI-assisted coding smoother for everyone.
