import os
import re
from collections import defaultdict
from urllib.parse import urlparse

def extract_links_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    return re.findall(r'href=["\'](.*?)["\']', content)

def get_domain(url):
    try:
        parsed_url = urlparse(url)
        return parsed_url.netloc
    except Exception:
        return None

html_files = [
    './example_homepage.html',
    './cpython/Lib/test/test_difflib_expect.html',
    './cpython/Lib/profiling/sampling/_flamegraph_assets/flamegraph_template.html',
    './cpython/Lib/profiling/sampling/_heatmap_assets/heatmap_index_template.html',
    './cpython/Lib/profiling/sampling/_heatmap_assets/heatmap_pyfile_template.html',
    './cpython/Lib/idlelib/help.html',
    './cpython/Doc/_static/tachyon-example-heatmap.html',
    './cpython/Doc/_static/tachyon-example-flamegraph.html',
    './cpython/Doc/library/profiling-sampling-visualization.html',
    './cpython/Doc/tools/templates/indexsidebar.html',
    './cpython/Doc/tools/templates/dummy.html',
    './cpython/Doc/tools/templates/customsourcelink.html',
    './cpython/Doc/tools/templates/layout.html',
    './cpython/Doc/tools/templates/download.html',
    './cpython/Doc/tools/templates/indexcontent.html',
    './cpython/Doc/tools/templates/search.html',
    './cpython/Doc/tools/templates/_docs_by_version.html',
    './cpython/Tools/freeze/win32.html',
    './cpython/Platforms/emscripten/web_example_pyrepl_jspi/index.html',
    './cpython/Platforms/emscripten/web_example/index.html',
    './requests/docs/_templates/sidebar.html',
    './kernel_homepage.html',
    './python_homepage.html',
    './osm_homepage.html'
]

domain_count = defaultdict(int)

for html_file in html_files:
    links = extract_links_from_file(html_file)
    for link in links:
        domain = get_domain(link)
        if domain:
            domain_count[domain] += 1

sorted_domains = sorted(domain_count.items(), key=lambda x: x[1], reverse=True)

with open('domain_analysis.csv', 'w') as csv_file:
    csv_file.write('Domain,Count\n')
    for domain, count in sorted_domains:
        csv_file.write(f'{domain},{count}\n')

top_ten_domains = sorted_domains[:10]
for domain, count in top_ten_domains:
    print(f'{domain}: {count}')