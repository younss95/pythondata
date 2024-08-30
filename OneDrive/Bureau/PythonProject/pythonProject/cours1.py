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
