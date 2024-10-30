# Завдання 5. Видалення HTML-тегів

import re


def remove_html_tags(html_text):
    """Видалення HTML-тегів
    """
    without_html = re.sub(r'<.*?>', '', html_text)
    return without_html


if __name__ == "__main__":
    text = '''
    <p>
    <span style="font-weight: 400;">Цим документом передбачено внесення змін до законів України </span>
    <span style="font-weight: 400;">«Про вищу освіту», «Про фахову передвищу освіту» та «Про повну загальну 
    середню освіту», </span><span style="font-weight: 400;">що врегульовують питання завершення навчального року 
    в системі загальної середньої освіти й проведення вступної кампанії до закладів вищої та фахової 
    передвищої освіти. </span>
    </p>
    '''
    print(remove_html_tags(text))
