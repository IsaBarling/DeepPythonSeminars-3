from collections import Counter
import nltk
nltk.download('stopwords')  # Загрузка стоп-слов из библиотеки nltk

def count_words(text):
    words = text.lower().split()  # Разбиение текста на слова и приведение к нижнему регистру
    word_counts = Counter(words)  # Подсчет частоты встречаемости слов
    return word_counts

def print_top_words(word_counts, n=10):
    print("10 самых часто встречающихся слов в статье:")
    for word, count in word_counts.most_common(n):
        print(f"- {word}: {count}")

# Открываем файл и считываем текст
file_path = "d:\Github5\seminar3\\text.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Подсчитываем слова и выводим топ-10
word_counts = count_words(text)
print_top_words(word_counts)
