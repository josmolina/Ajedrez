'''
Main driver file.
Handling user input.
Displaying current GameStatus object.
'''
import pygame as p
import Motor
import InteligenciaArtificial
import sys

BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSION = 8

SQUARE_SIZE = BOARD_HEIGHT // DIMENSION

MAX_FPS = 15

IMAGES = {}


def loadImages():
    '''
    Initialize a global directory of images.
    This will be called exactly once in the main.
    '''
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    '''
    The main driver for our code.
    This will handle user input and updating the graphics.
    '''
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = Motor.GameState()
    valid_moves = game_state.getValidMoves()
    move_made = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    loadImages()  # do this only once before while loop

    running = True
    square_selected = ()  # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
    player_clicks = []  # this will keep track of player clicks (two tuples)
    game_over = False

    white_did_check = ""
    black_did_check = ""
    last_move_printed = False
    moves_list = []
    move_log_font = p.font.SysFont("Arial", 14, False, False)

    turn = 1

    player_one = False  # if a human is playing white, then this will be True, else False
    player_two = False  # if a hyman is playing white, then thiss will be True, else False

    while running:
        human_turn = (game_state.white_to_move and player_one) or (not game_state.white_to_move and player_two)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                p.quit()
                sys.exit()
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if not game_over and human_turn:
                    location = p.mouse.get_pos()  # (x, y) location of the mouse
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE
                    if square_selected == (row, col) or col >= 8:  # user clicked the same square twice
                        square_selected = ()  # deselect
                        player_clicks = []  # clear clicks
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)  # append for both 1st and 2nd click
                    if len(player_clicks) == 2:  # after 2nd click
                        move = Motor.Move(player_clicks[0], player_clicks[1], game_state.board)
                        for i in range(len(valid_moves)):
                            if move == valid_moves[i]:
                                game_state.makeMove(valid_moves[i])
                                move_made = True
                                animate = True
                                square_selected = ()  # reset user clicks
                                player_clicks = []
                        if not move_made:
                            player_clicks = [square_selected]

            # key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo when 'z' is pressed
                    if game_state.white_to_move:
                        if turn > 1:
                            turn -= 1
                    game_state.undoMove()
                    move_made = True
                    animate = False
                    game_over = False
                    last_move_printed = False

                if e.key == p.K_r:  # reset the game when 'r' is pressed
                    game_state = Motor.GameState()
                    valid_moves = game_state.getValidMoves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    game_over = False
                    turn = 1
                    last_move_printed = False
                    moves_list = []

        # AI move finder
        if not game_over and not human_turn:
            AI_move = InteligenciaArtificial.findBestMoveNegaMaxAlphaBeta(game_state, valid_moves)
            if AI_move is None:
                AI_move = InteligenciaArtificial.findRandomMove(valid_moves)
            game_state.makeMove(AI_move, True)
            move_made = True
            animate = True

        if move_made:
            if game_state.checkForPinsAndChecks()[0]:
                if not game_state.white_to_move:
                    white_did_check = "+"
                else:
                    black_did_check = "+"
            if game_state.white_to_move:
                try:
                    moves_list.append(
                        f"\n{turn}. {game_state.move_log[-2].getChessNotation()}{white_did_check} {game_state.move_log[-1].getChessNotation()}{black_did_check}")
                    print(
                        f"\n{turn}. {game_state.move_log[-2].getChessNotation()}{white_did_check} {game_state.move_log[-1].getChessNotation()}{black_did_check}",
                        end="")
                    turn += 1
                    white_did_check = ""
                    black_did_check = ""
                except:
                    pass

            if animate:
                animateMove(game_state.move_log[-1], screen, game_state.board, clock)
            valid_moves = game_state.getValidMoves()
            move_made = False
            animate = False

        drawGameState(screen, game_state, valid_moves, square_selected, move_log_font)

        if not game_over:
            drawMoveLog(screen, game_state, move_log_font)

        if game_state.checkmate:
            game_over = True
            if game_state.white_to_move:
                drawEndGameText(screen, "Black wins by checkmate")
                if not last_move_printed:
                    moves_list[-1] += "+"
                    moves_list.append("result: 0-1")
                    print("+")
                    print("result: 0-1")
                    last_move_printed = True
                    saveGame(moves_list)

            else:
                drawEndGameText(screen, "White wins by checkmate")
                if not last_move_printed:
                    moves_list.append(f"\n{turn}. {game_state.move_log[-1].getChessNotation()}++")
                    moves_list.append("result: 1-0")
                    print(f"\n{turn}. {game_state.move_log[-1].getChessNotation()}++")
                    print("result: 1-0")
                    last_move_printed = True
                    saveGame(moves_list)

        elif game_state.stalemate:
            game_over = True
            drawEndGameText(screen, "Stalemate")
            if not last_move_printed:
                if not game_state.white_to_move:
                    moves_list.append(f"\n{turn}. {game_state.move_log[-1].getChessNotation()}")
                    moves_list.append("result: 1/2-1/2")
                    print(f"\n{turn}. {game_state.move_log[-1].getChessNotation()}")
                    print("result: 1/2-1/2")
                    last_move_printed = True
                    saveGame(moves_list)

        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, game_state, valid_moves, square_selected, move_log_font):
    '''
    Responsible for all the graphics within current game state.
    '''
    drawBoard(screen)  # draw squares on the board
    highlightSquares(screen, game_state, valid_moves, square_selected)
    drawPieces(screen, game_state.board)  # draw pieces on top of those squares
    # drawMoveLog(screen, game_state, move_log_font, moves_list)


