import random
choices = ["stone", "paper", "scissors"]

while True:
    user_choice = input("Виберіть будь-ласка 'stone', 'paper', 'scissors'")
    if user_choice not in choices:
        print("Неправильний вибір! Спробуйте ще раз")
        continue

    bot_choice = random.choice(choices)
    print(f"Bot choose: {bot_choice}")

    if user_choice == bot_choice:
        print("Draw!")
    elif (
        (user_choice == "stone" and bot_choice == "scissors") or
        (user_choice == "scissors" and bot_choice == "paper") or
        (user_choice == "paper" and bot_choice == "stone")
    ):
        print("Ви перемогли!")
    else: 
        print("Бот переміг!")
