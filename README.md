# Linux Log Monitoring Tool

## Description
A Python-based security monitoring tool that watches Linux authentication logs in real time and detects failed SSH login attempts.

## Features
- Monitors `/var/log/auth.log`
- Detects failed login attempts
- Prints alerts in real time
- Useful for basic intrusion detection

## Technologies Used
- Linux
- Python 
- System logs
- SSH
- Github

## How It Works
The script continuously reads the authentication log file and looks for keywords related to failed login attempts. When detected, it immediately prints an alert with the log entry.

## How to Run
```bash
python3 log_monitor.py

