from sqlalchemy.orm import Session
from models import User, Post, Comment

# --- CREATE ---
def create_user(db: Session, username: str, email: str):
    user = db.query(User).filter(User.username == username).first()
    if user:
        return user
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_post(db: Session, user_id: int, title: str, body: str):
    new_post = Post(title=title, body=body, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def create_comment(db: Session, user_id: int, post_id: int, text: str):
    new_comment = Comment(text=text, user_id=user_id, post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

# --- UPDATE ---
def update_post(db: Session, post_id: int, title: str, body: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.title = title
        post.body = body
        db.commit()
        db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None

   
    db.delete(post)
    db.commit()
    return post


# --- QUERY ---
def get_user_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_post_comment_count(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).count()

def get_latest_posts(db: Session, limit: int = 5):
    return db.query(Post).order_by(Post.created_at.desc()).limit(limit).all()

def search_posts_by_title(db: Session, keyword: str):
    return db.query(Post).filter(Post.title.ilike(f"%{keyword}%")).all()

def paginate_posts(db: Session, page: int = 1, per_page: int = 5):
    offset = (page - 1) * per_page
    return db.query(Post).offset(offset).limit(per_page).all()
