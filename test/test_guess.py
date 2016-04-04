'''
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

import unittest

from typeguess import guess

class GuessTest(unittest.TestCase):
    def test_guess_url(self):
        gtype = guess(['homepages', 'https://www.facebook.com/1234',
                 'www.atlassian.net', 'http://edu.edu'])
        self.assertTrue('url' in gtype)

    def test_guess_email(self):
        gtype = guess(['email addresses', 'jk@gmail.com', 'p.hanson@rq.org'])
        self.assertTrue('email' in gtype)

    def test_guess_year(self):
        gtype = guess(['date-of-birth', 1975, 1982, 2001, 1946, 1982, 1899])
        self.assertTrue('number.year' in gtype)

    def test_guess_float(self):
        gtype = guess(['readings', 23.1, 0.01])
        self.assertTrue('number' is gtype)

if __name__ == '__main__':
    unittest.main()
