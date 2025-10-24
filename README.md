# Py-port-scanner
Python, socket ve threading kullanan hızlı port ve versiyon tarayıcı.
# Py-Port-Scanner (Hızlı Port ve Versiyon Tarayıcı)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20|%20Windows%20|%20macOS-brightgreen?style=for-the-badge)

## (English)

A high-performance, multi-threaded port and version scanner built with Python. This tool uses `socket`, `threading`, and `Queue` modules to perform fast and concurrent network scanning. It's designed to be a simple yet powerful tool for network reconnaissance and learning about network programming.

### Features

* **Fast & Concurrent:** Uses multi-threading (`threading`) and a `Queue` system to scan multiple ports simultaneously (default 100 threads).
* **Version Detection (Banner Grabbing):** Connects to open ports to grab the service banner (`s.recv`) and identify the running service/version.
* **Flexible Targets:** Accepts both IP addresses (e.g., `8.8.8.8`) and domain names (e.g., `scanme.nmap.org`).
* **Flexible Port Input:** Supports multiple port formats:
    * **Single Port:** `80`
    * **Comma-separated list:** `80,443,22,3389`
    * **Port Range:** `1-1024`
* **Performance Metrics:** Calculates and displays the total scan time upon completion.
* **Reliable:** Includes proper error handling for host resolution (`socket.gaierror`), connection errors, and timeouts.

### Requirements

* Python 3
* All required modules (`socket`, `ipaddress`, `sys`, `threading`, `queue`, `time`) are part of the Python standard library. No `pip install` is needed.

### How to Use

1.  Clone the repository (veya kodu `tarayici.py` olarak kaydedin):
    ```bash
    git clone [https://github.com/Omerteq/Py-port-scanner.git](https://github.com/Omerteq/Py-port-scanner.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd Py-port-scanner
    ```
3.  Run the script:
    ```bash
    python3 tarayici.py
    ```
4.  Follow the interactive prompts:
    ```
    Lütfen hedef domain adı veya IP adresi giriniz: scanme.nmap.org
    Lütfen taranacak portları giriniz (örn: 80,443 veya 1-1000): 22,80,443,21,1000-1010
    ```

### Example Output
