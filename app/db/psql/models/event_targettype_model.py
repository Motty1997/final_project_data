from app.db.psql.models import Base
from sqlalchemy import Column, Integer, Table, ForeignKey


event_targettype = Table(
    'event_targettype', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.event_id')),
    Column('targettype_id', Integer, ForeignKey('targettypes.targettype_id'))
)
