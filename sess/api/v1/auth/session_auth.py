from os import getenv
from api.v1.auth.auth import Auth
from uuid import uuid4

from models.user import User

class SessionAuth(Auth):
    user_id_by_session_id = {}
    
    def create_session(self, user_id: str = None) -> str:
        if user_id is None or type(user_id) is not str:
            return None 
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
                    return None 
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """(overload) that returns a User instance based on a cookie value:"""
        if  request is None:
            return None
        return User.get(self.user_id_for_session_id(request.cookies.get(getenv('SESSION_NAME'))))
