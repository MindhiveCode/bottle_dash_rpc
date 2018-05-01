# bottle_dash_rpc
Testing Bottle as an HTTP server for Dash RPC Commands

## Setup
Now using monit for monitoring on port 2812

When setting up, make sure to set the httpd address = internal AWS IP address

When running, make sure to run inside of screen if testing. Then let cron take over.

* Fetch the latest proposoal and vote info (combines the two)
/api/get_latest_all

* Fetch the latest proposal info (Can also be done from the Insight Explorer in some other code)
/api/get_proposals

* Fetch the votes for a specific proposal
/api/get_votes? Pass a proposal hash after the ? (URI info)

* Fetch the masternode list
/api/masternodelist