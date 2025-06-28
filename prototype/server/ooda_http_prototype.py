

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
import random
import threading
import time

app = Flask(__name__)

# === Logger Setup ===
logger = logging.getLogger("OODA_HTTP_Server")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("ooda_http_server.log", maxBytes=100000, backupCount=5)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# === Threat analysis logic ===
def analyze_threat(req_data):
    score = 0
    user_agent = req_data.get("headers", {}).get("User-Agent", "").lower()
    if "bot" in user_agent:
        score += 3
    if req_data.get("payload_size", 0) > 4000:
        score += 2
    if req_data.get("tls_version", "") == "TLS 1.2":
        score += 1
    return score

def decide_action(score):
    if score >= 5:
        return "block"
    elif score >= 3:
        return "rotate_key"
    return "allow"

@app.route("/analyze", methods=["POST"])
def analyze():
    req_data = request.get_json()
    score = analyze_threat(req_data)
    decision = decide_action(score)
    log_msg = f"Request: {req_data} | Score: {score} | Decision: {decision}"
    logger.info(log_msg)
    print(log_msg)  # Display in terminal
    return jsonify({"score": score, "decision": decision})

# === Optional: simulate traffic for local testing ===
def simulate_requests():
    while True:
        req = {
            "ip": f"192.168.0.{random.randint(1, 255)}",
            "headers": {"User-Agent": random.choice(["Mozilla", "curl", "bot"])},
            "tls_version": random.choice(["TLS 1.2", "TLS 1.3"]),
            "payload_size": random.randint(100, 5000),
        }
        score = analyze_threat(req)
        decision = decide_action(score)
        log_msg = f"[SIMULATION] Request: {req} | Score: {score} | Decision: {decision}"
        logger.info(log_msg)
        print(log_msg)
        time.sleep(5)

if __name__ == "__main__":
    logger.info("🚀 Starting OODA-HTTP server on http://localhost:8000")
    print("🚀 OODA-HTTP server running at http://localhost:8000")
    # Optional simulation thread (disable if unwanted)
    # threading.Thread(target=simulate_requests, daemon=True).start()
    app.run(port=8000)
