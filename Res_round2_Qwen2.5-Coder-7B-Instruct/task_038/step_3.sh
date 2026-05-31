echo "It seems like there was an issue with the grep command. Let's try a different approach to find unclosed quotes."
find . -type f -exec grep -Hn "['\"]" {} +