# Log Visualizer

A Python-based log analysis tool that reads and analyzes web server logs to reveal potential security insights.

Features:
- Extracts IP addresses and HTTP status codes from raw logs
- Counts how many times each IP appears (can indicate brute force or scraping)
- Counts each HTTP response type (200, 403, 401, etc.)
- Visualizes both datasets using bar charts (matplotlib)

How to Use:
1. Make sure you have Python 3 and matplotlib installed:
   pip install matplotlib

2. Place your log file as sample_log.txt in the same directory

3. Run:
   python log_visualizer.py

Sample Log Format:
10.0.0.1 - - [10/May/2025:10:13:23] "GET /index.html HTTP/1.1" 200
8.8.8.8 - - [10/May/2025:10:15:23] "GET /home HTTP/1.1" 200

Output:
- Console prints top IPs and status codes
- Two bar charts:
  - IPs by request volume
  - HTTP response codes

Built as part of my cybersecurity learning while preparing for my CompTIA Security+ certification.
