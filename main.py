from random import choice
from resources import *  # logo, info, x_symbol, o_symbol, blank_space, space, line, menu
from datetime import datetime

running = True
players = ({'Player 1': [o_symbol, 1]}, {'Player 2': [x_symbol, -1]})
board_game = {
    'A': {'1': [], '2': [], '3': []},
    'B': {'1': [], '2': [], '3': []},
    'C': {'1': [], '2': [], '3': []}
}
slots_scores = [{'s1': '', 's2': ''}, {'s1': '', 's2': ''}]


def game(g_score):
    global board_game
    current_player = choice(players)
    matching = True
    while matching:
        no_winner = True
        winner = ""
        player_number = list(current_player.keys())[0]
        print("The first turn is for " + player_number)
        clean_board()
        show_board(board_game, g_score)
        while no_winner:
            place = input(player_number + ". Select the place where you want to put your mark: ")
            board_game[place[0]][int(place[1])] = current_player[player_number]
            if player_number == "Player 1":
                current_player = players[1]
            else:
                current_player = players[0]
            player_number = list(current_player.keys())[0]
            show_board(board_game, g_score)
            results = winner_check(board_game)
            no_winner = results[0]
            winner = results[1]
        print("The winner is " + winner + ".")
        if winner == "Player 1":
            g_score[0] += 1
            looser = players[1]
        else:
            g_score[1] += 1
            looser = players[0]
        no_choice = True
        while no_choice:
            select = input('Do you want to play again? (Y/N): ').upper()[0]
            if select == 'N':
                matching = False
                no_choice = False
            elif select == 'Y':
                current_player = looser
                no_choice = False
            else:
                print('Invalid option, please, select again.')
    today = str(datetime.now()).split(".")[0]
    record_scores(g_score, today)


def winner_check(board):
    result_h = 0
    result_v_1 = 0
    result_v_2 = 0
    result_v_3 = 0
    result_d_1 = 0
    result_d_2 = 0
    for column in board:
        result_h += (board[column][1][1] + board[column][2][1] + board[column][3][1])
        result_v_1 += board[column][1][1]
        result_v_2 += board[column][2][1]
        result_v_3 += board[column][3][1]
        if result_h == 3:
            #  print(column, result_h)
            return [False, "Player 1"]
        elif result_h == -3:
            # print(column, result_h)
            return [False, "Player 2"]
        result_h = 0
    result_d_1 += (board["A"][1][1] + board["B"][2][1] + board["C"][3][1])
    result_d_2 += (board["A"][3][1] + board["B"][2][1] + board["C"][1][1])
    if result_v_1 == 3 or result_v_2 == 3 or result_v_3 == 3 or result_d_1 == 3 or result_d_2 == 3:
        # print(result_v_1, result_v_2, result_v_3, result_d_1, result_d_2, board["A"][1][1])
        return [False, "Player 1"]
    elif result_v_1 == -3 or result_v_2 == -3 or result_v_3 == -3 or result_d_1 == -3 or result_d_2 == -3:
        # print(result_v_1, result_v_2, result_v_3, result_d_1, result_d_2, board["A"][1][1])
        return [False, "Player 1"]
    return [True, "No one"]


def clean_board():
    global board_game
    for column in board_game:
        for i in range(1, 4):
            board_game[column][i] = [blank_space, 0]


def show_board(board, pyrs_scores):
    for i in range(0, 2):
        if pyrs_scores[i] < 10:
            slots_scores[i]['s1'] = globals()['symbol_0']
            slots_scores[i]['s2'] = globals()['symbol_' + str(pyrs_scores[i])]
        else:
            slots_scores[i]['s1'] = globals()['symbol_' + str(pyrs_scores[i])[0]]
            slots_scores[i]['s2'] = globals()['symbol_' + str(pyrs_scores[i])[1]]
    for i in range(0, len(a_symbol)):
        print(
            slots_scores[0]['s1'][i],
            slots_scores[0]['s2'][i],
            no_space,
            space,
            no_space,
            slots_scores[1]['s1'][i],
            slots_scores[1]['s2'][i],
        )
    print("\n")
    for i in range(0, len(a_symbol)):
        print(
            blank_space[i],
            no_space,
            symbol_1[i],
            no_space,
            symbol_2[i],
            no_space,
            symbol_3[i]
        )
    print(no_line)
    for column in board:
        if column == 'A':
            current_row = a_symbol
        elif column == 'B':
            current_row = b_symbol
        else:
            current_row = c_symbol
        for i in range(0, 5):
            print(
                current_row[i],
                no_space,
                board[column][1][0][i],
                space,
                board[column][2][0][i],
                space,
                board[column][3][0][i]
            )
        if column != 'C':
            print(line)


def select_an_option(no_option):
    print(logo)
    while no_option:
        try:
            option = int(input(menu))
        except TypeError:
            print('Invalid answer, please try again.')
        else:
            if option < 1 or option > 4:
                print('Option number invalid. Please select an option between 1 and 4.')
            else:
                return option


def record_scores(score, match_date):
    with open('record.txt', "a") as file:
        file.write(str(score[0]) + " - " + str(score[1]) + " Date: " + match_date + "\n")


while running:
    selected_option = select_an_option(True)
    if selected_option == 1:
        score_1 = 0
        score_2 = 0
        scores = [score_1, score_2]
        game(scores)
    elif selected_option == 2:
        print(info)
        input("Press Enter to continue...")
    elif selected_option == 3:
        with open("record.txt") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        input("Press Enter to continue...")
    else:
        print("See you guys at the next time!")
        running = False
