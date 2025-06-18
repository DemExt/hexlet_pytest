with open('input.txt', 'r', encoding='utf-8') as f:
    original_text = f.read()

# Переворот текста
reversed_text = reverse(original_text)

# Запись перевернутого текста в файл output.txt
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(reversed_text)