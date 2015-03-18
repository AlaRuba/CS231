import shutil

lines = [line.strip() for line in open('./train.txt')]
for line in lines:
	filename = line.split("/")[-1]
	filename = filename.split()[0]
	print filename
	line = line.split()[0]
	dest = '/Users/alaruba/CS231/Pictures/images/train/' +filename
	with open(line, 'rb') as fsrc:
		with open(dest, 'wb') as fdest:
			shutil.copyfileobj(fsrc, fdest)
dest = '/Users/alaruba/CS231/Pictures/images/val/'
lines = [line.strip() for line in open('./test.txt')]
for line in lines:
	filename = line.split("/")[-1]
	filename = filename.split()[0]
	line = line.split()[0]
	dest = '/Users/alaruba/CS231/Pictures/images/val/' +filename
	with open(line, 'rb') as fsrc:
		with open(dest, 'wb') as fdest:
			shutil.copyfileobj(fsrc, fdest)