import requests
import random
import json
import time
import threading
import os

LOG_FILE = 'ooda_http_server.log'

def generate_request():
    # === Fonctionnalité de base : génération aléatoire ===
    return {
        "ip": f"192.168.0.{random.randint(1, 255)}",
        "headers": {"User-Agent": random.choice(["Mozilla", "curl", "bot"])},
        "tls_version": random.choice(["TLS 1.2", "TLS 1.3"]),
        "payload_size": random.randint(100, 5000),
    }

# 🚨 Fonctionnalité 1 : scénario nommé/taggé (à activer en remplacement ou ajout)
# def generate_request():
#     return {
#         "scenario": "slowloris",
#         "ip": "192.168.0.200",
#         "headers": {"User-Agent": "curl"},
#         "tls_version": "TLS 1.2",
#         "payload_size": 1500
#     }

# 🚨 Fonctionnalité 2 : burst attack (via start_scenario)
# Utiliser un délai très court : delay=0.1 dans start_scenario()

# 🚨 Fonctionnalité 3 : bot déguisé
# def generate_request():
#     return {
#         "ip": "192.168.0.101",
#         "headers": {"User-Agent": "Mozilla"},  # Déguisé
#         "tls_version": "TLS 1.2",
#         "payload_size": 50  # Payload trop petit = suspect
#     }

# 🚨 Fonctionnalité 4 : attacker persistant
# On pourrait faire une liste d'IP fixes et les utiliser en boucle.
PERSISTENT_IPS = ["192.168.0.10", "192.168.0.11"]
def generate_request():
    return {
        "ip": random.choice(PERSISTENT_IPS),
        "headers": {"User-Agent": random.choice(["Mozilla", "bot"])},
        "tls_version": "TLS 1.2",
        "payload_size": random.randint(100, 5000)
    }

# 🚨 Fonctionnalité 5 : score prédéfini simulé (exemple score 6 = block)
# def generate_request():
#     return {
#         "ip": "192.168.0.66",
#         "headers": {"User-Agent": "bot"},
#         "tls_version": "TLS 1.2",
#         "payload_size": 5001  # score 6 attendu
#     }

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
    # 🧵 Lancement du suivi temps réel des logs dans un thread
    log_thread = threading.Thread(target=tail_log, args=(LOG_FILE,), daemon=True)
    log_thread.start()

    # 🚀 Début de simulation (modifier request_count/delay selon scénario souhaité)
    start_scenario(request_count=10, delay=2)
