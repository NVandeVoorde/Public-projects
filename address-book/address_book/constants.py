import os

DATABASE_URL = os.path.join(
    # Absolute path
    os.path.split(os.path.dirname(__file__))[0],
    # Location database in project
    "data\\adbook.db"
)