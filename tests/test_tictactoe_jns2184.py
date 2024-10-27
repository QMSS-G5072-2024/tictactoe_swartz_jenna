import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tictactoe_jns2184.tictactoe_jns2184 import initialize_board, make_move

def test_initialize_board():
    actual_board = initialize_board()

    # Define the expected empty 3x3 board
    expected_board = [[' ' for _ in range(3)] for _ in range(3)]
    
    assert actual_board == expected_board, "The board is not initialized correctly"

#running the test, no output is good b/c test passed
test_initialize_board()

def test_make_move_valid():
    # Starting with an empty board
    board = initialize_board()
    
    # Making a move for player 'X' at position (1, 1)
    assert make_move(board, 1, 1, 'X') == True, "Since the space is available, should return True"
    assert board[1][1] == 'X', "Board should have 'X' at position (1, 1)"
    
    # Making a move for player 'O' at position (0, 2)
    assert make_move(board, 0, 2, 'O') == True, "Since the space is available, should return True"
    assert board[0][2] == 'O', "Board should have 'O' at position (0, 2)"

# Running the test, no output is good b/c test passed
test_make_move_valid()