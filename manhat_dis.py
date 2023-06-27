from queue import PriorityQueue
board =[['','1','2'],
       ['3','4','5'],
       ['6','7','8']]


board1=[['','8','7'],
       ['6','5','4'],
       ['3','2','1']]

def index(board1,char):
    for i in range(0,3):
        for j in range(0,3):
            if board1[i][j]==char:
                return (i,j)

def manhattanDistance(board,board1):
    val=[0,0,0,0,0,0,0,0,0]
    h1=0
    for i  in range(0,3):
        for j in range(0,3):
             if board[i][j]!=board1[i][j]:
                k,l=index(board1,board[i][j])
                while i!=k or j!=l:
                    if board[i][j]!='':
                        num=int(board[i][j])
                    else:
                        num=0
                    
                    if k==i :
                        while l<j:
                            val[num]+=1
                            l+=1
                        while l>j:
                            val[num]+=1
                            l-=1
                    elif l==j:
                         while k<i:
                            val[num]+=1
                            k+=1
                         while k>i:
                            val[num]+=1
                            k-=1
                    else:
                        if k<i:
                            while k<i:
                                val[num]+=1
                                k+=1
                        if k>i:
                            while k>i:
                                val[num]+=1
                                k-=1
                        if l<j:
                            while l<j:
                                val[num]+=1
                                l+=1
                        if l>j:
                            while l>j:
                                val[num]+=1
                                l-=1
    tot_heu=0
    for i in range(1,9):
        tot_heu+=val[i]          
    #print(val[1:])
    #print("Total Manhattan Distance Value for above 8-puzzle : ",tot_heu)
    return tot_heu

queue=PriorityQueue()
visited=[]

def copyB(board):
       c=[] 
       r=[]
       for i in range(0,3):
              for j in range(0,3):
                     c.append(board[i][j])
              r.append(c)
              c=[]
       return r

def up(iset,board):
       i,j=iset
       if i!=0:
              dummyb=copyB(board)
              dummyb[i][j]=dummyb[i-1][j]
              dummyb[i-1][j]=''
              return dummyb
       else :return 0
              
def down(iset,board):
       i,j=iset
       if i!=2:
              dummyb=copyB(board)
              dummyb[i][j]=dummyb[i+1][j]
              dummyb[i+1][j]=''
              return dummyb
       else :return 0


def left(iset,board):
       i,j=iset
       if j!=0:
              dummyb=copyB(board)
              dummyb[i][j]=dummyb[i][j-1]
              dummyb[i][j-1]=''
              return dummyb
       else :return 0

def right(iset,board):
       i,j=iset
       if j!=2:
              dummyb=copyB(board)
              dummyb[i][j]=dummyb[i][j+1]
              dummyb[i][j+1]=''
              return dummyb
       else :return 0




def bfs_Manhattan(visited,queue, goal, board):
  count=0
  visited.append(board)
  queue.put((0,board,"NONE"))
  while queue:
       c,n,m = queue.get()
       count+=1
       print("MOVE : ",m)
       print("______________")
       print("|",n[0][0],"|",n[0][1],"|",n[0][2],"|")
       print("|___|___|___|")
       print("|",n[1][0],"|",n[1][1],"|",n[1][2],"|")
       print("|___|___|___|")
       print("|",n[2][0],"|",n[2][1],"|",n[2][2],"|")
       print("|___|___|___|")
       print("*******************")
       if n not in visited:
              #print(n)
              visited.append(n)
       if n==goal:
              print("Goal Found in",count,"  Traversal!!!")
              return c
       iset=index(n,'')
       u=up(iset,n)
       if u!=0:
              if u not in visited:
                     queue.put((manhattanDistance(goal,u),u,"UP"))
                     visited.append(u)
                     
       d=down(iset,n)
       if d!=0:
              if d not in visited:
                     queue.put((manhattanDistance(goal,d),d,"DOWN"))
                     visited.append(d)
       l=left(iset,n)
       if l!=0:
              if l not in visited:
                     queue.put((manhattanDistance(goal,l),l,"LEFT"))
                     visited.append(l)
       r=right(iset,n)
       if r!=0:
              if r not in visited:
                     queue.put((manhattanDistance(goal,r),r,"RIGHT"))
                     visited.append(r)


print("8-Puzzle through Manhattan Distance  : ")
bfs_Manhattan(visited,queue,board,board1)

