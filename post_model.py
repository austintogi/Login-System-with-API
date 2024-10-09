from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        _userId = int(obj.get("userId"))
        _id = int(obj.get("id"))
        _title = str(obj.get("title"))
        _body = str(obj.get("body"))
        return Post(_userId, _id, _title, _body)