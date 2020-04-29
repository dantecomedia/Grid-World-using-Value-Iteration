Row=3
column=3
win=[0,3]
lose=[1,3]
start=[2,0]
Determinisitc=True





class State:
	def __init__(self,state= start):
		self.board=np.zeros([row, column])
		self.board[1,1]=-1
		self.determine=Determinisitc
		self.state=state
		self.isEnd=False


	def givereward(state):
		if self.state=win:
			return 1
		elif self.state=lose:
			return -1
		else:
			return 0
	def isEndfunc(state):
		if self.state==lose or self.state==win:
			isEnd=True


	def nxtaction(state,action):
		if self.determine:
			if self.action="up":
				nextstate=(self.state[0]-1,self.state[1])
			elif self.action="down":
				nextstate=(self.state[0]+1,self.state[1])
			elif self.action="left":
				nextstate=(self.state[0],self.state[1]+1)
			elif self.action="right":
				nextstate=(self.state[0],self.state[1]-1)
			if nextstate[0]>=0 and nextstate[0]<=2:
				if nextstate[1]>=0 and nextstate[1]<=3:
					if (nextstate[0]!=1 and nextstate[1]!=1):
						return nextstate