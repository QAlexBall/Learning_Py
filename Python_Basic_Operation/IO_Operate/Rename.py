import os
path = 'H:/Image'
i = 0
for file in os.listdir(path):
	newname = str(i) + '.jpg'
	os.rename(os.path.join(path, file), os.path.join(path, newname))
	i = i + 1
	print(newname, 'is ok!')
