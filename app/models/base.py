from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.inspection import inspect

class Base(DeclarativeBase):
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in inspect(self.__class__).columns
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)