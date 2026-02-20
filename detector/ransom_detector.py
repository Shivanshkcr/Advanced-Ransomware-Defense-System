from watchdog.events import FileSystemEventHandler
from collections import deque
import time
from detector.entropy_detector import calculate_entropy

HIGH_ENTROPY_THRESHOLD = 7.2
MODIFICATION_THRESHOLD = 15
TIME_WINDOW = 5  # seconds


class RansomwareDetector(FileSystemEventHandler):
    def __init__(self):
        self.events = deque()

    def on_moved(self, event):
        if event.is_directory:
            return

        # 🛡️ Safe file reading
        try:
            with open(event.dest_path, "rb") as f:
                data = f.read()
                entropy = calculate_entropy(data)
        except Exception as e:
            print(f"[ERROR] Could not read file: {event.dest_path} | {e}")
            return

        # 🔥 HIGH severity: encryption detection
        if entropy >= HIGH_ENTROPY_THRESHOLD:
            print(f"[HIGH] Possible encryption detected → {event.dest_path} | Entropy: {entropy:.2f}")

        # 📊 MEDIUM severity: high modification rate
        current_time = time.time()
        self.events.append(current_time)

        while self.events and current_time - self.events[0] > TIME_WINDOW:
            self.events.popleft()

        if len(self.events) >= MODIFICATION_THRESHOLD:
            print(f"[MEDIUM] High file modification activity detected ({len(self.events)} files in {TIME_WINDOW}s)")