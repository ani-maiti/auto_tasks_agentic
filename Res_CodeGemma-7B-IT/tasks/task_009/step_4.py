filenames = [f for f in os.listdir(".") if f.endswith(".txt")]

for filename in filenames:
    try:
        with open(filename, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        print(f"SHA256 hash of {filename}: {file_hash}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except SyntaxError:
        print(f"Error reading file '{filename}': invalid decimal literal")
```
execution trace:
stdout:
SHA256 hash of file3.txt: 599446907f855b04424c92bf8bf00ff6791883981305950448a0973040140834
SHA256 hash of file2.txt: 40bd0017237b5784380f49c634f009093370152832b98659542028960488b580
SHA256 hash of file1.txt: 91f8051435804794994d9715170be41f47308c6e407bf444f4940bc330947b2e


stderr:

return code: 0