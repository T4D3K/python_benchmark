import os

import falcon
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from falcon_frm.models import Base, User
db_url = os.environ.get('DB_URL', 'postgresql+psycopg2://postgres:postgres@db/postgres')
pool_size = int(os.environ.get('DB_POOL_SIZE', 20))
engine = sa.engine.create_engine(db_url, echo=False, pool_size=pool_size)
Base.metadata.create_all(engine)
SessionMaker = sessionmaker(engine)


class HelloResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "hello world"


class UserResource(object):
    def on_post(self, req, resp):
        session = SessionMaker()
        data = req.media
        user = User(name=data['name'])
        session.add(user)
        session.commit()
        resp.body = falcon.json.dumps({'id': user.id})


app = falcon.API()

things = HelloResource()
users = UserResource()
app.add_route('/hello', things)
app.add_route('/users', users)
