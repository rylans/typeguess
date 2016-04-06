'''
   vCard translator

   Translate typeguess types to vCard microformat types


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

TG_VCARD_MAP = (
    {'string.vcard.gender': 'GENDER',
     'string.vcard.geo': 'GEO',
     'string.vcard.tel': 'TEL',
    })

def to_vcard(tg_type):
    '''Translate typeguess style types to vCard types

    Raises ValueError when not possible

    >>> to_vcard('string.vcard.geo')
    'GEO'

    >>> to_vcard('foo.bar')
    Traceback (most recent call last):
    ValueError: Type foo.bar is not mapped to any vCard type
    '''
    vc_type = TG_VCARD_MAP.get(tg_type)
    if not vc_type:
        raise ValueError('Type %s is not mapped to any vCard type' % (tg_type))
    return vc_type

if __name__ == '__main__':
    import doctest
    doctest.testmod()
