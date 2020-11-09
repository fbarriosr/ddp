import subprocess
import sys
import os
from source.myPrint import *

class CubeGenPot:
    def __init__(self, inputFile1, inputFile2, outputFile ,Y, X):
	self.inputFile1 = inputFile1
	self.inputFile2 = inputFile2
	self.outputFile = outputFile
	self.X 		= str(X)
	self.Y		= str(Y)
	self.queryCMD	= ['cubegen', self.X, 'Potential=SCF',self.inputFile1, self.outputFile ,self.Y,'h', self.inputFile2 ]
	self.query	= ' '.join(self.queryCMD)
	self.log 	= 'No message'
	self.status     = False
    def getStatus(self):
	return self.status
    
    def view(self):
	printElementName('Resumen','-', 40)
	print('InputFile1:', self.inputFile1)
	print('InputFile2:', self.inputFile2)
	print('OutputFile:', self.outputFile)
	print('X', self.X)
	print('Y', self.Y)
	print('Status:',self.log)
	print('Log:', self.log)
	printElement('-',40)
	return 0

    def viewQuery(self):
	printElementName('Working','*',40)
	print self.query
	return  0
	
    def cubeWork(self,queryCMD,comunicate):

	try:
	    if len(comunicate) > 2:
		res = subprocess.Popen(queryCMD, shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		output, error = res.communicate(comunicate)
	    else:
		res = subprocess.Popen(queryCMD, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		output, error = res.communicate()
	    if output:
		self.status = True
		self.log    = 'Successful :)'
		return 0
	    if error:
		self.outputFile = ""
		self.status 	= False
		self.log	= error.strip()
		return 1
	except OSError as e:
	    self.outputFile = ""
	    self.status	    = False
	    self.log 	    = e.strerror
	    return 2
	except :
	    self.outputFile = ""
	    self.status	    = False
	    self.log 	    = sys.exc_info()[0]
	    return 3
	
    def cube(self):
	self.cubeWork(self.queryCMD,'')

class CubeGenDens(CubeGenPot):
    def __init__(self, inputFile, outputFile, Y, X):
	self.inputFile = inputFile
	self.outputFile = outputFile
	self.Y = str(Y)
	self.X = str(X)
	
	self.queryCMD = ['cubegen', self.X, 'Density=SCF', self.inputFile, self.outputFile, '-'+self.Y , 'h']
	self.query = ' '.join(self.queryCMD)
	self.log   = 'No message'
	self.status = False
	
    def view(self):
	printElementName('Resumen','-',40)
	print('InputFile:',self.inputFile)
	print('OutputFile:', self.outputFile)
	print('X',self.X)
	print('Y',self.Y)
	print('Status:',self.status)
	print('Log:', self.log)
	printElement('-',40)
	return 0
	
class CubenGenPotOneFile(CubeGenDens):
    def __init__(self, inputFile, outputFile, Y, X):
	self.inputFile  = inputFile
	self.outputFile = outputFile
	self.Y = str(Y)
	self.X = str(X)
	
	self.queryCMD = ['cubegen', self.X, 'Potential=SCF', self.inputFile, self.outputFile, '-'+self.Y, 'h' ]
	self.query = ' '.join(self.queryCMD)
	self.log   = 'No message'
	self.status = False
	

	
class CubeManP3NoScale(CubeGenPot):
    def __init__(self,inputFile1, inputFile2, outputFile, action):
	self.inputFile1 = inputFile1
	self.inputFile2 = inputFile2
	self.outputFile = outputFile
	
	self.status	= False
	self.log	= 'No message'
	
	# query
	
	self.cmd_suppression	= 'cubman'
	firstInput		= self.inputFile1
	isFormattedFirstInput   = 'yes'
	secondInput		= self.inputFile2
	isFormattedSecondInput	= 'yes'
	shouldItBeFormatted	= 'yes'
	
	self.queryCMD		= '\n'.join([action, firstInput, isFormattedFirstInput, secondInput, isFormattedSecondInput, outputFile, shouldItBeFormatted ])
	
	self.query		= ' '.join([self.cmd_suppression, action, firstInput, isFormattedFirstInput, secondInput, isFormattedSecondInput, outputFile, shouldItBeFormatted ])
	
    
	
    def view(self):
	printElementName('Resume','-',40)
	print('InputFile1', self.inputFile1)
	print('InputFile2', self.inputFile2)
	print('OutputFile', self.outFile)
	print('Status:', self.status)
	print('Log:', self.log)
	printElement('-',40)
	
    def cube(self):
	self.cubeWork(self.cmd_suppression, self.queryCMD)
	
class CubeManP3Scale(CubeManP3NoScale):

    def __init__(self, inputFile, outputFile, factor):
	self.inputFile 	= inputFile
	self.outputFile = outputFile
	self.factor 	= factor
	
	# query
	
	self.cmd_suppression	= 'cubman'
	action			= 'SC'
	firstInput		= self.inputFile
	isFormattedFirstInput	= 'yes'
	outputFile		= self.outputFile
	shouldItBeFormatted	= 'yes'
	scale			= str( round( ( float(1) / float(self.factor) ), 10) )

	self.queryCMD 		= '\n'.join([action, firstInput, isFormattedFirstInput, outputFile, shouldItBeFormatted, scale])
	self.query		= ' '.join([self.cmd_suppression, action, firstInput, isFormattedFirstInput, outputFile, shouldItBeFormatted, scale])
    
    def view(self):
	printElementName('Resume','-',40)
	print('InputFile:', self.inputFile)
	print('OutputFile:', self.outputFile)
	print('Status:', self.status)
	print('Log:', self.log)
	printElement('-',40)
	
    