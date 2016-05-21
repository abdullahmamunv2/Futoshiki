
from Node import node
from futoshikigame import futoshikigame

class Futoshiki(object):

	def __init__(self,input_file_name="init.txt"):
		self.board=[[]]
		fopen=file(input_file_name,'r')

board=[
		[0,0,0,0,2,0,0,0,0],
		[0,0,0,0,2,0,0,0,0],
		[8,5,4,0,0,0,0,0,2],
		[0,0,4,2,0,9,0,0,0],
		[2,0,8,0,0,0,9,0,0],
		[0,0,0,7,0,0,4,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0]
	]
constraint=[
			[(0,4), (0,3)],
			[(0,1), (0,2)]
		]
gameBoard=[]

domain=[1,2,3,4,5,6,7,8,9]

for i in range(0,len(board)):
	col=[]
	for j in range(0,len(board[0])):
		if board[i][j]!=0 :
			col.append(node(domain,(-1,-1),i,j,value=board[i][j]))
		else:
			col.append(node(domain,(-1,-1),i,j))
	gameBoard.append(col)
	col=[]
f=futoshikigame(gameBoard,domain,constraint)
f.play()





