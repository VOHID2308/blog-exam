from database import Base, engine, SessionLocal
from models import User, Post, Comment
import json


Base.metadata.create_all(bind=engine)
print(" Tables created successfully!")


db = SessionLocal()


with open("demo_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


for u in data.get("users", []):
    db.add(User(username=u["username"], email=u["email"]))
db.commit()

for p in data.get("posts", []):
    db.add(Post(title=p["title"], body=p["body"], user_id=p["user_id"]))
db.commit()


for c in data.get("comments", []):
    db.add(Comment(text=c["text"], user_id=c["user_id"], post_id=c["post_id"]))
db.commit()

db.close()
print(" Demo data loaded successfully!")
