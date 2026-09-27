from sqlalchemy import create_engine, text
from sqlalchemy.future import engine
from config import settings

Engine = create_engine(settings.databae_url())

with Engine.connect() as conn:
    conn.execute(text("SELECT 1"))