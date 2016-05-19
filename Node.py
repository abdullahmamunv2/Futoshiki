#import queue as Q

class node(object):
	def __init__(self,domain,parent,row,col,value=0):
		self.domain=domain
		self.value=value
		self.row=row
		self.col=col
		self.unassigned=True
		self.parent=parent
	def deletFromDomain(self,item):
		self.domain.remove(item)
	def addItem(self,item):
		self.domain.append(item)
	def __str__(self):
		return "value ",self.value," row ",self.row," col ",self.col


	########### least-constraining value (LCV) ############
	def oredingValue(self,board):
		neighbourPosition=self.__getneighbourPosition(board)
		maxeliminate=100
		eliminate=[]
		for val in self.domain:
			eli_count=0
			for nei in neighbourPosition:
				row,col=nei
				try:
					i = board[row][col].index(val)
					eli_count+=1
				except ValueError:
					pass
			eliminate.append((eli_count,val))
		eliminate.sort()
		new_domain=[]
		for i in eliminate:
			new_domain.append(i[1])
		self.domain=new_domain

	def orderingVariable(self,board):
		neighbourPosition=self.__getneighbourPosition(board)
		domainSize=[]
		orderedVariable=[]
		for nei in neighbourPosition:
				row,col=nei
				domainSize.append((len(board[row][col].domain),nei))
		domainSize.sort()

		##### compare two value equal or not if equal than apply degree heuristic
		for i in range(0,len(domainSize)):
			row,col=domainSize[i][1]
			if i < len(domainSize)-1:
				rowC,colC=domainSize[i+1][1]
				if len(board[row][col].domain) == len(board[rowC][colC].domain):
					length=__getneighbourPosition(board,Row=row,Col=col)
					lengthC=__getneighbourPosition(board,Row=rowC,Col=colC)
					if length > lengthC :
						domainSize[i+1],domainSize[i]=domainSize[i],domainSize[i+1]

		for i in domainSize:
			orderedVariable.append(i[1])
		return orderedVariable



			

	def __getneighbourPosition(self,board,Row=-1,Col=-1):
		x_update=[0,0,1,-1]
		y_update=[1,-1,0,0]
		neighbour=[]
		for i in range(0,4):
			row=None
			col=None
			if Row!=-1:
				row=self.row+x_update[i]
				col=self.col+y_update[i]
			else:
				row=Row+x_update[i]
				col=Col+y_update[i]

			############## check grid cell position valid or not ############
			if row >=0 and row < len(board) and col>=0 and len(board[0]):
				############## make sure that parent is not neighbour ############
				if row!=parent[0] and col!=parent[1] and board[row][col].value==0:
					neighbour.append((row,col))
		return neighbour

