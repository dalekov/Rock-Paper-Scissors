from ascii import rock, paper, scissors, logo, player_message_lose, player_message_win
import random
import time
import os


def game():
    print(logo)
    print("!!! WELCOME TO THE ROCK, PAPER, SCISSORS SIMULATOR !!!")
    choices_list = [rock, paper, scissors]

    cpu_lives = 5
    player_lives = 5
    should_continue = True

    while should_continue:
        user_choice = None
        while user_choice is None:
            try:
                user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
            except ValueError:
                print("Invalid input! Please try again...")
                user_choice = None
                time.sleep(2)
            else:
                if user_choice < 0 or user_choice >= 3:
                    print("Invalid input! Please try again...")
                    time.sleep(2)
                    user_choice = None
                else:
                    print("You play:")
                    print(choices_list[user_choice])

                    cpu_choice = random.randint(0, 2)
                    print("The CPU plays:")
                    print(choices_list[cpu_choice])

                # Handling game logic.
                if user_choice == cpu_choice:
                    print("Draw. Nothing happens! So boring...")
                elif (user_choice == 1 and cpu_choice == 2) or (user_choice == 0 and cpu_choice == 1) or (user_choice == 2 and cpu_choice == 0):
                    player_lives -= 1

                    if player_lives == 0:
                        should_continue = False
                        print(player_message_lose)
                    else:
                        print("You lose! You lose a life.")
                else:
                    cpu_lives -= 1
                    if cpu_lives == 0:
                        should_continue = False
                        print(player_message_win)
                    else:
                        print("!!! YOU WIN !!! The CPU loses one life. ")

                print("-------LIVES REMAINING-------")
                print(f"Player: {player_lives}")
                print(f"CPU: {cpu_lives}")
                print("-----------------------------")

    restart = input("Would you like to play another game? (Y/n): ").lower()
    if restart == "y":
        print("\n" * 100)
        game()
    else:
        print("Thank you for playing. Goodbye!")
game()
