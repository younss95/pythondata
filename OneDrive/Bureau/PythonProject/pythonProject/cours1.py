"""
def locate_card(carte, requete):
    position = 0

    print('cards: ', carte)
    print('requete: ', requete)

    while True:
        print('position: ', position)
        if carte[position]==requete:
            return position

        position += 1

        if position == len(carte):
            return -1


cartes = [4,5,8,9,11,2,4,3,7,6,5]
requetes = 6
result = 9

print(locate_card(cartes, requetes))
"""


########################################################################333


def locate_card(cards, query):
    lo, hi = 0, len(cards)-1

    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]

        print("lo: ", lo, "hi: ", hi, "mid: ", mid, "mid_number: ", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid -1

        elif mid_number > query:
            lo = mid +1
    return -1

cartes = [13,11,10,7,4,3,1,0]
query = 1

print(locate_card(cartes, query))

