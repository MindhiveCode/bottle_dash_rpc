from bottle import run, post, request, response, route
import os
from dash_tools.dashd import *

@route('/get_votes', method="post")
def get_votes():
    proposal_hash = request.forms.get("text")
    package = get_votes()
    response.content_type = 'application/json'
    return package

if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)