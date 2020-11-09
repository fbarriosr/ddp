from source.myPrint import *
import subprocess
import os

class Project:
	def __init__(self, name):
		aux 	= name[::-1]
		t1  	= aux.find('_')
		t1 	= len(aux)-1 -t1
		self.name = name[0:t1]
		self.N 	= name[t1+1]
		self.files = []
		self.p = 0
		self.q = 0
		self.status = False
		self.statusDen = False
		self.errorMsg = "No message"

	def getNamePosFile(self):
		aux = self.name +'_'+ self.N +'+'+ self.p +'.fchk'
		if aux in self.files:
			return aux
		else:
			return "False"

	def getNameNegFile(self):
		aux = self.name +'_'+ self.N +'-'+self.q +'.fchk'
		if aux in self.files:
			return aux
		else:
			return "False"

	def getNameMainFile(self):
		aux = self.name +'_'+ self.N +'.fchk'
		if aux in self.files:
			return aux
		else:
			return "False"
			
	def getNameDenFile(self):
		aux = self.name +'_'+self.N + '+' +self.p +'_den.cub'
		if aux in self.files:
			return aux
		else:
			return "False"

	def getP(self):
		return self.p

	def getQ(self):
		return self.q
		
	def getN(self):
		return self.N

	def getName(self):
		return self.name
		
	def viewName(self):
		print('Name:',self.name)

	def view(self):
		printElement('-',40)
		print('Name:',self.name)
		print('N:',self.N)
		print('p:',self.p)
		print('q:',self.q)
		print('files:',self.files)
		print('status:',self.status)
		print('statusDen:',self.statusDen)
		print('error:',self.errorMsg)
		printElement('-',40)
		return

	def set_P(self,name):
		aux = name[::-1]
		t1 = aux.find('+')
		t1 = len(aux)-1 - t1   # arreglo el puntero
		t2 = name.find('.')
		self.p = name[t1+1:t2]
		return

	def set_Q(self,name):
		aux = name[::-1]
		t1 = aux.find('-')
		t1 = len(aux)-1 -t1    #arreglo el puntero
		t2 = name.find('.')
		self.q = name[t1+1:t2]
		return

	def loadingFiles(self, allFilesNames):
		self.files =[]
		for i in range (len(allFilesNames)):
			if self.name in allFilesNames[i][0:len(self.name)]: 
				self.files.append(allFilesNames[i])
		return
	def checkUnique(self):
		countDen = 0
		countP	 = 0
		countQ	 = 0
		posP 	 = 0
		posQ 	 = 0
		

		for i in range (len(self.files)):
			
			aux = self.files[i].replace(self.name+'_'+self.N,'')
			
			if '_den' in aux:
			    countDen = countDen +1
			elif '+' in aux: 
			    countP=countP+1
			    posP = i 
			elif '-' in aux: 
			    countQ=countQ+1
			    posQ = i 

		#print('file:',self.files)
		#print('countP:',countP, 'countQ:',countQ, 'countDen:',countDen)

    
    
		if (countP == 1) and (countQ == 1) and (len(self.files)== 3):
			self.status = True
			self.set_P(self.files[posP])
			self.set_Q(self.files[posQ])
			self.errorMsg = "No hay errores en los nombres de los archivos"
			
		elif (countP == 1) and (countQ == 1) and (len(self.files) == 4) and (countDen == 1):
			self.status = True
			self.statusDen = True
			self.set_P(self.files[posP])
			self.set_Q(self.files[posQ])
			self.errorMsg = 'No hay errores en los nombres de los arhivos'
	
		elif len(self.files) > 4:
			self.status = False
			archivo1 = self.name 
			archivo2 = self.name + "+P"
			archivo3 = self.name + "-Q"
			archivo4 = self.name + "den"
			self.errorMsg = "Hay errores, se encontraron multiples archivos, solo debes tener a lo mas 4:"+archivo1+', '+archivo2 + ','+ archivo3 +' y/o '+archivo4
		
		else:
			self.status = False
			archivo1 = self.name 
			archivo2 = self.name + "+P"
			archivo3 = self.name + "-Q"
			archivo4 = self.name + "den"
			self.errorMsg = "Faltan archivos, solo debes tener a lo mas 4:"+archivo1+', '+archivo2 + ','+ archivo3 +' y/o '+archivo4
		
		
		return

def removeFiles(filesList):
    filesList.insert(0,'rm')
    #printElementName('Delete','*',40)
    query = ' '.join(filesList)
    #print query
    try:
	res = subprocess.Popen(filesList,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
	output,error = res.communicate()
	if output:
	    print "Output Code:",res.returncode
	    print "Succefull:",output
	    printElement('*',40)
	    return 0
	if error:
	    print "Output Code:",res.returncode
	    print "Error: ",error.strip()
	    printElement('*',40)
	    return 1
    except OSError as e:
	print "Output Code: ",e.errno
	print "Error:",e.strerror
	print "ErrorFile: ",e.filename
	printElement('*',40)
	return 2
    except:
	print "Error:", sys.exc_info()[0]
	printElement('*',40)
	return 3
    #printElement('*',40)
    
    

    
def checker(message):
    if message == "":
	inputt = raw_input()
    else:
	inputt = raw_input(message+'\n')
    try:
	return int(inputt)
    except ValueError:
	print "Error!, Enter a number!"
	return checker("")


def edit(fileName, line1, line2):
    with open(fileName) as f:
	lines = f.readlines() #read
	f.close()

    lines[0] = line1 +'\n'
    lines[1] = line2 +'\n'
				
    with open(fileName, "w") as f:
	f.writelines(lines) #write back
    return 0

def editLine2(fileName, line):
    with open(fileName) as f:
	lines = f.readlines() 
	f.close()
	
    lines[1] = line + '\n'
    
    with open(fileName,'w') as f:
	f.writelines(lines)
    return

	