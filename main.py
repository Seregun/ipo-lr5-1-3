def count(filename):
    try:
        with open(name, "r", encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "Файл не найден."
filename = 'text.txt'
count = count(filename)
print(f"Кол-во слов в файле'{filename}': {word_count}")