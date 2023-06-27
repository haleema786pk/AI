import manhat_dis
from queue import PriorityQueue

board =[['','1','2'],
       ['3','4','5'],
       ['6','7','8']]


board1=[['','8','7'],
       ['6','5','4'],
       ['3','2','1']]


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

def index(board1,char):
    for i in range(0,3):
        for j in range(0,3):
            if board1[i][j]==char:
                return (i,j)

def heuristic(board,board1):
    h1=0
    for i  in range(0,3):
        for j in range(0,3):
             if board[i][j]!=board1[i][j]:
                h1+=1
    return h1

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




def bfs_Simple_Heuristic(visited,queue, goal, board):
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
                     queue.put((heuristic(goal,u),u,"UP"))
                     visited.append(u)
                     
       d=down(iset,n)
       if d!=0:
              if d not in visited:
                     queue.put((heuristic(goal,d),d,"DOWN"))
                     visited.append(d)
       l=left(iset,n)
       if l!=0:
              if l not in visited:
                     queue.put((heuristic(goal,l),l,"LEFT"))
                     visited.append(l)
       r=right(iset,n)
       if r!=0:
              if r not in visited:
                     queue.put((heuristic(goal,r),r,"RIGHT"))
                     visited.append(r)

print("8-Puzzle through Simple Heuristic Function  : ")
bfs_Simple_Heuristic(visited,queue,board,board1)



