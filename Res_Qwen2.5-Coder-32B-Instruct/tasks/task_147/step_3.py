print("Found Python files with TODO comments:")
todo_files = [
    "./cpython/Lib/idlelib/idle_test/test_sidebar.py",
    "./cpython/Lib/idlelib/idle_test/test_config.py",
    "./cpython/Lib/idlelib/idle_test/htest.py",
    "./cpython/Lib/idlelib/idle_test/test_configdialog.py",
    "./cpython/Lib/idlelib/runscript.py",
    "./cpython/Tools/c-analyzer/c_parser/parser/__init__.py",
    "./cpython/Tools/cases_generator/plexer.py",
    "./cpython/Tools/cases_generator/lexer.py",
    "./cpython/Tools/ftscalingbench/ftscalingbench.py",
    "./cpython/Tools/clinic/libclinic/cli.py",
    "./cpython/Tools/clinic/libclinic/block_parser.py",
    "./cpython/Tools/peg_generator/pegen/sccutils.py",
    "./cpython/Tools/peg_generator/pegen/build.py",
    "./cpython/Tools/peg_generator/pegen/grammar.py",
    "./cpython/Tools/peg_generator/pegen/parser_generator.py",
    "./cpython/Tools/peg_generator/pegen/ast_dump.py",
    "./cpython/Tools/peg_generator/pegen/testutil.py",
    "./cpython/Tools/gdb/libpython.py",
    "./cpython/Tools/scripts/summarize_stats.py",
    "./cpython/Tools/build/freeze_modules.py",
    "./cpython/Tools/build/deepfreeze.py",
    "./requests/tests/test_testserver.py",
    "./requests/src/requests/hooks.py",
    "./requests/src/requests/adapters.py",
    "./requests/src/requests/models.py",
    "./requests/src/requests/_types.py"
]

for file in todo_files:
    print(file)