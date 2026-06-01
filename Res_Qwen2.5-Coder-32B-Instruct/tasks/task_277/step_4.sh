echo "wget is available. Downloading jq manually."
wget -O jq https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
chmod +x jq
mv jq /usr/local/bin/