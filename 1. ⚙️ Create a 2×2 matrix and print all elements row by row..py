#1. ⚙️ Create a 2×2 matrix and print all elements row by row.
'''
**Explanation:**
**Brute Force Method:** Create a 2×2 matrix using nested lists (list of lists). Initialize it with four values, such as [[1, 2], [3, 4]]. Then, use a loop to iterate over each row and print the entire row at once. Time complexity is O(rows) = O(2), space complexity is O(1).
'''


class BruteForceMatrix:
    def __init__(self):
        self.matrix = [[1, 2], [3, 4]]
    def print_matrix(self):
        for row in self.matrix:
            print(row)

if __name__ == '__main__':
    mat = BruteForceMatrix()
    mat.print_matrix()