import random
import numpy as np

class BCO:
	def __init__(self):
		self.bee = []
		self.hive = []
		self.totalCity = 0
		self.totalBee = 0
		self.nc = 0
		self.data = []
		self.ueclid = []

	def readData(self,s):	
		file = open(s,"r")
		for i in file:
			self.data.append(tuple(float(x)for x in i.split(" ")))
		file.close()

	def setCity(self,totalCity):
		self.bee = [0 for i in range(totalCity)]
		self.totalCity = totalCity

	def setBee(self,totalBee):
		self.hive = [self.bee for i in range(totalBee)]
		self.hive = np.array(self.hive)
		self.totalBee = totalBee
	
	def setNc(self,nc):
		self.nc = nc

	def acakCity(self,tmp,tc):
		status = True
		n = 0
		while status:
			n = random.randint(1,tc)
			if n not in tmp :
				status = False
		return n

	def forwardPass(self):
		for i in self.hive :
			k = 0
			for j in range(self.totalCity):
				if (i[j] == 0 and k < self.nc):
					i[j] = self.acakCity(i,self.totalCity)
					k += 1

	def backwardPass(self):
		acak = [0 for i in range(self.totalBee-1)]
		for i in acak:
			i = self.acakCity(acak,self.totalBee)
		tmp = self.hive
		for i in self.hive:
			for j in acak:
				tmp[j] = i
		self.hive = tmp

	def searchEuclid(self):
		self.ueclid = []
		for i in self.hive:
			d = 0
			for j in range(self.totalCity-1):
				city1 = []
				city2 = []
				if i[j+1] != 0:
					for k in self.data:
					    if i[j] == int(k[0]):
					        city1 = k
					    if i[j+1] == int(k[0]):
					        city2 = k
					d+= np.sqrt((city2[1] - city1[1])**2 + (city2[2] - city1[2])**2 ) 
			self.ueclid.append([i,d])
		self.ueclid = sorted(self.ueclid,key=lambda x: x[1])

	def printRoute(self):
		self.searchEuclid()
		s = ""
		for i in self.ueclid[0][0]:
			s = s+" --> "+str(i)
		s = s+"\nDengan Total Nilai : "+str(self.ueclid[0][1])
		return s


	def main(self):
		for i in self.hive:
			for j in range(self.totalCity-1):
				if i[j+1] == 0:
					self.forwardPass()
					self.backwardPass()
		self.searchEuclid()
		return self.ueclid[0]