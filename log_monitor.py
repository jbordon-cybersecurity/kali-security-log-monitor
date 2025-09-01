import subprocess

print("[*] Starting log monitoring...")
print("[*] Watching for failed SSH login attempts (journalctl -f)...\n")

# Start the journalctl process to follow logs in real-time
process = subprocess.Popen(
    ["sudo", "journalctl", "-f", "-o", "cat"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

for line in iter(process.stdout.readline, ''):
    if "Failed password" in line:
        print(f"[ALERT] {line.strip()}")
