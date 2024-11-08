import random
import requests

# Shodan API Key (Insert your own key here)
SHODAN_API_KEY = "0N3MduttCZVKFwVAga6Eap5jYGnNq65h"
BASE_URL = "https://api.shodan.io"

# Generate random IP range (from 1 to 9)
def random_ip_in_range():
    # Randomly select a range from 1 to 9
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

# Send request to Shodan API
def get_shodan_info(ip):
    try:
        # Shodan API endpoint
        url = f"{BASE_URL}/shodan/host/{ip}?key={SHODAN_API_KEY}"
        
        # HTTP GET request
        response = requests.get(url)
        
        if response.status_code == 200:
            result = response.json()

            # Print device information
            print(f"\033[1;31m [+] IP Address: \033[1;33m{ip}")
            print(f"\033[1;32m [+] Device Type: \033[1;34m{result.get('product', 'No Info')}")
            print(f"\033[1;35m [+] Ports: \033[1;36m{', '.join(str(port) for port in result['ports'])}")
            print(f"\033[1;36m [+] Device Info: \033[1;37m{result.get('data', 'No Data Found')}")
            print("\n")
        else:
            print(f"\033[1;31m[-] No information found for IP: {ip}")
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31m[!] HTTP request error: {e}")

# Get random Shodan device information
def random_shodan_info():
    for _ in range(5):
        start_ip, end_ip = random_ip_in_range()

        # Select a random IP from the generated range
        random_ip = random_ip_in_range()[0]
        print(f"\033[1;34mSelected IP Range: {start_ip} - {end_ip}")
        get_shodan_info(random_ip)

# Run the script
random_shodan_info()