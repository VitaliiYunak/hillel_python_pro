# Завдання 3. Видобування хеш-тегів з тексту

import re


def extract_hashtags(text):
    """ пошуку хеш-тегів
    """
    hashtags = re.findall(r'#\w+', text)
    return hashtags


if __name__ == "__main__":
    text = "ДПА-2025 скасовано, а вступна компанія відбудетьсчя за особливою процедурою (теги: #ДПА2025, #НМТ2025)."
    hash_tags = extract_hashtags(text)
    print(hash_tags)
