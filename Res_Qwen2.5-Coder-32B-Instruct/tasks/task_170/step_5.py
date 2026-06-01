import re

def extract_ipv4_addresses(file_paths):
    ipv4_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    ipv4_addresses = set()

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                addresses = ipv4_pattern.findall(content)
                ipv4_addresses.update(addresses)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    return ipv4_addresses

file_paths = [
    "st_doctest4.txt",
    "./cpython/Lib/test/test_doctest/test_doctest_skip.txt",
    "./cpython/Lib/test/test_doctest/test_doctest3.txt",
    "./cpython/Lib/test/test_doctest/test_doctest_errors.txt",
    "./cpython/Lib/test/translationdata/optparse/msgids.txt",
    "./cpython/Lib/test/translationdata/argparse/msgids.txt",
    "./cpython/Lib/test/translationdata/getopt/msgids.txt",
    "./cpython/Lib/test/test_email/data/msg_12a.txt",
    "./cpython/Lib/test/test_email/data/msg_25.txt",
    "./cpython/Lib/test/test_email/data/msg_26.txt",
    "./cpython/Lib/test/test_email/data/msg_31.txt",
    "./cpython/Lib/test/test_email/data/msg_11.txt",
    "./cpython/Lib/test/test_email/data/msg_23.txt",
    "./cpython/Lib/test/test_email/data/msg_15.txt",
    "./cpython/Lib/test/test_email/data/msg_35.txt",
    "./cpython/Lib/test/test_email/data/msg_07.txt",
    "./cpython/Lib/test/test_email/data/msg_22.txt",
    "./cpython/Lib/test/test_email/data/msg_43.txt",
    "./cpython/Lib/test/test_email/data/msg_20.txt",
    "./cpython/Lib/test/test_email/data/msg_06.txt",
    "./cpython/Lib/test/test_email/data/msg_16.txt",
    "./cpython/Lib/test/test_email/data/msg_10.txt",
    "./cpython/Lib/test/test_email/data/msg_44.txt",
    "./cpython/Lib/test/test_email/data/msg_03.txt",
    "./cpython/Lib/test/test_email/data/msg_32.txt",
    "./cpython/Lib/test/test_email/data/msg_09.txt",
    "./cpython/Lib/test/test_email/data/msg_17.txt",
    "./cpython/Lib/test/test_email/data/msg_18.txt",
    "./cpython/Lib/test/test_email/data/msg_04.txt",
    "./cpython/Lib/test/test_email/data/msg_02.txt",
    "./cpython/Lib/test/test_email/data/msg_33.txt",
    "./cpython/Lib/test/test_email/data/msg_08.txt",
    "./cpython/Lib/test/test_email/data/msg_47.txt",
    "./cpython/Lib/test/test_email/data/msg_38.txt",
    "./cpython/Lib/test/test_email/data/msg_29.txt",
    "./cpython/Lib/test/test_email/data/msg_36.txt",
    "./cpython/Lib/test/test_email/data/msg_34.txt",
    "./cpython/Lib/test/test_email/data/msg_30.txt",
    "./cpython/Lib/test/test_email/data/msg_14.txt",
    "./cpython/Lib/test/test_email/data/msg_37.txt",
    "./cpython/Lib/test/test_email/data/msg_21.txt",
    "./cpython/Lib/test/test_email/data/msg_40.txt",
    "./cpython/Lib/test/test_email/data/msg_42.txt",
    "./cpython/Lib/test/test_email/data/msg_28.txt",
    "./cpython/Lib/test/test_email/data/msg_27.txt",
    "./cpython/Lib/test/test_email/data/msg_39.txt",
    "./cpython/Lib/test/test_email/data/msg_24.txt",
    "./cpython/Lib/test/test_email/data/msg_05.txt",
    "./cpython/Lib/test/test_email/data/msg_19.txt",
    "./cpython/Lib/test/test_email/data/msg_41.txt",
    "./cpython/Lib/test/test_email/data/msg_46.txt",
    "./cpython/Lib/test/test_email/data/msg_45.txt",
    "./cpython/Lib/test/test_email/data/msg_12.txt",
    "./cpython/Lib/test/test_email/data/msg_13.txt",
    "./cpython/Lib/test/test_email/data/msg_01.txt",
    "./cpython/Lib/test/NormalizationTest-3.2.0.txt",
    "./