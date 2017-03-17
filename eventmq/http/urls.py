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

    Returns:
        (str) Normalizes ``request_path`` to the corresponding filesystem path
            for static files.
    """
    # Leading slashes break os.path.join so strip it off if it exists.
    if request_path.startswith('/'):
        request_path = request_path[1:]

    fs_path = os.path.normpath(os.path.join(DOCUMENT_ROOT, request_path))

    base_dir = os.path.dirname(fs_path)

    if not base_dir.startswith(DOCUMENT_ROOT):
        raise ValueError('Requested path {} outside DOCUMENT_ROOT'.format(
            fs_path))

    return fs_path