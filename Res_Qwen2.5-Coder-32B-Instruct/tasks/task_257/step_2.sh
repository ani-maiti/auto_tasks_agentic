echo "Checking if imagehash library is installed..."
pip show imagehash > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "imagehash library not found. Installing..."
    pip install imagehash
else
    echo "imagehash library already installed."
fi