import socket
import threading

HOST = "0.0.0.0"
PORT = 9000

clients = []
lock = threading.Lock()


def handle_slave(conn, addr):
    print(f"[+] Slave connected: {addr}")

    with lock:
        clients.append(conn)

    try:
        while True:
            result = conn.recv(1024).decode()

            if not result:
                break

            if result.startswith("FOUND"):
                print(f"[🔥 SUCCESS] Password cracked → {result}")
            else:
                print(f"[INFO] {addr}: {result}")

    except Exception as e:
        print(f"[ERROR] Connection lost: {addr} | {e}")

    finally:
        with lock:
            clients.remove(conn)
        conn.close()
        print(f"[-] Slave disconnected: {addr}")


def distribute_task(target_hash, start, end):
    if not clients:
        print("[!] No slaves connected")
        return

    chunk_size = (end - start) // len(clients)

    for i, client in enumerate(clients):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size if i != len(clients) - 1 else end

        message = f"{target_hash},{chunk_start},{chunk_end}"
        client.send(message.encode())

        print(f"[+] Task sent → {chunk_start} - {chunk_end}")


def start_master():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[*] Master running on {HOST}:{PORT}")

    threading.Thread(target=accept_connections, args=(server,), daemon=True).start()

    # 🧠 Demo task (you can modify later)
    target_hash = "202cb962ac59075b964b07152d234b70"  # "123"
    start = 0
    end = 100000

    while True:
        command = input("Enter 'start' to distribute task: ")

        if command.lower() == "start":
            distribute_task(target_hash, start, end)


def accept_connections(server):
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_slave, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    start_master()