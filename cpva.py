import chess
import chess.engine


engine = chess.engine.SimpleEngine.popen_uci(
    "stockfish_15_linux_x64_popcnt/stockfish_15_x64_popcnt"
)


def evaluate_board(board, depth=10):
    """
    Evaluate the board at the given depth. Returns the pawn score,
    with mate having a score of 100.
    """
    info = engine.analyse(board, chess.engine.Limit(depth=depth))
    score = info["score"].white()
    pawn_score = score.score(mate_score=10000) / 100.
    return pawn_score


def pawn_score_to_string(pawn_score):
    """
    Truncate the pawn score to two decimal points
    """
    return "{:.2f}".format(pawn_score)


def analyze_piece_values(board):
    """
    Return a dictionary mapping square to the piece value. The value
    is calculated by evaluating the board with the piece and subtracting
    the evaluation of the board without the piece.
    """
    piece_values = {}
    
    board_value = evaluate_board(board)
    for square, piece in board.piece_map().items():
        # print(f"Analyzing {piece.symbol()} at {chess.square_name(square)}")
        piece = board.remove_piece_at(square)
        if piece.piece_type == chess.ROOK:
            castling_rights = board.castling_rights
            board.castling_rights = board.clean_castling_rights()
        if board.is_valid():
            board_without_piece_value = evaluate_board(board)
            piece_values[square] = board_value - board_without_piece_value
        else:
            piece_values[square] = None
        if piece.piece_type == chess.ROOK:
            board.castling_rights = castling_rights
        board.set_piece_at(square, piece)

    return piece_values


def print_piece_values(board, piece_values):
    """
    Print piece value information
    """
    for square, piece_value in reversed(piece_values.items()):
        piece = board.piece_at(square)
        value_string = pawn_score_to_string(piece_value) if piece_value is not None else "N/A"
        print(f"{piece.symbol()}{chess.square_name(square)}: {value_string}")


# def print_piece_value_board(piece_values):
#     """
#     Print piece value in a board
#     """
#     pass


# fen = "r1bq1rk1/pp1pbpp1/2n4p/2pBp1N1/4P2P/3P4/PPP2PP1/R1BQK2R b KQ - 0 9"
# fen = "r1bqkbnr/pppp1ppp/2n5/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 3 3"
fen = "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4"

board = chess.Board(fen)
print(board)


piece_values = analyze_piece_values(board)
print_piece_values(board, piece_values)


engine.quit()
