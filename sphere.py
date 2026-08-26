import math
import os
import time

a=0.0
b=0.0
width=80
height=40
for i in range(1,999999999):
    
    arr=[[" " for _ in range(width)] for _ in range (height)]
    arrZ=[[-99999 for _ in range(width)] for _ in range (height)]
    long=-math.pi/2
    point=0
    radius=4
    while long<math.pi/2:
        long+=0.05
        lat=0
        while lat<math.pi*2:
            lat+=0.05
            y=radius*math.sin(long)
            layerR=radius*math.cos(long)
            x=layerR*math.cos(lat)
            z=layerR*math.sin(lat)
            point+=1
            distance=8
            y1=y
            x1=x*math.cos(a)+z*math.sin(a)
            z1=z*math.cos(a)-x*math.sin(a)
            
            rotx=x1
            roty=y1*math.cos(b)-z*math.sin(b)
            rotz=z1*math.cos(b)+y1*math.sin(b)
            oz=1/(distance-rotz) if (distance-rotz)!=0 else 0
            screenX=int(width/2+(rotx*oz)*40)
            screenY=int(height/2+(roty*oz)*18)
            normal=math.sqrt(rotx**2+roty**2+rotz**2)
            nx=rotx/normal
            ny=roty/normal
            nz=rotz/normal
            
            lx,ly,lz=0.577,0.577,-0.577
            dp=nx*lx+ny*ly+nz*lz
            special=".,;=+"
            specialI=int((dp+1)/2*(len(special)-1))
            if 0<=screenX<width and 0<=screenY<height and rotz>arrZ[screenY][screenX]:
                arr[screenY][screenX]=special[specialI]
                arrZ[screenY][screenX]=rotz
                
    os.system("cls")
    print('\n'.join("".join(row) for row in arr))
    print(point)
    time.sleep(0.01)
    a+=0.06
    b+=0.06
    
    #projection...z=0 is centre, inside? space add/multiply??