import questionary
import random
from yaspin import yaspin
import pyfiglet
import time


credits = 10

name = questionary.text("Enter your name").ask()

spinner = yaspin()
spinner.color = "green"


def coinflip(credits: int) -> int:
    winorlose = random.choice([True, False])
    amt = int(questionary.text(
        "Enter the amount of Credits to Gamble (Max 100 Credits)").ask())
    if amt > 100 or amt < 1:
        print("Amount of credits must be between 1-100 ")
    elif amt>credits:
        print("Amount must be lower than your actual credits")
    else:
        spinner.text = "Flipping the coin ..."
        spinner.start()
        time.sleep(1)
        spinner.stop()
        if winorlose == True:
            print(pyfiglet.figlet_format(f"Won {amt} credits"))
            credits += amt
        else:
            print(pyfiglet.figlet_format(f"Lost {amt} credits"))
            credits -= amt
    return credits

def create_lucky_ticket() -> str:
    e = ''
    for i in range(5):
        e = e + random.choice('123456789ABCD')
    return e

def luckydraw(credits: int) -> int:
    amt = int(questionary.text(
        "Enter the amount of Tickets (Max 100 tikets)(Cost of one is 10)").ask())
    if amt > 100 or amt < 1 :
        print("Amount of credits must be between 1-100 ")
    elif credits<amt*10:
        print(f"Not enough credits, have {credits} need {amt*10}")
    else:
        credits -= amt*10 
        tickets = []
        print('Tickets:')
        for i in range(amt):
            toappend = create_lucky_ticket()
            tickets.append(toappend)
            print(pyfiglet.figlet_format(toappend))
            
        winner = create_lucky_ticket()
        spinner.text = "Checking Winners"
        spinner.start()
        time.sleep(5)
        spinner.stop()
        print('Winner Ticket')
        if winner in tickets:
            print(pyfiglet.figlet_format(winner))
            print(pyfiglet.figlet_format('Won 10000 Credits'))
            credits+=10000
        else:
            print(pyfiglet.figlet_format(f'Lost {amt*10} Credits'))
            print(pyfiglet.figlet_format(winner))
            
        
rewards = [
    ("0",0.3),
    ("10", 0.20),  
    ("20", 0.20),  
    ("30", 0.15),  
    ("40", 0.09), 
    ("50", 0.09),
    ("100",0.01)  
]


def spin_the_wheel():
    rand_num = random.random() 

    
    cumulative_probability = 0
    for reward, probability in rewards:
        cumulative_probability += probability
        if rand_num <= cumulative_probability:
            return reward
            


def luckyspin(credits: int) -> int:
    amt = questionary.select(
        "Want to spin the luck wheel ",choices=['yes','no']).ask()
    if amt == 'no':
        pass
    else:
        if credits >= 10:
            print(credits)
            credits -=10
            spinner.text = "Spinning ..."
            spinner.start()
            time.sleep(2)
            spinner.stop()
            reward = spin_the_wheel()
            print(pyfiglet.figlet_format(f"Won {reward} credits"))
            reward=int(reward)
            print(type(reward))
            credits+=reward
            print(credits)
        elif credits<10:
            print("Not enough Credits, requires 10 to play")


def rps(credits: int) -> int:
    amt = int(questionary.text(
        "Enter the amount of Credits to Gamble (Max 100 Credits)").ask())
    if amt > 100 or amt < 1:
        print("Amount of credits must be between 1-100 ")
    elif amt>credits:
        print("Amount must be lower than your actual credits")
    else:
        possible_actions = ["rock", "paper", "scissors"]

        user_action = questionary.select(
            "Select One ", choices=possible_actions).ask()
        computer_action = random.choice(possible_actions)
        spinner.text = "Choosing ..."
        spinner.start()
        time.sleep(1)
        spinner.stop()
        
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print(pyfiglet.figlet_format(f"Won {amt} credits"))
                credits += amt
            else:
                print(pyfiglet.figlet_format(f"Lost {amt} credits"))
                credits -= amt
        elif user_action == "paper":
            if computer_action == "rock":
                print(pyfiglet.figlet_format(f"Won {amt} credits"))
                credits += amt
            else:
                print(pyfiglet.figlet_format(f"Lost {amt} credits"))
                credits -= amt
        elif user_action == "scissors":
            if computer_action == "paper":
                print(pyfiglet.figlet_format(f"Won {amt} credits"))
                credits += amt
            else:
                print(pyfiglet.figlet_format(f"Lost {amt} credits"))
                credits -= amt


run = True

while run:
    whattodo = questionary.select("How may I help you today?", choices=[
        'Gamble', 'Check Credits', 'exit']).ask()

    if whattodo == 'Gamble':
        print(f'Welcome {name}!')
        wheregamble = questionary.select("Where do you want to Gamble today?", choices=[
            'Lucky Spin', 'Coin Flip', 'Rock Paper Scissors', 'Lucky Draw']).ask()
        if wheregamble == 'Coin Flip':
            credits = coinflip(credits)
        elif wheregamble == 'Lucky Draw':
            credits=luckydraw(credits)
        elif wheregamble == 'Lucky Spin':
            credits=luckyspin(credits)
        elif wheregamble == 'Rock Paper Scissors':
            credits=rps(credits)

    elif whattodo == 'exit':
        print("Waiting For you to return, till then Have a good one!!")
        run = False
    elif whattodo == 'Check Credits':
        print(f"You currently have {credits} Credits ")
