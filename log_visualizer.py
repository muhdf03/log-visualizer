import re
import matplotlib.pyplot as plt
from collections import Counter

def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    ip_pattern = r'(\d{1,3}(?:\.\d{1,3}){3})'
    codes = []

    ips = [re.search(ip_pattern, line).group(1)
           for line in logs if re.search(ip_pattern, line)]

    for line in logs:
        match = re.search(r'" (\d{3})', line)
        if match:
            codes.append(match.group(1))

    return Counter(ips), Counter(codes)

def plot_data(counter, title, xlabel):
    labels, values = zip(*counter.items())
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ip_counts, code_counts = parse_log("sample_log.txt")

    print("Top IPs:")
    for ip, count in ip_counts.items():
        print(f"{ip} — {count} hits")

    print("\nHTTP Status Codes:")
    for code, count in code_counts.items():
        print(f"{code}: {count} times")

    plot_data(ip_counts, "Requests per IP", "IP Address")
    plot_data(code_counts, "HTTP Status Codes", "Status Code")
