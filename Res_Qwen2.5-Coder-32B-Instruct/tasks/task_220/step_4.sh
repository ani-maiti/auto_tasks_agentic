echo "Filtering out standard library and relative imports"
grep -vE '^(__future__|collections|collections\.abc|http\.cookiejar|typing|typing_extensions|urllib3|setuptools|the|which|here|a|another|using|None|DataType|Callable|given|lines|content|CookieJar|underspecified|JSONDecodeError|pygments\.style|pygments\.token|self\.raw\.stream)' imports.txt > filtered_imports.txt
echo "Filtered imports saved to filtered_imports.txt"
cat filtered_imports.txt