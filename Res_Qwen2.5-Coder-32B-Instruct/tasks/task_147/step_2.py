print("Found Python files with TODO comments:")
for line in """\
./cpython/Lib/idlelib/idle_test/test_sidebar.py:258:    # TODO: Re-work these tests or remove them from the test suite.
./cpython/Lib/idlelib/idle_test/test_config.py:376:        # TODO: finish.
./cpython/Lib/idlelib/idle_test/test_config.py:766:    # TODO: test that save_all calls usercfg Saves.
./cpython/Lib/idlelib/idle_test/test_config.py:778:        # TODO test for save call.
./cpython/Lib/idlelib/idle_test/htest.py:59:TODO test these modules and classes:
./cpython/Lib/idlelib/idle_test/htest.py:82:# TODO implement ^\; adding '<Control-Key-\\>' to function does not work.
./cpython/Lib/idlelib/idle_test/htest.py:135:# TODO Improve message
./cpython/Lib/idlelib/idle_test/htest.py:144:# TODO edit wrapper
./cpython/Lib/idlelib/idle_test/test_configdialog.py:128:        # TODO Improve checks when add IdleConf.get_font_values.
./cpython/Lib/idlelib/idle_test/test_configdialog.py:1299:#unittest.skip("Nothing here yet TODO")
./cpython/Lib/idlelib/runscript.py:10:TODO: Specify command line arguments in a dialog box.
./cpython/Tools/c-analyzer/c_parser/parser/__init__.py:111:TODO:
./cpython/Tools/cases_generator/plexer.py:33:        # TODO: Return synthetic EOF token instead of None?
./cpython/Tools/cases_generator/lexer.py:115:char = r"\'.\'"  # TODO: escape sequence
./cpython/Tools/cases_generator/lexer.py:379:            # TODO: dedent > 0
./cpython/Tools/ftscalingbench/ftscalingbench.py:246:    # TODO: super() on the same class from multiple threads still doesn't
./cpython/Tools/clinic/libclinic/cli.py:26:# TODO:
./cpython/Tools/clinic/libclinic/block_parser.py:68:    output: Any = None  # TODO: Very dynamic; probably untypeable in its current form?
./cpython/Tools/peg_generator/pegen/sccutils.py:76:        path = path + [node]  # TODO: Make this not quadratic.
./cpython/Tools/peg_generator/pegen/build.py:22:Incomplete = Any  # TODO: install `types-setuptools` and remove this alias
./cpython/Tools/peg_generator/pegen/build.py:326:        gen: ParserGenerator = PythonParserGenerator(grammar, file)  # TODO: skip_actions
./cpython/Tools/peg_generator/pegen/grammar.py:247:        # TODO: Decide whether to use [X] or X? based on type of X
./cpython/Tools/peg_generator/pegen/grammar.py:273:        # TODO: Decide whether to use (X)* or X* based on type of X
./cpython/Tools/peg_generator/pegen/grammar.py:286:        # TODO: Decide whether to use (X)+ or X+ based on type of X
./cpython/Tools/peg_generator/pegen/parser_generator.py:170:        name = f"_tmp_{self.counter}"  # TODO: Pick a nicer name.
./cpython/Tools/peg_generator/pegen/ast_dump.py:6:TODO: Remove the above-described hack.
./cpython/Tools/peg_generator/pegen/testutil.py:94:    TODO: express that using a Protocol.
./cpython/Tools/gdb/libpython.py:1642:    # TODO: repr() puts everything on one line; pformat can be nicer, but
./cpython/Tools/scripts/summarize_stats.py:35:# TODO: Check for parity
./cpython/Tools/build/freeze_modules.py:521:        # TODO: Is this necessary any more?
./cpython/Tools/build/freeze_modules.py:531:        # TODO: Use more obvious markers, e.g.
./cpython/Tools/build/deepfreeze.py:263:        # TODO: bump python version for this script.
./cpython/Tools/build/deepfreeze.py:407:        self.write("// TODO: The above tuple should be a frozenset")
./requests/tests/test_testserver.py: