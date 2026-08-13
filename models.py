from sqlalchemy import Column, Integer, String
from database import Base

class FileTransaction(Base):
    __tablename__ = "file_transactions"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_type = Column(String)
    status = Column(String)
    result_summary = Column(String)
