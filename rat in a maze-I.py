n=4
def check(maze,x,y,res):
    if  0<=x<n and 0<=y<n:
        if maze[x][y]==1 and res[x][y]==0:
            return True
    return False

def ratMaze(maze,x,y,res):
    if x==n-1 and y==n-1:
        return True
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in moves:
        new_x=x+dx
        new_y=y+dy

        if check(maze,new_x,new_y,res):
            res[new_x][new_y]=1

            if ratMaze(maze,new_x,new_y,res):
                return True
            
            res[new_x][new_y]=0
    return False

def solveMaze(maze):
    res=[[0] *n for _ in range(n)]
    #result strat open
    res[0][0]=1

    if ratMaze(maze,0,0,res):

        for row in res:
            print(*row)

    else:
        print("no solution exists")

maze=[[1,0,0,0],
      [0,1,0,0],
      [0,1,0,0],
      [0,1,1,1]
      


      ]

solveMaze(maze)