# This file is part of eventmq.
#
# eventmq is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# eventmq is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eventmq.  If not, see <http://www.gnu.org/licenses/>.
import unittest


from ..http import urls


class TestCase(unittest.TestCase):
    def test_normalize_static_path_strip_leading_slash(self):
        # The leading slash in a path causes os.path.join to return the path as
        # the full path. normalize_static_path should strip the leading slash
        # off to prevent this
        result = urls.normalize_static_path('/leading/slash/path/')
        self.assertFalse(result.startswith('/leading'))

        result = urls.normalize_static_path('no/leading/slash.js')
        self.assertFalse(result.startswith('no/'))

    def test_normalize_static_path_append_index_html(self):
        # Paths ending with a slash should append index.html. Paths which
        # have a specific file should not have index.html automatically
        # appeneded.

        # Slash only
        result = urls.normalize_static_path('/')
        self.assertTrue(result.endswith('index.html'))

        # Sub-directories
        result = urls.normalize_static_path('/lambs/silence/')
        self.assertTrue(result.endswith('index.html'))

        # Don't append index.html
        result = urls.normalize_static_path('/static/js/myfile.js')
        self.assertFalse(result.endswith('index.html'))

        # Don't append index.html to things that are probably paths. This magic
        # is beyond the scope of eventmq's http server
        result = urls.normalize_static_path('/leading/slash/path')
        self.assertFalse(result.endswith('index.html'))

    def test_normalize_static_path_stay_in_docroot_jail(self):
        with self.assertRaises(ValueError):
            urls.normalize_static_path('../../etc/passwd')
