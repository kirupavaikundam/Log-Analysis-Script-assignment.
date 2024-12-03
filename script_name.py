import re
import csv
from collections import defaultdict

# Define the log file path
log_file = "sample.log"
output_csv = "log_analysis_results.csv"

# Initialize data structures
ip_requests = defaultdict(int)
endpoint_access = defaultdict(int)
failed_logins = defaultdict(int)

# Regex to extract data from log lines
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?"(?P<method>\w+)\s(?P<endpoint>/\S*)\sHTTP/\d+\.\d+"\s(?P<status>\d+).*'
)

# Process the log file
with open(log_file, 'r') as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            ip = match.group("ip")
            endpoint = match.group("endpoint")
            status = int(match.group("status"))
            
            # Count requests per IP
            ip_requests[ip] += 1
            
            # Count access per endpoint
            endpoint_access[endpoint] += 1
            
            # Count failed logins (status 401)
            if status == 401:
                failed_logins[ip] += 1

# Determine the most accessed endpoint
most_accessed_endpoint = max(endpoint_access.items(), key=lambda x: x[1])

# Save the results to a CSV file
with open(output_csv, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write Requests per IP
    writer.writerow(["Requests per IP"])
    writer.writerow(["IP Address", "Request Count"])
    for ip, count in ip_requests.items():
        writer.writerow([ip, count])
    writer.writerow([])
    
    # Write Most Accessed Endpoint
    writer.writerow(["Most Accessed Endpoint"])
    writer.writerow(["Endpoint", "Access Count"])
    writer.writerow([most_accessed_endpoint[0], most_accessed_endpoint[1]])
    writer.writerow([])
    
    # Write Suspicious Activity
    writer.writerow(["Suspicious Activity"])
    writer.writerow(["IP Address", "Failed Login Count"])
    for ip, count in failed_logins.items():
        writer.writerow([ip, count])

print(f"Analysis saved to {output_csv}")
