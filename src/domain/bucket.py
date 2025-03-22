from typing import List


class BucketFile:
    def __init__(self, id: int, s3_key: str):
        self.id = id
        self.s3_key = s3_key

    def __repr__(self):
        return f"BucketFile(id={self.id}, s3_key='{self.s3_key}')"


class Bucket:
    def __init__(self, id: int, name: str, files: List[BucketFile] | None = None):
        self.id = id
        self.name = name
        self.files = files or []

    def add_file(self, file: BucketFile):
        self.files.append(file)

    def remove_file_by_id(self, file_id: int):
        self.files = [f for f in self.files if f.id != file_id]

    def __repr__(self):
        return f"Bucket(id={self.id}, name='{self.name}', files={self.files})"
    
    