import uuid
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from .base import Base
from .user import utcnow

class SourceDocument(Base):
    __tablename__ = 'source_documents'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    file_name = Column(String, nullable=False)
    source_url = Column(String, nullable=True)
    filing_metadata = Column(JSONB, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=utcnow)
    
    chunks = relationship("DocumentChunk", back_populates="document")
