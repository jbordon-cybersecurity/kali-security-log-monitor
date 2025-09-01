# Kali Security Log Monitor

A Python-based security tool for monitoring **system logs in real-time** on Kali Linux.  
Built to practice log monitoring, alerting, and scripting for security operations and SOC tasks.

---

## Features
- Real-time log monitoring using `journalctl`.
- Detects **failed SSH login attempts** and raises alerts.
- Beginner-friendly Python script that can be easily extended.
- Lightweight and portable for any systemd-based Linux environment.

---

## Skills Demonstrated
- **Python scripting**: subprocess handling and text parsing.
- **Linux log analysis**: reading and filtering system logs.
- **Security operations basics**: monitoring for suspicious login attempts.
- **Automation**: creating reusable tools for security tasks.

---

## How to Run

### Clone the repository
```bash
git clone https://github.com/jbordon-cybersecurity/kali-security-log-monitor.git
cd kali-security-log-monitor

### Run the script

sudo python3 log_monitor.py

### Simulate a failed login (test alert)
Open a second terminal and run:

ssh fakeuser@localhost

Enter any random password, then check your first terminal — you should see an alert like:

[ALERT] Failed password for invalid user fakeuser from 127.0.0.1 port 50550 ssh2


### Project Structure

kali-security-log-monitor/
│
├── log_monitor.py   # Main script
├── README.md        # Documentation
└── .gitignore       # Ignored files and folders


### Future Improvements ###

Save alerts to a log file.

Email or Slack notifications.

Multi-event detection for brute-force or privilege escalation attempts.

Web dashboard for real-time alerts.

This project is public for demonstration and educational purposes.
All rights reserved © 2025 Jose Bordon.
