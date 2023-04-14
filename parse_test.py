import unittest

from main import parse


class TestParse(unittest.TestCase):
    def test_correct(self):
        parse_data = parse("https://example.com/path/to/page?name=ferret&color=purple")
        self.assertEqual(parse_data, {"name": "ferret", "color": "purple"})

    def test_extra_spaces(self):
        parse_data = parse("https://example.com/path/to/page?name=ferret &color=purple ")
        self.assertEqual(parse_data, {"name": "ferret", "color": "purple"})

    def test_with_ampersand(self):
        parse_data = parse("https://example.com/path/to/page?name=ferret&color=purple&")
        self.assertEqual(parse_data, {"name": "ferret", "color": "purple"})

    def test_two_ampersand(self):
        parse_data = parse("https://example.com/path/to/page?name=ferret&color=purple&&")
        self.assertEqual(parse_data, {"name": "ferret", "color": "purple"})

    def test_no_question(self):
        self.assertEqual(parse("http://example.com/"), {})

    def test_with_question(self):
        self.assertEqual(parse("http://example.com/?"), {})

    def test_name(self):
        self.assertEqual(parse("http://example.com/?name=Dima"), {"name": "Dima"})

    def test_empty_name(self):
        self.assertEqual(parse("http://example.com/?name= "), {"name": ""})

    def test_empty_string(self):
        self.assertEqual(parse(""), {})

    def test_incorrect_type(self):
        data = ["https://example.com/path/to/page?name=ferret&color=purple"]
        self.assertRaises(TypeError, parse, data)


if __name__ == "__main__":
    unittest.main()
