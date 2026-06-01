import os
import re

markdown_files = [
    './cpython/InternalDocs/structure.md',
    './cpython/InternalDocs/stack_protection.md',
    './cpython/InternalDocs/frames.md',
    './cpython/InternalDocs/interpreter.md',
    './cpython/InternalDocs/code_objects.md',
    './cpython/InternalDocs/qsbr.md',
    './cpython/InternalDocs/exception_handling.md',
    './cpython/InternalDocs/profiling_binary_format.md',
    './cpython/InternalDocs/jit.md',
    './cpython/InternalDocs/compiler.md',
    './cpython/InternalDocs/README.md',
    './cpython/InternalDocs/generators.md',
    './cpython/InternalDocs/string_interning.md',
    './cpython/InternalDocs/asyncio.md',
    './cpython/InternalDocs/parser.md',
    './cpython/InternalDocs/changing_grammar.md',
    './cpython/InternalDocs/garbage_collector.md',
    './cpython/InternalDocs/stackrefs.md',
    './cpython/Modules/_hacl/README.md',
    './cpython/.github/SECURITY.md',
    './cpython/.github/PULL_REQUEST_TEMPLATE.md',
    './cpython/Objects/mimalloc/prim/readme.md',
    './cpython/Objects/mimalloc/prim/windows/readme.md',
    './cpython/Objects/object_layout.md',
    './cpython/Misc/mypy/README.md',
    './cpython/Misc/rhel7/README.md',
    './cpython/Lib/test/test_importlib/namespace_pkgs/foo/README.md',
    './cpython/Lib/test/archivetestdata/README.md',
    './cpython/Tools/picklebench/README.md',
    './cpython/Tools/cases_generator/interpreter_definition.md',
    './cpython/Tools/cases_generator/README.md',
    './cpython/Tools/jit/jit_infra.md',
    './cpython/Tools/jit/README.md',
    './cpython/Tools/pixi-packages/README.md',
    './cpython/Python/vm-state.md',
    './cpython/Python/tier2_engine.md',
    './cpython/Platforms/Apple/iOS/README.md',
    './cpython/Platforms/emscripten/README.md',
    './cpython/Platforms/Android/README.md',
    './cpython/Platforms/WASI/README.md',
    './requests/tests/certs/README.md',
    './requests/tests/certs/mtls/README.md',
    './requests/tests/certs/expired/README.md',
    './requests/HISTORY.md',
    './requests/.github/SECURITY.md',
    './requests/.github/CODE_OF_CONDUCT.md',
    './requests/.github/ISSUE_TEMPLATE.md',
    './requests/.github/AI_POLICY.md',
    './requests/.github/CONTRIBUTING.md',
    './requests/.github/ISSUE_TEMPLATE/Feature_request.md',
    './requests/.github/ISSUE_TEMPLATE/Custom.md',
    './requests/.github/ISSUE_TEMPLATE/Bug_report.md',
    './requests/README.md'
]

def extract_headings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    headings = re.findall(r'^(#+)\s+(.*)', content, re.MULTILINE)
    return headings

def build_toc(headings):
    toc = []
    for level, title in headings:
        indent = '  ' * (len(level) - 1)
        toc.append(f"{indent}- [{title}](#{title.lower().replace(' ', '-')})")
    return '\n'.join(toc)

def save_toc(file_path, toc):
    toc_file_path = file_path.replace('.md', '_toc.md')
    with open(toc_file_path, 'w', encoding='utf-8') as toc_file:
        toc_file.write(toc)

max_headings_count = 0
file_with_most_headings = None

for file_path in markdown_files:
    headings = extract_headings(file_path)
    if len(headings) > max_headings_count:
        max_headings_count = len(headings)
        file_with_most_headings = file_path
    toc = build_toc(headings)
    save_toc(file_path, toc)

print(f"File with the most headings: {file_with_most_headings}")