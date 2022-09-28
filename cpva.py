from contextlib import contextmanager

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


@contextmanager
def with_clean_castling_rights(board):
    """
    Ensures that the board has clean castling rights.
    """
    castling_rights = board.castling_rights
    board.castling_rights = board.clean_castling_rights()
    yield
    board.castling_rights = castling_rights


@contextmanager
def without_piece_at(board, square):
    """
    Remove the piece at the square on the board, and yield the piece.
    Afterwards, put the piece back. Also fixes castling rights when
    removing a rook.
    """
    piece = board.remove_piece_at(square)
    with with_clean_castling_rights(board):
        yield piece
    board.set_piece_at(square, piece)


def analyze_piece_values(board):
    """
    Return a dictionary mapping square to the piece value. The value
    is calculated by evaluating the board with the piece and subtracting
    the evaluation of the board without the piece.
    """
    piece_values = {}
    
    board_value = evaluate_board(board)
    for square, piece in board.piece_map().items():
        with without_piece_at(board, square):
            piece_values[square] = board_value - evaluate_board(board) if board.is_valid() else None
    
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
