import re


def parse_masternode_status_vin(status_vin_string):
    status_vin_string_regex = re.compile('CTxIn\(COutPoint\(([0-9a-zA-Z]+),\\s*(\d+)\),')

    m = status_vin_string_regex.match(status_vin_string)

    # To Support additional format of string return from masternode status rpc.
    if m is None:
        status_output_string_regex = re.compile('([0-9a-zA-Z]+)\-(\d+)')
        m = status_output_string_regex.match(status_vin_string)

    txid = m.group(1)
    index = m.group(2)

    vin = txid + '-' + index
    if (txid == '0000000000000000000000000000000000000000000000000000000000000000'):
        vin = None

    return vin


def parse_raw_votes(raw_votes):
    votes = []

    for count, v in enumerate(raw_votes.keys()):
        vote_hash = v
        (outpoint, ntime, outcome, signal) = raw_votes[vote_hash].split(':')
        signal = signal.lower()
        outcome = outcome.lower()

        mn_collateral_outpoint = parse_masternode_status_vin(outpoint)
        v = {
            'vote_hash': vote_hash,
            'mn_collateral_outpoint': mn_collateral_outpoint,
            'signal': signal,
            'outcome': outcome,
            'ntime': ntime,
        }
        votes.append(v)

    return votes