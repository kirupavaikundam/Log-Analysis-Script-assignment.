# Log Analysis Script

## Description
This project provides a Python-based solution for analyzing server log files to extract meaningful insights. The script processes web server logs, extracting key data such as the number of requests per IP address, the most accessed endpoint, and suspicious activity (failed login attempts). The results are saved in a structured CSV format for further analysis or reporting.

---

## Features
* **Analyze Server Logs**: Parse log files to extract IP addresses, HTTP methods, endpoints, and response statuses.
* **IP Activity Tracking**: Count the number of requests made by each IP address.
* **Endpoint Analytics**: Identify the most frequently accessed endpoint.
* **Security Insights**: Detect suspicious activities like failed login attempts (HTTP status 401).
* **CSV Output**: Export analyzed data to a CSV file for easy interpretation.
  
---


## Workflow
1. **Input**: The script reads from a server log file (`sample.log`).
2. **Processing**:
   * Extracts data using regular expressions.
   * Tracks request counts per IP.
   * Identifies the most accessed endpoint.
   * Counts failed login attempts per IP.
3. **Output**:
   * Generates a structured CSV file (`log_analysis_results.csv`) with:
     * Request counts per IP.
     * The most accessed endpoint and its access count.
     * Suspicious activity with failed login attempts.

---

## Setup Instructions
1. **Prerequisites**:
   * Python 3.x installed on your system.
   * `sample.log`: A log file in standard server log format.
   
2. **Clone or Download** the repository containing the script.

3. **Install Required Libraries** (if not available):
   ```bash
   pip install -r requirements.txt
   
4. **Directory Structure**:
graphql
├── sample.log                 # Input log file
├── log_analysis_results.csv   # Output CSV file (generated after execution)
├── script_name.py             # Main Python script

5.**Execution**:
Place the sample.log file in the same directory as the script.
Run the script:
bash
python script_name.py
Check the output in the generated log_analysis_results.csv.

6.**Output Format**:
The output CSV file includes the following sections:
1. #Requests per IP#
IP Address	    Request Count
192.168.1.1   	45
2. #Most Accessed Endpoint#
Endpoint	      Access Count
/home	          250
3. #Suspicious Activity#
IP Address	    Failed Login Count
203.0.113.10	  12
   
7.**Customization**:
Modify the log_file and output_csv variables in script_name.py to use custom input and output file paths.
Adjust the regex pattern (log_pattern) for parsing non-standard log formats.

8.**Potential Use Cases**:
Web server traffic analysis.
Identifying potential malicious activity based on failed login attempts.
Improving endpoint performance by analyzing high-traffic areas.

**Contact**
For issues or suggestions, contact:
Name: Kirupa Vaikundam
Email: kirupavaikundam@gmail.com
GitHub: https://github.com/kirupavaikundam
Linkedin: www.linkedin.com/in/kirupa-v
