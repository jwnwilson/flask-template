import os

from .default import *

if os.environ["FLASK_ENV"] == "testing":
    from .testing import *

if os.environ["FLASK_ENV"] == "staging":
    from .staging import *

if os.environ["FLASK_ENV"] == "production":
    from .production import *
