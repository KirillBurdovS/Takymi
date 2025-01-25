from app.db.session import engine, Base
from app.models.team import TeamLead, Participant

Base.metadata.create_all(bind=engine)