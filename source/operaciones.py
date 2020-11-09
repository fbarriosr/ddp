import os
import subprocess
from myPrint import *
from stages import *
from filesFunc import *

class Operaciones:
    def __init__(self):
	self.paso = 0
	self.X = 0
	self.Y = 0
	self.MainMep = 0
	self.PosMep  = 0
	self.NegMep  = 0
	self.FDAPos  = 0
	self.FDANeg  = 0
	
	self.FFP     = 0
	self.DDP     = 0
	
	self.tempFiles = []
	
    def viewMep(self):
	printElementName('MEP','-',40)
	print self.MainMep
	print self.PosMep
	print self.NegMep
	
    def getX(self):
	if self.X == 0:
	    printElementName('Number Cores X', '-',40)
	    print('Recommended 4, but you choose 1,2 or 3')
	    while True:
		answer = checker('Insert Cores')
		if answer <1 or answer > 4:
		    print('Action not valid: ', answer)
		else:
		    self.X = answer
		    break
	return self.X
    
    def getY(self):
	if self.Y == 0:
	    printElementName('Resolution Y','-',40)
	    print('Recommended 3, but you can choose:')
	    print('Low   : 2')
	    print('Medium: 3')
	    print('High  : 4')
	    while True:
		answer = checker('Insert Resolution')
		if answer <2 or answer >4:
		    print('Action not valid: ', answer)
		else:
		    self.Y = answer
		    break
	return self.Y
		
    
    def operacion1(self, project):
	printElementName('OP1','-',40)
	input1 = project.getNameMainFile()
	input2 = project.getNameDenFile()
	output = project.getName()+'_MEP_'+project.getN()+'.cub'
	
	x = self.getX()
	y = -1
	
	op1_a = CubeGenPot(input1, input2, output, y , x )
	#op1_a.view()
	
	op1_a.viewQuery()
	#print op1_a.cube()
	
	op1_a.cube()
	 
	self.MainMep = output
	#op1_a.view()
	
	if op1_a.getStatus():
	    input1 = project.getNamePosFile()
	    output = project.getName()+'_MEP_'+ project.getN()+'+'+ project.getP()+'.cub'
	    
	    op1_b = CubeGenPot(input1, input2, output, y, x)
	    op1_b.viewQuery()
	    op1_b.cube()
	    
	    self.PosMep = output
	    
	    if op1_b.getStatus():
		input1 = project.getNameNegFile()
		output = project.getName()+'_MEP_'+ project.getN()+'-'+ project.getQ()+'.cub'
		op1_c = CubeGenPot(input1, input2, output, y, x)
		
		op1_c.viewQuery()
		op1_c.cube()
		
		self.paso = 1
		self.NegMep = output
		
	    else:
		printElementName('Error','-',40)
		self.paso = 0
		sys.exit(0)
		
    
	else:
	    printElementName('Error','-',40)
	    self.paso = 0
	    sys.exit(0)
	    
    def operacion2(self, project):
	printElementName('OP2','-',40)
	input1  = project.getNamePosFile()
	output = project.getName() + '_'+ project.getN()+'+'+project.getP()+'_den.cub'
	
	x = self.getX()
	
	y = self.getY()
	
	op2 = CubeGenDens(input1, output, y, x)
	
	op2.viewQuery()
	
	op2.cube()
	
	project.statusDen = True
	
	project.files.append(output)
	
	#op2.view()
	
    def operacion3(self,project):
	printElementName('OP3','-',40)
	input1 = project.getNamePosFile()
	output = project.getName() + '_MEP_' + project.getN()+'+'+ project.getP()+'.cub'
	
	x = self.getX()
	y = self.getY()
	
	op3_1 = CubenGenPotOneFile(input1, output, y , x)
	op3_1.viewQuery()
	op3_1.cube()
	
	self.PosMep = output
	
	input1 = project.getNameMainFile()
	input2 = project.getName() + '_MEP_' + project.getN()+ '+' + project.getP()+'.cub'
	
	output = project.getName() + '_MEP_' + project.getN()+ '.cub'
	y = -1
	
	op3_2 = CubeGenPot(input1, input2, output, y, x)
	op3_2.viewQuery()
	
	op3_2.cube()
	
	self.MainMep = output
	
	input1 = project.getNameNegFile()
	output = project.getName() + '_MEP_' + project.getN()+'-'+project.getQ()+'.cub'
	
	op3_3 = CubeGenPot(input1, input2, output, y, x)
	op3_3.viewQuery()
	
	op3_3.cube()
	self.NegMep = output
	
    def operacion4(self,project):
	printElementName('OP4','-',40)
	input1 = project.getNameMainFile()
	output = project.getName() + '_MEP_' + project.getN()+'.cub'
	
	x = self.getX()
	y = self.getY()
	
	op4_1 = CubenGenPotOneFile(input1, output, y , x)
	op4_1.viewQuery()
	op4_1.cube()
	
	self.MainMep= output
	
	input1 = project.getNamePosFile()
	input2 = project.getName() + '_MEP_' + project.getN()+ '.cub'
	
	output = project.getName() + '_MEP_' + project.getN()+ '+' + project.getP()+'.cub'
	y = -1
	
	op4_2 = CubeGenPot(input1, input2, output, y, x)
	op4_2.viewQuery()
	
	op4_2.cube()
	
	self.PosMep = output
	
	input1 = project.getNameNegFile()
	output = project.getName() + '_MEP_' + project.getN()+'-'+project.getQ()+'.cub'
	
	op4_3 = CubeGenPot(input1, input2, output, y, x)
	op4_3.viewQuery()
	
	op4_3.cube()
	self.NegMep = output
	
    def operacion5(self,project):
	printElementName('OP5','-',40)
	input1 = project.getNameNegFile()
	output = project.getName() + '_MEP_' + project.getN()+'-'+ project.getQ() +'.cub'
	
	x = self.getX()
	y = self.getY()
	
	op5_1 = CubenGenPotOneFile(input1, output, y , x)
	op5_1.viewQuery()
	op5_1.cube()
	self.NegMep = output
	
	input1 = project.getNamePosFile()
	input2 = project.getName() + '_MEP_' + project.getN()+ '-'+ project.getQ()  +'.cub'
	
	output = project.getName() + '_MEP_' + project.getN()+ '+' + project.getP()+'.cub'
	y = -1
	
	op5_2 = CubeGenPot(input1, input2, output, y, x)
	op5_2.viewQuery()
	
	op5_2.cube()
	self.PosMep = output
	
	input1 = project.getNameMainFile()
	output = project.getName() + '_MEP_' + project.getN()+'.cub'
	
	op5_3 = CubeGenPot(input1, input2, output, y, x)
	op5_3.viewQuery()
	
	op5_3.cube()
	self.MainMep = output
    
    def paso1(self, project, info):
	printElementName(info,'-',40)
	if project.statusDen == False:
	    while True:
		printElementName('den.cub File is missing!', '*',40)
		answer = str(raw_input('Do you want create it? y/n\n'))
		if answer == 'y':
		    self.operacion2(project)
		    #project.view()
		    self.operacion1(project)
		    break
		elif answer == 'n':
		    while True:
			printElementName('Options','-',40)
			print '3: From N+p.fchk File'
			print '4: From N.fchk File'
			print '5: From N-q.fchk File'
			
			answer = checker('Choose Option')
			
			if answer == 3:
			    self.operacion3(project)
			    self.paso = 1
			    break
			elif answer == 4:
			    self.operacion4(project)
			    self.paso = 1
			    break 
			elif answer == 5:
			    self.operacion5(project)
			    self.paso = 1
			    break
		    break
		else:
		    print('Action not valid',answer)
	else:
	    #print 'OP1'
	    self.operacion1(project)
	    
    def paso2(self,project,info):
    
	#self.viewMep()
    
	printElementName(info,'-',40)
	line = 'Molecular electrostatic potencial( system with '+project.getN()+'+'+project.getP() +' electrons)'
	
	printElementName('Writing','*',40)
	print self.PosMep 
	
	editLine2(self.PosMep,line)
	
	line = 'Molecular electrostatic potential( system with '+project.getN()+ ' electrons)'
	editLine2(self.MainMep, line)
	
	print self.MainMep
	
	line = 'Molecular electrostatic potential( system with '+project.getN()+'-'+project.getQ() + ' electrons)'
    	editLine2(self.NegMep, line)
    	
    	print self.NegMep
    	
    	self.paso= 2
    	
    	
    def paso3a(self, value, action,inputFile1, inputFile2,outputFile ):
    
	#print ('value:',value)
    
	if value == 1:

	    t= CubeManP3NoScale(inputFile1, inputFile2,outputFile, action)
	    t.viewQuery()
	    t.cube()
	
	elif value > 1:
	    outputFilePro = outputFile.replace('_F-FP_FDA.cub','_pro_F-FP_FDA.cub')
	    outputFilePro = outputFilePro.replace('_F+FP_FDA.cub','_pro_F+FP_FDA.cub')
	    
	    t1 = CubeManP3NoScale(inputFile1, inputFile2, outputFilePro, action)
	    t1.viewQuery()
	    t1.cube()
	    
    	    t2 = CubeManP3Scale(outputFilePro, outputFile, value)
    	    t2.viewQuery()
    	    t2.cube()
    	    
    	    self.tempFiles.append(outputFilePro)
    	    
    	return outputFile

    def paso3(self,project, info):
    
	printElementName(info,'-',40)
	
	
	self.FDAPos = self.paso3a(int(project.getP()), 'SU', self.MainMep , self.PosMep  ,  project.getName()+'_F+FP_FDA.cub')

	self.FDANeg = self.paso3a(int(project.getQ()), 'SU', self.NegMep  , self.MainMep ,  project.getName()+'_F-FP_FDA.cub') 
    
	self.paso = 3
	
    def paso4(self, project, info ):
	printElementName(info,'-',40)
	line = 'Nucleophilic Fukui function potential by means of the finite difference approximation'
	
	printElementName('Writing','*',40)
	print self.FDAPos
	
	editLine2(self.FDAPos, line)
	
	print self.FDANeg
	line = line.replace('Nucleophilic','Electrophilic')
	editLine2(self.FDANeg, line)
	
	self.paso = 4
	
    def paso5b(self, action, inputFile1, inputFile2, outputFile ):
    
	t = CubeManP3NoScale(inputFile1, inputFile2, outputFile, action)
	t.viewQuery()
	t.cube()
	return outputFile
	
    def paso5a(self, action, inputFile1, inputFile2, outputFile):
	outputFilePro = outputFile.replace('_FFP_FDA.cub','_pro_FFP_FDA.cub')
	
	t1= CubeManP3NoScale(inputFile1, inputFile2, outputFilePro, action)
	t1.viewQuery()
	t1.cube()
	
	scale = 0.5
	t2 = CubeManP3Scale(outputFilePro, outputFile, 1/scale)
	t2.viewQuery()
	t2.cube()
	
	self.tempFiles.append(outputFilePro)
	
	return outputFile
	
    def paso5(self,project, info):
	printElementName(info, '-', 40)
	
	self.FFP = self.paso5a( 'A', self.FDAPos, self.FDANeg, project.getName()+'_FFP_FDA.cub' )
	self.DDP = self.paso5b('SU', self.FDAPos, self.FDANeg, project.getName()+'_DDP_FDA.cub' )
	
	
	self.paso = 5
	
    def paso6(self, info):
	printElementName(info,'-',40)
	
	line = 'Fukui function potential by means of finite difference approximation'
	
	printElementName('Writing','*',40)
	print self.FFP
	
	editLine2(self.FFP, line)
	
	line = line.replace('Fukui function','Dual descriptor')
    
	print self.DDP
	
	editLine2(self.DDP, line)
	
	
	
	self.paso = 6
	
    def paso7(self, info):
	printElementName(info,'-',40)
	printElementName('remove','*',40)
	for t in self.tempFiles:
	    print t
	removeFiles(self.tempFiles)
    

	
	
	
	

	


	
	
	
	
    
