from bottle import get, run, post, request, response, route
import os
import sys


if sys.version_info[0] < 3:
    sys.path.append(os.path.join(os.path.dirname(__file__), './dash_tools'))
    import dashd

else:
    from dash_tools import dashd


@route('/api/get_latest_all')
def get_votes():
    package = dashd.get_everything()
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
    vote_info = dashd.get_ballot(prop_hash)
    return vote_info

@route('/api/masternode_list')
def get_masternode_list():
    package = dashd.get_masternodes()
    response.content_type = 'application/json'
    return dict(data=package)


if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)
