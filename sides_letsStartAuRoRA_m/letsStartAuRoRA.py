# Alexandre Caldeira 02/08 

import os 

parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

!mkdir robots
!mkdir tools
!mkdir worlds
!mkdir strats
!mkdir sides

robs = parent+'/robots'
accs = parent+'/tools'
envs = parent+'/worlds'
stts = parent+'/strats'
side = parent+'/sides'
aurora = [robs,accs,envs,stts,side]

for dir in aurora:
    if not os.path.exists(dir):
        os.mkdir(dir)
