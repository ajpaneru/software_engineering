import unittest
import sys
sys.path.append(".")  # Add current directory to Python path

from boggle_solver import Boggle  # Import the Boggle class

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):
    def test_Scalability_4x4(self):
        grid = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["I", "J", "K", "L"], ["M", "N", "O", "P"]]
        dictionary = ["abc", "def", "ghi", "jkl", "mnop"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["abc", "def", "ghi", "jkl", "mnop"]
        self.assertEqual(expected, sorted(solution))

    def test_Scalability_5x5(self):
        grid = [["A", "B", "C", "D", "E"], ["F", "G", "H", "I", "J"], ["K", "L", "M", "N", "O"], ["P", "Q", "R", "S", "T"], ["U", "V", "W", "X", "Y"]]
        dictionary = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
        self.assertEqual(expected, sorted(solution))

class TestSuite_Complete_Coverage(unittest.TestCase):
    def test_Complex_case_1(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "def", "ghi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["abc", "def", "ghi"]
        self.assertEqual(expected, sorted(solution))

if __name__ == '__main__':
    unittest.main()
