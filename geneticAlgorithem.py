from random import randint


pairs=[]
def makeBoard(l):
    board=[['','','',''],['','','',''],['','','',''],['','','','']]
    for i in range(0,4):
        board[l[i]-1][i]=i
    return board
def attack(indexes,qno,board):
    global pairs
    count=0
    m=0
    n=0
    i,j=indexes[qno]
    n=i
    m=0
    while m<4:      #attack check in same row
        if (n,m) in indexes:
            if m!=j and sorted((qno,board[n][m])) not in pairs:
                count+=1
                pairs.append(sorted((qno+1,board[n][m])))
        m+=1
    n=i-1
    m=j+1
    while n>=0 and m<4:     #attack check in upper right
        if (n,m) in indexes and sorted((qno,board[n][m])) not in pairs:
            pairs.append(sorted((qno,board[n][m])))
            count+=1
        m+=1
        n-=1 
    n=i-1
    m=j-1
    while n>=0 and m>=0:     #attack check in upper left
        if (n,m) in indexes and sorted((qno,board[n][m])) not in pairs:
            pairs.append(sorted((qno,board[n][m])))
            count+=1
        m-=1
        n-=1 
    n=i+1
    m=j+1
    while n<4 and m<4:     #attack check in lower right
        if (n,m) in indexes and sorted((qno,board[n][m])) not in pairs:
            pairs.append(sorted((qno,board[n][m])))
            count+=1
        m+=1
        n+=1 
    n=i+1
    m=j-1
    while n<4 and m>=0:     #attack check in lower left
        if (n,m) in indexes and sorted((qno,board[n][m])) not in pairs:
            pairs.append(sorted((qno,board[n][m])))
            count+=1
        m-=1
        n+=1 
    return count


def nonAttack(l):
    count=0
    indexes=[]
    board=makeBoard(l)
    for i in range(0,4):
        indexes.append((l[i]-1,i))
    count+=attack(indexes,0,board)
    count+=attack(indexes,1,board)
    count+=attack(indexes,2,board)
    count+=attack(indexes,3,board)
    pairs.clear()
    del board
    return 6-count

def crossOver(p1,p2):
    l=[]
    for i in range(0,2):
        l.append(p1[i])
    for i in range(2,4):
        l.append(p2[i])
    return l


def mutation(l):
    index=randint(0,3)
    newVal=randint(1,4)
    l[index]=newVal
    return l


def geneticAlgorithem(l1,l2,l3,l4,count):
    
    #####   Finging non attacking pairs of each list
    c1=nonAttack(l1)
    c2=nonAttack(l2)
    c3=nonAttack(l3)
    c4=nonAttack(l4)
    if c1==6:
        print("After ",count," Iterations")
        print("Solution Found--->\t",l1)
        return l1
    if c2==6:
        print("After ",count," Iterations")
        print("Solution Found--->\t",l2)
        return l2
    if c3==6:
        print("After ",count," Iterations")
        print("Solution Found--->\t",l3)
        return l3
    if c4==6:
        print("After ",count," Iterations")
        print("Solution Found--->\t",l4)
        return l4
    ######      CRoss Over  #######    
    c1=crossOver(l1,l2)
    c2=crossOver(l2,l1)
    c3=crossOver(l3,l4)
    c4=crossOver(l4,l3)
    ######      Mutation  #######    
    c1=mutation(c1)
    c2=mutation(c2)
    c3=mutation(c3)
    c4=mutation(c4)
    count+=1
    ######      Recursive call for Childs  #######    
    return geneticAlgorithem(c1,c2,c3,c4,count)
    


l=[4,1,2,1]
l2=[3,2,1,4]
l3=[2,3,1,3]
l4=[1,4,2,3]

b=geneticAlgorithem(l,l2,l3,l4,0)
b=makeBoard(b)
print("--------------")
print("|",b[0][0],"|",b[0][1],"|",b[0][2],"|",b[0][3],"|",)
print("--------------")
print("|",b[1][0],"|",b[1][1],"|",b[1][2],"|",b[1][3],"|")
print("--------------")
print("|",b[2][0],"|",b[2][1],"|",b[2][2],"|",b[2][3],"|")
print("--------------")
print("|",b[3][0],"|",b[3][1],"|",b[3][2],"|",b[3][3],"|")
print("--------------")

# print("\t### List number 1 ###")
# for i in range(0,4):
#     print("Enter position of queen # ",i+1," : ")
#     l[i]=int(input())

# print("\n\n\t### List number 2 ###")
# for i in range(0,4):
#     print("Enter position of queen # ",i+1," : ")
#     l2[i]=int(input())
# print("\n\n\t### List number 3 ###")
# for i in range(0,4):
#     print("Enter position of queen # ",i+1," : ")
#     l3[i]=int(input())
# print("\n\n\t### List number 4 ###")
# for i in range(0,4):
#     print("Enter position of queen # ",i+1," : ")
#     l4[i]=int(input())
