import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from .base import Base
from .user import utcnow

class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    thread_id = Column(UUID(as_uuid=True), ForeignKey('chat_threads.id'), nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    ai_sdk_json = Column(JSONB, nullable=True)
    created_at = Column(DateTime, default=utcnow)
    
    thread = relationship("ChatThread", back_populates="messages")
    citations = relationship("MessageCitation", back_populates="message")
