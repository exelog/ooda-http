
# OODA-HTTP: Minimal Prototype in Python
# Language: Python 3.9+
# Goal: Simulate a basic Observe-Orient-Decide-Act loop on HTTP traffic

import random
import time

# === Observe Phase ===
def observe_request():
    # Simulate observation of HTTP request features
    return {
        "ip": f"192.168.0.{random.randint(1, 255)}",
        "headers": {"User-Agent": random.choice(["Mozilla", "curl", "bot"])},
        "tls_version": random.choice(["TLS 1.2", "TLS 1.3"]),
        "payload_size": random.randint(100, 5000),
    }

# === Orient Phase ===
def analyze_threat(request):
    score = 0
    if "bot" in request["headers"].get("User-Agent", "").lower():
        score += 3
    if request["payload_size"] > 4000:
        score += 2
    if request["tls_version"] == "TLS 1.2":
        score += 1
    return score

# === Decide Phase ===
def decide_action(score):
    if score >= 5:
        return "block"
    elif score >= 3:
        return "rotate_key"
    else:
        return "allow"

# === Act Phase ===
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
