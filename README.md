# 🌐 Proxy Selector  

## 📝 Description  
**Proxy Selector** is a Python script that filters and selects the best proxies from a `result.json` file based on customizable criteria:  
- 🔒 **Anonymity Level** (`anonymity_level`)  
- ⏳ **Uptime** (`min_uptime`)  
- ⚡ **Latency** (`max_latency`)  
- 🌍 **Protocols** (`protocol`)  

The script requires running a parsing process through the `parsing_process` function beforehand. The parsing results are saved in the `result.json` file.  

## 🛠 Installation  
1. Clone the repository:  
   ```bash
   https://github.com/security-hab/proxy-scraper.git
   cd proxy-scraper
   ```

2. Install the required dependencies (if any):  
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage  
1. Execute the main script:  
   ```bash
   python main.py
   ```

3. If valid proxies are found, they will be displayed in the terminal:  
   ```plaintext
   🌟 Best proxies:
   [1] IP: 192.168.0.1, Uptime: 99.50%, Latency: 50ms, Protocols: socks5, http
   [2] IP: 192.168.0.2, Uptime: 99.70%, Latency: 30ms, Protocols: socks5
   ```

## ⚙️ Customization  
You can adjust the filtering criteria by modifying the parameters of the `proxySelector` function in `main.py`:  
```python
best_proxies = proxySelector(
    proxies,
    anonymity_level="elite",
    min_uptime=99.0,
    max_latency=100.0,
    protocol="socks5",
)
```

## ❗ Error Handling  
- ❌ If the `result.json` file is not found, the script will prompt you to run the parser first.  
- ⚠️ If the `result.json` file contains invalid JSON, an error message will be displayed.  

## 📋 Requirements  
- 🐍 Python 3.7 or higher  
- 📂 `result.json` file generated by the parsing process  
