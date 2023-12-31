from enum import IntEnum
import random

# https://realpython.com/python-rock-paper-scissors/


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Spock = 3
    Lizard = 4


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    user_input = input(f"Enter a choice ({choices_str}: ")
    selection = int(user_input)
    action = Action(selection)
    return action


def get_comp_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determine_winner(user: Action, comp: Action):
    print(f"user={user.name} comp={comp.name}")
    victories = {
        Action.Rock: [Action.Scissors, Action.Lizard],
        Action.Paper: [Action.Rock, Action.Spock],
        Action.Scissors: [Action.Paper, Action.Lizard],
        Action.Spock: [Action.Scissors, Action.Rock],
        Action.Lizard: [Action.Spock, Action.Paper],
    }
    defeats = victories[user]
    if user == comp:
        print("tie")
    elif comp in defeats:
        print("user win")
    else:
        print("user lose")


def main():
    while True:
        try:
            user = get_user_selection()
        except ValueError as _:
            range_str = f"[0, {len(Action)-1}]"
            print(f"choose only value in this range{range_str}")
            continue

        comp = get_comp_selection()
        determine_winner(user, comp)
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break


if __name__ == "__main__":
    main()
