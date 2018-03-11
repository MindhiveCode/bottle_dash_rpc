from bottle import get, run, post, request, response, route
import os
from dash_tools.dashd import *

@get('/get_votes')
def get_votes():
    package = get_votes()
    response.content_type = 'application/json'
    return package

@route('/get_proposals')
def get_proposals():
    package = get_proposals()
    response.content_type = 'application/json'
    return dict(data=package)


if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)