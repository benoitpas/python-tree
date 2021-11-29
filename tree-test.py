import unittest

from tree import add_id

class TestAddId(unittest.TestCase):

    def test_empty_tree(self):
        et = ()
        self.assertEqual((), add_id(et, 0))

    def test_one_node(self):
        t = ("a",)
        self.assertEqual( ((("a",0),),1), add_id(t, 0))


if __name__ == '__main__':
    unittest.main()