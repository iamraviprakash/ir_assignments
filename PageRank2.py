# Declarations
inputfile='pagerank.txt'
outputfile='result3.txt'
edges=[]   #list of edges
df=0.85 #damping factor
pagerank={}
# Functions

def initialize():
	global pagerank
	pagerank=dict.fromkeys(listNodes(),1/totalNodes())

def addEdge(edge):
	global edges
	edges+=[edge]

def pageRankOf(node):
	global pagerank
	return pagerank[node]

def extractEdges():
	global inputfile
	filePointer = open(inputfile, 'r')
	for line in filePointer:
		edge=[]
		edge1=line.split()
		for i in edge1:
			edge+=[int(i)]
		addEdge(edge)
		#print(edge)

def listNodes():
	global edges, inputfile
	f = open(inputfile, 'r')
	test=f.read().split()
	test=list(map(int,test))
	test_set=set(test)
	return test_set
			
def totalNodes():
	return len(listNodes())

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
	pr=pr/totalNodes()
	flag=0
	for i in edges:
		if i[0]==node:
			for j in i:
				if j!=node:
					n=outgoingEdges(j)
					ratioSum=ratioSum+pageRankOf(j)/n
			flag=1
			pr=pr+df*ratioSum

		if flag==1:
			break
			
	return pr


# Data processing from txt

## File read
#print('extractEdges\n')
extractEdges()

initialize()

#Computing page rank for each node
print("pagerank\n\n")

f=open(outputfile, 'w')


#for i in pagerank:        #for less input.txt
#	pagerank[i]=calculatePageRank(i)
#	f.write('node: %s ; pagerank: %s\n' % (i, pagerank[i]))

print("Mr. Bachchan")
pagerank[145125358] = calculatePageRank(145125358)
print("pagerank: %s\n" % pagerank[145125358])


print("Mr. Modi")
pagerank[18839785] = calculatePageRank(18839785)
print("pagerank: %s\n" % pagerank[18839785])

