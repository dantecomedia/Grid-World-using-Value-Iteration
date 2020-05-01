import numpy as np

Row=3
column=3
win=[0,3]
lose=[1,3]
start=[2,0]
Determinisitc=True





class State:
	def __init__(self,state= start):
		self.board=np.zeros([Row, column])
		self.board[1,1]=-1
		self.determine=Determinisitc
		self.state=state
		self.isEnd=False


	def givereward(state):
		if self.state==win:
			return 1
		elif self.state==lose:
			return -1
		else:
			return 0
	def isEndfunc(self):
		if self.state==lose or self.state==win:
			isEnd=True

	def nxtposition(self, action):
		if self.determine:
			if action == "up":
				nxtState = (self.state[0] - 1, self.state[1])
			elif action == "down":
				nxtState = (self.state[0] + 1, self.state[1])
			elif action == "left":
				nxtState = (self.state[0], self.state[1] - 1)
			else:
				nxtState = (self.state[0], self.state[1] + 1)
			# if next state legal
			if (nxtState[0] >= 0) and (nxtState[0] <= 2):
				if (nxtState[1] >= 0) and (nxtState[1] <= 3):
					if nxtState != (1, 1):
						return nxtState
			return self.state

	def  showboard(self):
		self.board[self.state]=1
		for i in range(0,row):
			print("-------------------------------")
			out="|"
			for j in range(0, column):
				if self.board[i,j]==1:
					token="*"
				elif self.board[i,j]==-1:
					token="z"
				elif self.board[i,j]==0:
					token="0"
				out=out+token+"|"
			print(out)
		print("-------------------------------")



class Agent:

	def __init__(self):
		self.actions=["up","down","left","right"]
		self.states=[]
		self.State=State()
		self.lr_rate=0.1
		self.exp_rate=0.3

		
		self.state_values={}

		#initalizing the state values to 0
		for i in range(0,Row):
			for j in range(0,column):
				self.state_values[(i,j)]=0


	 def chooseaction(self):
	 	mx_nxt_reward = 0
		action = ""

		if np.random.uniform(0, 1) <= self.exp_rate:
		    action = np.random.choice(self.actions)
		else:
		    # greedy action
		    for a in self.actions:
		        # if the action is deterministic
		        nxt_reward = self.state_values[self.State.nxtPosition(a)]
		        if nxt_reward >= mx_nxt_reward:
		            action = a
		            mx_nxt_reward = nxt_reward
		return action

	def takeAction(self,action):
		position=self.State.nxtposition(action)
		return State(state=position)

	def reset(self):
		self.states=[]
		self.State=State()

	def play(self,round=10):
		i=0
		while i < round:
			if self.State.isEnd:
				reward=self.State.givereward()
				self.state_values[self.State.state]=reward
				print("Game end reward", reward)

				for s in reversed(self.states):
					reward=self.state_values[s]+self.lr*(reward-self.state_values[s])
					self.state_values[s]=round(reward,s)
				self.reset()
				i+=1
			else:
				action=self.chooseaction()
				self.states.append(self.State.nxtposition(action))
				print("position {} action {}".format(self.State.state,action))
				self.State=self.takeAction(action)
				self.State.isEndfunc()
				print("Next state",self.State.state)
				print("----------------------------")


	def showvalues(self):
		for i in range(0,row):
			out="| "
			print("----------------------------------")
			for j in range(0, column):
				out+=str(self.state_values[(i,j)]).ljust(6)+"|"
			print(out)
		print("----------------------------------")



if __name__=="__main__":
	ag=Agent()
	ag.play(50)
	print(ag.showvalues())









	
