from tkinter import *
from tkinter import ttk

#cores
cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#333230"
cor4 = "#424140"
cor5 = "#b55e14"


# create window
window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg=cor1)

# create frames
frame_window = Frame(window, width=235, height=50, bg=cor3)
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# CREATE FUNCTIONS

all_values = ''
text_value = StringVar()

def log_values(event):
    global all_values
    all_values += str(event)
    
    # value to string
    text_value.set(all_values)

def calculate():
    global all_values
    result = eval(all_values)
    
    text_value.set(str(result))

def clear():
    global all_values
    all_values = ''
    text_value.set(all_values)


# CREATE LABEL
app_label = Label(frame_window, textvariable=text_value, width=16,
                  height=2, padx=7, relief="flat", anchor="e", justify="right", 
                  font=("Ivy 18"), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# CREATE BUTTONS
# first line
button1 = Button(frame_body,command=clear, text="C", width=11, height=2, bg=cor5,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button1.place(x=0, y=0)
button2 = Button(frame_body,command=lambda: log_values("%"), text="%", width=5, height=2, bg=cor5,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button2.place(x=118.5, y=0)
button3 = Button(frame_body,command=lambda: log_values("/"), text="/", width=5, height=2, bg=cor5,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button3.place(x=177, y=0)

# second line
button4 = Button(frame_body,command=lambda:log_values("7"), text="7", width=5, height=2, bg=cor4, fg=cor2,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button4.place(x=0, y=52)
button5 = Button(frame_body,command=lambda:log_values("8"), text="8", width=5, height=2, bg=cor4, fg=cor2,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button5.place(x=59, y=52)
button6 = Button(frame_body,command=lambda:log_values("9"), text="9", width=5, height=2, bg=cor4, fg=cor2,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button6.place(x=118, y=52)
button7 = Button(frame_body,command=lambda:log_values("*"), text="*", width=5, height=2, bg=cor5,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button7.place(x=177, y=52)

# third line
button8 = Button(frame_body,command=lambda:log_values("4"), text="4", width=5, height=2, bg=cor4, fg=cor2,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button8.place(x=0, y=104)
button9 = Button(frame_body,command=lambda:log_values("5"), text="5", width=5, height=2, bg=cor4, fg=cor2,
             font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button9.place(x=59, y=104)
button10 = Button(frame_body,command=lambda:log_values("6"), text="6", width=5, height=2, bg=cor4, fg=cor2,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button10.place(x=118, y=104)
button11 = Button(frame_body,command=lambda:log_values("-"), text="-", width=5, height=2, bg=cor5,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button11.place(x=177, y=104)

# fourth line
button12 = Button(frame_body,command=lambda:log_values("1"), text="1", width=5, height=2, bg=cor4, fg=cor2,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button12.place(x=0, y=156)
button13 = Button(frame_body,command=lambda:log_values("2"), text="2", width=5, height=2, bg=cor4, fg=cor2,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button13.place(x=59, y=156)
button14 = Button(frame_body,command=lambda:log_values("3"), text="3", width=5, height=2, bg=cor4, fg=cor2,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button14.place(x=118, y=156)
button15 = Button(frame_body,command=lambda:log_values("+"), text="+", width=5, height=2, bg=cor5,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button15.place(x=177, y=156)

# fifth line
button16 = Button(frame_body,command=lambda:log_values("0"), text="0", width=11, height=2, bg=cor4, fg=cor2,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button16.place(x=0, y=208)
button17 = Button(frame_body,command=lambda:log_values("."), text=".", width=5, height=2, bg=cor4, fg=cor2,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button17.place(x=118.5, y=208)
button18 = Button(frame_body,command=calculate, text="=", width=5, height=2, bg=cor5,
              font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
button18.place(x=177, y=208)


window.mainloop()
