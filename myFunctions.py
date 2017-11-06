



def polygon(t, s, d):
    a = 360/s



    for times in range(s):
        t.forward(d)
        t.right(a)





def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()



def cool(t,d,c1,c2):
    t.color(c1)
    polygon(t,4,d)
    t.color(c2)
    polygon(t,3,d)
        
        
