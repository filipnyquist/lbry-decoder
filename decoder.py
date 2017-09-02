import json
from bitcoinrpc.authproxy import AuthServiceProxy
from lbryschema.decode import smart_decode
from flask import Flask, url_for
app = Flask(__name__)

def get_lbrycrdd_connection_details():
    with open('config.json', 'r') as f:
        config = json.load(f)
    rpc_user = config['rpc_user']
    rpc_pass = config['rpc_password']
    rpc_port = config['rpc_port']
    rpc_url = config['rpc_url']
    return "http://%s:%s@%s:%i" % (rpc_user, rpc_pass, rpc_url, rpc_port)

@app.errorhandler(500)
def internal_error(error):

    return 'error when decoding claims'

@app.route('/claim_decode_id/<claimid>')
def api_decode(claimid):
    connection_string = get_lbrycrdd_connection_details()
    rpc = AuthServiceProxy(connection_string)
    claim = rpc.getclaimbyid(claimid)
    if claim:
        converted = "".join([chr(ord(i)) for i in claim['value']])
        decoded = smart_decode(converted) # Decode the claims and dump them back to logstash plugin
        claim['value'] = decoded.claim_dict
        return json.dumps(claim)

@app.route('/claim_decode/<claimid>')
def api_decodebyclaim(claimid):
    connection_string = get_lbrycrdd_connection_details()
    rpc = AuthServiceProxy(connection_string)
    claim = rpc.getvalueforname(claimid)
    if claim:
        converted = "".join([chr(ord(i)) for i in claim['value']])
        decoded = smart_decode(converted) # Decode the claims and dump them back to logstash plugin
        return json.dumps(decoded.claim_dict)

if __name__ == '__main__':
    app.run(host='127.0.0.1')
