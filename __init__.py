from ayo import AyoGame


def game_loop(choose_all_randomly):
    ayo = AyoGame()
    # ayo.display()
    while True:
        if choose_all_randomly:
            ayo.choose_random()
        else:
            if ayo.first_player:
                ayo.choose_best_pot()
            else:
                ayo.choose_random()

        if ayo.invalid:
            print("That is an invalid input.")
            print()
            continue
        if ayo.is_chosen_hole_empty():
            continue
        ayo.move()
        ayo.gain()
        # ayo.display()
        if ayo.goal_state():
            print("==============================================")
            print("Player 1 =", ayo.player1, " Player 2 =", ayo.player2)
            print("==============================================")
            print("Player ", ayo.goal_state(), " Wins")
            print()
            print()
            break

        ayo.next_player()


def main():
    #print("Start")
    # for i in range(1000):
    #     game_loop(False)
    game_loop(False)

if __name__ == '__main__':
    main()
