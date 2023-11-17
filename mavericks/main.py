import random

INPUTS = ["rock", "paper", "scissors"]


def handle_player_input() -> int:
    while True:
        choice = input("please enter 0-2 ([0]rock, [1]paper, [2]scissors): ")
        if choice.isnumeric():
            res = int(choice)
            if res in (range(len(INPUTS))):
                return res
        else:
            print("please enter 0-2 only")


def handle_computer_input():
    res = random.randint(0, len(INPUTS) - 1)
    return res

def determine_winner(p1:int, p2:int)->str:
    if p1== 0

class Option:
    def __init__(self, name,winners, losers) -> None:
        self.name=name
        self.winners= winners
        self.losers= losers

    def get_result(self, target):
        if target in self.winners:
            return "win"
        if target in self.losers:
            return "lose"
        return "draw"
    def update_winner(self,add:list[str], remove:list[str]):
        for item in add:
            if item not in self.winners:
                self.winners.append(item)
        for item in remove:
            if item in self.winners:
                self.winners.remove(item)
                
class Choice(enu)
def main():
    while True:
        print("please select game mode 1. pvp 2.pvpc 3.quit:")
        # ask how many object, 
        choice= int(input())
        if choice ==3:
            break
        elif choice==1:
            rock= Option(INPUTS[0],[INPUTS[2]], INPUTS[1])
            p1: Option= handle_player_input()
            p2: Option= handle_player_input()
            result= p1.get_result(p2.name)
            if result == "win":
                print("p1 win")
            elif result == "lose":
                print("p2 win")
            else:
                print("draw")
        elif choice==2:
            p1: Option= handle_player_input()
            p2: Option= handle_computer_input()
            result= p1.get_result(p2.name)
            if result == "win":
                print("p1 win")
            elif result == "lose":
                print("p2 win")
            else:
                print("draw")

