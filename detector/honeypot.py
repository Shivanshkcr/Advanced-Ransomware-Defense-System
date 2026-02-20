from watchdog.events import FileSystemEventHandler
import os


class HoneypotHandler(FileSystemEventHandler):
    def __init__(self, decoy_files):
        # Normalize paths for consistency
        self.decoy_files = set(os.path.abspath(path) for path in decoy_files)

    def on_modified(self, event):
        if event.is_directory:
            return

        file_path = os.path.abspath(event.src_path)

        if file_path in self.decoy_files:
            print(f"[CRITICAL] 🚨 Honeypot file MODIFIED → {file_path}")

    def on_moved(self, event):
        if event.is_directory:
            return

        src_path = os.path.abspath(event.src_path)
        dest_path = os.path.abspath(event.dest_path)

        if src_path in self.decoy_files or dest_path in self.decoy_files:
            print(f"[CRITICAL] 🚨 Honeypot file RENAMED/MOVED → {src_path} → {dest_path}")