def drawBoard(screen):
    '''
    Draw the squares on the board.
    The top left square is always light.
    '''
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def highlightSquares(screen, game_state, valid_moves, square_selected):
    '''
    Highlight square selected and moves for piece selected.
    '''
    if (len(game_state.move_log)) > 0:
        last_move = game_state.move_log[-1]
        s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('green'))
        screen.blit(s, (last_move.end_col * SQUARE_SIZE, last_move.end_row * SQUARE_SIZE))
    if square_selected != ():
        row, col = square_selected
        if game_state.board[row][col][0] == (
        'w' if game_state.white_to_move else 'b'):  # square_selected is a piece that can be moved
            # highlight selected square
            s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
            s.set_alpha(100)  # transparency value 0 -> transparent, 255 -> opaque
            s.fill(p.Color('blue'))
            screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            # highlight moves from that square
            s.fill(p.Color('yellow'))
            for move in valid_moves:
                if move.start_row == row and move.start_col == col:
                    screen.blit(s, (move.end_col * SQUARE_SIZE, move.end_row * SQUARE_SIZE))


def drawPieces(screen, board):
    '''
    Draw the pieces on the board using the current game_state.board
    '''
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawMoveLog(screen, game_state, font):
    '''
    Draws the move log.
    '''
    move_log_rect = p.Rect(BOARD_WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    p.draw.rect(screen, p.Color('black'), move_log_rect)
    move_log = game_state.move_log
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = str(i // 2 + 1) + '. ' + str(move_log[i]) + " "
        if i + 1 < len(move_log):
            move_string += str(move_log[i + 1]) + "  "
        move_texts.append(move_string)

    moves_per_row = 3
    padding = 5
    line_spacing = 2
    text_y = padding
    for i in range(0, len(move_texts), moves_per_row):
        text = ""
        for j in range(moves_per_row):
            if i + j < len(move_texts):
                text += move_texts[i + j]

        text_object = font.render(text, True, p.Color('white'))
        text_location = move_log_rect.move(padding, text_y)
        screen.blit(text_object, text_location)
        text_y += text_object.get_height() + line_spacing


def saveGame(moves_list):
    result = moves_list.pop()
    turns_dict = {}
    for i in range(len(moves_list) - 1, -1, -1):
        try:
            int(moves_list[i][1])
            if moves_list[i][1] not in turns_dict:
                turns_dict[moves_list[i][1]] = moves_list[i][1:] + "\n"
        except:
            pass
    file = open("last_game_logs.txt", "w")
    for turn in sorted(turns_dict.keys()):
        file.write(turns_dict[turn])
    file.write(result)
    file.close()


def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvitica", 32, True, False)
    text_object = font.render(text, 0, p.Color("gray"))
    text_location = p.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT).move(BOARD_WIDTH / 2 - text_object.get_width() / 2,
                                                                 BOARD_HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render(text, 0, p.Color('black'))
    screen.blit(text_object, text_location.move(2, 2))


def animateMove(move, screen, board, clock):
    '''
    Animating a move
    '''
    global colors
    d_row = move.end_row - move.start_row
    d_col = move.end_col - move.start_col
    frames_per_square = 10  # frames to move one square
    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square
    for frame in range(frame_count + 1):
        row, col = (move.start_row + d_row * frame / frame_count, move.start_col + d_col * frame / frame_count)
        drawBoard(screen)
        drawPieces(screen, board)
        # erease the piece moved from its ending square
        color = colors[(move.end_row + move.end_col) % 2]
        end_square = p.Rect(move.end_col * SQUARE_SIZE, move.end_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        p.draw.rect(screen, color, end_square)
        # draw captured piece onto rectangle
        if move.piece_captured != '--':
            if move.is_enpassant_move:
                enpassant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = p.Rect(move.end_col * SQUARE_SIZE, enpassant_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            screen.blit(IMAGES[move.piece_captured], end_square)
        # draw moving piece
        screen.blit(IMAGES[move.piece_moved], p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        p.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()