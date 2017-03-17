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

import mock

from ..http import wsgi


class TestCase(unittest.TestCase):
    def test_application_404(self):
        environ = {
            'PATH_INFO': 'missing_page.html'
        }
        start_response = mock.Mock()

        result = wsgi.application(environ, start_response)

        start_response.assert_called_with(
            '404 Not Found', [('Content-Type', 'text/html')])

        self.assertEqual('missing_page.html Not Found', result)

    def test_application_404_error_sneaky_path(self):
        environ = {
            'PATH_INFO': '/../../../etc/passwd'
        }
        start_response = mock.Mock()
        result = wsgi.application(environ, start_response)

        start_response.assert_called_with(
            '404 Not Found', [('Content-Type', 'text/html')])

        self.assertEqual(
            'Requested path ../../../etc/passwd outside DOCUMENT_ROOT', result)
