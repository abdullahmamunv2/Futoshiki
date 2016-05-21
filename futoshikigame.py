from pprint import pprint
import time
class futoshikigame(object):
	"""docstring for futoshikigame"""
	def __init__(self, X,D,C):
		self.board = X
		self.value=D
		self.constraints=C

	def play(self):
		check=self.backtrack()
	def backtrack(self):
		cells=self.unassignedCell()


		if len(cells)==0:
			for i in range(0,len(self.board)):
				for j in range(0,len(self.board[0])):
					print self.board[i][j].value,
				print " "
			return True
		cells=self.orderingVariable(cells)
		row,col=cells[0]
		self.board[row][col].orderingValue(self.board)
		for dom in self.board[row][col].domain:
			self.board[row][col].value=dom
			check=self.__checkConsistency(row,col)
			if check :
				if self.backtrack():
					return True
			self.board[row][col].value=0
		return False
				


	def unassignedCell(self):
		cells=[]
		for i in range(0,len(self.board)):
			for j in range(0,len(self.board[0])):
				if self.board[i][j].value==0:
					cells.append((i,j))
		return cells


	def orderingVariable(self,cells):
		neighbourPosition=cells
		domainSize=[]
		orderedVariable=[]
		for nei in neighbourPosition:
				row,col=nei
				domainSize.append((len(self.board[row][col].domain),nei))
		domainSize.sort()

		##### compare two value equal or not if equal than apply degree heuristic
		for i in range(0,len(domainSize)):
			row,col=domainSize[i][1]
			if i < len(domainSize)-1:
				rowC,colC=domainSize[i+1][1]
				if len(self.board[row][col].domain) == len(self.board[rowC][colC].domain):
					length=self.__getneighbourPosition(self.board,Row=row,Col=col)
					lengthC=self.__getneighbourPosition(self.board,Row=rowC,Col=colC)
					if length > lengthC :
						domainSize[i+1],domainSize[i]=domainSize[i],domainSize[i+1]

		for i in domainSize:
			orderedVariable.append(i[1])
		return orderedVariable
	def __getneighbourPosition(self,board,Row=-1,Col=-1):
		row_update=[0,0,1,-1]
		col_update=[1,-1,0,0]
		neighbour=[]
		for i in range(0,4):
			row=None
			col=None
			parent=None
			if Row==-1:
				row=self.row+row_update[i]
				col=self.col+col_update[i]
			else:
				row=Row+row_update[i]
				col=Col+col_update[i]
			############## check grid cell position valid or not ############
			if row >=0 and row < len(board) and col>=0 and col<len(board[0]):
				############## make sure that parent is not neighbour ############
				if board[row][col].value==0:
					neighbour.append((row,col))
		return neighbour


	def __isBoardFull(self):
		for i in range(0,len(self.board)):
			for j in range(0,len(self.board)):
				if self.board[i][j].value==0:
					return False
		return True

	def __checkConsistency(self,row,col):

		checkCol=self.board[row][col].value
		for j in range(0,len(self.board)):
			if self.board[row][j].value==checkCol and col!=j:
					return False
		checkRow=self.board[row][col].value
		for j in range(0,len(self.board)):
			if self.board[j][col].value==checkRow and row!=j:
				return False
		for con in self.constraints:
			row,col=con[0]
			rowC,colC=con[1]
			if self.board[row][col].value !=0 and self.board[rowC][colC].value!=0:
				if self.board[row][col].value < self.board[rowC][colC].value:
					return False
		return True




		