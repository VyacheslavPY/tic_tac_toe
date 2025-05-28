from gameparts import Board
# from gameparts.exceptions import CellOccupiedError, FieldIndexError
import pygame

pygame.init()

# Здесь определены разные константы, например 
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики.
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
# Задать размер графического окна для игрового поля.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установить заголовок окна.
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом.
screen.fill(BG_COLOR)


# Функция, которая отвечает за отрисовку горизонтальных и вертикальных линий.
def draw_lines():
    # Горизонтальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # Вертикальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


# Функция, которая отвечает за отрисовку фигур 
# (крестиков и ноликов) на доске. 
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def save_result(add_results):
    # file_results = open('results.txt', 'a', encoding='utf-8')
    # file_results.write(add_results + '\n')
    # file_results.close()
    with open('results.txt', 'a') as file_results:
        file_results.write(add_results + '\n')


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    #game.display()
    draw_lines()

    # Тут запускается основной цикл игры.
    while running:
        # print(f'Ход делают {current_player}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)

                    if game.check_win(current_player):
                        # print(f'Победили {current_player}')
                        add_results = f'Победили {current_player}.'
                        print(add_results)
                        save_result(add_results)
                        running = False
                    elif game.is_board_full():
                        add_results = 'Ничья!'
                        save_result(add_results)
                        running = False
                        # Тернарный оператор, через который реализована смена игроков.
                        # Если current_player равен X, то новым значением будет O,
                        # иначе - новым значением будет X.
                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_figures(game.board)
        pygame.display.update()


pygame.quit

if __name__ == '__main__':
    main()

        # Запускается бесконечный цикл.
        # while True:
            # этом блоке содержатся операции, которые могут вызвать исключение.
            # try:
            #     # Пользователь вводит значение номера строки.
            #     row = int(input('Введите номер строки: '))
            #     # Если введённое число меньше 0 или больше
            #     # или равно game.field_size...
            #     if row < 0 or row >= game.field_size:
            #         # ...выбрасывается собственное исключение FieldIndexError
            #         raise FieldIndexError
            #     column = int(input('Введите номер столбца:'))
            #     # Если введённое число меньше 0 или больше
            #     # или равно game.field_size...
            #     if column < 0 or column >= game.field_size:
            #         # ...выбрасывается собственное исключение FieldIndexError
            #         raise FieldIndexError
            #     if game.board[row][column] != ' ':
            #         raise CellOccupiedError
            # # Если возникает исключение FieldIndexError...
            # except FieldIndexError:
            #     # ...выводятся сообщения...
            #     print(
            #         'Значение должно быть неотрицательным и меньше'
            #         f' {game.field_size}.'
            #     )
            #     print('Пожалуйста, введите значения для строки и столбца заново.')
            #     # ...и цикл начинает свою работу сначала,
            #     # предоставляя пользователю еще одну попытку ввести данные.
            #     continue
            # # Если возникает исключение
            # except ValueError:
            #     # ...выводятся сообщения...
            #     print('Буквы вводить нельзя. Только числа.')
            #     print('Пожалуйста, введите значения для строки и столбца заново.')
            #     # ...и цикл начинает свою работу сначала,
            #     # предоставляя пользователю еще одну попытку ввести данные.
            #     continue
            # except Exception as e:
            #     print(f'Возникла ошибка: {e}')
            # # Если в блоке try исключения не возникло...
            # else:
            #     # ...значит, введенные значения прошли все проверки
            #     # и могут быть использованы в дадльнейшем.
            #     # Цикл прерывается.
            #     break
        # Теперь для установки значения на поле само значение берётся
        # из переменной current_player
     #   game.make_move(row, column, current_player)
     #   game.display()
        # print('Ход сделан!')
        # После каждого хода надо делать проверку на победу и на ничью.
        