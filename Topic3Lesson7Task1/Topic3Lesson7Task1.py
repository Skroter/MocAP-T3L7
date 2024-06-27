word = input("Введите слово: ")
word1 = word[::-1]
if word == word1:
    print("Yes")
else:
    print("No")