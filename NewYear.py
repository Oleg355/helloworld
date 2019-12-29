import time
import mcpi.minecraft as minecraft
import mcpi.block as block
import keyboard
a = 0.5
if keyboard.is_pressed('u'):
    a=a+0.1
if keyboard.is_pressed('i'):
    a=a-0.1
def b(x,y):
    return block.Block(x,y)
lis = [b(35,14),b(35,1),b(35,4),b(35,5),b(35,11)]
mc = minecraft.Minecraft.create()
tree = block.Block(35,13)
mc.setBlocks(29999983,99,87,29999958,0,62,0)
mc.setBlocks(29999983,72,87,29999958,72,62,80)
mc.setBlocks(29999969,73,76,29999975,73,70,tree)
mc.setBlocks(29999974,74,75,29999970,74,71,tree)
mc.setBlocks(29999971,75,72,29999973,75,74,tree)
mc.setBlocks(29999974,76,75,29999970,76,71,tree)
mc.setBlocks(29999971,77,72,29999973,77,74,tree)
mc.setBlock(29999972,78,73,tree)
while True:
    for i in lis:
        
        mc.setBlock(29999973,74,70,i)
        time.sleep(a)
