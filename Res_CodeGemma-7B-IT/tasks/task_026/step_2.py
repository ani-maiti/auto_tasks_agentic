for filename in os.listdir("."):
    if not filename.isascii():
        os.remove(filename)