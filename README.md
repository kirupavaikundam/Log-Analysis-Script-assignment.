markdown
# Log Analysis Script

## Description
This project provides a Python-based solution for analyzing server log files to extract meaningful insights. The script processes web server logs, extracting key data such as the number of requests per IP address, the most accessed endpoint, and suspicious activity (e.g., failed login attempts). The results are saved in a structured CSV format for further analysis or reporting.

---

## Features
- **Analyze Server Logs:** Parse log files to extract IP addresses, HTTP methods, endpoints, and response statuses.
- **IP Activity Tracking:** Count the number of requests made by each IP address.
- **Endpoint Analytics:** Identify the most frequently accessed endpoint.
- **Security Insights:** Detect suspicious activities like failed login attempts (HTTP status 401).
- **CSV Output:** Export analyzed data to a CSV file for easy interpretation.

---

## Workflow
### Input
The script reads from a server log file (`sample.log`).

### Processing
- Extracts data using regular expressions.
- Tracks request counts per IP.
- Identifies the most accessed endpoint.
- Counts failed login attempts per IP.

### Output
Generates a structured CSV file (`log_analysis_results.csv`) with:
1. Request counts per IP.
2. The most accessed endpoint and its access count.
3. Suspicious activity with failed login attempts.

---

## Setup Instructions
### Prerequisites
1. **Python 3.x** installed on your system.
2. A server log file (`sample.log`) in standard log format.
3. Clone or download the repository containing the script.

### Installation
Install the required libraries (if not already available):
bash
pip install -r requirements.txt


### Directory Structure

log-analysis/
├── sample.log                   # Input log file
├── log_analysis_results.csv     # Output CSV file (generated after execution)
├── script_name.py               # Main Python script


---

## Execution
1. Place the `sample.log` file in the same directory as the script.
2. Run the script:
   bash
   python script_name.py
   
3. Check the output in the generated `log_analysis_results.csv`.

---

## Output Format
The output CSV file includes the following sections:

### 1. Requests per IP
| IP Address     | Request Count |
|----------------|---------------|
| 192.168.1.1    | 45            |

### 2. Most Accessed Endpoint
| Endpoint | Access Count |
|----------|--------------|
| /home    | 250          |

### 3. Suspicious Activity
| IP Address     | Failed Login Count |
|----------------|---------------------|
| 203.0.113.10   | 12                  |

---

## Customization
1. Modify the `log_file` and `output_csv` variables in `script_name.py` to use custom input and output file paths.
2. Adjust the regex pattern (`log_pattern`) for parsing non-standard log formats.

---

## Potential Use Cases
- **Web Server Traffic Analysis:** Understand server usage patterns and optimize performance.
- **Security Monitoring:** Identify potential malicious activity based on failed login attempts.
- **Endpoint Optimization:** Improve endpoint performance by analyzing high-traffic areas.

---

## Contact
For issues or suggestions, please reach out:
- **Name:** Kirupa Vaikundam  
- **Email:** kirupavaikundam@gmail.com  
- **GitHub:** [https://github.com/kirupavaikundam](https://github.com/kirupavaikundam)  
- **LinkedIn:** [https://www.linkedin.com/in/kirupa-v](https://www.linkedin.com/in/kirupa-v)  
