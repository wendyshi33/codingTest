import json
import unittest

#  coordinates.json
# [
#     {"id":"a", "value":"31,49"},
#     {"id":"b", "value":"44,67"},
#     {"id":"c", "value":"0,81"},
#     {"id":"d", "value":"75,92"}
# ]


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        nn = NearestNeighbour('coordinates.json')
        res1 = [['a', 31, 49], ['b', 44, 67], ['c', 0, 81], ['d', 75, 92]]
        self.assertEqual(nn.get_ordered_list(0, 0), res1)
        res2 = [['a', 31, 49], ['b', 44, 67], ['c', 0, 81], ['d', 75, 92]]
        self.assertEqual(nn.get_ordered_list(-1, -1), res2)
        res3 = [['a', 31, 49], ['b', 44, 67], ['c', 0, 81], ['d', 75, 92]]
        self.assertEqual(nn.get_ordered_list(-1, -1), res2)
        res4 = [['a', 31, 49], ['b', 44, 67], ['c', 0, 81], ['d', 75, 92]]
        self.assertEqual(nn.get_ordered_list(-1, -1), res4)


    # Other test cases
    # [[a,1,1],[b,-1,-1],[c,1,-1],[d,-1,1]] and give point of 0,0

if __name__ == '__main__':
    unittest.main()


class NearestNeighbour:
    def __init__(self, _f):
        self.points = []
        with open(_f) as data_file:
            data = json.load(data_file)

        for p in data:
            coord = [int(x.strip()) for x in p['value'].split(',')]
            self.points.append([p['id'], coord[0], coord[1]])

    def get_ordered_list(self, x, y):
        """Make http call and get canonical url and items for that vpreso call and facets

        Args:
            x : input coordinate x
            y : input coordinate y
        Returns:
            list of points that are closest to point (x,y) in ascending order
        Raises:
            None.

        """

        # for given point, calculate the distance and use it as sort key
        # using lambda expression and pass it as key to compare
        self.points.sort(key=lambda p: (p[1] - x) ** 2 + (p[2] - y) ** 2)

        # return the sorted result
        return self.points

