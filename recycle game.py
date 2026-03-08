import pgzrun
import random
WIDTH=800
HEIGHT=600
finallevel=6
startspeed=10
items=["bag","bottle","battery","chips"]
gameover=False
gamecomplete=False
currentlevel=1
animations=[]
currentitems=[]
def draw ():
    global currentitems,currentlevel,gameover,gamecomplete
    screen.clear()
    screen.fill((50,255,0))
    if gameover:
        screen.draw.text("gameover",fontsize=60,center=(400,300))
    elif gamecomplete:
        screen.draw.text("you won ",fontsize=60,center=(400,300))
    else:
        for i in currentitems:
            i.draw()





def update():
    global currentitems
    if len(currentitems)==0:
        currentitems=make_items(currentlevel)


def get_option_to_create(extraitems):
    itemstocreate=["paper"]
    for i in range(extraitems):
        extra=random.choice(items)
        itemstocreate.append(extra)
    return itemstocreate
def create_items(itemstocreate):
    newitems=[]
    for i in itemstocreate:
        item=Actor(i)
        newitems.append(item)
    return newitems
def over():
    global gameover
    gameover=True
def on_mouse_down(pos):
    global currentitems,currentlevel
    for i in currentitems:
        if i.collidepoint(pos):
            if"paper"in i.image:
                complete()
            else:
                over()
def complete():
    global currentlevel,currentitems,animations,gamecomplete
    stop_animations(animations)
    if currentlevel==finallevel:
        gamecomplete=True
    else:
        currentlevel=currentlevel+1
        currentitems=[]
        animations=[]



def stop_animations(stop_animation):
    for i in stop_animation:
        if i.running:
            i.stop()

def layout_items(item_to_layout):
    gaps=len(item_to_layout)+1
    gaps_size=WIDTH/gaps
    random.shuffle(item_to_layout)
    for i,j in enumerate(item_to_layout):
        new_x=(i+1)*gaps_size
        j.x=new_x
def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration=startspeed-currentlevel
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,on_finished=over,y=HEIGHT)
        animations.append(animation)
def make_items(extra_items):
    items_to_create= get_option_to_create(extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
pgzrun.go()
