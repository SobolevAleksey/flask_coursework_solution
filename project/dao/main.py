from project.dao.base import BaseDAO
from project.models import Genre


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

 # Разбить на разные файлы    
class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

class UsersDAO(BaseDAO[User]):
    __model__ = User
    
    def __init__(self, session):
        self.session = session
    # Дублируется
    def get_one(self, bid):
        return self.session.query(User).get(uid)
    # Дублируется
    def get_all(self):
        return self.session.query(User).all()
    
    def get_by_email(self, email):
        return self.session.query(User).filter(User.email = email).first()

    def create(self, user_d):
        try:
            user = User(**user_d)
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        if user_d.get("email"):
            user.email = user_d.get("email")
        if user_d.get("password"):
            user.email = user_d.get("password")
        if user_d.get("name"):
            user.email = user_d.get("name")
        if user_d.get("surname"):
            user.email = user_d.get("surname")
        try: 
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists
     
    def update_password(self, email, new_password):
        user = self.get_by_email(email)
        user.password = generate_password_hash(new_password)
        
        self.session.add(user)
        self.session.commit()
        
        
        

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_by_filter(self, status: Optional[str], page: Optional[int]=None) -> list[Movie]:
        stmt: BaseQuery = self._db_session_query(self.__model__)
            if status == "new":
                status = stmt.order_by(desc(self.__model__.year))
            else:
                stmt = stmt.order_by(self.__model__.year)
            if page:
                try:
                    return stmt.paginate(page, self._items_per_page).items
                except NotFound:
                    return []
            return stmt.all()
        



