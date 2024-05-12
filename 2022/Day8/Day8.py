input = open('Input8.txt', 'r')
trees = []

for line in input: 
    trees.append([*line.rstrip('\n')])

for i in range(len(trees)):
    for j in range(len(trees)): 
        trees[i][j] = int(trees[i][j])

# PART 1
visible = ((len(trees) - 1) * 4)

def isTreeVisible(treeRow, treeCol): 
    treeVisible = False
    treeVisibleLeft = True
    treeVisibleRight = True
    treeVisibleUp = True
    treeVisibleDown = True

    for x in range(0, treeRow): 
        if(trees[x][treeCol] >= trees[treeRow][treeCol]): 
            treeVisibleUp = False

    for x in range(treeRow + 1, len(trees)): 
        if(trees[x][treeCol] >= trees[treeRow][treeCol]): 
            treeVisibleDown = False

    for x in range(0, treeCol): 
        if(trees[treeRow][x] >= trees[treeRow][treeCol]): 
            treeVisibleLeft = False
            
    for x in range(treeCol + 1, len(trees)): 
        if(trees[treeRow][x] >= trees[treeRow][treeCol]): 
            treeVisibleRight = False

    if (treeVisibleLeft == True or treeVisibleRight == True or treeVisibleUp == True or treeVisibleDown == True): 
        treeVisible = True

    return treeVisible

for i in range(1,len(trees) - 1): 
    for j in range(1, len(trees) - 1): 
        if (isTreeVisible(i, j)): 
            visible += 1

# PART 2 --> doesn't work
highestScenicScore = 0
def scenicScore(treeRow, treeCol): 
    for x in reversed(range(0, treeRow)): 
        tallestTree = 0
        if(trees[x][treeCol] > tallestTree and trees[x][treeCol] < trees[treeRow][treeCol]): 
            tallestTree = trees[x][treeCol]
        up = tallestTree

    for x in range(treeRow + 1, len(trees)): 
        tallestTree = 0
        if(trees[x][treeCol] > tallestTree and trees[x][treeCol] < trees[treeRow][treeCol]): 
            down = trees[x][treeCol]
        down = tallestTree

    for x in reversed(range(0, treeCol)):
        tallestTree = 0 
        if(trees[treeRow][x] > tallestTree and trees[treeRow][x] < trees[treeRow][treeCol]): 
            left = trees[treeRow][x]
        left = tallestTree
            
    for x in range(treeCol + 1, len(trees)): 
        tallestTree = 0
        if(trees[treeRow][x] > tallestTree and trees[treeRow][x] < trees[treeRow][treeCol]): 
            right = trees[treeRow][x]
        right = tallestTree

    scenicScore = right * left * up * down

    return scenicScore

for i in range(1,len(trees) - 1): 
    for j in range(1, len(trees) - 1): 
        if (scenicScore(i, j) > highestScenicScore): 
            highestScenicScore = scenicScore

# SOLUTIONS
print('Part 1:', visible)
print('Part 2:', highestScenicScore)