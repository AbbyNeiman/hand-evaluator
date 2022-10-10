import random
import re
deck = [
  '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', '11h', '12h',
  '13h', '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', '11d',
  '12d', '13d', '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s',
  '11s', '12s', '13s', '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c',
  '10c', '11c', '12c', '13c'
]
all_hands = {}
num_players = input('Number of Players: ')
community = []
final_hands = {}
final_values = {}
final_suits = {}
# define hands
royal_flush = 1
straight_flush = 2
four_of_a_kind = 3
full_house = 4
flush = 5
straight = 6
three_of_a_kind = 7
two_pair = 8
pair = 9
high_card = 10



def hero():
  hc1 = 0
  hc2 = 0
  while hc1 == 0: 
    card1 = input('First Card: ')
    if card1 in deck:
      hc1 = card1
    else:
      print('try again: format 1-13, h,d,c, or s')
  while hc2 == 0:
    card2 = input('Second Card: ')
    if card2 in deck:
      hc2 = card2
    else:
      print('try again: format 1-13, h,d,c, or s')
  deck.remove(hc1)
  deck.remove(hc2)
  hero = [hc1, hc2]
  all_hands['hero'] = hc1, hc2


def deal():
  x = 1
  while x < int(num_players):
    x = x + 1
    player = ('player', x)
    hand1 = random.choice(deck)
    deck.remove(hand1)
    hand2 = random.choice(deck)
    deck.remove(hand2)
    all_hands[player] = [hand1, hand2]
  def flop():
    flop1 = random.choice(deck)
    deck.remove(flop1)
    community.append(flop1)
    flop2 = random.choice(deck)
    deck.remove(flop2)
    community.append(flop2)
    flop3 = random.choice(deck)
    deck.remove(flop3)
    community.append(flop3)
  def river():
    river = random.choice(deck)
    deck.remove(river)
    community.append(river)

  def turn():
    turn = random.choice(deck)
    deck.remove(turn)
    community.append(turn)
  flop()
  river()
  turn()
def final_cards():
  player = 0
  for item in all_hands.items():
    hand = list(item[1])+community
    final_hands[player]=hand
# def hands():
#   values = []
#   suits = []
#   player = 0
#   for item in all_hands.items():
#     player+=1
#     hand = list(item[1]) + community
#     values = []
#     suits = []
#     for i in hand: 
#       x=re.split('(\d+)',i)
#       n = int(x[1])
#       values.append(n)
#       suits.append(x[2])
#     values.sort()
#     suits.sort()
#     final_hands[player]=hand
#     final_values[player]=values
#     final_suits[player]=suits

class Player:
  def __init__(self,player,hand):
    self.player = player
    self.hand = hand
  def hands(self):
    values = []
    suits = []
    for i in self.hand:
      x = re.split('(\d+)',i)
      n = int(x[1])
      values.append(n)
      suits.append(x[2])
    values.sort()
    suits.sort()
    final_values[self.player] = values
    final_suits[self.player] = suits

  def eval(self):
    print('in eval: ',self.player,self.hand)
    # values = []
    # suits = []
    # for i in self.hand: 
    #   x=re.split('(\d+)',i)
    #   n = int(x[1])
    #   values.append(n)
    #   suits.append(x[2])
    # values.sort()
    # suits.sort()
  
  
    




    
  # def eval():
  #   def flush():
  #     suits = final_suits.items()
  #     for key,value in suits:
  #       suit = value[0]
  #       flush = True
  #       for i in value:
  #         if i == suit:
  #           flush = True
  #         else:
  #           flush = False
  #       return flush
  #   def straight():
  #     values = final_values.items()
  #     for key,value in values:
  #       print(value)
    
        
      
   
    
    
    
    
hero()
deal()
final_cards()
print(final_hands)
for key,value in final_hands.items():
  print(key,'-->',value)
  x=Player(key,value)
  x.hands()
  x.eval()

