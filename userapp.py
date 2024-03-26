# needed imports
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras import layers

# STEP 1: save the model in the Jupyter -notebook (for example
# mobilephoneprices.keras)
# we'll use the lecture4 / ann_classification_example1.ipynb

# STEP 2: load the model, and test it briefly
# loading the model from file, see that you also have the folder correctly
model = keras.saving.load_model('Dataset1.keras')

print("Testing")


import tkinter
 
# Creating the GUI window.
window = tkinter.Tk()
window.title("Deep learning GUI")
window.geometry("800x800")
window.option_add("*font", "lucida 12 bold")
 
#    'national_rank': 20,
#    'quality_of_education': 300,
#    'alumni_employment': 300,
#    'quality_of_faculty': 200,
#    'publications': 175,
#    'influence': 500,
#    'citations': 160,
#    'broad_impact': 500,
#    'patents': 500,
#    'score': 150,
#    'year': 2015

# make a text label for the first Entry
label1 = tkinter.Label(window, text="National rank")
label1.pack(pady=4)

# Creating our text widget.
entry_nat_rank = tkinter.Entry(window)
entry_nat_rank.pack(pady=0)

# make a text label for the first Entry
label2 = tkinter.Label(window, text="Quality of education")
label2.pack(pady=4)

# Creating our text widget.
entry_quality = tkinter.Entry(window)
entry_quality.pack(pady=0)

# make a text label for the first Entry
label3 = tkinter.Label(window, text="Alumni employment")
label3.pack(pady=4)

# Creating our text widget.
entry_empl = tkinter.Entry(window)
entry_empl.pack(pady=0)

# make a text label for the first Entry
label4 = tkinter.Label(window, text="Quality of faculty")
label4.pack(pady=4)

# Creating our text widget.
entry_qual_of_fac = tkinter.Entry(window)
entry_qual_of_fac.pack(pady=0)

# make a text label for the first Entry
label5 = tkinter.Label(window, text="Publications")
label5.pack(pady=4)

# Creating our text widget.
entry_publications = tkinter.Entry(window)
entry_publications.pack(pady=0)

# make a text label for the first Entry
label6 = tkinter.Label(window, text="Influence")
label6.pack(pady=4)

# Creating our text widget.
entry_influence= tkinter.Entry(window)
entry_influence.pack(pady=0)

# make a text label for the first Entry
label7 = tkinter.Label(window, text="Citations")
label7.pack(pady=4)

# Creating our text widget.
entry_citations = tkinter.Entry(window)
entry_citations.pack(pady=0)

# make a text label for the first Entry
label8 = tkinter.Label(window, text="Broad impact")
label8.pack(pady=4)

# Creating our text widget.
entry_impact = tkinter.Entry(window)
entry_impact.pack(pady=0)

# make a text label for the first Entry
label9 = tkinter.Label(window, text="Patents")
label9.pack(pady=4)

# Creating our text widget.
entry_patents = tkinter.Entry(window)
entry_patents.pack(pady=0)

# make a text label for the first Entry
label10 = tkinter.Label(window, text="Score")
label10.pack(pady=4)

# Creating our text widget.
entry_score = tkinter.Entry(window)
entry_score.pack(pady=0)

# make a text label for the first Entry
label11 = tkinter.Label(window, text="Year")
label11.pack(pady=4)

# Creating our text widget.
entry_year = tkinter.Entry(window)
entry_year.pack(pady=0)


# Creating the function to set the text 
# with the help of button
def set_text_by_button():
    tester_row = {
        'battery_power': int(entry_nat_rank.get()), 
        'dual_sim': int(entry_quality.get()) ,
        'fc': int(entry_empl.get()), 
        'int_memory': int(entry_qual_of_fac.get()), 
        'n_cores': int(entry_publications.get()), 
        'pc': int(entry_influence.get()),
        'px_height': int(entry_citations.get()),
        'px_width': int(entry_impact.get()), 
        'ram': int(entry_patents.get()), 
        'sc_h': int(entry_score.get()), 
        'sc_w': int(entry_year.get()), 
    }

    # convert to pandas-format
    tester_row = pd.DataFrame([tester_row])
    result = model.predict(tester_row)[0]
    result = result.round(0)

    # print the result
    result_string.set(f"Predicted World rank: {result}")
 
 
# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Set", 
                    command=set_text_by_button)

set_up_button.pack(pady=10)
 
# the result text we will change with the function
# this is connected to the label below
result_string = tkinter.StringVar()
result_string.set("Waiting for user input...")

# make a text label for the first Entry
label_result = tkinter.Label(window, textvariable=result_string, fg="red")
label_result.pack(pady=4)


window.mainloop()
