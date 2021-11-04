import copy 
import graphviz
import os

os.system('del test-output /q')

#from operator import attrgetter

moves = [(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1)]
		  # #	  # #    #   
			#	  #	   # #    # #
finishing_char = ''
barrier_x = 0
barrier_y = 0
barriers = []
while finishing_char  not in['no','No','n','N']:

	try:
		barrier_x,barrier_y = map(int,input('Enter x and y barrier:').split(','))
	except:
		print('invalid input')
		continue
	if not(8>barrier_x>-1 and 8>barrier_y>-1) or (barrier_x,barrier_y) in [(0,0),(7,7)]:
		print('invalid input')
		continue

	barriers.append((barrier_x,barrier_y))
	finishing_char = input('Do you want to countinue?(yes/no) ')

print('barriers = ',barriers)
#print(barriers[0][0],type(barriers[0][0]))
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

	def get_information(self):
		info = ''
		info += '({0},{1})'.format(self.x,self.y) + '\\n\\n'
		info += ' depth = {0}'.format(self.depth) + '\\n'
		info += 'f(n)  =  g(n)  +  h(n)'+'\\n'
		info += '{0} = {1} + {2}'.format(self.f_n , self.g_n , self.h_n) + '\\n'

		return info




final_leaves=[]
#graph = graphviz.Digraph(comment='The Round Table',node_attr={'shape':'square'},format = 'pdf')

#def draw_graph():

count = 0
def move_horse(self):
	global moves,board,count
#	graph = graphviz.Digraph(comment='The Round Table',node_attr={'shape':'square'},format = 'png')
	count+=1	



#	graph.node(str(self),self.get_information())
	for i in moves:
		if 8 > self.x+i[0]  >= 0 and 8 > self.y+i[1] >= 0 and i!=self.symmetry and not((self.x+i[0],self.y+i[1]) in barriers): 
			self.leaves.append(Node(self.x+i[0],self.y+i[1],self.depth+1))

#			graph.node(str(self.leaves[-1]),self.leaves[-1].get_information())
#			graph.edge(str(self),str(self.leaves[-1]))

			self.leaves[-1].symmetry = (-i[0],-i[1])
			self.leaves[-1].parent = self
			if self.leaves[-1].x==7 and self.leaves[-1].y==7 :
				print(self.leaves[-1].x,self.leaves[-1].y,self.leaves[-1].parent.x , self.leaves[-1].parent.y)
				return self.leaves[-1]
		else:
			continue

	

	self_index = final_leaves.index(self)
	final_leaves.remove(self)
	#self.leaves.reverse()

	for i in self.leaves[::-1]:
		final_leaves.insert(self_index,i)

	min_value = 1000000000
	min_obj=None
	for i in final_leaves:
		if i.f_n < min_value:
			min_value = i.f_n
			min_obj = i
		
#	graph.node(str(min_obj),min_obj.get_information(),color = 'red')


#	graph.render('test-output/'+str(count))
	return move_horse(min_obj)

tree = Node(0,0,0)
final_leaves.append(tree)

last_leaf = move_horse(tree)
print(last_leaf.x , last_leaf.y , last_leaf.f_n)
print(len(final_leaves))

print('\n-------------------------------\n')

while last_leaf.parent is not None:
	print(last_leaf ,last_leaf.x,last_leaf.y,last_leaf.f_n,last_leaf.depth)
	last_leaf = last_leaf.parent

#print(final_leaves[0].x, final_leaves[0].y)
#print(final_leaves[1].x, final_leaves[1].y)
		
