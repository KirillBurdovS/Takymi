from pydantic import BaseModel, EmailStr
from typing import List

class ParticipantBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    consent: str

class ParticipantCreate(ParticipantBase):
    pass

class Participant(ParticipantBase):
    id: int
    team_lead_id: int

    class Config:
        from_attributes = True

class TeamLeadBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    university: str
    specialization_code: str
    specialization_name: str
    course: int
    consent: str
    mentor_name: str
    mentor_email: EmailStr
    mentor_phone: str
    mentor_consent: str

class TeamLeadCreate(TeamLeadBase):
    pass

class TeamLead(TeamLeadBase):
    id: int
    participants: List[Participant] = []

    class Config:
        from_attributes = True