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


class HttpError(Exception):
    """
    All other HTTP related exceptions should inherit from this

    https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
    """
    REASON_PHRASE = ''
    STATUS_CODE = 500

    def __init__(self, response_body='', content_type='text/html', *args):

        """
        Args:
            response_body (str): Additional information to be included as the
                response body of the error. (default: '')
            content_type (str): The content type of the response body.
                (default: 'text/html')
        """
        self.response_body = response_body
        self.content_type = content_type

        super(HttpError, self).__init__(*args)


class Http400(HttpError):
    """
    Raised when the server cannot or will not process the request due to a
    client error
    """
    REASON_PHRASE = 'Bad Request'
    STATUS_CODE = 400


class Http403(HttpError):
    """
    Raised when the server understands the request but the client is
    unauthorized to make it
    """
    REASON_PHRASE = 'Forbidden'
    STATUS_CODE = 403


class Http404(HttpError):
    """
    Raised when the server can't find the requested resource
    """
    REASON_PHRASE = 'Not Found'
    STATUS_CODE = 404


class Http500(HttpError):
    """
    Raised when the server encounters an unexpected condition
    """
    REASON_PHRASE = 'Internal Server Error'
    STATUS_CODE = 500
