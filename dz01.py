import math
from pathlib import Path
from collections import Counter


def area():
    print("Unesi radijus: ")
    r = float(input())
    return (r ** 2) * math.pi


def bondify():
    print("Unesi puno ime agenta: ")
    ime = input()
    prezime = ime.split()[-1]
    if prezime.count('-'):
        zime = prezime.split('-')[-1]
        return f'{zime}. {ime}\n'
    else:
        return f'{prezime}. {ime}\n'


def cleanex():
    print("Unesi ime datoteke: ")
    file = input()
    return Path(file).stem


def is_palindrome():
    print("Unesi string: ")
    s = input()
    s = s.replace(" ", "").upper()
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return "Nije palindrom :(\n"
    # if str == str[::-1]:
    return "Palindrom ^^\n"


def leap_year():
    print("Unesi godinu: ")
    year = int(input())
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Prijestupna\n (o)\n  (\n < \\ \n"
    else:
        return "Nije prijestupna\n \\ /\n  |\n /o\\ \n"


def when_is_it_easter_mister():
    # Anonymous Gregorian algorithm
    print("Unesi godinu: ")
    year = int(input())
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    j = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 19 * j) // 433
    month = (h + j - 7 * m + 90) // 25
    day = (h + j - 7 * m + 33 * month + 19) % 32
    return f'Uskrs je {day}.{month}.\n'


def rowmanize():
    with open("in.txt", "r") as file1:
        lines = file1.readlines()
        with open("rowmanize.txt", "w") as file2:
            for line in lines:
                file2.write(line.strip() + " ")


def analyze():
    with open("in.txt", "r") as file1:
        lines = file1.read().splitlines()
        mc = Counter(lines).most_common(5)
        with open("analyze.txt", "w") as file2:
            for element in mc:
                file2.write(f'{element[0]}: {element[1]}\n')


def fermat():
    print("Unesi broj: ")
    n = int(input())
    return f'Ti kazes {n}, Fermat kaze {2 ** (2 ** n) + 1}\n'


def prime():
    print("Unesi broj: ")
    num = int(input())
    flag = True
    if num > 1:
        flag = False
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return f'{num} nije prost\n'
    else:
        return f'{num} je prost\n'


def encrypt(text, pomak):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + pomak - 65) % 26 + 65)
        else:
            result += chr((ord(char) + pomak - 97) % 26 + 97)
    return result


def decrypt(text, pomak):
    return encrypt(text, -pomak)


if __name__ == '__main__':
    print(area())
    print(bondify())
    print(cleanex())
    print(is_palindrome())
    print(leap_year())
    print(when_is_it_easter_mister())
    rowmanize()
    analyze()
    print(fermat())
    print(prime())

    text = "INCOGNITO"
    pomak = 3
    dext = encrypt(text, pomak)

    print(text + " --> " + dext)
    print(dext + " --> " + decrypt(dext, pomak))
