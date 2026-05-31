echo "The previous command failed due to an unexpected EOF. This might be because there was an unclosed quote somewhere in the script."
echo "Let's check if there are any unclosed quotes in the script."
grep -r "['\"]" .