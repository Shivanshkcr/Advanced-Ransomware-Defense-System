import time
import os
from watchdog.observers import Observer

from detector.ransomware_detector import RansomwareDetector
from detector.honeypot_handler import HoneypotHandler
from simulator import RansomwareSimulator


# 📁 Folder to monitor (change if needed)
MONITOR_DIR = "./monitor_folder"


def setup_honeypots():
    """
    Create decoy files (honeypots) inside monitored directory
    """
    decoy_files = []

    if not os.path.exists(MONITOR_DIR):
        os.makedirs(MONITOR_DIR)

    for i in range(3):
        file_path = os.path.join(MONITOR_DIR, f"decoy_file_{i}.txt")
        with open(file_path, "w") as f:
            f.write("This is a honeypot file. Do not modify.\n")
        decoy_files.append(file_path)

    return decoy_files


def start_detection():
    print("[*] Initializing Advanced Ransomware Defense System...\n")

    # 🪤 Setup honeypot files
    decoy_files = setup_honeypots()

    # 🧠 Initialize handlers
    ransomware_handler = RansomwareDetector()
    honeypot_handler = HoneypotHandler(decoy_files)

    # 👀 Observer setup
    observer = Observer()
    observer.schedule(ransomware_handler, MONITOR_DIR, recursive=True)
    observer.schedule(honeypot_handler, MONITOR_DIR, recursive=True)

    observer.start()
    print(f"[+] Monitoring started on: {MONITOR_DIR}\n")

    return observer, decoy_files


def start_simulation(decoy_files):
    """
    Run safe ransomware simulation
    """
    simulator = RansomwareSimulator(decoy_files)
    simulator.simulate_activity()


if __name__ == "__main__":
    observer, decoy_files = start_detection()

    try:
        # 🧪 Run simulation after system starts
        time.sleep(2)
        start_simulation(decoy_files)

        # 🔁 Keep system running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[!] Shutting down system...")
        observer.stop()

    observer.join()