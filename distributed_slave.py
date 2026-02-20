import socket
import hashlib


def crack_hash(target_hash, start, end):
    for i in range(start, end):
        word = str(i)

        if hashlib.md5(word.encode()).hexdigest() == target_hash:
            return word

    return None


def start_slave(master_ip, port=9000):
    s = socket.socket()
    s.connect((master_ip, port))

    print("[*] Connected to master")

    try:
        while True:
            data = s.recv(1024).decode()

            if not data:
                break

            # Format: hash,start,end
            target_hash, start, end = data.split(",")

            start = int(start)
            end = int(end)

            print(f"[+] Task received → {start} - {end}")

            result = crack_hash(target_hash, start, end)

            if result:
                s.send(f"FOUND:{result}".encode())
            else:
                s.send(f"NOT_FOUND:{start}-{end}".encode())

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        s.close()
        print("[-] Disconnected from master")


if __name__ == "__main__":
    start_slave("127.0.0.1")