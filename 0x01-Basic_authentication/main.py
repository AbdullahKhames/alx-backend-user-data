# #!/usr/bin/env python3
# """ Main 100
# """
# import base64
# from api.v1.auth.basic_auth import BasicAuth
# from models.user import User

# """ Create a user test """
# user_email = "bob100@hbtn.io"
# user_clear_pwd = "H0lberton:School:98!"

# user = User()
# user.email = user_email
# user.password = user_clear_pwd
# print("New user: {}".format(user.id))
# user.save()

# basic_clear = "{}:{}".format(user_email, user_clear_pwd)
# print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

def test(path, excluded_paths):
    for current_path in excluded_paths:
            if path[-1] == '/':
                path = path.split("/")[-2]
            else:
                path = path.split("/")[-1]
            current_path = current_path.split("/")[-1]
            print(current_path[0:-1])
            print(path)
            print(current_path[0:-1] in path)
            if current_path.endswith('*') and current_path[0:-1] in path:
                return False
    return True
path = "/api/v1/users"
excluded_paths = ["/api/v1/stat*", "/api/v1/us*"]
print(test(path, excluded_paths))
print('*'*150)
path2 = "/api/v1/us"
print(test(path2, excluded_paths))
print('*'*150)

path3 = "/api/v1/us/"
print(test(path3, excluded_paths))
print('*'*150)

path4 = "/api/v1/usual"
print(test(path4, excluded_paths))
print('*'*150)
