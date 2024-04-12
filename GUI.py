import tkinter as tk
from tkinter import ttk
import Algorithm 
import PLOT

res=[]
algorithm=""

def calculate_seek_time():
    global res
    global algorithm
    requests=entry_requests.get().split(" ")
    for i in range(len(requests)):
        requests[i]=int(requests[i])
    head=int(entry_head_position.get())
    dir= "left" if radio_var.get()==0 else "right"
    total=int(entry_total_tracks.get())
    algorithm=combo_scheduling_algorithm.get()
    
    match algorithm:
        case "FCFS":
            res , time=Algorithm.fcfs(requests,head)
            change_text(res,time)
            res.insert(0,head)
            print(res,time)
            pass
        case "SSTF":
            res , time=Algorithm.sstf(requests,head)
            change_text(res,time)
            res.insert(0,head)
            print(res,time)
            pass
        case "SCAN":
            res , time=Algorithm.scan(requests,head,dir,total)
            change_text(res,time)
            res.insert(0,head)
            print(res,time)
            pass
        case "LOOK":
            res , time=Algorithm.look(requests,head,dir)
            change_text(res,time)
            res.insert(0,head)
            print(res,time)
            pass
        case "C-LOOK":
            res , time=Algorithm.c_look(requests,head,dir)
            change_text(res,time)
            res.insert(0,head)
            print(res,time)
            pass
        case "C-SCAN":
            res , time=Algorithm.c_scan(requests,head,dir,total)
            change_text(res,time)
            res.insert(0,head)
            print(res,time)
            pass
def show():
    PLOT.show(res,algorithm)    
def change_text(res,time):
    entry_order_requests.config(text=res)
    entry_total_seek_time.config(text=time)
window = tk.Tk()
window.title("Disk Scheduling")
window.geometry("573x400")

# Background image
# bg = tk.PhotoImage(file="bg.png")
# label_bg = tk.Label(window, image=bg)
# label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# Entry widget for disk requests
entry_requests = tk.Entry(window, width=20)
entry_requests.grid(row=2, column=1, columnspan=2)
label_requests = tk.Label(window, text="Enter the disk requests (space-separated):")
label_requests.grid(row=1, column=1, columnspan=2)

# Entry widget for head position
entry_head_position = tk.Entry(window, width=20)
entry_head_position.grid(row=4, column=1, columnspan=2)
label_head_position = tk.Label(window, text="Enter the head position:")
label_head_position.grid(row=3, column=1, columnspan=2)

# Combobox for scheduling algorithm
scheduling_algorithms = ["FCFS", "SSTF","SCAN","LOOK","C-LOOK","C-SCAN"]  # Add more algorithms as needed
combo_scheduling_algorithm = ttk.Combobox(window, values=scheduling_algorithms)
combo_scheduling_algorithm.current(0)  
combo_scheduling_algorithm.grid(row=6, column=1, columnspan=2)
label_scheduling_algorithm = tk.Label(window, text="Select Scheduling Algorithm:")
label_scheduling_algorithm.grid(row=5, column=1, columnspan=2)

# Label for order of requests
label_order_requests = tk.Label(window, text="Order of Requests:")
label_order_requests.grid(row=8, column=1)
entry_order_requests = tk.Label(window, text="")
entry_order_requests.grid(row=8, column=2)

# Label for total seek time
label_total_seek_time = tk.Label(window, text="Total Seek Time:")
label_total_seek_time.grid(row=9, column=1)
entry_total_seek_time = tk.Label(window, text="")
entry_total_seek_time.grid(row=9, column=2)


# Entry widget for total number of tracks
entry_total_tracks = tk.Entry(window, width=20 )
entry_total_tracks.insert(0,"0")
entry_total_tracks.grid(row=12, column=2)
label_total_tracks = tk.Label(window, text="Enter the total number of tracks:")
label_total_tracks.grid(row=12, column=1)

# Radio buttons for direction
radio_var = tk.IntVar()
radio_left = tk.Radiobutton(window, text="Left (Toward Lower)", variable=radio_var, value=0)
radio_left.grid(row=14, column=2)
radio_right = tk.Radiobutton(window, text="Right (Toward Inner)", variable=radio_var, value=1)
radio_right.grid(row=14, column=3)
label_direction = tk.Label(window, text="Enter the direction:")
label_direction.grid(row=14, column=1)

# Button to display results
button_display_results = tk.Button(window, text="Display Results", command=show )
button_display_results.grid(row=15, column=1, columnspan=3)
# Button to calculate
button_calculate = tk.Button(window, text="Calculate", command=calculate_seek_time)
button_calculate.grid(row=15, column=2,columnspan=3)

window.mainloop()
