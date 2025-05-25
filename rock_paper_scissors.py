import random


choices= ('r','p','s')
choices_dict ={'r':'🪨','p':'📃','s':'✂️'}

while True:

    user_choice = input("Rock paper or scissors r/p/s: ").lower()
    

    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice=random.choice(choices)

    print(f"You chose {choices_dict[user_choice]}")
    print(f"The computer chose {choices_dict[computer_choice]}")

    if user_choice==computer_choice:
        print("Tie!!!")

    elif ((user_choice=='r'and computer_choice=='s') or
        (user_choice=='p'and computer_choice=='r') or
        (user_choice=='s'and computer_choice=='p')
        ):
        print("You win !!!")
    else:
        print("You lost")

    To_continue = input("Do you wanna continue playing y/n : ").lower()
    if To_continue =='n':
        print("The end of the game !! : ")
        break
