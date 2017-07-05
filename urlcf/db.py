"""
Created on Nov 17, 2016

@author: alkorgun
"""

import uuid

import sqlalchemy

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session as ORMSession
from sqlalchemy.sql import text

DB_PATH = "/var/lib/urlcf/urls.db"
CONNECT_STRING = "sqlite:///" + DB_PATH

SCHEMA_URLS = """
CREATE TABLE IF NOT EXISTS `urls` (
    `uid` char(6) NOT NULL,
    `url` text,
    PRIMARY KEY (`uid`)
);
"""

SELECT_URL = """
SELECT url
  FROM urls
 WHERE uid=:uid;
"""
INSERT_URL = """
INSERT INTO urls VALUES (:uid, :url);
"""


class Session(ORMSession):
    """
    Implements "with statement" interface.
    """
    autocommit = True

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self.autocommit:
            pass
        self.close()

    def __call__(self, query, **kwargs):
        """
        # TODO: fill it
        """
        return self.execute(text(query), kwargs)


class UrlcfScope(Session):
    """
    # TODO: fill it
    """
    def get(self, uid):
        cu = self(SELECT_URL, uid=uid)
        cu = cu.fetchone()
        if not cu:
            raise LookupError()
        return cu[0]

    def put(self, url):
        for _ in xrange(3):
            uid = uuid.uuid4().get_hex()[:6]
            try:
                self(INSERT_URL, uid=uid, url=url)
            except SQLAlchemyError:
                continue
            else:
                break
        else:
            raise RuntimeError()
        self.commit()
        return uid


def connect(conn_str=CONNECT_STRING):
    """
    # TODO: fill it
    """
    engine = sqlalchemy.create_engine(conn_str)
    return sessionmaker(
        bind=engine,
        class_=UrlcfScope
    )()


def init(conn_str=CONNECT_STRING):
    """
    # TODO: fill it
    """
    with connect(conn_str) as db:
        db(SCHEMA_URLS)
        db.commit()


def get(uid):
    """
    Gets URL.
    """
    with connect() as db:
        return db.get(uid)


def put(url):
    """
    Saves URL and returns URL's uID.
    """
    with connect() as db:
        return db.put(url)
