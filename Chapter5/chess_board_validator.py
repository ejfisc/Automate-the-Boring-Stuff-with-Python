# checks to see if a dictionary that represents a chessboard is a valid chessboard or not

# dictionary with 3 keys, white pieces whose value is a tuple of each white piece,
# black pieces whose value is a tuple of each black piece, and the empty space
chessPieces = {'white pieces': ('wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking'), 
               'black pieces': ('bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking'),
               'empty space':  ' '}

# tuple of chess positions, each pos represents a space on the chess board
chessPositions = ('1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a',
                  '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b',
                  '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c',
                  '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d',
                  '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e',
                  '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f',
                  '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g',
                  '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h')

# dictionary data structure represents chess board, each key is a position and each key has a piece value
chessBoard = {'1a': 'wking', '2a': ' ', '3a': ' ', '4a': ' ', '5a': ' ', '6a': ' ', '7a': ' ', '8a': ' ',
              '1b': ' ', '2b': ' ', '3b': ' ', '4b': ' ', '5b': ' ', '6b': ' ', '7b': ' ', '8b': ' ',
              '1c': ' ', '2c': ' ', '3c': ' ', '4c': ' ', '5c': ' ', '6c': ' ', '7c': ' ', '8c': ' ',
              '1d': ' ', '2d': ' ', '3x': ' ', '4d': ' ', '5d': ' ', '6d': ' ', '7d': ' ', '8d': ' ',
              '1e': ' ', '2e': ' ', '3e': ' ', '4e': ' ', '5e': ' ', '6e': ' ', '7e': ' ', '8e': ' ',
              '1f': ' ', '2f': ' ', '3f': ' ', '4f': ' ', '5f': ' ', '6f': ' ', '7f': ' ', '8f': ' ',
              '1g': ' ', '2g': ' ', '3g': ' ', '4g': ' ', '5g': ' ', '6g': ' ', '7g': ' ', '8g': ' ',
              '1h': ' ', '2h': ' ', '3h': ' ', '4h': ' ', '5h': ' ', '6h': ' ', '7h': 'bking', '8h': ' '}

# function to check if board is a valid chess board
# a chess board is a valid chess board if:
# there are no unkown pieces or positions,
# There is only one black king and one white king,
# each player can have at most 16 pieces and at most 8 pawns
def isValidBoard(board):

    pieceCount = {}
    numberOfWhite = 0
    numberOfBlack = 0

    for k,v in board.items():
        # check if position is valid
        if k not in chessPositions:
            return False
        # check if piece is valid
        if v not in chessPieces['black pieces'] and \
           v not in chessPieces['white pieces'] and \
           v not in chessPieces['empty space']: 
            return False

        # count pieces
        pieceCount.setdefault(v, 0)
        pieceCount[v] += 1
        if v in chessPieces['black pieces']:
            numberOfBlack += 1
        elif v in chessPieces['white pieces']:
            numberOfWhite += 1

    if pieceCount.get('wking') != 1 or pieceCount.get('bking') != 1:
        return False
    # pass get() a 0 in the second parameter if there are no pawns on the board to avoid error 
    if pieceCount.get('wpawn', 0) > 8 or pieceCount.get('bpawn', 0) > 8:
        return False
    if numberOfWhite > 16 or numberOfBlack > 16:
        return False

    # if the function hasn't already returned false, this is a valid chess board, return true
    return True

if isValidBoard(chessBoard):
    print('valid board')
else:
    print('invalid board')



