# Завдання 7. Пошук IP-адрес

import re


def search_ip(text):
    """ Знаходження IPv4-адрес
    """
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
    ip4 = re.findall(pattern, text)

    valid_ip = []
    for ip in ip4:
        is_valid = True
        for num in ip.split('.'):
            if not (0 <= int(num) <= 255):
                is_valid = False
                break
        if is_valid:
            valid_ip.append(ip)

    return valid_ip


if __name__ == "__main__":
    text = "Використовуємо наступні адреси: 192.168.1.889, 256.100.50.25, 10.0.0.255, 172.16.0.10., 786.764.234.10"
    ipv4_addresses = search_ip(text)
    print(ipv4_addresses)
