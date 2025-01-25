from sqlalchemy.orm import Session
from app.models.team import TeamLead, Participant
from app.schemas.team import TeamLeadCreate, ParticipantCreate

def create_team_lead(db: Session, team_lead: TeamLeadCreate):
    db_team_lead = TeamLead(
        name=team_lead.name,
        email=team_lead.email,
        phone=team_lead.phone,
        university=team_lead.university,
        specialization_code=team_lead.specialization_code,
        specialization_name=team_lead.specialization_name,
        course=team_lead.course,
        consent=team_lead.consent,
        mentor_name=team_lead.mentor_name,
        mentor_email=team_lead.mentor_email,
        mentor_phone=team_lead.mentor_phone,
        mentor_consent=team_lead.mentor_consent
    )
    db.add(db_team_lead)
    db.commit()
    db.refresh(db_team_lead)
    return db_team_lead

def get_team_lead(db: Session, team_lead_id: int):
    return db.query(TeamLead).filter(TeamLead.id == team_lead_id).first()

def create_participant(db: Session, participant: ParticipantCreate, team_lead_id: int):
    db_participant = Participant(
        name=participant.name,
        email=participant.email,
        phone=participant.phone,
        consent=participant.consent,
        team_lead_id=team_lead_id
    )
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

def get_participants(db: Session, team_lead_id: int):
    return db.query(Participant).filter(Participant.team_lead_id == team_lead_id).all()