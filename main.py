import sys
import random
import pygame



def cut_image():
    """New feature to appear in the next version."""
    pass



def random_board_generator(n=3):
    """
    get a random board n*n.
    """
    board_vec = [i for i in range(n * n)]
    random.shuffle(board_vec)

    reverse_pair_num = 0
    for i in range(len(board_vec)):
        for j in range(i+1, len(board_vec)):
            if board_vec[i]>board_vec[j]:
                reverse_pair_num += 1
    
    if (reverse_pair_num + board_vec.index(0) + n) % 2 == 0:
        if board_vec.index(0)>=2:
            board_vec[0], board_vec[1] = board_vec[1], board_vec[0]
        else:
            board_vec[-2], board_vec[-1] = board_vec[-1], board_vec[-2]
    return [list(x) for x in zip(*[iter(board_vec)]*n)]


def is_win(board, n=3):
    """ruturn win flag."""
    return board == [list(x) for x in zip(*[iter([(i + 1) % (n * n) for i in range(n * n)])]*n)]




def move(direction,board_list, n=3):
    """"""
    i0, j0 = 0, 0
    for i in range(n):
        for j in range(n):
            if board_list[i][j] == 0:
                i0, j0 = i, j
    if 0 <= i0+direction[0] <= n-1 and 0 <= j0+direction[1] <= n-1:
        i1, j1 = i0+direction[0], j0+direction[1]
        board_list[i0][j0], board_list[i1][j1] = board_list[i1][j1], board_list[i0][j0]
        return






def main():
    """"""


    N = 3
    WIDTH = 864
    HEIGHT = 864
    FPS = 10
    GAME_CAPTION = 'Catch Stupid Dog'
    FULL_IMAGE_PATH = "./img/裁剪.png"
    WINNING_TEXT = 'Congratulations'

    direction_dict = {pygame.K_UP: (1,0), pygame.K_DOWN: (-1,0),pygame.K_LEFT: (0,1), pygame.K_RIGHT: (0,-1)}

    pygame.init()
    pygame.display.set_caption(GAME_CAPTION)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    win_img = pygame.image.load(FULL_IMAGE_PATH)
    num_img_dict = {}
    for i in range(9):
        num_img_dict[i] = pygame.image.load(f'./img/1{i}.png')##########
    
    board = random_board_generator()
    win_flag = False


    clock = pygame.time.Clock()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and (not win_flag):
                if event.key in direction_dict.keys():
                    direction = direction_dict[event.key]
                    move(direction, board)
                    if is_win(board):
                        win_flag = True
            elif win_flag and event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                win_flag = False
                board = random_board_generator()

        screen.fill(pygame.Color('#000000'))

        #screen.blit(board_img, (0,0))

        for row,line in enumerate(board):
            for col, num in enumerate(line):
                screen.blit(num_img_dict[num], (288*col, 288*row))

        if win_flag:
            screen.blit(win_img, (0,0))
            my_font = pygame.font.SysFont("Verdana", 50)
            subtitle = my_font.render(WINNING_TEXT, True, (0, 120, 0))
            screen.blit(subtitle, (250,250))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
