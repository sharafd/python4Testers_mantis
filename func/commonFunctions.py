# -*- coding: utf-8 -*-

# Общие вспомогательные функции
import random
import re, string

max_char_count = len(string.ascii_letters + string.digits + string.punctuation)

class Common:

    # Вырезаем символы по шаблону
    def clear(self,s, pattern):
        return re.sub(pattern,"",s)

    # Случайная строка из цифр
    # count - количество символов в строке
    def random_digits(selfself, count = None):
       if count is None:
           count = random.randrange(max_char_count)
       return "".join([random.choice(string.digits) for i in range(count)])

    # Случайная строка
    # count - количество символов в строке
    def random_ascii_string(self, count = None):
        if count is None:
           count = random.randrange(max_char_count)
        return "".join([random.choice(string.ascii_letters) for i in range(count)])

    # Случайная строка из знаков препинания
    # count - количество символов в строке
    def random_punctuation(self, count = None):
        if count is None:
           count = random.randrange(max_char_count)
        return "".join([random.choice(string.punctuation) for i in range(count)])

    # Случайная строка (буквы и цифры)
    # count - количество символов в строке
    def random_string(self, count = None):
       if count is None:
           count = random.randrange(max_char_count)
       return "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(count)])

