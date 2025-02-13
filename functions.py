def is_in(big_word, small_word):
    for i in small_word:
        if small_word.count(i) > big_word.count(i):
            return False
    return True

def find_words(word):
    result = []
    with open('words.txt', 'r', encoding='utf-8') as file:
        # Проходимся по каждой строке файла
        for line in file:
            # Убираем лишние пробелы и символы перевода строки
            clean_line = line.strip()
            # Выводим строку
            if is_in(word, clean_line):
                result.append(clean_line)
            
    return result