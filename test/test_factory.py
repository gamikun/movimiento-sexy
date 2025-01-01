import unittest
from sexy.factory import arc_pos

class TestFactory(unittest.TestCase):
    def test_arc_pos(self):
        self.assertEqual(arc_pos(1, 0), (1.0, 0.0))
        self.assertEqual(arc_pos(1, 0, r=2.0), (2.0, 0.0))
        self.assertEqual(
            arc_pos(12, 1, r=1.0),
            (0.8660254037844387, 0.49999999999999994),
        )


if __name__ == '__main__':
    unittest.main()