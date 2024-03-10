import random 

deck = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def play():
    steve_choice = random.choice(deck)
    josh_choice = random.choice(deck)
    return steve_choice, josh_choice


def winner(deck_steve, deck_josh):
    final_steve = 0
    final_josh = 0

    for i in range(len(deck_steve)):
        steve_index = deck.index(deck_steve[i])
        josh_index = deck.index(deck_josh[i])

        if steve_index > josh_index:
            final_steve += 1
        elif josh_index > steve_index:
            final_josh += 1

    if final_steve > final_josh:
        return f"Steve wins {final_steve} to {final_josh}"
    elif final_josh > final_steve:
        return f"Josh wins {final_josh} to {final_steve}"
    else:
        return f"Tie"


def main():
    deck_steve = [] 
    deck_josh = []

    for i in range(3): 
        steve, josh = play()
        deck_steve.append(steve)
        deck_josh.append(josh)
    
    print("Steve's Deck", deck_steve, "Josh's Deck", deck_josh)
    print(winner(deck_steve, deck_josh))
    



if __name__ == "__main__":
    main()