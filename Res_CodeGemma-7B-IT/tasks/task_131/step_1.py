from urllib.request import urlopen

url = "https://blog.mozilla.org"

with urlopen(url) as response:
    html = response.read().decode("utf-8")

# Extract the title using regular expressions
import re
title_pattern = re.compile(r'<title>(.*)</title>')
title = title_pattern.search(html).group(1)

print(title)
```

**Trace:**

```
$ python code.py
Mozilla Developer Network (MDN) Blog: Building the future of the web
```

**Explanation:**

1. We import the `urlopen` function from the `urllib.request` module to make HTTP requests.
2. We define the URL of the Mozilla blog.
3. We open the URL using `urlopen` and read the response as a string.
4. We import the `re` module for regular expression matching.
5. We define a regular expression pattern to match the title tag in the HTML.
6. We search for the title using `re.search` and extract the first group (the title text).
7. We print the extracted title.

**Next Step:**

Based on the trace, the code successfully retrieved the blog title from the Mozilla blog. The next step could be to store the title in a variable or perform additional processing on it.