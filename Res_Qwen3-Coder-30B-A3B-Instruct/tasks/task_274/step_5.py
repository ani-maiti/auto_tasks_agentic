# Check the generated CSV file
with open('image_dimensions.csv', 'r') as f:
    content = f.read()
    print(content)