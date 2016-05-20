from pprint import pprint
class futoshikigame(object):
	"""docstring for futoshikigame"""
	def __init__(self, X,D,C):
		self.board = X
		self.value=D
		self.constraints=C

	def play(self):
		check=self.backtrack((0,0))
		

	def backtrack(self,position):

		if self.__isBoardFull():
			print "print full"
			return True

		node=self.board[position[0]][position[1]]
		node.orderingValue(self.board)
		for dom in node.domain:
			neighbours=node.orderingVariable(self.board)
			print "nei",neighbours
			if neighbours:
				break
			for nei in neighbours:
				row,col=nei
				self.board[row][col].value=dom
				check=self.__checkConsistency(row,col)
				if check :
					self.board[row][col].parent=node.parent
					retCheck=self.backtrack((row,col))
					if retCheck :
						return True
				self.board[row][col].value=0
		return False

	def __isBoardFull(self):
		for i in range(0,len(self.board)):
			for j in range(0,len(self.board)):
				if self.board[i][j].value==0:
					return False
		for i in range(0,len(self.board)):
			for j in range(0,len(self.board[0])):
				print self.board[i][j].value,
			print ""
		return True

	def __checkConsistency(self,row,col):
		checkCol=self.board[row][col]
		for j in range(1,len(self.board)):
			if self.board[row][j]==checkCol and col!=j:
					return False
		checkRow=self.board[row][col]
		for j in range(1,len(self.board)):
			if self.board[j][col]==checkRow and row!=j:
				return False
		for con in self.constraints:
			row,col=con[0]
			rowC,colC=con[1]
			if self.board[row][col].value !=0 and self.board[rowC][colC].value!=0:
				if self.board[row][col].value < self.board[rowC][colC].value:
					return False
		return True




		