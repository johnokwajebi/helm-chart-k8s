from bigfastapi.models.user_models import User
from bigfastapi.db.database import get_db
import sqlalchemy.orm as orm
import fastapi as fastapi
async def query_users(
    db: orm.Session = fastapi.Depends(get_db),
):
    users = db.query(User).filter(User.is_deleted == False).all()
    return users

    