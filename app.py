# -*- coding: utf-8 -*-
"""
Text extract API
"""

import json

from bottle import Bottle, request, response
from newspaper.api import fulltext


app = Bottle(catchall=False)


@app.route("/extract", method="POST")
def extract():
    """
    """
    html = request.body.read()

    for lang in ('zh', 'en'):
        try:
            extracted = fulltext(html, language=lang)
        except AttributeError:
            pass

    response.content_type = 'application/json'
    return json.dumps({'result': {'text': extracted}}, ensure_ascii=False)


if __name__ == '__main__':
    from bottle import run
    run(app, debug=True)
