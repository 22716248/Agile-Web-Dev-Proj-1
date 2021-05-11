from app import app, db
from app.models import User, Score
@app.shell_context_processor
def a():
    return{'db':db,'User':User,'Score':Score}
