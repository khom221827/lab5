import re

class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.text = self._read_file()
        self.first_sentence = self._get_first_sentence()
        self.words = self._get_words()
        
    def _read_file(self):
        """Читає вміст файлу."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print("Файл не знайдено.")
            return ""
        except Exception as e:
            print("Помилка: ", str(e))
            return ""

    def _get_first_sentence(self):
        """Отримує перше речення з тексту."""
        if self.text:
            first_sentence = re.split(r'(?<=[.!?])\s', self.text)[0]
            return first_sentence
        return ""

    def _get_words(self):
        """Отримує всі слова з тексту."""
        return re.findall(r'\b[а-яїєіїґa-z]+\b', self.text.lower())

    def analyze(self):
        """Аналізує текст і виводить результати."""
        print("Перше речення:")
        print(self.first_sentence)

        ukrainian_words = sorted([word for word in self.words if re.match(r'^[а-яїєіїґ]+$', word)])
        english_words = sorted([word for word in self.words if re.match(r'^[a-z]+$', word)])

        if ukrainian_words:
            print("\nУкраїнські слова:")
            print(', \n'.join(ukrainian_words))
        if english_words:
            print("\nАнглійські слова:")
            print(', \n'.join(english_words))

        print("\nЗагальна кількість слів:", len(self.words))


# Використання класу
analyzer = TextAnalyzer('filename.txt')
analyzer.analyze()
