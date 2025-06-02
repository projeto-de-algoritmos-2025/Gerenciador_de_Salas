import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

activities = [
    "Artes",
    "Música",
    "Educação Física",
    "Ballet",
    "Teatro",
    "Dança",
    "Yoga",
    "Meditação",
    "Oficina de Artesanato",
    "Canto"
]

def convert_to_ampm(hour):
    if hour == 0:
        return "12 AM"
    elif hour < 12:
        return f"{hour} AM"
    elif hour == 12:
        return "12 PM"
    else:
        return f"{hour - 12} PM"

class Reservation:
    def __init__(self, id, activity, start, end):
        self.id = id
        self.activity = activity
        self.start = start
        self.end = end

def generate_reservations(n, max_time=24):
    reservations = []
    for i in range(1, n+1):
        start = random.randint(0, max_time - 2)  
        end = random.randint(start + 1, max_time)
        activity = random.choice(activities)
        reservations.append(Reservation(i, activity, start, end))
    return reservations

def max_non_overlapping_reservations(reservations):
    
    sorted_res = sorted(reservations, key=lambda r: r.end)
    selected = []
    current_end = -1
    for r in sorted_res:
        if r.start >= current_end:
            selected.append(r)
            current_end = r.end
    return selected

class ReservationApp:
    def __init__(self, root): 
        self.root = root
        self.root.title("Reserva - Sala Multiuso (Atividades)")
        self.root.geometry("1000x700")
        
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Número de pedidos de reserva:", font=("Arial", 12)).pack(side=tk.LEFT)
        self.entry = tk.Entry(frame, width=5, font=("Arial", 12))
        self.entry.insert(0, "10")
        self.entry.pack(side=tk.LEFT, padx=10)

        self.btn = tk.Button(frame, text="Gerar e Agendar", font=("Arial", 12), bg="#2196F3", fg="white",
                             command=self.run_scheduling)
        self.btn.pack(side=tk.LEFT)

        
        self.tree_all = ttk.Treeview(root, columns=("ID", "Atividade", "Início", "Fim"), show="headings")
        for col in ("ID", "Atividade", "Início", "Fim"):
            self.tree_all.heading(col, text=col)
            self.tree_all.column(col, width=150, anchor=tk.CENTER)
        self.tree_all.pack(pady=10)

        tk.Label(root, text="Atividades Aceitas na Sala Multiuso:", font=("Arial", 14, "bold")).pack()
        
        self.tree_selected = ttk.Treeview(root, columns=("ID", "Atividade", "Início", "Fim"), show="headings")
        for col in ("ID", "Atividade", "Início", "Fim"):
            self.tree_selected.heading(col, text=col)
            self.tree_selected.column(col, width=150, anchor=tk.CENTER)
        self.tree_selected.pack(pady=10)
        
        self.fig, self.ax = plt.subplots(figsize=(10, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()
def run_scheduling(self):
    try:
            n = int(self.entry.get())
            self.tree_all.delete(*self.tree_all.get_children())
            self.tree_selected.delete(*self.tree_selected.get_children())
            self.ax.clear()

            reservations = generate_reservations(n)
            accepted = max_non_overlapping_reservations(reservations)

            for r in reservations:
                start_ampm = convert_to_ampm(r.start)
                end_ampm = convert_to_ampm(r.end)
                self.tree_all.insert("", tk.END, values=(r.id, r.activity, start_ampm, end_ampm))

            for r in accepted:
                start_ampm = convert_to_ampm(r.start)
                end_ampm = convert_to_ampm(r.end)
                self.tree_selected.insert("", tk.END, values=(r.id, r.activity, start_ampm, end_ampm))

            y_all = []
            for i, r in enumerate(reservations):
                self.ax.barh(i, r.end - r.start, left=r.start, color='lightgray', edgecolor='black', label='Não aceito' if i==0 else "")
                label = f"{r.activity}\n{convert_to_ampm(r.start)}-{convert_to_ampm(r.end)}"
                self.ax.text(r.start + (r.end - r.start)/2, i, label, ha='center', va='center', fontsize=8, color='black')
                y_all.append(i)
