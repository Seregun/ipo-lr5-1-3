file = open("text.txt", "r") # Открытие файла text.txt для чтения
text = file.read() # Считывание текста из файла   
print(text) 
words_count = len(text.split()) # Разделение текста на слова с помощью пробелов и подсчет их количества
print(f"В файле text.txt {words_count} слов.") # Вывод результата
