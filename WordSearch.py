import random
import string


def create_grid(width, height):
    """Creates an empty grid filled with random letters."""
    grid = [[random.choice(string.ascii_uppercase) for _ in range(width)] for _ in range(height)]
    return grid


def place_word(word, grid):
    """Attempts to place a word in the grid randomly."""
    height = len(grid)
    width = len(grid[0])
    word_placed = False

    for _ in range(50):  # Try multiple times to place the word
        direction = random.choice(
            [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)])  # 8 directions
        start_row = random.randint(0, height - 1)
        start_col = random.randint(0, width - 1)

        # Check if word fits and doesn't conflict with existing letters
        can_place = True
        for i, char in enumerate(word):
            r = start_row + i * direction[0]
            c = start_col + i * direction[1]

            if not (0 <= r < height and 0 <= c < width) or \
                    (grid[r][c] != char and grid[r][c] != random.choice(
                        string.ascii_uppercase)):  # Allow overwriting random letters
                can_place = False
                break

        if can_place:
            for i, char in enumerate(word):
                r = start_row + i * direction[0]
                c = start_col + i * direction[1]
                grid[r][c] = char
            word_placed = True
            break
    return word_placed


def print_grid(grid):
    """Prints the word search grid."""
    for row in grid:
        print(" ".join(row))


def check_word(word, grid, found_words):
    """Checks if a word exists in the grid and marks it as found."""
    height = len(grid)
    width = len(grid[0])

    for r in range(height):
        for c in range(width):
            for dr, dc in [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]:
                # Check forward direction
                match_forward = True
                for i, char in enumerate(word):
                    nr = r + i * dr
                    nc = c + i * dc
                    if not (0 <= nr < height and 0 <= nc < width) or grid[nr][nc] != char:
                        match_forward = False
                        break
                if match_forward and word not in found_words:
                    found_words.add(word)
                    return True

                # Check reverse direction
                match_reverse = True
                reversed_word = word[::-1]
                for i, char in enumerate(reversed_word):
                    nr = r + i * dr
                    nc = c + i * dc
                    if not (0 <= nr < height and 0 <= nc < width) or grid[nr][nc] != char:
                        match_reverse = False
                        break
                if match_reverse and word not in found_words:
                    found_words.add(word)
                    return True
    return False


# Game setup
grid_width = 20
grid_height = 20
words_to_find = ["COZIER", "HURRYING", "HEAVIEST", "VICTORIOUS", "DIFFICULTIES", 'DYNAMITE', 'HYDRANT', 'ANAYLZE',
                 'TYRANT', 'ENCYCLOPEDIA', 'CONNECTICUT', 'DELAWARE', 'APPETITE', 'BISCUIT']

grid = create_grid(grid_width, grid_height)

for word in words_to_find:
    place_word(word, grid)

print("Find these words:")
print(", ".join(words_to_find))
print_grid(grid)

found_words = set()
while len(found_words) < len(words_to_find):
    guess = input("Enter a word you found (or 'quit' to exit): ").upper()
    if guess == "QUIT":
        break
    if guess in words_to_find:
        if check_word(guess, grid, found_words):
            print(f"You found '{guess}'!")
        else:
            print(f"'{guess}' is in the list, but not found in the grid yet or already found.")
    else:
        print(f"'{guess}' is not a word to find.")

if len(found_words) == len(words_to_find):
    print("Congratulations! You found all the words!")
else:
    print(f"You found {len(found_words)} out of {len(words_to_find)} words.")





