import os
import zipfile
import json

def get_file_extensions(file_path):
  """
  Returns a list of file extensions from a given file path.
  """
  with zipfile.ZipFile(file_path, 'r') as zip_file:
    return [file.split('.')[-1] for file in zip_file.namelist()]

def get_archive_extensions(directory):
  """
  Returns a list of file extensions from all compressed archives in a directory.
  """
  extensions = []
  for filename in os.listdir(directory):
    if filename.endswith('.zip'):
      extensions.extend(get_file_extensions(os.path.join(directory, filename)))
  return extensions

def generate_extension_frequencies(extensions):
  """
  Returns a dictionary of file extension frequencies.
  """
  frequencies = {}
  for extension in extensions:
    frequencies[extension] = frequencies.get(extension, 0) + 1
  return frequencies

def save_to_json(data, filename):
  """
  Saves data to a JSON file.
  """
  with open(filename, 'w') as f:
    json.dump(data, f)

# Set the directory containing the compressed archives
directory = '/path/to/archives'

# Get the file extensions from all archives
extensions = get_archive_extensions(directory)

# Generate the extension frequencies
frequencies = generate_extension_frequencies(extensions)

# Save the report to JSON
save_to_json(frequencies, 'extension_frequencies.json')