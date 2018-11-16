from app import db
from app.models import User, Post

def cleanAll():
	users = User.query.all()
	deletedUsers = 0
	deletedPosts = 0
	for u in users:
		db.session.delete(u)
		deletedUsers = deletedUsers + 1

	posts = Post.query.all()
	for p in posts:
		db.session.delete(p)
		deletedPosts = deletedPosts + 1

	db.session.commit()
	print('\ndeleted users={} posts={}'.format(deletedUsers, deletedPosts))

cleanAll()

u = User(username='john', email='john@example.com')
db.session.add(u)
u = User(username='susan', email='susan@example.com')
db.session.add(u)
db.session.commit()

print('\nusers')
users = User.query.all()
for u in users:
	print(u.id, u.username)

u = users[0]
u = User.query.get(u.id)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()

posts = u.posts.all()
print('\nall posts')
print(posts)

u = users[0]
print('\nposts of user ' + u.username)
print(u.posts.all())

u = users[1]
print('\nposts of user ' + u.username)
print(u.posts.all())

print('\nall posts')
posts = Post.query.all()
for p in posts:
	print(p.id, p.author.username, p.body)

print('\nusers')
users = User.query.order_by(User.username.desc()).all()
for u in users:
	print(u.id, u.username)

cleanAll()