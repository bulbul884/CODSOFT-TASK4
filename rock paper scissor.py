import random
while True:
    user_choice=input("enter your choice(rock,paper,scissor):")
    choices=("rock","paper","scissor")
    computer_choice =('computer will choose randomly not conditionally')
    print("/nYou choose {user_choice}and computer choose{computer_choice}./n")
    if user_choice==computer_choice:
        print("both player selected{user_choice}.It's a tie")
    elif user_choice=="rock":
        if computer_choice=="paper":
            print("paper covers rock!!,you loose")
        else:
            print("rock smashes scissor.you won")
    elif user_choice=="paper":
        if computer_choice=="rock":
            print("paper covers rock. you won")
        else:
            print("scissor cuts paper,you loose")
    elif user_choice=="scissor":
        if computer_choice=="rock":
            print("rock smashes scissor, you loose")
        else:
            print("scissor cuts paper,you won")
    play_again=input("you wanna play again??(yes/no):")
    if play_again=="no":
        break
    
          



