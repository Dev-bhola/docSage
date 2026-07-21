import uuid
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import Base
from .user import utcnow

class MessageCitation(Base):
    __tablename__ = 'message_citations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message_id = Column(UUID(as_uuid=True), ForeignKey('chat_messages.id'), nullable=False)
    chunk_id = Column(UUID(as_uuid=True), ForeignKey('document_chunks.id'), nullable=False)
    created_at = Column(DateTime, default=utcnow)
    
    message = relationship("ChatMessage", back_populates="citations")
    chunk = relationship("DocumentChunk")
