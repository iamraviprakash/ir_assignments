# Declarations

edges=[]   #list of edges
df=0.85 #damping factor

# Functions


def addEdge(edge):
	global edges
	edges+=[edge]


def extractEdges(inputfile):

	filePointer = open(inputfile, 'r')
	for line in filePointer:
		edge=[]
		edge1=line.split()
		for i in edge1:
			edge+=[int(i)]
		addEdge(edge)
		#print(edge)

def listNodes():
	global edges, nodes
	f = open('pagerank.txt', 'r')
	test=f.read().split()
	test_set=set(test)
	return len(test_set)
			

def outgoingEdges(node):
	count=0

	for i in edges:
		if node in i:
			if i[0]!=node:
				count+=1

	return count


def calculatePageRank(node):
	global df, edges

	ratioSum=0
	pr=1-df
	pr=pr/listNodes()
	flag=0
	for i in edges:
		if i[0]==node:
			for j in i:
				if j!=node:
					n=outgoingEdges(j)
					ratioSum=ratioSum+1/n
			flag=1
			pr=pr+df*(ratioSum/listNodes())     #initial pagerank=1/total_no_of_ nodes for all nodes

		if flag==1:
			break
			
	return pr


# Data processing from txt

## File read
#print('extractEdges\n')
extractEdges('pagerank.txt')

#Computing page rank for each node
print("pagerank\n\n")


print("Mr. Bachchan")
pr = calculatePageRank(145125358)
print("pagerank: %s\n" % pr)


print("Mr. Modi")
pr = calculatePageRank(18839785)
print("pagerank: %s\n" % pr)
