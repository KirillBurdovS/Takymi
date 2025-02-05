from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.crud.team import create_team_lead, get_team_lead, create_participant, get_participants
from app.schemas.team import TeamLeadCreate, TeamLead, ParticipantCreate, Participant
from app.db.session import get_db
import shutil
from typing import List

router = APIRouter()

@router.post("/team_leads/", response_model=TeamLead)
def register_team_lead(team_lead: TeamLeadCreate, db: Session = Depends(get_db)):
    db_team_lead = create_team_lead(db, team_lead)
    return db_team_lead

@router.post("/team_leads/{team_lead_id}/participants/", response_model=Participant)
def register_participant(team_lead_id: int, participant: ParticipantCreate, db: Session = Depends(get_db)):
    db_team_lead = get_team_lead(db, team_lead_id)
    if not db_team_lead:
        raise HTTPException(status_code=404, detail="Team lead not found")
    db_participant = create_participant(db, participant, team_lead_id)
    return db_participant

@router.get("/team_leads/{team_lead_id}/participants/", response_model=List[Participant])
def list_participants(team_lead_id: int, db: Session = Depends(get_db)):
    db_team_lead = get_team_lead(db, team_lead_id)
    if not db_team_lead:
        raise HTTPException(status_code=404, detail="Team lead not found")
    return get_participants(db, team_lead_id)

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}