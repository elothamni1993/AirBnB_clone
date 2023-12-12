#!/usr/bin/python3
"""Initialization for the models directory."""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload data from the storage
storage.reload()

