from tkinter import *
import math
def clickvalue(value):
    ex = dataentry.get()
    answer = ''
    if value == 'C':
        ex = dataentry.get()
        ex = ex[0:len(ex) - 1]
        dataentry.delete(0,END)
        dataentry.insert(0, ex)
        return
    elif value == 'CE':
        dataentry.delete(0,END)
    elif value == '√':
        answer = math.sqrt(eval (ex))
    elif value == 'π':
        answer = math.pi

    elif value == 'cosθ':
        answer = math.cos(math.radians(eval(ex)))

    elif value == 'tanθ':
        answer = math.tan(math.radians(eval(ex)))

    elif value == 'sinθ':
        answer = math.sin(math.radians(eval(ex)))

    elif value == '2π':
        answer = 2 * math.pi

    elif value == 'cosh':
        answer = math.cosh(eval(ex))

    elif value == 'tanh':
        answer = math.tanh(eval(ex))

    elif value == 'sinh':
        answer = math.sinh(eval(ex))

    elif value == chr(8731):
        answer = eval(ex) ** (1 / 3)

    elif value == 'x\u02b8':
        dataentry.insert(END,'**')
        return

    elif value == 'x\u00B3':
        answer = eval(ex) ** 3

    elif value == 'x\u00B2':
        answer = eval(ex) ** 2

    elif value == 'ln':
        answer = math.log2(eval(ex))

    elif value == 'deg':
        answer = math.degrees(eval(ex))

    elif value == "rad":
        answer = math.radians(eval(ex))

    elif value == 'e':
        answer = math.e

    elif value == 'log10':
        answer = math.log10(eval(ex))

    elif value == 'x!':
        answer = math.factorial(ex)

    elif value == chr(247):  # 7/2=3.5
        dataentry.insert(END, "/")
        return

    elif value == '=':
        answer = eval(ex)

    else:
        dataentry.insert(END, value)
        return
    dataentry.delete(0, END)
    dataentry.insert(0, answer)

calculator = Tk()
calculator.title('Calculator')
calculator.config(bg = 'black', borderwidth=10)
calculator.geometry('700x500+100+100')   #width * height +x axis and y axis
dataentry = Entry(calculator, font = ('Times New Roman',15), bg = 'black',fg = 'white',borderwidth = 10,relief=SUNKEN,width = 50)
dataentry.place(x=0,y =0,relwidth=1)
#C button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'C',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'C' : clickvalue(button))
button.place(x =0,y =50)
# CE button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'CE',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'CE' : clickvalue(button))
button.place(x=70,y =50)
#sqrt button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '√',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '√' : clickvalue(button))
button.place(x =140,y = 50)
# + button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '+',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '+' : clickvalue(button))
button.place(x =210,y =50)
# pi  button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'π',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'π' : clickvalue(button))
button.place(x =280,y =50)
# cosθ button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'cosθ',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'cosθ' : clickvalue(button))
button.place(x =350,y =50)
#tanθ button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'tanθ',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'tanθ' : clickvalue(button))
button.place(x =420,y =50)
#sin(θ) button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'sinθ',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'sinθ' : clickvalue(button))
button.place(x =490,y =50)

#1st row completed..............................
#1 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '1',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '1' : clickvalue(button))
button.place(x =0,y =115)
#2 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '2',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '2' : clickvalue(button))
button.place(x =70,y =115)
#3 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '3',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '3' : clickvalue(button))
button.place(x =140,y =115)
# - button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '-',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '-' : clickvalue(button))
button.place(x =210,y =115)
#2π button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '2π',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '2π' : clickvalue(button))
button.place(x =280,y =115)
#cosh button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'cosh',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'cosh' : clickvalue(button))
button.place(x =350,y =115)
#tanh button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'tanh',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'tanh' : clickvalue(button))
button.place(x =420,y =115)
#sinh button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'sinh',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'sinh' : clickvalue(button))
button.place(x =490,y =115)


# 2nd row completed.................................


# 4 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '4',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '4' : clickvalue(button))
button.place(x =0,y =180)
# 5 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '5',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '5' : clickvalue(button))
button.place(x =70,y =180)
# 6 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '6',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '6' : clickvalue(button))
button.place(x =140,y =180)
# * button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '*',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '*' : clickvalue(button))
button.place(x =210,y =180)
# cube root button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text =chr(8731),bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = chr(8731) : clickvalue(button))
button.place(x =280,y =180)
#exponential function
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'x\u02b8',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button='x\u02b8': clickvalue(button))
button.place(x =350,y =180)
#  sqaure button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'x\u00b3',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button='x\u00b3': clickvalue(button))
button.place(x =420,y =180)
# cube button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'x\u00B2',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button ='x\u00B2' : clickvalue(button))
button.place(x =490,y =180)

#3 rd row completed.....................................

# 7 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '7',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '7' : clickvalue(button))
button.place(x =0,y =245)
# 8 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '8',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '8' : clickvalue(button))
button.place(x =70,y =245)
# 9 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '9',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '9' : clickvalue(button))
button.place(x =140,y =245)
# divide button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '/',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '/' : clickvalue(button))
button.place(x =210,y =245)
#natural loagrthmic function
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'ln',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'ln' : clickvalue(button))
button.place(x =280,y =245)
#degree conversion button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'deg',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'deg' : clickvalue(button))
button.place(x =350,y =245)
#Radian button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'rad',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'rad' : clickvalue(button))
button.place(x =420,y =245)
# e button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'e',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'e' : clickvalue(button))
button.place(x =490,y =245)

# 4th row completed.................................................

# 0 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '0',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '0' : clickvalue(button))
button.place(x =0,y =310)
# decimal or dot button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '.',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '.' : clickvalue(button))
button.place(x =70,y =310)
# modulus button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '%',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '%' : clickvalue(button))
button.place(x =140,y =310)
# equal to button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '=',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '=' : clickvalue(button))
button.place(x =210,y =310)
# log 10 button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'log10',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'log10' : clickvalue(button))
button.place(x =280,y =310)
# left pparanthesis button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = '(',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = '(' : clickvalue(button))
button.place(x =350,y =310)
# right paranthesis button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = ')',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = ')' : clickvalue(button))
button.place(x =420,y =310)
#factorial button
button = Button(calculator,height = 2,width = 5,bd =2,relief =SUNKEN,text = 'x!',bg ='black',
                fg ='white',font = ('Times New Roman',15,'bold'),activebackground='black',
                command = lambda button = 'x!' : clickvalue(button))
button.place(x =490,y =310)
calculator.mainloop()