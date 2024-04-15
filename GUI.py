import tkinter as tk
from tkinter import ttk
import Algorithm 
import PLOT

def calculate_seek_time():
    global res
    global algorithm
    requests = [int(req) for req in entry_requests.get().split()]
    head = int(entry_head_position.get())
    direction = "left" if radio_var.get() == 0 else "right"
    total_tracks = int(entry_total_tracks.get())
    algorithm = combo_scheduling_algorithm.get()
    
    res = []
    time = 0
    
    if algorithm == "FCFS":
        res, time = Algorithm.fcfs(requests, head)
    elif algorithm == "SSTF":
        res, time = Algorithm.sstf(requests, head)
    elif algorithm == "SCAN":
        res, time = Algorithm.scan(requests, head, direction, total_tracks)
    elif algorithm == "LOOK":
        res, time = Algorithm.look(requests, head, direction)
    elif algorithm == "C-LOOK":
        res, time = Algorithm.c_look(requests, head, direction)
    elif algorithm == "C-SCAN":
        res, time = Algorithm.c_scan(requests, head, direction, total_tracks)
        
    res.insert(0, head)
    change_text(res, time)
    show()

def show():
    PLOT.show(res,algorithm)    
def change_text(res,time):
    entry_order_requests.config(text=res)
    entry_total_seek_time.config(text=time)
def show_input(event):
    selected_algorithm = combo_scheduling_algorithm.get()
    if selected_algorithm in ["SCAN", "LOOK", "C-LOOK", "C-SCAN"]:
        entry_total_tracks.grid(row=12, column=2, padx=5, pady=5)
        label_total_tracks.grid(row=12, column=1, padx=5, pady=5)
        label_direction.grid(row=14, column=1, padx=5, pady=5)
        radio_left.grid(row=14, column=2, padx=5, pady=5)
        radio_right.grid(row=14, column=3, padx=5, pady=5)
    else:
        entry_total_tracks.grid_remove()
        label_total_tracks.grid_remove()
        label_direction.grid_remove()
        radio_left.grid_remove()
        radio_right.grid_remove()

window = tk.Tk()
window.title("Disk Scheduling")
window.geometry("573x400")

# Entry widget for disk requests
entry_requests = tk.Entry(window, width=20, font=("Helvetica", 10))
entry_requests.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
label_requests = tk.Label(window, text="Enter the disk requests (space-separated):", font=("Helvetica", 10))
label_requests.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Entry widget for head position
entry_head_position = tk.Entry(window, width=20, font=("Helvetica", 10))
entry_head_position.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
label_head_position = tk.Label(window, text="Enter the head position:", font=("Helvetica", 10))
label_head_position.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# Combobox for scheduling algorithm
scheduling_algorithms = ["FCFS", "SSTF", "SCAN", "LOOK", "C-LOOK", "C-SCAN"]
combo_scheduling_algorithm = ttk.Combobox(window, values=scheduling_algorithms, font=("Helvetica", 10))
combo_scheduling_algorithm.current(0)  
combo_scheduling_algorithm.grid(row=6, column=1, columnspan=2, padx=5, pady=5)
combo_scheduling_algorithm.bind("<<ComboboxSelected>>", show_input)
label_scheduling_algorithm = tk.Label(window, text="Select Scheduling Algorithm:", font=("Helvetica", 10))
label_scheduling_algorithm.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

# Label for order of requests
label_order_requests = tk.Label(window, text="Order of Requests:", font=("Helvetica", 10))
label_order_requests.grid(row=8, column=1, padx=5, pady=5)
entry_order_requests = tk.Label(window, text="", font=("Helvetica", 10))
entry_order_requests.grid(row=8, column=2, padx=5, pady=5)

# Label for total seek time
label_total_seek_time = tk.Label(window, text="Total Seek Time:", font=("Helvetica", 10))
label_total_seek_time.grid(row=9, column=1, padx=5, pady=5)
entry_total_seek_time = tk.Label(window, text="", font=("Helvetica", 10))
entry_total_seek_time.grid(row=9, column=2, padx=5, pady=5)

# Entry widget for total number of tracks
entry_total_tracks = tk.Entry(window, width=20, font=("Helvetica", 10))
entry_total_tracks.insert(0, "0")
label_total_tracks = tk.Label(window, text="Enter the total number of tracks:", font=("Helvetica", 10))

# Radio buttons for direction
radio_var = tk.IntVar()
radio_left = tk.Radiobutton(window, text="Left (Toward Lower)", variable=radio_var, value=0, font=("Helvetica", 10))
radio_right = tk.Radiobutton(window, text="Right (Toward Inner)", variable=radio_var, value=1, font=("Helvetica", 10))
label_direction = tk.Label(window, text="Enter the direction:", font=("Helvetica", 10))

button_calculate = tk.Button(window, text="Calculate", command=calculate_seek_time, font=("Helvetica", 10))
button_calculate.grid(row=15, column=2, columnspan=3, padx=5, pady=5)

window.mainloop()
