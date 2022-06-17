# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:33:37 2022

@author: -
"""

from tkinter import *

root=Tk()
root.geometry("600x600")
root.title("Fever Analysis Report")
root.configure(bg="light blue")

question1_rb=StringVar(value=0)
Question1=Label(root, text="Do you have a headache or a sore throat?")
Question1.pack()
q1_r1=Radiobutton(root, text="yes", variable=question1_rb, value="yes")
q1_r1.pack()
q1_r2=Radiobutton(root, text="no", variable=question1_rb, value="no")
q1_r2.pack()

question2_rb=StringVar(value=0)
Question2=Label(root, text="Is your body temperature high?")
Question2.pack()
q2_r1=Radiobutton(root, text="yes", variable=question2_rb, value="yes")
q2_r1.pack()
q2_r2=Radiobutton(root, text="no", variable=question2_rb, value="no")
q2_r2.pack()

question3_rb=StringVar(value=0)
Question3=Label(root, text="Are there any symptoms of eye redness?")
Question3.pack()
q3_r1=Radiobutton(root, text="yes", variable=question3_rb, value="yes")
q3_r1.pack()
q3_r2=Radiobutton(root, text="no", variable=question3_rb, value="no")
q3_r2.pack()

def fever_score():
    score=0
    if question1_rb.get()=="yes":
        score=score+20
        print(score)
        
    if question2_rb.get()=="yes":
        score=score+20
        print(score)
        
    if question3_rb.get()=="yes":
        score=score+20
        print(score)
        
    if score<=20:
        messagebox.showinfo("Report","You don't need to visit a doctor")
    elif score>20 and score<=40:
        messagebox.showinfo("Report","You might need to visit a doctor")
    else:
        messagebox.showinfo("Report","You are strongly advised to visit a doctor")
btn=Button(root, text="Analyze", bg="blue",fg="white", command=fever_score)
btn.pack()
root.mainloop()
        
        
        
        
        
        
        
        
        
        
        