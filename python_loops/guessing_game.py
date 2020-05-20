# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
print('Texmin oyunu')
num = 77
count = 10
iterator = 0

while iterator < count:
    guess = int(input('Texmininizi daxil edin: '))
    if guess == num:
        print('Siz qalib geldiniz bizim nezerde tutdugumuz eded', num, 'idi')
        break
    print('Bir daha ceht edin!')
    iterator += 1

print('Oyun bitti')