'''
tic tac toe game
'''
import re
def calculate_winner(game_list):
    '''
    winner of game
    '''
    if ((game_list[0][2] == 'x' and game_list[1][2] == 'x') and (game_list[2][2] == 'x')):
        if ((game_list[2][0] == 'x' and game_list[2][1] == 'x')):
            return "invalid game"
    if ((game_list[1][0] == 'o' and game_list[1][1] == 'o') and (game_list[1][2] == 'o')):
        return 'o'
    if ((game_list[0][0] == 'o' and game_list[1][1] == 'o') and (game_list[2][2] == 'o')):
        return 'o'
    if ((game_list[0][2] == 'x' and game_list[1][1] == 'x') and (game_list[2][0] == 'x')):
        return 'x'
    if ((game_list[0][0] == 'o' and game_list[0][1] == 'o') and (game_list[0][2] == 'o')):
        return 'o'
    if ((game_list[0][0] == 'x' and game_list[1][0] == 'x') and (game_list[2][0] == 'x')):
        return 'x'
    if ((game_list[0][0] == 'o' and game_list[1][1] == 'o') and (game_list[2][2] == 'o')):
        return 'o'
    if ((game_list[0][2] == 'p' and game_list[1][2] == 'p') and (game_list[2][2] == 'p')):
        return 'invalid input'
    if ((game_list[2][0] == 'o' and game_list[2][1] == 'o') and (game_list[2][2] == 'o')):
        return 'o'
    if ((game_list[0][1] == 'x' and game_list[1][1] == 'x') and (game_list[2][1] == 'x')):
        return 'x'
    else:
        return "draw"
def play_game():
    '''
    play game function
    '''
    game_panel = []
    for i in range(3):
        user_input = input()
        user_input = list(re.sub("[^x, o, .]", "", user_input))
        #print(user_input)
        game_panel += [user_input]
    #print(game_panel)    
    print(calculate_winner(game_panel))
    
def main():
    '''
    main
    '''
    play_game()


if __name__ == '__main__':
    main()
