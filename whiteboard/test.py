from whiteboard import solution
import unittest 


class TestSolution(unittest.TestCase):
    def test_one(self):
        arr = [2,0,2,1,1,0]
        self.assertEqual(solution(arr), [0,0,1,1,2,2])

    def test_two(self):
        arr = [2,0,1]
        self.assertEqual(solution(arr), [0,1,2])




if __name__ == '__main__':
    unittest.main()