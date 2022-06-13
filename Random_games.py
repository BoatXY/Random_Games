import random
def guess_num():
    No_of_Guesses = 1
    print("Welcome To the Guess The Number Game :\n"
          "In this game , you will have to guess a random number"
          "between  0 and the upper limit set by you.\n"
          "\n Please Enter The Upper Limit Number(Note: More the upper limit, Higher the Difficulty)\n")
    upper_limit = input()
    randnum = random.randint(0, int(upper_limit))
    while (No_of_Guesses<=5):
        number = input("\n Please Guess The Number :")
        if int(number) < randnum:
            print("\nThe Number is Greater than You have Guessed\n")
            No_of_Guesses = No_of_Guesses + 1
            Guesses_left = 6 - No_of_Guesses
            print(f"No.of Guesses Left is {Guesses_left}")
        elif int(number) > randnum:
            print("The Number is Lesser Than You Have Guessed\n")
            No_of_Guesses = No_of_Guesses + 1
            Guesses_left = 6 - No_of_Guesses
            print(f"No.of Guesses Left is {Guesses_left}")
        elif int(number) == randnum:
            print(f"Congratulations! , You have Guessed Correctly, The Number is {randnum}\n")
            print(f"\nThe No.of Chances it took is {No_of_Guesses}")
            break
        else:
            print("Wrong input")

        if No_of_Guesses > 5:
            print("Game Over")
            print(f"The No.of Chances it took is {No_of_Guesses}")

def stone():
    OptionsStone = ["Stone",  "stone", "1"]
    OptionsPaper = ["paper", "Paper",  "2"]
    OptionsScissor = ["scissor", "Scissor", "3"]
    CompOptions = ("Stone", "Paper", "Scissor")
    print("Welcome to the Stone-Paper-Scissor Game\n")
    print("You Can Enter Any of The Choices From The Following :\n"
          "1 : Stone\n"
          "2 : Paper\n"
          "3 : Scissor\n")
    name = input("Please Enter Player Name :")
    rounds = int(input("Enter The Amount of Rounds You want to Play : "))
    rounds2 = 1
    comp1 = 0
    play1 = 0
    chance = 1
    print(f"\n Alright {name} , So Let's Start The Game!\n ")
    while(rounds2<=rounds):
        rand = random.choice(CompOptions)
        print(f"Round : {chance} \n")
        n1 = input("Enter Your Choice :")
        if rand == "Stone" and any(item in n1 for item in OptionsStone):
            print("\nIt's a Draw !\n")
            rounds2 = rounds2 + 1
            chance = chance + 1
        elif rand=="Stone" and any(item in n1 for item in OptionsPaper):
            print(f"{name} Won!\n")
            rounds2 = rounds2 + 1
            play1 = play1 +1
            chance = chance + 1
        elif rand == "Stone" and any(item in n1 for item in OptionsScissor):
            print("The Computer Won!\n")
            rounds2 = rounds2 + 1
            comp1 = comp1 +1
            chance = chance +1
        elif rand == "Paper" and any(item in n1 for item in OptionsStone):
            print("The Computer Won!\n")
            rounds2 = rounds2 + 1
            comp1 = comp1 +1
            chance = chance + 1
        elif rand == "Paper" and any(item in n1 for item in OptionsPaper):
            print("It's a Draw!\n")
            rounds2 = rounds2 + 1
            chance = chance + 1
        elif rand == "Paper" and any(item in n1 for item in OptionsScissor):
            print(f"{name} Won!\n")
            rounds2 = rounds2 + 1
            play1 = play1 + 1
            chance = chance + 1
        elif rand == "Scissor" and any(item in n1 for item in OptionsStone):
            print(f"{name} Won!\n")
            rounds2 = rounds2 + 1
            play1 = play1 + 1
            chance = chance + 1
        elif rand == "Scissor" and any(item in n1 for item in OptionsPaper):
            print(f"Computer Won!\n")
            rounds2 = rounds2 + 1
            comp1 = comp1 + 1
            chance = chance + 1
        elif rand == "Scissor" and any(item in n1 for item in OptionsScissor):
            print(f"It's a Draw! \n")
            rounds2 = rounds2 + 1
            chance = chance + 1
        else:
            print("Wrong Input , Try Again !")
    if comp1 > play1:
        print("The Computer Won all the Rounds ,\n"
              "Hence The Computer Won The Game")
    if comp1 < play1:
        print(f" {name} Won all the Rounds ,\n"
              f"Hence {name} Won The Game")
    if comp1 == play1:
        print(f"Since the amount of rounds was an even number,\n"
              f"The Game is a draw")

print("Welcome To Random Games , We Have Two Games Currently :\n"
      "1 : Stone-Paper-Scissor \n"
      "2 : Guess The Number \n")
lisstone = ["Stone","stone",'Paper',"paper","Scissor","scissor","1"]
lisguess= ["Guess","guess","Guess the number ","number","guess number","2"]

n1 = input("Enter Your Choice : \n")

if any(item in n1 for item in lisstone):
    stone()
if any(item in n1 for item in lisguess):
    guess_num()