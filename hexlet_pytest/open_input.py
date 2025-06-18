def reverse(string):
    return string[::-1]

long_text = (
    "Это пример длинного текста, который мы будем использовать для тестирования функции reverse.\n"
    "Он содержит несколько строк, чтобы проверить работу функции на большом объёме данных.\n"
    "Пожалуйста, убедитесь, что функция правильно переворачивает весь текст.\n"
    "Спасибо за внимание!"
)

with open('input.txt', 'w', encoding='utf-8') as f:
    f.write(long_text)

with open('input.txt', 'r', encoding='utf-8') as f:
    original_text = f.read()

reversed_text = reverse(original_text)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(reversed_text)