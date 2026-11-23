import random
def guess_game():
    lucky_number = random.randint(1,100)
    
    while True :
        A = int(input("Guess the number: "))
        if A  == lucky_number :
            print ("You won the game!")
            break
        elif A  > lucky_number :
            print("Come Down")
        else:
            print("Go UP")
        
    print("Thanks for playing the game")

guess_game()