import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB, TSVECTOR
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from .base import Base
from .user import utcnow

class DocumentChunk(Base):
    __tablename__ = 'document_chunks'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(UUID(as_uuid=True), ForeignKey('source_documents.id'), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    page = Column(String, nullable=True)
    section = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(1536))
    search_vector = Column(TSVECTOR)
    token_count = Column(Integer, nullable=False)
    chunk_metadata = Column(JSONB, nullable=False)
    created_at = Column(DateTime, default=utcnow)
    
    document = relationship("SourceDocument", back_populates="chunks")
