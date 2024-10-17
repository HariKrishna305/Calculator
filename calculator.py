from tkinter import *


mani_window = Tk()
mani_window.title('Calculator')


def clear():
    displaybox.delete(0, END)



def btn_click(num):
    current_num = displaybox.get()
    clear()
    final_num = current_num + num
    displaybox.insert(0, final_num)

first_num = 0
math = ''

def calc(math_type):
    global first_num, math
    math = math_type
    first_num = displaybox.get()
    clear()


def equal():
    result = ''
    global first_num
    second_num = displaybox.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        result = int(first_num) / int(second_num)
    elif math == 'modulus':
        result = int(first_num) % int(second_num)
    elif math == 'exponential':
        result = int(first_num) ** int(second_num)



    displaybox.insert(0, str(result))



## Createing Widgets 
### cration of the buttons
displaybox = Entry(mani_window, width=14, font=('Arial', 28), justify=RIGHT)

btn_0 = Button(mani_window, text='0', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('0'))
btn_1 = Button(mani_window, text='1', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('1'))
btn_2 = Button(mani_window, text='2', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('2'))
btn_3 = Button(mani_window, text='3', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('3'))
btn_4 = Button(mani_window, text='4', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('4'))
btn_5 = Button(mani_window, text='5', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('5'))
btn_6 = Button(mani_window, text='6', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('6'))
btn_7 = Button(mani_window, text='7', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('7'))
btn_8 = Button(mani_window, text='8', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('8'))
btn_9 = Button(mani_window, text='9', padx=36, pady=10, font=('Arial', 14),command=lambda: btn_click('9'))



btn_clear = Button(mani_window, text='clear', padx=75.2, pady=10, font=('Arial', 14), command=clear)
btn_sin = Button(mani_window, text='sin', padx=29, pady=10, font=('Arial', 14),command=lambda: btn_click('sin')) 
btn_cos = Button(mani_window, text='cos', padx=30, pady=10, font=('Arial', 14),command=lambda: btn_click('cos'))
btn_tan= Button(mani_window, text='tan', padx=29, pady=10, font=('Arial', 14),command=lambda: btn_click('tan'))
btn_exponential = Button(mani_window, text='**', padx=34, pady=10, font=('Arial', 14), command=lambda: calc('exponential'))
btn_log = Button(mani_window, text='log', padx=34, pady=10, font=('Arial', 14),command=lambda: btn_click('log'))
btn_pi = Button(mani_window, text='pi', padx=34, pady=10, font=('Arial', 14),command=lambda: btn_click('pi'))
btn_modulus = Button(mani_window, text='%', padx=32, pady=10, font=('Arial', 14), command=lambda: calc('modulus'))
btn_mul = Button(mani_window, text='*', padx=43, pady=10, font=('Arial', 14), command=lambda: calc('mul'))
btn_sub = Button(mani_window, text='-', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('sub'))
btn_div = Button(mani_window, text='/', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('div'))
btn_add = Button(mani_window, text='+', padx=40, pady=10, font=('Arial', 14), command=lambda: calc('add'))
btn_equal = Button(mani_window, text='=', padx=36, pady=10, font=('Arial', 14), command=equal)




# Showing Widgets

btn_equal.grid(row=8, column=2, padx=2, pady=2)
btn_add.grid(row=8, column=1, padx=2, pady=2)
btn_div.grid(row=8, column=0, padx=2, pady=2)

btn_sub.grid(row=7, column=2, padx=2, pady=2)
btn_mul.grid(row=7, column=1, padx=2, pady=2)
btn_modulus.grid(row=7, column=0, padx=2, pady=2)

btn_pi.grid(row=6, column=2, padx=2, pady=2)
btn_log.grid(row=6, column=1, padx=2, pady=2)
btn_exponential.grid(row=6, column=0, padx=2, pady=2)

btn_tan.grid(row=5, column=2, padx=2, pady=2)
btn_cos.grid(row=5, column=1, padx=2, pady=2)
btn_sin.grid(row=5, column=0, padx=2, pady=2)


btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
btn_0.grid(row=4, column=0, padx=2, pady=2)


btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

 
displaybox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


mani_window.mainloop()
                                    








                                    