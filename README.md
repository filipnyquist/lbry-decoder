# Lbry-decoder
>Lbry-decoder is a simple bridge that works as a server listening for requests to decode a claim within the lbry blockchain (with the currect protobuf scheme.)
_It uses the RPC-server exposed by the lbrycrd daemon._

# Usage
>This is a decoder made for the logstash-input-plugin that works as a brige to convert claim data as there is no ruby implentation of the decoder yet.
**This decoder needs to be running in the background if you use the logstash-input-cortesexplorer with LBRY support.**

To get it up and running clone the repo with:
```bash
#Clone the repo:
git clone https://github.com/cryptodevorg/lbry-decoder
#Be sure that you have python 2.7 and pip installed and run:
sudo pip install -r requirements.txt
#Configure the decoder with the config.json file to your lbrtcrd daemon settings.
Edit the config.json to your lbrycrd daemon settings...
#Run the decoder server
python decoder.py
```

## Known bugs
> A small percent of the claims in the blockchain cannot be decoded by this tool in its current state, the bridge will then just return nothing to the logstash-plugin.