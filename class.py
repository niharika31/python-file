class Avenger:
	avengerscount = 0

	def __init__(self,name,power):  #self is an object but name and power is parameter
		Avenger.avengerscount += 1    # belongs to class as self is not used
		self.name = name              # belong to obj as self is used
		self.power = power

	def howmany():
		print("Total avengers %d" % Avenger.avengerscount)

	def getname(self):
		print("Avenger Name: " +self.name+ "  have power"+ self.power)

#ironman = Avenger()
hulk = Avenger("Hulk","Angryness") #hulk is name nd angryness is power 
print(hulk.name)
print(hulk.power)
print("Avengerscount: ", Avenger.avengerscount)
print("%%%%%%%%%%%%%%%%")
ironman = Avenger("ironman","suite")
print(ironman.name)
print(ironman.power)
print("Avengerscount: ", Avenger.avengerscount)

Avenger.howmany()
hulk.getname()
print(ironman.name)
print(ironman.power)
print("###############")
print("Avengerscount = ",Avenger.avengerscount)
hulk.size =  "very big"
print(hulk.size)  
del hulk.power
#print(hulk.power)
print(hulk.name)
print(getattr(hulk,"name") )              # return value
print(setattr(hulk,"name","badahulk"))





