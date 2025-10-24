# =================================================================
# ÇOK İŞ PARÇACIKLI (THREADED) PORT TARAYICI
# Amacı: Bir hedefin (IP/Domain) belirtilen portlarını yüksek hızda kontrol eder.
# =================================================================

import socket         # Ağ iletişimi (Soket oluşturma ve bağlanma) için ana modül
import ipaddress      # IP adresi formatını kontrol etmek için
import sys            # Programı hata durumunda temiz bir şekilde sonlandırmak için
import threading      # Tarama işlemini hızlandırmak için çoklu iş parçacığı (thread) kullanmak
from queue import Queue # İşleri (portları) thread'lere güvenli bir şekilde dağıtmak için Kuyruk yapısı
import time           # Zamanlayıcı ve gecikme işlemleri için (şimdilik kullanılmıyor)



# --- GLOBAL AYARLAR ---
# Birden fazla thread'in aynı anda ekrana yazarken çıktıları karıştırmasını engelleyen kilit
print_lock = threading.Lock() 
THREAD_SAYISI = 100   # Aynı anda çalışacak işçi (thread) sayısı  
# --- FONKSİYONLAR ---

def ip_mi_adres_mi(hedef_adres):
    # Girilen adresin geçerli bir IP adresi olup olmadığını kontrol eder.
    try:
        ipaddress.ip_address(hedef_adres)
        return True
    except ValueError:
        return False
    
def port_tara(hedef_ip, hedef_port):
    # Bir işçi (thread) tarafından çağrılır, tek bir portu tarar.

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Timeout'u ayarla. (Aslında settimeout kullanmak daha iyidir ama bu da çalışır.)
    s.settimeout(1)
    try:    
         
        
        # connect_ex: Bağlanmayı dener. Başarılıysa 0 döndürür, aksi halde hata kodu.nereleri değiiştr
        s.connect((hedef_ip, hedef_port))
        try:
            banner = s.recv(1024).decode().strip()  # Sunucudan banner bilgisi almaya çalış
        except socket.timeout:
            banner = "Banner alınamadı (zaman aşımı)" #port açık olsa bile banner alınamazsa
        except UnicodeDecodeError:
            banner = "Banner alınamadı (kodlama hatası)" #banner kodlama hatası varsa
            
        
        with print_lock:
            print(f"Port {hedef_port} açık - server banner: {banner[:50]}") #banner bilgisini ilk 50 karakterle sınırla
        
    except socket.timeout:
        pass # Zaman aşımı bekleniyorsa yakala ve görmezden gel.
    except socket.error:
        pass # Genel bağlantı hatalarını yakala ve görmezden gel.
    finally:
        # Soketi (telefon hattını) her durumda kapatmak kritik öneme sahiptir.
        s.close()
        

def worker(q, hedef_ip):
    # Kuyruktan iş çeken ve tarama yapan sürekli çalışan işçi (thread).
    while True: # Sonsuz döngü: İş olduğu sürece çalış.
        try:    
            # Kuyruktan bir port numarası çek. (Kuyruk boşsa burada bekler)
            w_port = q.get() 
            # Çekilen portu tarama fonksiyonuna gönder
            port_tara(hedef_ip, w_port)
        finally:
            # İş bitince, kuyruğa o işin tamamlandığını bildir 
            q.task_done()

# ================= ANA PROGRAM AKIŞI =================

# --- GİRDİ ALMA ---
hedef_adres = input("Lütfen hedef domain adı veya IP adresi giriniz: ")
port_listesi = input("Lütfen taranacak portları giriniz (virgül koyunuz aralarına) : ") 


# --- PORT LİSTESİ İŞLEME VE HATA KONTROLÜ ---
taranacakportlar =[]

try:
    if "-" in port_listesi:    
        bolunmus_liste = port_listesi.split("-") # '-' ile ayrılmış port aralığını kontrol et
        baslangı_dizi = bolunmus_liste[0]
        bitis_dizi = bolunmus_liste[1]
        baslangıç = int(baslangı_dizi.strip()) # Başlangıç portu
        bitis = int(bitis_dizi.strip())        # Bitiş portu
        taranacakportlar = list(range(baslangıç, bitis + 1)) # Aralıktaki tüm portları listeye ekle

    else:
        # Virgülle ayrılmış port listesini işle
        str_port = port_listesi.split(",")
        for dizi_port in str_port :
            # dizi_port: Virgülle ayrılmış metin parçasını temsil eder
            # Bunu tam sayıya çevirip listeye ekle
            taranacakportlar.append(int(dizi_port)) #split ile boşlukları da temizle 

except ValueError:
    # Kullanıcı sayı yerine harf vb. girerse yakala
    print("Lütfen geçerli port numaraları giriniz.")
    sys.exit()


# --- IP ÇÖZÜMLEME VE HATA KONTROLÜ ---
try:
    if ip_mi_adres_mi(hedef_adres):
        hedef_ip = hedef_adres # Zaten IP ise, direkt kullan
    else :
        # Domain ise, IP'ye çevir. (Hata bu satırda oluşabilir)
        hedef_ip = socket.gethostbyname(hedef_adres)
except socket.gaierror:
    # Hedef bulunamazsa (DNS hatası), programı durdur.
    print("-"*50)
    print("Hedef adres bulunamadı. Lütfen geçerli bir domain adı giriniz.")
    sys.exit()


# --- BİLGİLENDİRME ÇIKTISI ---
print("-" * 50)
print(f"Taranan hedef: {hedef_adres}")
print(f"Çözümlenen IP adresi: {hedef_ip}")
print(f"Taranacak port sayısı: {len(taranacakportlar)}") # len() ile liste uzunluğunu al
print(f"Eşzamanlı işçi sayısı: {THREAD_SAYISI}") 
print("Tarama başlıyor (çoklu iş parçacığı ile)...")
print("-" * 50)

baslangic_zamani = time.time()  # Program başlangıç zamanını kaydet (şimdilik kullanılmıyor)
# --- THREADING VE KUYRUK BAŞLATMA ---
q = Queue() # Boş Sipariş Panosu'nu oluştur

for _ in range(THREAD_SAYISI):
    # 100 adet işçi (thread) oluştur ve başlat
    t = threading.Thread(target=worker, args=(q, hedef_ip), daemon=True) #target ile worker fonksiyonunu çağır args ile argümanları ver daemon=True ile ana program kapanınca thread'lerin de kapanmasını sağla (verimlilik için)
    t.start()

# Taranacak tüm portları kuyruğa ekle (İşçiler şimdi iş çekmeye başlar)
for portlar in taranacakportlar:
    q.put(portlar) #q için put metodu ile portları ekle

# Kuyruktaki tüm işler (portlar) bitene kadar ana programı bekle
q.join()

bitis_zamani = time.time()  # Program bitiş zamanını kaydet 
gecen_sure = bitis_zamani - baslangic_zamani  # Toplam geçen süre 


# --- BİTİŞ ---
print("-"*50)
print("Tarama tamamlandı.")
print(f"Toplam süre: {gecen_sure:.2f} saniye")  # Geçen süreyi ekrana yazdır 