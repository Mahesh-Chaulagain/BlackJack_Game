import random

#Blackjack House Rule
#The deck is unlimited in size.
#There are no jockers.
#The Jack/Queen/King all count as 10
#The ace can be count as 11 or 1.
#The cards in the list have the equal probability of being drawn.
#Cards are not removed from the deck as they are drawn.
#Use the following list as the deck of cards:
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#function that uses the list of cards tp return a random card
def deal_card():
    """Returns a random card from a deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

#fucntion that takes a list of cards as input and returns the score
def calculate_score(cards):
    """takes a list of cards as input and returns the score"""
    #check for a blackjack and return 0 instead of actual score. 0 will represent blackjack in the game
    if sum(cards) ==21 and len(cards) == 2: 
        return 0
    #check for an 11 . if the score is already over 21, remove the 11 and replace it with a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lost,opponent has a blackjack"
    elif user_score == 0:
        return "You won with a blackjack"
    elif user_score > 21:
        return "you went over. you lose" 
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"

#Deal the user and computer 2 cards each
user_cards = []
computer_cards = []
is_game_over = False

for i in range(2):
    user_cards.append(deal_card()) #use append when you want to enter single item to the list
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards:{user_cards}, current score:{user_score}")
    print(f"computer's first card : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        #ask the user if they want to draw another card if the game has not ended.
        user_deal = input("type 'y' to get another card, type 'n' to pass:")
        if user_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

#The computer should keep drawing cards as long as it has a score less than 17
while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"your final hand:{user_cards},final score:{user_score}")
print(f"computer's final hand:{computer_cards},final score:{computer_score}")
print(compare(user_score,computer_score))
