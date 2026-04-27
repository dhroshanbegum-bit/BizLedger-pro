import tkinter as tk
from tkinter import messagebox, ttk
import os

# --- HELPER: BRANDING ---
def set_icon(window):
    try: window.iconbitmap("app_logo.ico")
    except: pass

# --- MODULE 1: BUSINESS ALERTS ---
def open_alerts():
    a_win = tk.Toplevel(root)
    a_win.title("Business Alerts")
    a_win.geometry("400x350")
    set_icon(a_win)
    tk.Label(a_win, text="Critical Business Alerts", font=("Arial", 12, "bold"), fg="#e74c3c").pack(pady=10)
    box = tk.Listbox(a_win, font=("Arial", 10), fg="#c0392b")
    box.pack(fill="both", expand=True, padx=20, pady=10)

    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as f:
            for line in f:
                try:
                    n, q = line.strip().split(":")
                    if int(q) < 5: box.insert(tk.END, f"⚠️ LOW STOCK: {n} ({q} left)")
                except: continue
    if box.size() == 0: box.insert(tk.END, "✅ Business is healthy. No alerts.")

# --- MODULE 2: CUSTOMER CONTACTS ---
def open_contacts():
    c_win = tk.Toplevel(root); c_win.title("Contacts"); c_win.geometry("400x450")
    set_icon(c_win)
    f = tk.Frame(c_win, pady=10); f.pack()
    tk.Label(f, text="Name:").grid(row=0, column=0)
    ne = tk.Entry(f); ne.grid(row=0, column=1)
    tk.Label(f, text="Phone:").grid(row=1, column=0)
    pe = tk.Entry(f); pe.grid(row=1, column=1)
    tree = ttk.Treeview(c_win, columns=("N", "P"), show="headings")
    tree.heading("N", text="Name"); tree.heading("P", text="Phone")
    tree.pack(fill="both", expand=True, padx=10)

    def load():
        for i in tree.get_children(): tree.delete(i)
        if os.path.exists("contacts.txt"):
            with open("contacts.txt", "r") as f:
                for line in f: tree.insert("", tk.END, values=line.strip().split("|"))

    def save():
        if ne.get() and pe.get():
            with open("contacts.txt", "a") as f: f.write(f"{ne.get()}|{pe.get()}\n")
            load(); ne.delete(0, tk.END); pe.delete(0, tk.END)

    tk.Button(c_win, text="Save Contact", command=save, bg="#3b5998", fg="white").pack(pady=5)
    load()

# --- MODULE 3: INVENTORY SYSTEM ---
def open_inventory():
    i_win = tk.Toplevel(root); i_win.title("Inventory"); i_win.geometry("400x450")
    set_icon(i_win)
    f = tk.Frame(i_win, pady=10); f.pack()
    tk.Label(f, text="Item Name:").grid(row=0, column=0)
    ie = tk.Entry(f); ie.grid(row=0, column=1)
    tk.Label(f, text="Quantity:").grid(row=1, column=0)
    qe = tk.Entry(f); qe.grid(row=1, column=1)
    tree = ttk.Treeview(i_win, columns=("I", "Q"), show="headings")
    tree.heading("I", text="Item"); tree.heading("Q", text="Qty")
    tree.pack(fill="both", expand=True, padx=10)

    def load():
        for i in tree.get_children(): tree.delete(i)
        if os.path.exists("inventory.txt"):
            with open("inventory.txt", "r") as f:
                for line in f: tree.insert("", tk.END, values=line.strip().split(":"))

    def save():
        if ie.get() and qe.get().isdigit():
            with open("inventory.txt", "a") as f: f.write(f"{ie.get()}:{qe.get()}\n")
            load(); ie.delete(0, tk.END); qe.delete(0, tk.END)

    tk.Button(i_win, text="Update Stock", command=save, bg="#2980b9", fg="white").pack(pady=5)
    load()

# --- MODULE 4: DAILY LEDGER ---
def open_ledger():
    l_win = tk.Toplevel(root); l_win.title("Daily Ledger"); l_win.geometry("400x450")
    set_icon(l_win)
    f = tk.Frame(l_win, pady=10); f.pack()
    tk.Label(f, text="Details:").grid(row=0, column=0)
    de = tk.Entry(f); de.grid(row=0, column=1)
    tk.Label(f, text="Amount (₹):").grid(row=1, column=0)
    ae = tk.Entry(f); ae.grid(row=1, column=1)
    tree = ttk.Treeview(l_win, columns=("D", "A"), show="headings")
    tree.heading("D", text="Transaction"); tree.heading("A", text="Amount (₹)")
    tree.pack(fill="both", expand=True, padx=10)

    def load():
        for i in tree.get_children(): tree.delete(i)
        if os.path.exists("ledger.txt"):
            with open("ledger.txt", "r") as f:
                for line in f: tree.insert("", tk.END, values=line.strip().split(":"))

    def save():
        if de.get() and ae.get():
            with open("ledger.txt", "a") as f: f.write(f"{de.get()}:{ae.get()}\n")
            load(); de.delete(0, tk.END); ae.delete(0, tk.END)

    tk.Button(l_win, text="Add Transaction", command=save, bg="#27ae60", fg="white").pack(pady=5)
    load()

# --- MAIN DASHBOARD ---
def main():
    global root
    root = tk.Tk()
    root.title("BizLedger Pro")
    root.geometry("400x550")
    root.config(bg="#f0f2f5")
    set_icon(root)

    header = tk.Frame(root, bg="#0084ff", height=80); header.pack(fill="x")
    tk.Label(header, text="BIZLEDGER PRO", font=("Arial", 16, "bold"), bg="#0084ff", fg="white").pack(pady=25)

    btn_s = {"width": 22, "height": 2, "font": ("Arial", 10, "bold"), "fg": "white", "bd": 0, "cursor": "hand2"}
    
    tk.Button(root, text="🚨 BUSINESS ALERTS", bg="#e74c3c", command=open_alerts, **btn_s).pack(pady=10)
    tk.Button(root, text="📞 CUSTOMER CONTACTS", bg="#3b5998", command=open_contacts, **btn_s).pack(pady=10)
    tk.Button(root, text="📦 INVENTORY SYSTEM", bg="#2980b9", command=open_inventory, **btn_s).pack(pady=10)
    tk.Button(root, text="💰 DAILY LEDGER", bg="#27ae60", command=open_ledger, **btn_s).pack(pady=10)

    tk.Label(root, text="Developed for Society", bg="#f0f2f5", fg="gray", font=("Arial", 8)).pack(side="bottom", pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()