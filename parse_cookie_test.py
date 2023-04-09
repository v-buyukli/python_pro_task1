import unittest

from main import parse_cookie


class TestParseCookie(unittest.TestCase):
    def test_correct1(self):
        parse_data = parse_cookie("name=Dima")
        self.assertEqual(parse_data, {"name": "Dima"})

    def test_correct2(self):
        parse_data = parse_cookie("name=Dima;age=28")
        self.assertEqual(parse_data, {"name": "Dima", "age": "28"})

    def test_empty(self):
        self.assertEqual(parse_cookie(""), {})

    def test_semicolon(self):
        parse_data = parse_cookie("name=Dima;age=28;")
        self.assertEqual(parse_data, {"name": "Dima", "age": "28"})

    def test_extra_equal(self):
        parse_data = parse_cookie("name=Dima=User;age=28;")
        self.assertEqual(parse_data, {"name": "Dima=User", "age": "28"})

    def test_extra_spaces(self):
        parse_data = parse_cookie("name=Vitya ;age=22 ;")
        self.assertEqual(parse_data, {"name": "Vitya", "age": "22"})

    def test_empty_name(self):
        self.assertEqual(parse_cookie("name="), {"name": ""})

    def test_comma(self):
        parse_data = parse_cookie("name=Vitya,age=22")
        self.assertEqual(parse_data, {})

    def test_space(self):
        parse_data = parse_cookie("name=Vitya age=22")
        self.assertEqual(parse_data, {"name": "Vitya", "age": "22"})

    def test_incorrect_type(self):
        data = ["name=Vitya;"]
        self.assertRaises(TypeError, parse_cookie, data)


if __name__ == "__main__":
    unittest.main()
