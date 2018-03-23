# bottle_dash_rpc
Testing Bottle as an HTTP server for Dash RPC Commands

* Fetch the latest proposoal and vote info (combines the two)
/api/get_latest_all

* Fetch the latest proposal info (Can also be done from the Insight Explorer in some other code)
/api/get_proposals

* Fetch the votes for a spefici proposal
/api/get_votes? Pass a proposal hash after the ? (URI info)
