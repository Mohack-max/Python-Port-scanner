import socket
import threading
import time
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Proxy"
}

print("🔍 Simple Python Port Scanner\n")

target = input("Enter IP address to scan: ").strip()
start_port = int(input("Enter start port (e.g. 1): ").strip())
end_port = int(input("Enter end port (e.g. 1024): ").strip())

open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((target, port))
        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"[+] Port {port} is open ({service})")
            open_ports.append((port, service))
        s.close()
    except:
        pass

threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
    
if not open_ports:
    print("\n❌ No open ports found.")
else:
    print("\n✅ Scan complete.")
