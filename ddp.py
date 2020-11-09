import os
import sys

from source.filesFunc import *

from source.operaciones import *

from source.myPrint import *

myCmd = os.popen('ls | egrep "\.fchk$|\_den.cub$"').read()
allFilesNames = myCmd.split()

nameProgram = 'DDP'


printElement('-',40)
printElementName(nameProgram.upper(),'-',40)
printElement('-',40)

if len(allFilesNames)==0:
    printElementName('No Files *.fchk','=',40)
    sys.exit(0)


# List for Projects

projectName 		= []	# Project List Name
projectBadName	 	= []	# Project Bad List Name

projectDDP 		= []	# List DDP
projectIncompleteDDP 	= []	# List DDP Incomplete


# load the projectName

for i in range(len(allFilesNames)):
    name = allFilesNames[i].replace('.fchk','')
    name = name.replace('_den.cub','')
    name = name[::-1]
    t1   = name.find('_')
    
    if t1 != -1:
	t1 = len(name)-1 -t1
	aux = allFilesNames[i][0:t1+2]
	if not(aux in projectName):
	    projectName.append(aux)
    else:
	projectBadName.append(name[::-1])
	
'''
printList('all',allFilesNames)
printList('good',projectName)
printList('bad', projectBadName)
'''

for data in projectName :
    a = Project(data)
    a.loadingFiles(allFilesNames)
    #a.view()
    a.checkUnique()
    #a.view()
    if a.status == True:
	projectDDP.append(a)
    else:
	projectIncompleteDDP.append(a)

#printListDDP('ProjectDDP', projectDDP)
#printListDDP('Incompletos', projectIncompleteDDP)

if len(projectDDP) != 0:
    printElementName('Project List',' ',40)
    for i in range( len(projectDDP) ):
	print(i,projectDDP[i].getName())
    printElement('-',40)
else:
    printElementName('No project :(','=',40)
    sys.exit(0)
    
    
# Choose the project to work


while True:
    answer = checker('Choose Project')
    if (answer<0) or (answer > len(projectDDP) -1):
	print('Action not valid:',answer)
    else:
	break

project = projectDDP[answer]

op = Operaciones()
op.paso1(project, 'Step 1/7')
op.paso2(project, 'Step 2/7')
op.paso3(project, 'Step 3/7')
op.paso4(project, 'Step 4/7')
op.paso5(project, 'Step 5/5')
op.paso6('Step 6/7')
op.paso7('Step 7/7')



    
    

