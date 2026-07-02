import sys
import os

# Add the current directory to sys.path so we can import from the app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from db.database import SessionLocal, engine, Base
from schemas.user import UserCreate
from services.user_service import register_user
from db.models import User

# Ensure tables are created
Base.metadata.create_all(bind=engine)

def create_super_admin():
    db = SessionLocal()
    
    # Check if admin exists
    admin = db.query(User).filter(User.email == "admin@example.com").first()
    if admin:
        print("Admin user already exists.")
        return
        
    admin_data = UserCreate(
        name="Super Admin",
        email="admin@example.com",
        password="admin" # Using a simple password for testing, could be admin123
    )
    
    try:
        register_user(db, admin_data)
        print("Super admin created successfully: admin@example.com / admin")
    except Exception as e:
        print(f"Error creating admin: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_super_admin()
