from app import app, db

with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("Database tables created successfully!")
