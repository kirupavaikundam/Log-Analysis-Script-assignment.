# Log Analysis Script

## 📄 **Description**
This Python script analyzes server log files to uncover critical insights. It processes web server logs to extract meaningful data, such as:
- IP-wise request counts  
- Most accessed endpoints  
- Suspicious activities like failed logins  

Results are exported as a well-structured CSV file for reporting or deeper analysis.  

---

## ✨ **Features**
- **Log Parsing:** Extracts IP addresses, endpoints, HTTP methods, and response statuses using regex.
- **Activity Tracking:** Tracks request counts by IP and highlights high-traffic sources.
- **Endpoint Analysis:** Identifies the most frequently accessed endpoints.
- **Security Insights:** Detects failed login attempts (HTTP 401 errors) for potential threats.
- **CSV Output:** Saves insights in a clear CSV format.

---

## ⚙️ **Workflow**

### 🔗 **Input**  
The script reads server logs in standard format (e.g., `sample.log`).  

### 🔄 **Processing**  
- **Regex extraction** of key data points from log entries.  
- Counts requests per IP.  
- Tracks most accessed endpoints.  
- Identifies failed login attempts per IP.  

### 📂 **Output**  
A CSV file (`log_analysis_results.csv`) containing:  
1. **Request Counts per IP**  
2. **Most Accessed Endpoint**  
3. **Suspicious Activities (Failed Logins)**  

---

## 🛠️ **Setup Instructions**

### **Prerequisites**
1. **Python 3.x** installed.  
2. Access to a log file (`sample.log`).  
3. Clone or download the project repository.  

### **Installation**
Install dependencies using:
```bash
pip install -r requirements.txt
```

### **Directory Structure**
```plaintext
log-analysis/
├── sample.log                   # Input log file
├── log_analysis_results.csv     # Output CSV (generated after script execution)
├── script_name.py               # Main Python script
```

---

## 🚀 **Execution Steps**
1. Place the `sample.log` file in the script directory.  
2. Run the script:  
   ```bash
   python script_name.py
   ```  
3. Locate the output in `log_analysis_results.csv`.

---

## 📊 **Output Format**

### **1. Requests per IP**
| **IP Address**  | **Request Count** |
|------------------|-------------------|
| 192.168.1.1      | 45                |
| 203.0.113.22     | 33                |

### **2. Most Accessed Endpoint**
| **Endpoint** | **Access Count** |
|--------------|------------------|
| /home        | 250              |
| /login       | 200              |

### **3. Suspicious Activities**
| **IP Address**  | **Failed Login Count** |
|------------------|------------------------|
| 203.0.113.10     | 12                     |
| 198.51.100.15    | 8                      |

---

## 🎨 **Customization Options**
1. Update `log_file` and `output_csv` paths in `script_name.py` for custom file paths.  
2. Modify the regex pattern (`log_pattern`) to match specific log formats.  

---

## 📌 **Potential Use Cases**
- **Traffic Analysis:** Monitor server usage patterns and optimize resources.  
- **Security Monitoring:** Detect suspicious activities like brute-force attempts.  
- **Endpoint Optimization:** Identify and refine high-traffic endpoints for performance gains.  

---

## 📬 **Contact Information**
For questions, suggestions, or issues, reach out:  
- **Name:** Kirupa Vaikundam  
- **Email:** [kirupavaikundam@gmail.com](mailto:kirupavaikundam@gmail.com)  
- **GitHub:** [https://github.com/kirupavaikundam](https://github.com/kirupavaikundam)  
- **LinkedIn:** [https://www.linkedin.com/in/kirupa-v](https://www.linkedin.com/in/kirupa-v)  

---  

**Happy Logging!** 🎉
