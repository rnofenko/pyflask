https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
python -m venv venv
venv\Scripts\activate
pip install flask
pip install python-dotenv
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
SET FLASK_APP=microblog.py
flask run
flask shell



venv\Scripts\activate
flask run


flask db init
flask db migrate -m "users table"
flask db migrate -m "posts table"
flask db upgrade