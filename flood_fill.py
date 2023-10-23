board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: list[str], old: str, new: str, x: int, y: int) -> list[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    # Implement your code here.
    
    # Add new change
    if invalid_length(input_board):
        raise ValueError("input boards length invalid")
    if out_of_index(input_board, x, y):
        return input_board
    if input_board[x][y] != old:
        return input_board
        
    input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
    input_board = flood_fill(input_board, old, new, x + 1, y)
    input_board = flood_fill(input_board, old, new, x - 1, y)
    input_board = flood_fill(input_board, old, new, x, y + 1)
    input_board = flood_fill(input_board, old, new, x, y - 1)
    return input_board

    # Add new change
def invalid_length(input_board: list[str]) -> bool:
    for s in input_board:
        if len(s) != len(input_board[0]):
            return True
    return False

def out_of_index(input_board: list[str], x: int, y: int) -> bool:
    if x < 0 or x > len(input_board) - 1:
        return True
    if y < 0 or y > len(input_board[x]) - 1:
        return True
    return False


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
