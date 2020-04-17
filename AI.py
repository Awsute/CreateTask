
import random
import math

opRow = None

def gRowCount(CRow):
  global opRow
  rowC = CRow.count({'row': 1})
  rowC1 = CRow.count({'row': 5})
  rowC2 = CRow.count({'row': 9})

  if rowC > rowC1 and rowC > rowC2:
    opRow = 1
    return opRow
  elif rowC1 > rowC and rowC1 > rowC2:
    opRow = 5
    return opRow
  elif rowC2 > rowC1 and rowC2 > rowC:
    opRow = 9
    return opRow
  else:
    return 0

opColumn = []

def gColumnCount(columnC):
  global opColumn
  C = columnC.count({'column': 0})
  C1 = columnC.count({'column': 4})
  C2 = columnC.count({'column': 2})

  if C > C1 and C > C2:
    opColumn = 0
    return opColumn
  elif C1 > C and C1 > C2:
    opColumn = 2
    return opColumn
  elif C2 > C1 and C2 > C:
    opColumn = 4
    return opColumn
  else:
    return None


def lRowCount(CRow):
  global opRow
  rowC = CRow.count({'row': 1})
  rowC1 = CRow.count({'row': 5})
  rowC2 = CRow.count({'row': 9})

  if rowC < rowC1 and rowC < rowC2:
    opRow = 1
    return opRow
  elif rowC1 < rowC and rowC1 < rowC2:
    opRow = 5
    return opRow
  elif rowC2 < rowC1 and rowC2 < rowC:
    opRow = 9
    return opRow
  else:
    return None

opColumn = None

def lColumnCount(columnC):
  global opColumn
  C = columnC.count({'column': 0})
  C1 = columnC.count({'column': 4})
  C2 = columnC.count({'column': 2})

  if C < C1 and C < C2:
    opColumn = 0
    return opColumn
  elif C1 < C and C1 < C2:
    opColumn = 2
    return opColumn
  elif C2 < C1 and C2 < C:
    opColumn = 4
    return opColumn
  else:
    return None

chosenSpots = []
def coord(num):
  if num > 6:
    num -= 6
    ro = 9
  elif num > 3:
    num -= 3
    ro = 5
  elif num <= 3:
    ro = 1
  col = (2*num) - 2
  #return [{column, row}]
  return [{int(col)}, {int(ro)}]

lockedInR = False
lockedR = None


def chooseColumn(column):
  global Pchoice
  global chosenSpots
  global opColumn
  global opRow
  global lockedInR
  global lockedInC
  global lockedC
  global lockedR
  if lockedInR == True:
    Pchoice = lColumnCount(column)
  elif lockedInR == False:
    Pchoice = gColumnCount(column)
    lockedInC = True
  else:
    Pchoice = None
    return None


Pchoice = None

def chooseRow(row):
  global Pchoice
  global chosenSpots
  global opColumn
  global opRow
  global lockedInR
  global lockedInC
  global lockedC
  global lockedR
  if lockedInC == True:
    Pchoice = lRowCount(row)
    choice = Pchoice
  elif lockedInC == False:
    Pchoice = gRowCount(row)
    choice = Pchoice
    lockedInR = True
  else:
    Pchoice = None
    choice = None  


  return choice

lockedInC = False
lockedC = None
count = None





class runAI:

  def choices(openSpaces, moreSpaces, P1C, P2C, P1R, P2R, OriginBoard, SavedBoard, UserDet):
    global chosenSpots
    if UserDet == 1:
      row = P2R
      column = P2C
    else:
      row = P1R
      column = P1C
    rand = random.randint(0, len(moreSpaces) - 1)

    Rchoice = chooseRow(row)
    Cchoice = chooseColumn(column)

    if Cchoice == None or Rchoice == None:
      choice = moreSpaces[rand]
      chosenSpots.append(coord(choice))

    elif SavedBoard[int(Rchoice)][int(Cchoice)] in moreSpaces and not SavedBoard[int(Rchoice)][int(Cchoice)] in chosenSpots:
      choice = OriginBoard[int(Rchoice)][int(Cchoice)]
      chosenSpots.append([{Cchoice}, {Rchoice}])
    
    else:
      choice = moreSpaces[rand]
      chosenSpots.append(coord(choice))


    return str(choice)
    print(chosenSpots)
