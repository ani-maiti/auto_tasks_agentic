echo "Downloading jq binary manually..."
wget https://github.com/jqlang/jq/releases/download/jq-1.6/jq-linux-amd64 -O jq
chmod +x jq
sudo mv jq /usr/local/bin/