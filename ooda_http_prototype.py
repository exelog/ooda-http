
# OODA-HTTP: Minimal Prototype in Python
# Language: Python 3.9+
# Goal: Simulate a basic Observe-Orient-Decide-Act loop on HTTP traffic

import random
import time

# === Phase 1: Observe ===
def observe_request():
    # Simulated request metadata
    return {
        "ip": "192.168.1.23",
        "user_agent": "curl/8.5.0",
        "request_path": "/api/data",
        "request_size_kb": random.randint(1, 500),  # simulate size
        "tls_handshake_time_ms": random.randint(30, 300)
    }

# === Phase 2: Orient ===
def analyze_threat(request):
    # Simple risk model based on size and handshake time
    score = 0
    if request["request_size_kb"] > 400:
        score += 3
    if request["tls_handshake_time_ms"] > 250:
        score += 2
    if "curl" in request["user_agent"]:
        score += 1
    return score  # Higher is riskier

# === Phase 3: Decide ===
def decide_action(threat_score):
    if threat_score >= 5:
        return "block"
    elif threat_score >= 3:
        return "rotate_key"
    else:
        return "allow"

# === Phase 4: Act ===
def act(action):
    if action == "block":
        print("⚠️ Blocking request.")
    elif action == "rotate_key":
        print("🔁 Rotating encryption key.")
    else:
        print("✅ Request allowed.")

# === Simulate the OODA loop ===
def ooda_loop():
    for _ in range(3):  # simulate 3 incoming requests
        print("\n--- New Request ---")
        request = observe_request()
        print(f"Observed: {request}")
        score = analyze_threat(request)
        print(f"Threat Score: {score}")
        action = decide_action(score)
        print(f"Decision: {action}")
        act(action)
        time.sleep(1)

if __name__ == "__main__":
    ooda_loop()
