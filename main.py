from database import Base, engine, SessionLocal
from models import User, Post, Comment
import json

# Jadvalni yaratish
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")

# Sessiyani ochish
db = SessionLocal()

# JSON fayldan ma’lumot o‘qish
with open("demo_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Users
for u in data.get("users", []):
    db.add(User(username=u["username"], email=u["email"]))
db.commit()

# Posts
for p in data.get("posts", []):
    db.add(Post(title=p["title"], body=p["body"], user_id=p["user_id"]))
db.commit()

# Comments
for c in data.get("comments", []):
    db.add(Comment(text=c["text"], user_id=c["user_id"], post_id=c["post_id"]))
db.commit()

db.close()
print("✅ Demo data loaded successfully!")
