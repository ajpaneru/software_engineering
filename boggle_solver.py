class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = set([word.lower() for word in dictionary])
        self.solutions = set()
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.min_word_length = 3  # Adjust this if necessary
        self.prefix_set = self.build_prefix_set(dictionary)

    # Build a set of valid prefixes from the dictionary
    def build_prefix_set(self, dictionary):
        prefix_set = set()
        for word in dictionary:
            word = word.lower()
            for i in range(1, len(word)):
                prefix_set.add(word[:i])
        return prefix_set

    # Check if a word is valid
    def is_valid_word(self, word):
        return word.lower() in self.dictionary

    # Check if a prefix is valid
    def is_valid_prefix(self, prefix):
        return prefix.lower() in self.prefix_set

    # Depth-First Search (DFS)
    def dfs(self, x, y, visited, current_word):
        # Add valid words of sufficient length to solutions
        if len(current_word) >= self.min_word_length and self.is_valid_word(current_word):
            self.solutions.add(current_word.lower())

        # Check if the current word is a valid prefix to avoid unnecessary recursion
        if not self.is_valid_prefix(current_word):
            return

        # Possible movement directions: up, down, left, right, and diagonals
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the new coordinates are within the bounds of the grid
            if 0 <= nx < self.rows and 0 <= ny < self.cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                next_char = self.grid[nx][ny]  # Now safe to access the grid

                # Handle special "Qu" case
                if next_char == "Qu":
                    self.dfs(nx, ny, visited, current_word + "Qu")
                else:
                    self.dfs(nx, ny, visited, current_word + next_char)

                visited.remove((nx, ny))  # Backtrack

    # Main method to find all valid words
    def getSolution(self):
        self.solutions = set()  # Reset the solutions
        if not self.grid or self.rows == 0 or self.cols == 0:  # Handle empty grids
            return []

        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, set([(i, j)]), self.grid[i][j])

        return sorted(self.solutions)
