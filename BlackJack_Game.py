import random 
print(str.center("BlackJack Game", 50, "*"))
K = 10
J = Q = K 
A = {"A1": 1, "A2": 11}
card_deck=[2,3,4,5,6,7,8,9,10,J,Q,K,A] * 4
random.shuffle(card_deck)
counter_player = 0
counter_computer = 0
def your_game():
    while True:
        take_card = input("Would you take a card? Y or N?\n")
        if take_card == "Y" or take_card == "y":
            global counter_player  
            card = card_deck.pop()
            if card == A:
                if counter_player<11:
                    card = A["A2"]
                else:
                    card = A["A1"]
            print("You took the card %d" %card)
            counter_player +=card
            print("Your score is: %d" %counter_player)
            if counter_player < 21:
                continue
            elif counter_player == 21:
                break
            else:
                break  
        elif take_card == "N" or take_card == "n":
            break

def comp_game():
    while True:
        global counter_computer
        card2 = card_deck.pop()
        if card2 == A:
            if counter_computer < 11:
                card2 = A["A2"]
            else:
                card2 = A["A1"]
        counter_computer += card2
        if counter_computer < 18:
            continue
        else:
            break

while True:
    start = input("Start new game? Y or N? \n")
    counter_player = 0
    counter_computer = 0
    if start == "Y" or start == "y":
        your_game()
        comp_game()
        if (counter_player <= 21 and counter_player > counter_computer) or (counter_player<=21 and counter_computer>21):
            print("Player score is: " + str(counter_player))
            print("Computer score is: " + str(counter_computer))
            print("You win!")
        elif counter_player <= 21 and counter_player == counter_computer:
            print("Player score is: " + str(counter_player))
            print("Computer score is: " + str(counter_computer))
            print("Dead heat!")
        else:
            print("Player score is: " + str(counter_player))
            print("Computer score is: " + str(counter_computer))
            print("You lose!")
    elif start == "N" or start == "n":
        exit()
    else:
        start = input("Start new game? Y or N?\n")