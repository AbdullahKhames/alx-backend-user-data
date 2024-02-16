from datetime import datetime, timedelta
from os import getenv
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        duration = 0
        try:
            duration = int(getenv('SESSION_DURATION'))
        except Exception as ex:
            pass
        self.session_duration = duration
            
    def create_session(self, user_id=None):
        session_id = super().create_session(user_id=user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {'user_id': user_id,
                                                  'created_at': datetime.now()}
        return session_id

    def user_id_for_session_id(self, session_id=None):
        if session_id is None:
                    return None
        if session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']
        if 'created_at' not in self.user_id_by_session_id[session_id]:
            return None
        max_duration = self.user_id_by_session_id[session_id]['created_at'] + timedelta(seconds=self.session_duration)
        print(max_duration)
        if datetime.now() > max_duration:
            return None
        return self.user_id_by_session_id[session_id]['user_id']
