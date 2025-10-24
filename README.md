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
Taranan hedef: scanme.nmap.org Çözümlenen IP adresi: 45.33.32.156 Taranacak port sayısı: 15 Eşzamanlı işçi sayısı: 100 Tarama başlıyor (çoklu iş parçacığı ile)...
Port 80 açık - Servis: (Banner bilgisi yok veya zaman aşımı)... Port 22 açık - Servis: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1... Port 443 açık - Servis: (Şifreli/Binary Veri)...
Tarama tamamlandı. Toplam süre: 1.02 saniye

### ⚠️ Disclaimer

This tool is intended for educational purposes and for use in authorized security testing (e.g., CTFs, your own lab) only. Unauthorized scanning of networks or systems is illegal. The author is not responsible for any misuse or damage caused by this program.

---

## (Türkçe)

Python ile geliştirilmiş yüksek performanslı, çok iş parçacıklı (multi-threaded) bir port ve versiyon tarayıcı. Bu araç, hızlı ve eşzamanlı ağ taraması yapmak için Python'un `socket`, `threading` ve `Queue` modüllerini kullanır. Ağ keşfi ve ağ programlama öğrenimi için basit ama güçlü bir araç olarak tasarlanmıştır.

### Özellikler

* **Hızlı ve Eşzamanlı:** Birden fazla portu aynı anda taramak için çoklu iş parçacığı (`threading`) ve bir `Queue` (Kuyruk) sistemi kullanır (varsayılan 100 işçi).
* **Versiyon Tespiti (Banner Yakalama):** Açık portlara tam bağlantı kurarak servis "banner"ını (`s.recv`) yakalar ve çalışan servisi/versiyonu tanımlamaya çalışır.
* **Esnek Hedefleme:** Hem IP adreslerini (örn: `8.8.8.8`) hem de alan adlarını (örn: `scanme.nmap.org`) kabul eder.
* **Esnek Port Girişi:** Birden fazla port giriş formatını destekler:
    * **Tek Port:** `80`
    * **Virgülle Ayrılmış Liste:** `80,443,22,3389`
    * **Port Aralığı:** `1-1024`
* **Performans Ölçümü:** Tamamlandığında toplam tarama süresini hesaplar ve gösterir.
* **Güvenilir:** Hedef çözümleme (`socket.gaierror`), bağlantı hataları ve zaman aşımları için uygun hata yönetimi içerir.

### Gereksinimler

* Python 3
* Gerekli tüm modüller (`socket`, `ipaddress`, `sys`, `threading`, `queue`, `time`) Python standart kütüphanesinin bir parçasıdır. Ek bir `pip install` kurulumu gerekmez.

### Nasıl Kullanılır

1.  Depoyu klonlayın (veya kodu `tarayici.py` olarak kaydedin):
    ```bash
    git clone [https://github.com/Omerteq/Py-port-scanner.git](https://github.com/Omerteq/Py-port-scanner.git)
    ```
2.  Proje dizinine gidin:
    ```bash
    cd Py-port-scanner
    ```
3.  Betiği çalıştırın:
    ```bash
    python3 tarayici.py
    ```
4.  Etkileşimli komutları izleyin:
    ```
    Lütfen hedef domain adı veya IP adresi giriniz: scanme.nmap.org
    Lütfen taranacak portları giriniz (örn: 80,443 veya 1-1000): 22,80,443,21,1000-1010
    ```

### Örnek Çıktı
Taranan hedef: scanme.nmap.org Çözümlenen IP adresi: 45.33.32.156 Taranacak port sayısı: 15 Eşzamanlı işçi sayısı: 100 Tarama başlıyor (çoklu iş parçacığı ile)...
Port 80 açık - Servis: (Banner bilgisi yok veya zaman aşımı)... Port 22 açık - Servis: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1... Port 443 açık - Servis: (Şifreli/Binary Veri)...
Tarama tamamlandı. Toplam süre: 1.02 saniye

### ⚠️ Yasal Uyarı

Bu araç yalnızca eğitim amaçlı ve yetkili güvenlik testlerinde (örn: CTF'ler, kendi laboratuvarınız) kullanım için tasarlanmıştır. Ağların veya sistemlerin izinsiz taranması yasa dışıdır. Yazar, bu programın kötüye kullanılmasından veya neden olduğu zararlardan sorumlu değildir.
