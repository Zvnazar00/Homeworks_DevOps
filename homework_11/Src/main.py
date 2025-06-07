import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(" ".join(self.letters))

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        return "I am learning Python to build modern web applications and automate everyday tasks."


if __name__ == "__main__":
    eng_alphabet = EngAlphabet()

    print("Літери англійського алфавіту:")
    eng_alphabet.print()

    print("\nКількість літер в алфавіті:")
    print(eng_alphabet.letters_num())

    print("\nЧи належить літера 'F' до англійського алфавіту?")
    print(eng_alphabet.is_en_letter('F'))

    print("Чи належить літера 'Щ' до англійського алфавіту?")
    print(eng_alphabet.is_en_letter('Щ'))

    print("\nПриклад англійського тексту:")
    print(EngAlphabet.example())
