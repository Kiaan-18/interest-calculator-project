from tkinter import*
from tkinter import messagebox
def calculate_interest():
    try:
       P=float(principal_entry.get())
       T=float(time_entry.get())
       R=float(rate_entry.get())
       SI=(P*T*R)/100
       CI=P*((1+R/100)**T)-P
       result_label.config(text=f"Simple Interest:{SI:.2f}\nCompound interest:{CI:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter valid numeric values")
root=Tk()
root.title("Age Calculator App")
root.geometry("400x400")
input_frame=Frame(root,padx=20,pady=20)
input_frame.pack(pady=20)
Label(input_frame,text="Principal:").grid(row=0,column=0,sticky=E,pady=5)
principal_entry=Entry(input_frame)
principal_entry.grid(row=0,column=1,pady=5)
Label(input_frame,text="Time(years):").grid(row=1,column=0,sticky=E,pady=5)
time_entry=Entry(input_frame)
time_entry.grid(row=1,column=1,pady=5)
Label(input_frame,text="Rate of interest(%):").grid(row=2,column=0,sticky=E,pady=5)
rate_entry=Entry(input_frame)
rate_entry.grid(row=2,column=1,pady=5)
Button(root,text="Calculate Interest",command=calculate_interest,bg='lightblue').pack(pady=20)
result_label=Label(root,text="",font=("Arial",12),fg="green")
result_label.pack(pady=10)
root.mainloop()