from abc import ABC, abstractmethod

"""
To enforce abstraction in Python, we use the abc (Abstract Base Classes) module. This prevents someone from creating an instance of the "Idea" and forces them to implement the "Action."
"""

class CloudStorage(ABC):
    @abstractmethod
    def upload(self, file_name):
        pass

class S3Storage(CloudStorage):
    def upload(self, file_name):
        return f"Uploading {file_name} to AWS S3 bucket..."

class GoogleDriveStorage(CloudStorage):
    def upload(self, file_name):
        return f"Uploading {file_name} to Google Drive..."

# storage = CloudStorage()  # This would raise a TypeError!
