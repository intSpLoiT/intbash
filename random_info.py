import random
import requests

# Shodan API Anahtarını Buraya Ekleyin
SHODAN_API_KEY = "0N3MduttCZVKFwVAga6Eap5jYGnNq65h"
BASE_URL = "https://api.shodan.io"

# Rastgele IP aralığı oluşturma (1 ile 9 arasından)
def random_ip_in_range():
    # 1 ile 9 arasından rastgele bir aralık seç
    start_first = random.randint(1, 9)
    end_first = random.randint(start_first, 9)

    start_second = random.randint(0, 255)
    end_second = random.randint(0, 255)

    start_third = random.randint(0, 255)
    end_third = random.randint(0, 255)

    start_fourth = random.randint(1, 254)
    end_fourth = random.randint(start_fourth, 254)

    start_ip = f"{start_first}.{start_second}.{start_third}.{start_fourth}"
    end_ip = f"{end_first}.{end_second}.{end_third}.{end_fourth}"

    return start_ip, end_ip

# Shodan API'ye istek gönder
def get_shodan_info(ip):
    try:
        # Shodan API endpointi
        url = f"{BASE_URL}/shodan/host/{ip}?key={SHODAN_API_KEY}"
        
        # HTTP GET isteği
        response = requests.get(url)
        
        if response.status_code == 200:
            result = response.json()

            # Cihaz bilgilerini yazdır
            print(f"\033[1;31m [+] IP Adresi: \033[1;33m{ip}")
            print(f"\033[1;32m [+] Cihaz Tipi: \033[1;34m{result.get('product', 'Bilgi Yok')}")
            print(f"\033[1;35m [+] Portlar: \033[1;36m{', '.join(str(port) for port in result['ports'])}")
            print(f"\033[1;36m [+] Cihaz Bilgisi: \033[1;37m{result.get('data', 'Veri bulunamadı')}")
            print("\n")
        else:
            print(f"\033[1;31m[-] IP için bilgi alınamadı: {ip}")
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31m[!] HTTP isteği sırasında hata: {e}")

# Rastgele IP'lerle cihaz bilgisi al
def random_shodan_info():
    for _ in range(5):
        start_ip, end_ip = random_ip_in_range()

        # Rastgele bir IP seç
        random_ip = random_ip_in_range()[0]
        print(f"\033[1;34mSeçilen IP Aralığı: {start_ip} - {end_ip}")
        get_shodan_info(random_ip)

# Çalıştır
random_shodan_info()