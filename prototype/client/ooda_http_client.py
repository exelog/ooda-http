
import requests
import random
import time

def simulate_request():
    request_data = {
        "ip": f"192.168.0.{random.randint(1, 255)}",
        "headers": {"User-Agent": random.choice(["Mozilla", "curl", "bot"])},
        "tls_version": random.choice(["TLS 1.2", "TLS 1.3"]),
        "payload_size": random.randint(100, 5000),
    }
    return request_data

def send_request():
    url = "http://localhost:8000/analyze"
    try:
        for _ in range(3):  # simulate 3 client requests
            data = simulate_request()
            print(f"Sending: {data}")
            response = requests.post(url, json=data)
            print("Server response:", response.json())
            print("-" * 40)
            time.sleep(1)
    except requests.RequestException as e:
        print("Client error:", e)

if __name__ == "__main__":
    send_request()
