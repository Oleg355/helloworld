from mcpi.minecraft import Minecraft
import time
import datetime
import random
import sys

mc = Minecraft.create()

Score=0
mc.setBlocks(102,99,396,154,0,347,0)
mc.setBlocks(103,69,395,153,69,346,2)
x=random.randint(102,154)
y=72
z=random.randint(346,395)
mc.setBlock(x,y,z,41)
mc.postToChat("Score " + str(Score))
lastTime = datetime.datetime.now()
lastDelta = 180
while True:
       deltaTime = datetime.datetime.now() - lastTime
       if deltaTime.total_seconds() > 180:
              mc.postToChat("Game Over")
              mc.postToChat("Total Score " +str(Score))
              break
       else:
##              print(lastDelta - (180 - deltaTime.total_seconds()))
              if (lastDelta - (180 - deltaTime.total_seconds())) > 1:
                     mc.postToChat("Time: " + str(round(180 - deltaTime.total_seconds())) + "  Score: " +str(Score))
                     lastDelta = 180 - deltaTime.total_seconds()
       pos = mc.player.getTilePos()
       if(int(pos.x)==x and int(pos.z)==z):
               mc.setBlock(x,y,z,0)
               x=random.randint(102,154)
               y=72
               random.randint(347,396)
               mc.setBlock(x,y,z,41)
               Score+=1
               time.sleep(0.1)
       if(Score%10 == 0 and Score > 9):
              lastDelta - 10
              time.sleep(0.1)
              
   
