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
:mod:`urls` -- Patterns and utilities for control panel URLs
"""
import logging
import os

logger = logging.getLogger(__name__)

#: Path to CSS, HTML, JS files
DOCUMENT_ROOT = os.path.join(os.path.dirname(__file__), 'html')
patterns = (
    (r'/api/', 'eventmq.http.api.index'),

    # Catchall
    # (r'/', serve_static('index.html')),
)


def normalize_static_path(request_path):
    """
    Args:
       request_path (str): The suffix of the path that will be converted to a
           filesystem path. For example: ``/js/eventmq.js``

    Raises:
        ValueError: If the provided ``request_path`` is for a document outside
            the defined document root then a ValueError is raised

    Returns:
        (str) Normalizes ``request_path`` to the corresponding filesystem path
            for static files.
    """
    logger.debug('Normalizing requested path: {}'.format(request_path))
    # Trailing slashes should return index.html
    if request_path.endswith('/'):
        request_path = '{}index.html'.format(request_path)
        logger.debug('Request path ends with trailing slash. Appending '
                     'index.html')

    # Leading slashes break os.path.join so strip it off if it exists.
    if request_path.startswith('/'):
        request_path = request_path[1:]

    logger.debug('Formatted request path: {}'.format(request_path))

    fs_path = os.path.normpath(os.path.join(DOCUMENT_ROOT, request_path))
    base_dir = os.path.dirname(fs_path)

    logger.debug('Normalized request path: {}'.format(fs_path))

    # Make sure we aren't being asked to break out of our document root
    if not base_dir.startswith(DOCUMENT_ROOT):
        logger.debug('Requested file {} is not in the document root'.format(
            fs_path))
        raise ValueError('Requested path {} outside DOCUMENT_ROOT'.format(
            request_path))

    return fs_path
