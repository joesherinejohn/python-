# from art_project11 import logo  
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""







import random
def play_game():
    cont_BJ = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\' : ")

    if cont_BJ == 'y':
        # count = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        print(logo)
        your_card = [ random.randint(2, 11), random.randint(2, 11)]
        current_score = sum(your_card)
        computer_first_card = [random.randint(2, 11), random.randint(2, 11)]
        computer_score = sum(computer_first_card)

        print(f"Your Cards: {your_card} , Current Score: {current_score}")
        print(f"Computer's first card: {computer_first_card[0]}")
        if current_score == 21:
            print(f"Your final Cards: {your_card} , final Score: {current_score}")
            print(f"Computer's  final hand: {computer_first_card} , final score : {computer_score}")
            print("You win Blackjack....Hooray...")
            play_game()
        cont_1 = input("Type \'y\' to get another card, type \'n\' to pass: ")
        cont(cont_1, your_card, current_score, computer_first_card, computer_score)
    elif cont_BJ == 'n':
        print("Thank you for your interset in visiting our Blackjack game")
    else:
        print("Please enter either \'y\' or \'n\'.Thank you.")
        play_game()

def cont(cont_1, your_card, current_score, computer_first_card, computer_score):

        if cont_1 == 'y':
            your_card.append(random.randint(2,11))
            num = len(your_card)
            current_score = sum(your_card)
            if your_card[num -1] == 11 and (current_score > 21):
                your_card[num -1] = 1
                current_score = sum(your_card)
            if current_score > 21:
                if 11 in your_card:
                  your_card[your_card.index(11)] = 1
                else:
                    # computer_first_card.append(random.randint(2, 11))
                    # computer_score = sum(computer_first_card)
                    # # num1 = len(computer_first_card)
                    # if 11 in computer_first_card and (computer_score > 21):
                    #     computer_first_card[computer_first_card.index(11)] = 1
                    #     computer_score = sum(computer_first_card)
                    print(f"Your final Cards: {your_card} , final Score: {current_score}")
                    print(f"Computer's  final hand: {computer_first_card} , final score : {computer_score}")
                    print("Your score is more than \'21\'. You Lose.")
                    play_game()
            else:
                print(f"Your Cards: {your_card} , Current Score: {current_score}")
                print(f"Computer's first card: {computer_first_card[0]}")
                cont_1 = input("Type \'y\' to get another card, type \'n\' to pass: ")
                # computer_first_card.append(random.randint(2, 11))
                # computer_score = sum(computer_first_card)
                # # num1 = len(computer_first_card)
                # if 11 in computer_first_card and (computer_score > 21):
                #     computer_first_card[computer_first_card.index(11)] = 1
                #     computer_score = sum(computer_first_card)
                cont(cont_1, your_card, current_score, computer_first_card, computer_score)
        else:
            if computer_score == 21 and current_score == 21:
                print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                print("It\'s a Draw")
                play_game()
            elif computer_score == 21:
                print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                print("Computer wins with BlackJack.....Oops")
                play_game()
            else:
                print("All The Best:)")

            while computer_score < 17:
                computer_first_card.append(random.randint(2, 11))
                computer_score = sum(computer_first_card)
                if 11 in computer_first_card and (computer_score > 21):
                    computer_first_card[computer_first_card.index(11)] = 1
                    computer_score = sum(computer_first_card)
            if current_score == 21 or current_score < 21:
                if current_score == computer_score:
                    print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                    print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                    print("It\'s a Draw")
                    play_game()
                elif computer_score > current_score:
                    if computer_score > 21:
                        # num1 = len(computer_first_card)
                        if 11 in computer_first_card and (computer_score > 21):
                            computer_first_card[computer_first_card.index(11)] = 1
                            computer_score = sum(computer_first_card)
                        if computer_score > 21:
                            print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                            print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                            print("Opponent goes over \'21\'. You Win")
                            play_game()

                        else:
                            print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                            print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                            print("Ooops .You Lose")
                            play_game()

                    else:
                        print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                        print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                        print("Opponent is within \'21\'. You Lose")
                        play_game()
                else:
                    print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                    print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                    print("You Win")
                    play_game()
            else:
                print(f"Your final Cards: {your_card} , Final Score: {current_score}")
                print(f"Computer's final card: {computer_first_card},Final Score: {computer_score} ")
                print("You are more than\'21\'.Sorry.You Lose")
                play_game()


play_game()


