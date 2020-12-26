from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z = mc.player.getTilePos()

number = 1
for i in range(12):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    number = number*2
    mc.postToChat("生成了"+str(number)+"之蠹魚")
    time .sleep(0.5)
