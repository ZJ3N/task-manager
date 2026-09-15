from sqlmodel import Session, select

from app.database import engine
from app.enums import Role
from app.models import User
from app.security import hash_password


def create_admin():
    username = input("Admin username: ")
    email = input("Admin email: ")
    password = input("Admin password: ")

    with Session(engine) as session:
        existing = session.exec(
            select(User).where(User.username == username)
        ).first()
        if existing:
            print("A user with this username already exists.")
            return

        admin = User(
            username=username,
            email=email,
            hashed_password=hash_password(password),
            role=Role.admin,
            is_active=True,
        )
        session.add(admin)
        session.commit()
        session.refresh(admin)
        print(f"Admin created successfully with id={admin.id}")


if __name__ == "__main__":
    create_admin()