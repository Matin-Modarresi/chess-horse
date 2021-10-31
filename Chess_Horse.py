import copy 
import graphviz
#from operator import attrgetter

board = [[None for col in range(8)]for row in range(8)]

for i in board:
	print(*i)

moves = [(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1)]
		  # #	  # #    #   
			#	  #	   # #    # #
class Node:
	def __init__(self,x,y,depth):
		self.x = x
		self.y = y
		self.depth = depth
		self.h_n = 7-self.x if 7-self.x > 7-self.y else 7-self.y
		self.g_n = depth*3
		self.f_n = self.h_n + self.g_n
		self.symmetry = (None,None)

		self.leaves=[]
		self.parent = None






final_leaves=[]


def move_horse(self):
	global moves,board

	
	print('(',self.x,self.y,self.depth,')')

	#if self.x==7 and self.y==7:
	#	return

	#board_copy = copy.deepcopy(board)

	for i in moves:
		if 8 > self.x+i[0]  >= 0 and 8 > self.y+i[1] >= 0 and i!=self.symmetry: 
			self.leaves.append(Node(self.x+i[0],self.y+i[1],self.depth+1))
			self.leaves[-1].symmetry = (-i[0],-i[1])
			self.leaves[-1].parent = self
			if self.leaves[-1].x==7 and self.leaves[-1].y==7 :
				print(self.leaves[-1].x,self.leaves[-1].y,self.leaves[-1].parent.x , self.leaves[-1].parent.y)
				return self.leaves[-1]
		else:
			continue
	print('self.leaves:')
	
	for i in self.leaves:
		print(i.x,i.y ,i.f_n,self.depth)

	print()
	

	self_index = final_leaves.index(self)
	final_leaves.remove(self)
	#self.leaves.reverse()
	print('\n\nafter insert:')

	for i in self.leaves[::-1]:
		final_leaves.insert(self_index,i)
	for i in final_leaves:
		print('(',i.x,i.y,i.f_n,end = '), ')

	min_value = 1000000000
	min_obj=None
	for i in final_leaves:
		if i.f_n < min_value:
			min_value = i.f_n
			min_obj = i
		

	print('\nmin_obj',min_obj.f_n)
	print('\n'+'-'*30+'\n')
	return move_horse(min_obj)

tree = Node(0,0,0)
final_leaves.append(tree)

last_leaf = move_horse(tree)
print(last_leaf.x , last_leaf.y , last_leaf.f_n)
print(len(final_leaves))

print('\n-------------------------------\n')

while last_leaf.parent is not None:
	print(last_leaf.x,last_leaf.y,last_leaf.f_n,last_leaf.depth)
	last_leaf = last_leaf.parent

#print(final_leaves[0].x, final_leaves[0].y)
#print(final_leaves[1].x, final_leaves[1].y)
		
		
		

		
		
		

		

		
	
	