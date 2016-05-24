
from Node import node
from futoshikigame import futoshikigame
from timeit import default_timer

class Futoshiki(object):

	def __init__(self,domain,input_file_name="ini.txt"):
		self.board=[]
		self.gameBoard=[]
		self.constraint=[]
		self.input_file_name=input_file_name
		self.domain=domain
	def readfile(self, delim):
		with open(self.input_file_name, 'r') as f:
			for line in f:
				yield list(line[:-1].split(delim))
	def initialize(self):
		readline=self.readfile(' ')
		pushIntoBoard=1
		for line in readline:
			if len(line)==1:
				if pushIntoBoard==1:
					pushIntoBoard=0
				else:
					pushIntoBoard=1
				continue
			if pushIntoBoard==0:
				self.board.append(map(int,line))
			else:
				l=[]
				for t in line:
					l.append(eval(t))
				self.constraint.append(l)
		self.iniGameBoard()
		self.f=futoshikigame(self.gameBoard,self.domain,self.constraint)
	def play(self):
		self.f.play()
		
	def iniGameBoard(self):
		for i in range(0,len(self.board)):
			col=[]
			for j in range(0,len(self.board[0])):
				if self.board[i][j]!=0 :
					col.append(node(domain,(-1,-1),i,j,value=self.board[i][j]))
				else:
					col.append(node(domain,(-1,-1),i,j))
			self.gameBoard.append(col)
			col=[]
	def print_board(self):
		for i in range(0,len(self.board)):
			for j in range(0,len(self.board[0])):
				print self.board[i][j],
			print ""
		print "constraints :"
		print self.constraint


if __name__=="__main__":
	
	start=default_timer()
	domain=[1,2,3,4,5,6,7,8,9]
	
	futo=Futoshiki(domain)
	futo.initialize()
	print "input :"
	futo.print_board()
	print "output :"
	futo.play()
	stop=default_timer()
	print "Total time: ",stop-start,"S"			





