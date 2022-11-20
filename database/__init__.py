from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:admin@127.0.0.1/ainsys-telegram')
Session = sessionmaker(bind=engine)
session = Session()

