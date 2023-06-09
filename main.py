from urllib import parse as prs
from http.cookies import SimpleCookie


def parse(query: str) -> dict:
    if not isinstance(query, str):
        raise TypeError("Query is not a string")

    if not query:
        return {}

    split_result = prs.urlsplit(query)
    dict_result = dict(prs.parse_qsl(split_result.query))
    dict_result = {key: value.strip() for key, value in dict_result.items()}

    return dict_result   


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
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
