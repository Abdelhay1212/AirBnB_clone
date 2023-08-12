# /usr/bin/python3
"""
This script initializes a FileStorage object and reloads data from storage.

It serves as an entry point for interacting with the file storage engine.
"""

from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class
storage = FileStorage()

# Reload data from storage
storage.reload()
