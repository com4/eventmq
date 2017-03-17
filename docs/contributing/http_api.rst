#################
Writing HTTP APIs
#################
EventMQ implements a simple HTTP server and API toolkit. This page is an overview of what to expect when contributing APIs to EventMQ.

URL Routing
===========
URL resolution follows an order.

 #. Search ``eventmq.http.urls.patterns`` for matches on the requested path.
 #. Look in the document root for file path matches. This path is built and sanitized using :func:`eventmq.http.urls.normalize_static_path`.
 #. Return a 404

Patterns
--------
URLs are defined in the ``patterns`` variable found in ``eventmq/http/urls.py``. It is a list of lists with two arguments. The first argument is a regular expression  used to compare the requested path and the second is the full path to the function to execute if a match is found.

For example the following would define a /api/v1/hello_world/ endpoint which executes a fictional ``eventmq.http.views.hello_world`` function.

.. code:: python

	  patterns = (
	      (r'^/api/v1/hello_world/$', 'eventmq.http.views.hello_world')
	  )

Static Files
------------
Static files are served from `eventmq/http/html/`. Please add additional files sparingly. Credit for any included assets must be documented in CREDITS.md.

Views
=====
Views house the logic for returning information about a page.

Mithril
=======
`Mithril.js <https://mithril.js.org>`_ is used as the framework for the built-in dashboard.

Calling the API
---------------
Soon...

Updating the DOM
----------------
Soon...
