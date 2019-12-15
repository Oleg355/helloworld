import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import keyboard
def chikibamboni():
    mc.setBlocks(pos.x+2,pos.y,pos.z-2,pos.x+3,pos.y+5,pos.z-1,35)
    mc.setBlocks(pos.x+2,pos.y,pos.z+2,pos.x+3,pos.y+5,pos.z+1,35)
    mc.setBlocks(pos.x-2,pos.y,pos.z-2,pos.x-3,pos.y+5,pos.z-1,35)
    mc.setBlocks(pos.x-2,pos.y,pos.z+2,pos.x-3,pos.y+5,pos.z+1,35)
    mc.setBlocks(pos.x+3,pos.y+5,pos.z+2,pos.x-3,pos.y+9,pos.z-2,35)
    mc.setBlocks(pos.x+3,pos.y+9,pos.z+1,pos.x+5,pos.y+11,pos.z-1,35)
    mc.postToChat("1")
while True:
    pos = mc.player.getTilePos()
    if keyboard.is_pressed('c'):
        chikibamboni()
