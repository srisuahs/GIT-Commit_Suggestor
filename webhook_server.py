# webhook_server.py

from flask import Flask, request, jsonify
from suggest import suggest_commit_message

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "👋 Webhook server is running!"

@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json

    if "pull_request" in data:
        pr_body = data["pull_request"]["body"]
        print("📥 Received PR Description:", pr_body)

        commit_msg = suggest_commit_message(pr_body)
        print("💡 Suggested Commit Message:\n", commit_msg)

        return jsonify({
            "status": "success",
            "suggested_commit_message": commit_msg
        }), 200
    else:
        return jsonify({"status": "ignored"}), 200

if __name__ == "__main__":
    app.run(port=5000)
