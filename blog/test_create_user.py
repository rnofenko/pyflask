from app import db
from app.models import User, Post

u = User(username='ro', email='ro@gmail.com')
u.set_password('1')
db.session.add(u)
db.session.commit()