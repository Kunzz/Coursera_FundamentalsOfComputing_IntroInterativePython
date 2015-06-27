# template for "Stopwatch: The Game"

# define global variables
import simplegui
message=("%s:%s%s.%s" %(0,0,0,0))
fun=("%s/%s" %(0,0)) 
t=0
counter1=0
counter2=0
#flag=0 reset the play register
flag=1
# flag2 is set to avoid updating by clicking "Stop" button w
# when the stop watch is stopped
flag2=1

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(x):
    global message
    global D
    global t
    t=x
    A=int(t/600)
    B=int((t-A*600)/100)
    C=int((t-A*600-B*100)/10)
    D=t-A*600-B*100-C*10   
    message=("%s:%s%s.%s" %(A,B,C,D))
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global timer
    global flag2
    #timer = simplegui.create_timer(100, interval)
    frame.set_draw_handler(draw_handler)
    timer.start()
    flag2=1

def stop():
    global flag
    global flag2
    timer.stop()
    flag=1
    if flag2==1:
        register()
        
    
def reset():
    global flag
    global flag2
    timer.stop()
    format(0)
    flag=0
    flag2=1
    register()
    frame.set_draw_handler(draw_handler)
   

# define event handler for timer with 0.1 sec interval
def interval():
    global t
    t=t+1
    format(t)
    return t
    
# define draw handler

def draw_handler(canvas):
    canvas.draw_text(message, (90, 130), 30, 'White')
    canvas.draw_text(fun, (190, 190), 20, 'Grey')
    
# create frame
frame = simplegui.create_frame('Testing', 250, 250, 250)

# Opens frame with two buttons
button1 = frame.add_button('Start', start, 150)
button2 = frame.add_button('Stop', stop,  150)
button2 = frame.add_button('Reset', reset, 150)

# register event handlers
def register():
    global fun
    global counter1
    global counter2
    global flag2
    counter1=counter1+1
    if D==0 and (flag==1):
        counter2=counter2+1 
        fun=("%s/%s" %(counter2, counter1))  
        frame.set_draw_handler(draw_handler) 
        flag2=0
    elif (flag==0):
        counter1=0
        counter2=0
        fun=("%s/%s" %(counter2, counter1))
        frame.set_draw_handler(draw_handler) 
        flag2=0
    else:
        fun=("%s/%s" %(counter2, counter1))  
        frame.set_draw_handler(draw_handler)
        flag2=0
    
# start frame
frame.start()
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, interval)
# Please remember to review the grading rubric
