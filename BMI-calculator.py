from tkinter import *

window = Tk()
window.title("BMİ Calculator")
window.minsize(width = 300,height= 300)
window.config(bg="light blue")

def calculate_bmi():
    height = enter_height.get()
    weight = enter_weight.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height")

    else:
        try:
            bmi = float(weight)/((float(height) /100) **2)
            result_string = write_result(bmi)
            result_label.config(text= result_string)
        except:
            result_label.config(text="please enter a valid number")



your_weight = Label(text="Enter Your Weight: (kg)",bg="white",width=20)
your_weight.pack()

enter_weight = Entry(bg="white",width=24,)
enter_weight.pack()

your_height = Label(text="Enter Your Height: (cm)",bg="white",width=20)
your_height.pack()

enter_height = Entry(bg="white",width=24,)
enter_height.pack()

button = Button(text="Calculate",command=calculate_bmi)
button.pack()

result_label = Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string


window.mainloop()