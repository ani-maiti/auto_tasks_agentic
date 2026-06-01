echo "Step 3: Install jq without sudo"
wget -O jq https://github.com/stedolan/jq/releases/download/jq-1.7/jq-linux64
chmod +x jq
export PATH="$PATH:$PWD"