from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
pos = mc.player.getTilePos()
mc.setBlocks(pos.x+1,pos.y,pos.z,pos.x+1,pos.y+3,pos.z,35)
a = 0
b = pos.y
while True:
    while a<=3:
        mc.setBlock(pos.x+1,b,pos.z,41)
        b+=1
        a += 1
        time.sleep(1)
    while a>0:
        mc.setBlock(pos.x+1,b-1,pos.z,35)
        b -= 1
        a -= 1
        time.sleep(1)
