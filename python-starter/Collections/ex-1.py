#
# File: ex-1.py
# Auth: Martin Burolla
# Date: 8/10/2021
# Desc: Every other color.
#

def everyOtherColor(colorList):
  retval = []
  idx = 0
  for color in colorList:
    if (idx % 2):
      retval.append(color)
    idx += 1
  return retval

def main():
  colorList = ['red', 'yellow', 'green', 'orange', 'black', 'purple', 'amber', 'pink']
  newList = everyOtherColor(colorList)
  print(newList)

if __name__ == "__main__":  
    main()

