'''
    Data-type guesser

   Copyright 2016 Rylan Santinon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''


def guess(lst, raise_error=False):
    '''guess datatype from data

    if raise_error is True, then an error will be raised
    when no type can be determined. otherwise None is returned

    vCard properties:
        LANG http://tools.ietf.org/html/rfc6350#section-6.4.4
        string.vcard.lang, fn=TODO

        GENDER http://tools.ietf.org/html/rfc6350#section-6.2.7
        string.vcard.gender, fn=vgender

        GEO http://tools.ietf.org/html/rfc6350#section-6.5.2
        string.vcard.geo, fn=TODO

        TEL https://tools.ietf.org/html/rfc6350#section-6.4.1
        string.vcard.tel, fn=TODO

        TZ https://tools.ietf.org/html/rfc6350#section-6.5.1
        string.vcard.tz, fn=TODO

        URL https://tools.ietf.org/html/rfc6350#section-6.7.8
        string.vcard.url, fn=TODO

    XML Schema:
        string.xml.string: xs:string https://www.w3.org/TR/xmlschema-2/#string
        string.xml.boolean xs:boolean https://www.w3.org/TR/xmlschema-2/#boolean
        string.xml.date xs:date https://www.w3.org/TR/xmlschema-2/#date
        string.xml.hex xs:hexBinary https://www.w3.org/TR/xmlschema-2/#hexBinary
        number.xml.float xs:float https://www.w3.org/TR/xmlschema-2/#float

    string-name
    string-email
    string-text
    string-url
    string-categorical
    string-location
    string-boolean
    string

    number-float
    number-year
    number-int
    number

    time-date
    time-timestamp
    time
    '''
    kind = (guess_number(lst) or
            guess_string(lst) or
            None)
    if not kind and raise_error:
        raise RuntimeError('Could not determine type')
    return kind


def guess_number(lst):
    '''guess number

    types
    number.year
    number
    '''
    kind = 'number'
    if not most_float(lst):
        return None
    kind += (guess_year(lst) or '')
    return kind

def guess_year(lst):
    '''year is sub-type of number'''
    if most_dob(lst):
        return '.year'
    return None

def guess_string(lst):
    '''guess string

    types:
    string.email
    string.name
    string.url
    string

    '''
    kind = 'string'
    if any_float(lst) or any_int(lst):
        return None
    if not most_str(lst):
        return None

    kind += (guess_email(lst) or '')
    kind += (guess_url(lst) or '')
    if guess_bool(lst):
        return kind + guess_bool(lst)
    kind += (guess_vgender(lst) or '')

    return kind

def guess_bool(lst):
    if most_booly(lst):
        return '.boolean'
    return None

def guess_vgender(lst):
    if most_vgender(lst):
        return '.vcard.vgender'
    return None

def guess_email(lst):
    if most_email(lst):
        return '.email'
    return None

def guess_url(lst):
    if most_url(lst):
        return '.url'
    return None

def most_float(lst):
    return _most(float, lst)

def most_dob(lst):
    return _most(dob, lst)

def most_email(lst):
    return _most(email, lst)

def most_url(lst):
    return _most(url, lst)

def most_str(lst):
    return _most(str, lst)

def most_booly(lst):
    return _most(booly, lst)

def most_vgender(lst):
    return _most(vgender, lst)

def _most(f, lst):
    vals = [v for v in [_try(f, l) for l in lst] if v is not None]
    return len(vals) > float(len(lst))/2.0

def any_float(lst):
    return any([_try(float, l) for l in lst])

def any_int(lst):
    return any([_try(int, l) for l in lst])

def _try(f, datum):
    '''try to apply f to datum. Return None if ValueError occurs'''
    try:
        return f(datum)
    except ValueError:
        return None

def dob(datum):
    '''date of birth'''
    if int(datum) < 2020 and int(datum) > 1932:
        return int(datum)
    raise ValueError('Probably not date of birth')

def email(datum):
    '''email address'''
    if '@' in str(datum) and '.' in str(datum):
        return str(datum)
    raise ValueError('Probably not an email')

def url(datum):
    '''url'''
    if ('https://' in str(datum) or
            'http://' in str(datum) or
            'www.' in str(datum)):
        return str(datum)
    raise ValueError('Probably not a url')

def booly(datum):
    '''boolean value'''
    lower = str(datum).lower()
    booleans = ['true', 'false', 't', 'f']
    if lower in booleans:
        return str(datum)
    raise ValueError('Probably not boolean')

def vgender(datum):
    '''vCard gender

    See http://tools.ietf.org/html/rfc6350#section-6.2.7

    >>> vgender('m')
    'm'

    >>> vgender('F;lady lol')
    'F;lady lol'

    >>> vgender('foobar')
    Traceback (most recent call last):
    ValueError: Not vCard gender
    '''
    options = ['m', 'f', 'o', 'n', 'u']
    symbol = str(datum).lower().split(';')[0]
    if symbol in options:
        return str(datum)
    raise ValueError('Not vCard gender')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
