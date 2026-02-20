import time
import random

class RansomwareSimulator:
    """
    SAFE ransomware behavior simulator.
    This does NOT modify, encrypt, or damage any real files.
    It only mimics patterns for detection testing.
    """

    def __init__(self, target_files):
        self.target_files = target_files

    def simulate_activity(self):
        print("[SIMULATION] Starting ransomware behavior simulation...\n")

        for file in self.target_files:
            # Simulate delay between actions
            time.sleep(random.uniform(0.5, 1.5))

            # Simulate suspicious file modification
            print(f"[SIMULATION] Modifying file: {file}")

            # Simulate entropy spike (fake)
            fake_entropy = round(random.uniform(7.5, 8.0), 3)
            print(f"[SIMULATION] High entropy detected: {fake_entropy}")

            # Simulate rename behavior
            print(f"[SIMULATION] Renaming file: {file} -> {file}.locked\n")

        print("[SIMULATION] Simulation complete. No real files were harmed ✅")


if __name__ == "__main__":
    # Example test files (safe, no real modification happens)
    test_files = [
        "document1.txt",
        "image1.jpg",
        "notes.pdf"
    ]

    simulator = RansomwareSimulator(test_files)
    simulator.simulate_activity()