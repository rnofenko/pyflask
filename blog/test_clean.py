from app import db
from app.models import User, Post

users = User.query.all()
for u in users:
	db.session.delete(u)

posts = Post.query.all()
for p in posts:
	db.session.delete(p)

db.session.commit()