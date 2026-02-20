# 🛡️ Ransomware Detection & Distributed Password Recovery System

## 📌 Overview
This project is a dual-purpose cybersecurity tool that:
1. Detects ransomware using behavioral and entropy-based analysis
2. Performs distributed password cracking using a client-server model

---

## ⚙️ Features

### 🔹 Ransomware Detection
- Real-time file monitoring
- Entropy-based encryption detection
- Detects suspicious file modifications

### 🔹 Distributed Hash Cracking
- Master-server distributes tasks
- Clients perform hash cracking
- Scalable architecture

---

## 🏗️ Tech Stack
- Python
- Socket Programming
- Watchdog
- Cryptography
- Hashlib

---

## 🚀 How to Run

### 1. Start Server
```bash
cd server
python server.py