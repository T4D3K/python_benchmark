from gino.ext.starlette import Gino
from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret
config = Config(".env")

DB_DRIVER = config("DB_DRIVER", default="postgresql")
DB_HOST = config("DB_HOST", default='db')
DB_PORT = config("DB_PORT", cast=int, default=5432)
DB_USER = config("DB_USER", default='postgres')
DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default='postgres')
DB_DATABASE = config("DB_DATABASE", default='postgres')
DB_DSN = config(
    "DB_DSN",
    cast=make_url,
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),
)
DB_POOL_MIN_SIZE = config("DB_POOL_MIN_SIZE", cast=int, default=1)
DB_POOL_MAX_SIZE = config("DB_POOL_MAX_SIZE", cast=int, default=16)
DB_ECHO = config("DB_ECHO", cast=bool, default=False)
DB_SSL = config("DB_SSL", default=None)
DB_USE_CONNECTION_FOR_REQUEST = config(
    "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=True
)
DB_RETRY_LIMIT = config("DB_RETRY_LIMIT", cast=int, default=1)
DB_RETRY_INTERVAL = config("DB_RETRY_INTERVAL", cast=int, default=1)


db = Gino(
    dsn=DB_DSN,
    pool_min_size=DB_POOL_MIN_SIZE,
    pool_max_size=DB_POOL_MAX_SIZE,
    echo=DB_ECHO,
    ssl=DB_SSL,
    use_connection_for_request=DB_USE_CONNECTION_FOR_REQUEST,
    retry_limit=DB_RETRY_LIMIT,
    retry_interval=DB_RETRY_INTERVAL,
)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="unnamed")
