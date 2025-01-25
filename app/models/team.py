from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class TeamLead(Base):
    __tablename__ = 'team_leads'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    university = Column(String)
    specialization_code = Column(String)
    specialization_name = Column(String)
    course = Column(Integer)
    consent = Column(String)
    mentor_name = Column(String)
    mentor_email = Column(String)
    mentor_phone = Column(String)
    mentor_consent = Column(String)
    participants = relationship("Participant", back_populates="team_lead")

class Participant(Base):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    consent = Column(String)
    team_lead_id = Column(Integer, ForeignKey('team_leads.id'))
    team_lead = relationship("TeamLead", back_populates="participants")