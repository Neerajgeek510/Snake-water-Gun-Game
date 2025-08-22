import random

def game():
    print("😊 Snake, Water, Gun Game 🎮")
    print("🤔 Choose one: Snake (s), Water (w), Gun (g)")

    user_choice = input("Your choice🤞: ").lower()
    choices = ['s', 'w', 'g']
    computer_choice = random.choice(choices)
    if user_choice not in choices:
        print("please chose valid input[s,w,g]😒")
        return
    print(f"Computer chose: {computer_choice}")
   

    if user_choice == computer_choice:
        print("It's a Draw! 😐")
    elif (user_choice == 's' and computer_choice == 'w') or \
         (user_choice == 'w' and computer_choice == 'g') or \
         (user_choice == 'g' and computer_choice == 's'):
        print("🎉 You Win!")
    else:
        print("💻 Computer Wins!")


game()