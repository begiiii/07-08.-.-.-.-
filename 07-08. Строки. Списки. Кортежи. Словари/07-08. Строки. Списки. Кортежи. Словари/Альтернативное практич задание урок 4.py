
import random 
words = ["���������", "������", "����������", "��������"] 
word = random.choice(words) 
answerList = ['-' for c in range(len(word))] 
remainingLetters = len(word) 

attempt = 15

for element in word: 
    while remainingLetters > 0 and attempt > 0: 
        print(*answerList) 
        guess = input("�������� �����: ") 
        if len(guess) != 1: 
            print("������� ��������� �����") 
        elif answerList.__contains__(guess.lower()):
            print("��� ����� ��� ���� �������!")
        elif guess.lower() < chr(1072) or guess.lower() > chr(1103):
            print('������� �����!')
        else: 
            for i in range(len(word)): 
               if word[i] == guess.lower(): 
                    answerList[i] = guess 
                    remainingLetters -= 1 
            attempt -=1
if(attempt <=0):
    print("�� ���������")
else :
    print(*answerList) 
    print(f"�������, ���� �������� ����� {word}")  
                  
