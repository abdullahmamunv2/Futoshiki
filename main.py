
from Node import node

class Futoshiki(object):

	def __init__(self,input_file_name="init.txt"):
		self.board=[[]]
		fopen=file(input_file_name,'r')

board=[
		[0,0,0,0,0],
		[4,0,0,0,2],
		[0,0,4,0,0],
		[0,0,0,0,4],
		[0,0,0,0,0]
	]
constraint=[
			[(0,0), (0,1)],
			[(0,2), (0,3)],
			[(0,3), (0,4)],
			[(3,4), (3,3)],
			[(4,2), (4,1)],
			[(4,1), (4,0)]
		]
gameBoard=[]
domain=[1,2,3,4,5]

for i in range(0,len(board)):
	col=[]
	for j in range(0,len(board[0])):
		if board[i][j]!=0 :
			col.append(node(domain,(-1,-1),i,j,value=board[i][j]))
		else:
			col.append(node(domain,(-1,-1),i,j))
	gameBoard.append(col)
	col=[]

"""for i in range(0,len(gameBoard)):
	for j in range(0,len(gameBoard[0])):
		print gameBoard[i][j].value,
	print """""




