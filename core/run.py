import importlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import modules
from core.flask import create_app

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/clean_arch_project"
)
Session = sessionmaker(bind=engine)
session = Session()

app = create_app()


for module in modules:
    app_module = importlib.import_module(f"{module}.setup")
    app_module.setup(app, session)

app.run()
