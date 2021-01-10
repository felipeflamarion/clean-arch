from core import modules
from core.flask import create_app
import importlib

app = create_app()


for module in modules:
    app_module = importlib.import_module(f"{module}.setup")
    app_module.setup(app)

app.run()
