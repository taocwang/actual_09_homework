import json

def get_user():
	with open('userportal.txt','rb') as f:
		cxt = f.read()
		return json.loads(cxt)


def validate_login(username,password):
	users = get_user()

	for user in users:

		if user.get('username') == username and user.get('password') == password:
			return True

	return False


def add_user(user_list):
	with open('userportal.txt','wb') as wf:
		wf.write(user_list)

