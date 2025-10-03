from database import SessionLocal
import crud

db = SessionLocal()
print("Starting full CRUD + Query test...")

user = crud.create_user(db, "test_user", "test@example.com")
print(f" Created User: {user.id} {user.username} {user.email}")

post1 = crud.create_post(db, user.id, "Test Post 1", "Bu test uchun yozilgan birinchi post.")
post2 = crud.create_post(db, user.id, "Test Post 2", "Bu test uchun yozilgan ikkinchi post.")
print(" Created Posts:")
print(f"  - {post1.id}: {post1.title}")
print(f"  - {post2.id}: {post2.title}")

comment1 = crud.create_comment(db, user.id, post1.id, "Birinchi postga comment")
comment2 = crud.create_comment(db, user.id, post2.id, "Ikkinchi postga comment")
print(" Created Comments:")
print(f"  - {comment1.id}: {comment1.text}")
print(f"  - {comment2.id}: {comment2.text}")

updated_post = crud.update_post(db, post1.id, "Updated Post 1", "Yangilangan post body")
print(f" Updated Post: {updated_post.id} {updated_post.title}")

deleted_post = crud.delete_post(db, post2.id)
print(f" Deleted Post: {deleted_post.id} {deleted_post.title}")

user_posts = crud.get_user_posts(db, user.id)
print("\n User posts from DB:")
for p in user_posts:
    print(f"  - {p.id}: {p.title}")

comment_count = crud.get_post_comment_count(db, post1.id)
print(f"\n Comment count for post {post1.id}: {comment_count}")

latest_posts = crud.get_latest_posts(db)
print("\n Latest posts:")
for p in latest_posts:
    print(f"  - {p.id}: {p.title}")

search_result = crud.search_posts_by_title(db, "Updated")
print("\n Search posts with 'Updated':")
for p in search_result:
    print(f"  - {p.id}: {p.title}")

paginated_posts = crud.paginate_posts(db, page=1, per_page=2)
print("\n Paginated posts (page 1, 2 per page):")
for p in paginated_posts:
    print(f"  - {p.id}: {p.title}")

print("\n Full CRUD + Query test finished successfully!")
