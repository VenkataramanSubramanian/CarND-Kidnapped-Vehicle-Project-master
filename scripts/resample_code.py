w=[0.15,0.38,0.54]
tmp=0
index=random.randrange(0,len(w))

for i in range(len(w)):
	tmp+=random.random()* max(w) *2
	while(tmp>w[index]):
		#print(tmp)
		#print(w[i])
		tmp-=w[index]
		index=(index+1) % len(w)
	print(w[index])

