import urllib

with open('photo.txt','r') as f:
	counter=0
	for line in f:
		urllib.urlretrieve(line,'/home/zeus/pic/'+str(counter)+'.jpg')
		counter=counter+1
		if counter ==5:
			break

