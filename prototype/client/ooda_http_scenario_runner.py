import requests
import random
import json
import time
import threading
import os

LOG_FILE = 'ooda_http_server.log'

def generate_request():
    return {
        "ip": f"192.168.0.{random.randint(1, 255)}",
        "headers": {"User-Agent": random.choice(["Mozilla", "curl", "bot"])},
        "tls_version": random.choice(["TLS 1.2", "TLS 1.3"]),
        "payload_size": random.randint(100, 5000),
    }

def send_request():
    req = generate_request()
    try:
        response = requests.post("http://localhost:8000/analyze", json=req)
        print(f"Sent: {json.dumps(req)}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Client error: {e}")

def tail_log(filepath):
    print("\n🔍 Real-time Log View (Ctrl+C to stop) 🔍\n")
    with open(filepath, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            print(line.strip())

def start_scenario(request_count=5, delay=1.5):
    for _ in range(request_count):
        send_request()
        time.sleep(delay)

if __name__ == "__main__":
    # Run the log tail in a thread
    log_thread = threading.Thread(target=tail_log, args=(LOG_FILE,), daemon=True)
    log_thread.start()

    # Start scenario
    start_scenario(request_count=10, delay=2)
