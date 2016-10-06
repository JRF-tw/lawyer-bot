import os
import peewee as p

DATABASE = p.SqliteDatabase(os.environ.get('DBPATH', 'bot.db'))

class User(p.Model):
    user_id = p.CharField(max_length=64, unique=True)
    is_admin = p.BooleanField(default=False)
    class Meta:
        database = DATABASE

class Match(p.Model):
    keyword = p.CharField(max_length=32)
    answer = p.TextField()
    class Meta:
        database = DATABASE

def create_tables():
    User.create_table(fail_silently=True)
    Match.create_table(fail_silently=True)

# Make database available immediately
DATABASE.connect()
create_tables()
