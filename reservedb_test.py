import json

def reserve_copy():
	# init reserve copy of db, very damn and temporary
	with open('db_snapshot.txt') as f:
		read_data = f.read()
	f.close()

	#print(read_data)
	users = json.loads(read_data)
	#print(users)
	for user in users:
		#print("user = " + str(user))
		if user['fob'] == '0013329927':
			print(user['name'])

reserve_copy()