height = int(raw_input("Please give the height of the Tree: "))
Trunkh = int(raw_input("Please give the height of the trunk: "))
Trunkw = int(raw_input("Please give the width of the trunk: "))
p=0
while p < height:
  print((' '*(height-p))+('*'*(p*2+1))+(' '*(height-p)))
  p=p+1
  if(p == height):
      j=0
      while j < Trunkh :
          print((' ' *height) + ('*'*Trunkw))
          j=j+1
  
