echo "Checking if necessary tools are installed..."
command -v curl >/dev/null 2>&1 && echo "curl is installed" || echo "curl is not installed"
command -v jq >/dev/null 2>&1 && echo "jq is installed" || echo "jq is not installed"
command -v python3 >/dev/null 2>&1 && echo "python3 is installed" || echo "python3 is not installed"