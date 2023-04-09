from http.cookies import SimpleCookie


# def parse(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    if not isinstance(query, str):
        raise TypeError("Query is not a string")

    if not query:
        return {}

    if "," in query:
        return {}

    cookie = SimpleCookie()
    cookie.load(query)
    cookie = {k: v.value for k, v in cookie.items()}

    return cookie


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

