import os

async_files = [
    "./cpython/Lib/test/test_grammar.py",
    "./cpython/Lib/test/test_monitoring.py",
    "./cpython/Lib/test/test_inspect/inspect_fodder2.py",
    "./cpython/Lib/test/test_inspect/inspect_fodder.py",
    "./cpython/Lib/test/test_inspect/test_inspect.py",
    "./cpython/Lib/pydoc_data/topics.py",
    "./cpython/Lib/_ast_unparse.py",
    "./cpython/Lib/idlelib/idle_test/test_colorizer.py",
    "./cpython/Tools/inspection/benchmark_external_inspection.py",
    "./cpython/Tools/jit/_llvm.py",
    "./cpython/Tools/jit/_dwarf.py",
    "./cpython/Tools/jit/_targets.py",
    "./cpython/Platforms/Android/__main__.py"
]

for file in async_files:
    print(f"File: {file}")
    with open(file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "async def" in line:
                print(f"Line {i+1}: {line.strip()}")