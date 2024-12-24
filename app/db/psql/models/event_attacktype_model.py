from app.db.psql.models import Base
from sqlalchemy import Column, Integer, Table, ForeignKey


event_attacktype = Table(
    'event_attacktype', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.event_id')),
    Column('attacktype_id', Integer, ForeignKey('attacktypes.attacktype_id'))
)
