def safe_pawns(pawns):
    positions = []
    safe_pawns_number = 0
    for pawn in pawns:
        column = ord(pawn[0]) - 97
        row = int(pawn[1]) - 1
        positions.append((column, row))
    for pos in positions:
        if (pos[0] - 1, pos[1] - 1) in positions or (pos[0] + 1, pos[1] - 1) in positions:
            safe_pawns_number += 1
    return safe_pawns_number
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
