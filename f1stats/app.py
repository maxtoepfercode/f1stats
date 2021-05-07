from f1stats.website import app  # noqa: F401
import db

import os
if os.environ.get('DATABASE_URL'):
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
else:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'