
"""
NAME: Rojan Paneru
SID: @03042926

This is a Python implementation of the Boggle game.
It identifies all valid words in an NxN grid using a given dictionary.
"""
class Boggle:
    """Class to implement the Boggle game logic."""

    def __init__(self, grid, dictionary):
        """Initialize the game with the given grid and dictionary."""
        self.setGrid(grid)  # Prepare the grid for use
        self.setDictionary(dictionary)  # Load the dictionary
        self.solution = set()  # Store valid words found during the search

    def setGrid(self, grid):
        """Convert all letters in the grid to uppercase and set dimensions."""
        # Convert each letter to uppercase for uniformity
        self.grid = [[cell.upper() for cell in row] for row in grid]
        self.rows = len(self.grid)  # Number of rows in the grid
        self.cols = len(self.grid[0]) if self.rows > 0 else 0  # Number of columns
        # Initialize a visited matrix to track explored cells during DFS
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        print(f"Grid set: {self.grid}")  # Debugging output to verify the grid

    def setDictionary(self, dictionary):
        """Convert dictionary words to uppercase and generate prefix set."""
        # Store words in uppercase for consistent matching
        self.dictionary = set(word.upper() for word in dictionary)
        # Build a prefix set to optimize the search process
        self.prefix_set = self.build_prefix_set(self.dictionary)
        print(f"Dictionary set: {self.dictionary}")  # Debug print to confirm dictionary
        print(f"Prefix set: {self.prefix_set}")  # Debug print to confirm prefix set

    def build_prefix_set(self, dictionary):
        """Generate all possible prefixes from the dictionary."""
        prefix_set = set()  # Store prefixes
        # Iterate through each word to extract its prefixes
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])  # Add each prefix to the set
        return prefix_set

    def getSolution(self):
        """Clear previous solutions and find all valid words."""
        self.solution.clear()  # Reset the solution set before starting a new search
        self.findAllWords()  # Search the grid for valid words
        print(f"Final solution: {self.solution}")  # Debug print to display results
        # Return the words found, sorted alphabetically
        return sorted(list(self.solution))

    def isValidWord(self, word):
        """Check if a word is valid (exists in dictionary and has length ≥ 3)."""
        valid = word in self.dictionary and len(word) >= 3  # Validate word
        print(f"Checking word: {word}, Valid: {valid}")  # Debug print for validation
        return valid

    def isValidPrefix(self, prefix):
        """Check if a prefix exists in the prefix set."""
        valid = prefix in self.prefix_set  # Validate prefix
        print(f"Checking prefix: {prefix}, Valid: {valid}")  # Debug print for validation
        return valid

    def findAllWords(self):
        """Initiate a depth-first search from every cell in the grid."""
        # Start DFS from every cell to find possible words
        for row in range(self.rows):
            for col in range(self.cols):
                self.dfs(row, col, "")  # Start DFS with an empty path

    def dfs(self, row, col, path):
        """Perform depth-first search from the given cell."""
        # Return if out of grid bounds or the cell is already visited
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.visited[row][col]:
            return

        # Get the current letter and add it to the path
        letter = self.grid[row][col]
        new_path = path + letter
        print(f"Exploring: {new_path}")  # Debug print for the current path

        # Stop exploring if the path is not a valid prefix
        if not self.isValidPrefix(new_path):
            return

        # Mark the current cell as visited
        self.visited[row][col] = True

        # Add the path to the solution if it forms a valid word
        if self.isValidWord(new_path):
            self.solution.add(new_path)  # Add valid word to the solution set
            print(f"Added to solution: {new_path}")  # Debug print for added word

        # Explore all 8 possible directions from the current cell
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        # Recursively search in all 8 directions
        for drow, dcol in directions:
            self.dfs(row + drow, col + dcol, new_path)

        # Unmark the current cell to allow other paths to use it
        self.visited[row][col] = False


