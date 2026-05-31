# Step 3: Install exiftool if it's not already installed
sudo apt-get update
sudo apt-get install -y libimage-exiftool-perl
```

This step installs `exiftool` using `apt-get`, which should allow us to extract metadata from the images in the next step.