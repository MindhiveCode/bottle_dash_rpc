from bottle import get, run, post, request, response, route
import os
import sys

if sys.version > 3:
    sys.path.append('dash_tools')
    import dashd

else:
    from dash_tools import dashd

@route('/api/get_latest_all')
def get_votes():
    package = dashd.get_votes()
    response.content_type = 'application/json'
    return dict(data=package)

@route('/api/get_proposals')
def get_proposals():
    package = dashd.get_proposals()
    response.content_type = 'application/json'
    return dict(data=package)

@route('/api/get_votes')
def get_votes_for_hash():
    prop_hash = request.query.proposal_hash
    #print(prop_hash)
    vote_info = dashd.get_ballot(prop_hash)

    return vote_info


if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)