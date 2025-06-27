# client/client.py

import requests

def simulate_client_request():
    url = "http://localhost:8000/analyze"  # adresse du serveur OODA
    payload = {
        "headers": {"User-Agent": "ClientBot/1.0"},
        "ip": "192.168.1.50"
    }

    try:
        response = requests.post(url, json=payload)
        print("Server response:")
        print(response.json())
    except Exception as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    simulate_client_request()
