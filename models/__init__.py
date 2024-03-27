#!/usr/bin/python3
"""
initializw the models package
"""
from models.engine.file_storage import FileStorage

"""
Create a unique FileStorage instance
"""
storage = FileStorage()
storage.reload()
