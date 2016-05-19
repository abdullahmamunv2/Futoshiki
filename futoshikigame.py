
class futoshikigame(object):
	"""docstring for futoshikigame"""
	def __init__(self, X,D,C):
		self.board = X
		self.value=D
		self.constraints=C

	def play(self):
		self.backtrack((0,0))
		

	def backtrack(self,position):
		node=board[position[0]][position[1]]
		node.oredingValue(self.board)
		for i in node.domain:
			nei=node.orderingVariable(self.board)



		