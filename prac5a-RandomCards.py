import itertools , random
card = ['Spade','Heart','Diamond','Club']
deck = list(itertools.product(range(1,14),card))
random.shuffle(deck)
No_of_Card = int(input("How many cards do you want to Display : "))
print("You got",No_of_Card,"Random cards")
if No_of_Card > 52:
    print("A deck of cards has only 52 Unique cards so try below 52 !")
else:
    for i in range(No_of_Card):
        print(deck[i][0],"of",deck[i][1])
