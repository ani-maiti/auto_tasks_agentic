import os
import ast
import json

def extract_info_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    tree = ast.parse(content)
    
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    imports = [alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names]
    imports += [alias.name for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) for alias in node.names]
    docstrings = {node.name: ast.get_docstring(node) for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef))}
    
    return {
        'file': file_path,
        'functions': functions,
        'classes': classes,
        'imports': imports,
        'docstrings': docstrings
    }

files = [
    "scripts/divmod_threshold.py",
    "./cpython/Tools/scripts/sortperf.py",
    "./cpython/Tools/scripts/long_conv_tables.py",
    "./cpython/Tools/scripts/var_access_benchmark.py",
    "./cpython/Tools/scripts/combinerefs.py",
    "./cpython/Tools/scripts/summarize_stats.py",
    "./cpython/Tools/check-c-api-docs/main.py",
    "./cpython/Tools/build/smelly.py",
    "./cpython/Tools/build/consts_getter.py",
    "./cpython/Tools/build/generate_global_objects.py",
    "./cpython/Tools/build/generate_slots.py",
    "./cpython/Tools/build/freeze_modules.py",
    "./cpython/Tools/build/parse_html5_entities.py",
    "./cpython/Tools/build/generate_token.py",
    "./cpython/Tools/build/umarshal.py",
    "./cpython/Tools/build/generate_stdlib_module_names.py",
    "./cpython/Tools/build/stable_abi.py",
    "./cpython/Tools/build/generate_sre_constants.py",
    "./cpython/Tools/build/generate_build_details.py",
    "./cpython/Tools/build/update_file.py",
    "./cpython/Tools/build/deepfreeze.py",
    "./cpython/Tools/build/compute-changes.py",
    "./cpython/Tools/build/check_warnings.py",
    "./cpython/Tools/build/generate_levenshtein_examples.py",
    "./cpython/Tools/build/check_extension_modules.py",
    "./cpython/Tools/build/generate_re_casefix.py",
    "./cpython/Tools/build/verify_ensurepip_wheels.py",
    "./cpython/Tools/build/generate_sbom.py",
    "./cpython/Tools/jit/_llvm.py",
    "./cpython/Tools/jit/_dwarf.py",
    "./cpython/Tools/jit/_stencils.py",
    "./cpython/Tools/jit/build.py",
    "./cpython/Tools/jit/example_trace_dump.py",
    "./cpython/Tools/jit/_optimizers.py",
    "./cpython/Tools/jit/_writer.py",
    "./cpython/Tools/jit/_schema.py",
    "./cpython/Tools/jit/_targets.py",
    "./cpython/Tools/wasm/emscripten/__main__.py",
    "./cpython/Tools/wasm/wasi.py",
    "./cpython/Tools/wasm/wasi/__main__.py",
    "./cpython/Tools/unicode/dawg.py",
    "./cpython/Tools/unicode/comparecodecs.py",
    "./cpython/Tools/unicode/listcodecs.py",
    "./cpython/Tools/unicode/genmap_korean.py",
    "./cpython/Tools/unicode/genwincodec.py",
    "./cpython/Tools/unicode/genmap_support.py",
    "./cpython/Tools/unicode/makeunicodedata.py",
    "./cpython/Tools/unicode/genmap_japanese.py",
    "./cpython/Tools/unicode/gencodec.py",
    "./cpython/Tools/unicode/genmap_schinese.py",
    "./cpython/Tools/unicode/mkstringprep.py",
    "./cpython/Tools/unicode/genmap_tchinese.py",
    "./cpython/Tools/unicode/gencjkcodecs.py",
    "./cpython/Tools/patchcheck/patchcheck.py",
    "./cpython/Tools/patchcheck/reindent.py",
    "./cpython/Tools/patchcheck/untabify.py",
    "./cpython/Tools/importbench/importbench.py",
    "./cpython/Parser/asdl_c.py",
    "./cpython/Parser/asdl.py",
    "./cpython/Platforms/Apple/testbed/__main__.py",
    "./cpython/Platforms/Apple/__main__.py",