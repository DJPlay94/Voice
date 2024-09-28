import random, time
from logic import *

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}

count = 0

level = input("Выберите сложность игры: (easy/normal/hard) \n")

if isinstance(level, str):
    if level == "easy":
        for i in range(3):
            random_word = random.choice(levels["easy"])
            print(f"Скажите слово {random_word}")
            time.sleep(1)
            print("Говорите")
            text = speach_en()
            if random_word == text.lower():
                count += 1
                print("Верно")
            else:
                print("Неправильно")
                print(text)
    elif level == "normal":
        for i in range(3):
            random_word = random.choice(levels["normal"])
            print(f"Скажите слово {random_word}")
            time.sleep(1)
            print("Говорите")
            text = speach_en()
            if random_word == text.lower():
                count += 1
                print("Верно")
            else:
                print("Неправильно")
                print(text)
    elif level == "hard":
        for i in range(3):
            random_word = random.choice(levels["hard"])
            print(f"Скажите слово {random_word}")
            time.sleep(1)
            print("Говорите")
            text = speach_en()
            if random_word == text.lower():
                count += 1
                print("Верно")
            else:
                print("Неправильно")
                print(text)

print(f"У вас {count} очков")