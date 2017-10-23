from engine import BCO

BCO = BCO()
def iterasi(data,n):
	best = []
	for i in range(n):
		best.append(data)
	best = sorted(best,key=lambda x: x[1])
	s = ""
	for i in best[0][0]:
		s = s+" --> "+str(i)
	s = s+"\nDengan Total Nilai : "+str(best[0][1])
	return s

16
BCO.readData("16.txt")
BCO.setCity(16)
BCO.setBee(1000)
BCO.setNc(2)
print("Kasus 16 kota")
print(iterasi(BCO.main(),10))

# #52
# BCO.readData("52.txt")
# BCO.setCity(52)
# BCO.setBee(1000)
# BCO.setNc(2)
# print("Kasus 52 kota")
# print(iterasi(BCO.main(),10))

# #96
# BCO.readData("96.txt")
# BCO.setCity(96)
# BCO.setBee(1000)
# BCO.setNc(2)
# print("Kasus 96 kota")
# print(iterasi(BCO.main(),100))

#202
# BCO.readData("202.txt")
# BCO.setCity(202)
# BCO.setBee(1000)
# BCO.setNc(8)
# print("Kasus 202 kota")
# print(iterasi(BCO.main(),10))