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
"""
:mod:`wsgi` -- WSGI interface for control panel
===============================================
Processes the requests for EventMQ's web based control panel.
"""
import logging
import re
import os
import mimetypes
from string import Template

from eventmq import __version__
from . import urls

logger = logging.getLogger(__name__)


VALID_TEMPLATE_TYPES = ['text/html', ]


def applicaiton(environ, start_response):
    """
    Manage HTTP requests for EventMQ's control panel

    Args:
       environ (dict): WSGI environment
       start_response (func): The function used to start the HTTP response.

    Returns:
        (list) Http content
    """
    request_path = environ.get('PATH_INFO')

    # Check defined patterns
    for pattern, callable_path in urls.patterns:
        if re.search(pattern, request_path):
            logger.debug(callable_path)

            start_response('200 OK', [('Content-Type', 'text/html')])

            return ['asdf']

    # Fall back to the file system
    normalized_path = urls.normalize_static_path(request_path)

    if os.path.exists(normalized_path):
        mimetype = mimetypes.guess_type(normalized_path)[0] or \
                   'application/octet-stream'

        with open(normalized_path, 'r') as f:
            if mimetype in VALID_TEMPLATE_TYPES:
                template = Template(f.read())
                # Inject some default template variables
                content = template.safe_substitute(
                    emq_version=__version__
                )
            else:
                content = f.read()

        start_response('200 OK', [('Content-Type', mimetype)])

        return [content]

    return not_found_view(environ, start_response)


def not_found_view(environ, start_response):
    """
    """
    start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
    return ['404 Not Found']
