import string, random, re

n = random.randint(1,1000)
i = 0
longWord = ''

while i<n:
    longWord += random.choice(string.ascii_lowercase + ' ') # string.ascii_lowercase <- ���� �������� �� 'a' ��������� �������� ����� ��������
    i += 1
print(longWord)

while '  ' in longWord:
    longWord = longWord.replace('  ', ' ')
print(longWord)