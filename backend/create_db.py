# create_db.py

from app import app, db

# Ensure app is properly configured
app.app_context().push()

# Create all tables
db.create_all()



