def readdata(filename):

	photos = []
	uniquetags = []
	with open(filename, 'r') as fin:
	
		N = int(fin.readline()) # number of photos
		tagnum = 0

		for j in range(N):
			photo = []

			line = fin.readline().split()
			photo.append(line[0])
			photo.append(int(line[1]))
			tags = []
			for i in range(photo[1]):
				tag = line[2+i]
				if tag not in uniquetags:
					uniquetags.append(tag)
					tags.append(tagnum)
					tagnum = tagnum + 1
				else:
					tags.append(tagnum)
			
			photo.append(sorted(tags))
			
			photo.append(j)
			photos.append(photo)

	
	return photos

def score(photo1,photo2):
	tags1 = photo1[2]
	tags2 = photo2[2]
	common = list(set(tags1).intersection(tags2))
	not_common1 = list(set(tags1) - set(common))
	not_common2 = list(set(tags2) - set(common))
	score = min(len(common),len(not_common2),len(not_common1))
	return score

def common(photo1,photo2):
	tags1 = photo1[2]
	tags2 = photo2[2]
	common = list(set(tags1).intersection(tags2))
	return len(common)

def printData(slideShow):
	print (len(slideShow))
	for i in slideShow:
		if i[0]=='V':
			for j in i[3]:
				print(j,' ', end='')
			print()
		else:
			print(i[3])

# def uniteVertical(photos):
#     vertical = [p for p in photos if p[0] == 'V']
	
#     united = []
	
#     for i in range(len(vertical)):
#         min = 9999
#         id = 0
#         for j in range(len(vertical)):
#             if vertical[j] != vertical[i]:
#                 score = common(vertical[i],vertical[j])
#                 if score < min :
#                     min = score
#                     id = j


def uniteVertical(photos):
	Vertical = [p for p in photos if p[0] == 'V']
	Vertical = sorted(Vertical, key=lambda k: k[1])
	united = []
	used = []
	counter = 0

	for i in range(len(Vertical)):
		# print('!!!!')
		# min = 999999
		# min_p = []
		# if Vertical[i][3] in used:
		# 	continue
		# elif i < len(Vertical) - i:
		# 	break
		last = len(Vertical)-(i+1)
		if i - (last) == 0:
			break
		elif Vertical[last][3] in used or Vertical[i][3] in used:
			continue
		
		# for p in range(i+1,len(Vertical)):
		# 	if common(Vertical[i],Vertical[p]) < min and Vertical[p][3] not in used:
		# 		min_p = Vertical[p]
		# 		min = common(Vertical[i],Vertical[p])
		# 		count = 0
		# 	else:
		# 		count +=1
			
		min_p = Vertical[last]
		if min != 999999:	
			used.append(min_p[3])
			u = unique(Vertical[i],min_p)
			l =[]
			l.append('V')
			l.append(len(u))
			l.append(u)
			l.append([Vertical[i][3],min_p[3]])
			united.append(l)
	
	return united

def unique(photo1,photo2):
	tags1 = photo1[2]
	tags2 = photo2[2]

	tags1set = set(tags1)
	tags2set = set(tags2)
	
	common = list(tags1set.intersection(tags2))
	commonset = set(common)
	
	not_common1 = list(tags1set - commonset)
	not_common2 = list(tags2set - commonset)
	
	return common+not_common2+not_common1
		



if __name__ == "__main__":
	from random import randint
	
	photos = readdata('c_memorable_moments.txt')
	photosH = [p for p in photos if p[0] == 'H']
	photosH = sorted(photosH, key=lambda k: k[1], reverse=True)
	
	photosV = uniteVertical(photos)
	photosV = sorted(photosV, key=lambda k: k[1], reverse=True)
	
	
	photos = photosH + photosV
	photos = sorted(photos, key=lambda k: k[1], reverse=True)

	#print(photosH)
	
	slideshow = [photos[0]]
	del(photos[0])


	count = 0

	for p in slideshow:
		half = p[1]/2
		max_score = 0
		p_id = 0
		count = 0
		if photos:
			for i in range(len(photos)):
				
				if count > 1000000 or max_score == half:
					break
				ind_score = score(p,photos[i])
				if ind_score > max_score:
					max_score = ind_score
					p_id = i
				else:
					count += 1
			
			slideshow.append(photos[p_id])
			del(photos[p_id])
			
	printData(slideshow)
