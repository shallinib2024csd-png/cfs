import tkinter as tk
from tkinter import ttk, messagebox
import uuid

# -----------------------------
# DATA STORAGE
# -----------------------------
donors = {}
donations = {}

# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("Charity Fund Management System")
root.geometry("800x600")
root.configure(bg="lightblue")

# -----------------------------
# FUNCTIONS
# -----------------------------

# ---------- DONOR ----------
def add_donor():

    name = entry_name.get()
    age = entry_age.get()
    gender = combo_gender.get()
    phone = entry_phone.get()
    city = entry_city.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "Fill Required Fields")
        return

    donor_id = "DON-" + str(uuid.uuid4())[:5]

    donors[donor_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "city": city
    }

    messagebox.showinfo("Success", f"Donor Added\nID: {donor_id}")

    clear_donor()


def clear_donor():

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_city.delete(0, tk.END)


def search_donor():

    donor_id = entry_search.get()

    if donor_id in donors:

        donor = donors[donor_id]

        result.set(
            f"Name: {donor['name']} | "
            f"Age: {donor['age']} | "
            f"Gender: {donor['gender']} | "
            f"Phone: {donor['phone']} | "
            f"City: {donor['city']}"
        )

    else:
        result.set("Donor Not Found")


# ---------- DONATION ----------
def add_donation():

    donor_id = entry_donor_id.get()
    amount = entry_amount.get()
    purpose = entry_purpose.get()

    if donor_id not in donors:
        messagebox.showerror("Error", "Invalid Donor ID")
        return

    if amount == "":
        messagebox.showerror("Error", "Enter Amount")
        return

    donation_id = "FUND-" + str(uuid.uuid4())[:5]

    donations[donation_id] = {
        "donor_id": donor_id,
        "donor_name": donors[donor_id]["name"],
        "amount": amount,
        "purpose": purpose
    }

    messagebox.showinfo(
        "Success",
        f"Donation Added\nDonation ID: {donation_id}"
    )

    clear_donation()


def clear_donation():

    entry_donor_id.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_purpose.delete(0, tk.END)


# ---------- VIEW DONATIONS ----------
def view_donations():

    donation_text.delete("1.0", tk.END)

    if len(donations) == 0:
        donation_text.insert(tk.END, "No Donations Available")

    else:

        for did, donation in donations.items():

            donation_text.insert(
                tk.END,
                f"\nDonation ID : {did}\n"
                f"Donor Name  : {donation['donor_name']}\n"
                f"Amount      : ₹{donation['amount']}\n"
                f"Purpose     : {donation['purpose']}\n"
                f"-----------------------------\n"
            )


# ---------- TOTAL COLLECTION ----------
def total_collection():

    total = 0

    for donation in donations.values():

        total = total + int(donation["amount"])

    messagebox.showinfo(
        "Total Collection",
        f"Total Charity Fund = ₹{total}"
    )


# -----------------------------
# NOTEBOOK TABS
# -----------------------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# -----------------------------
# DONOR TAB
# -----------------------------
frame1 = tk.Frame(notebook, bg="lightyellow")
notebook.add(frame1, text="Donor")

tk.Label(frame1, text="Donor Name", bg="lightyellow").pack()
entry_name = tk.Entry(frame1)
entry_name.pack()

tk.Label(frame1, text="Age", bg="lightyellow").pack()
entry_age = tk.Entry(frame1)
entry_age.pack()

tk.Label(frame1, text="Gender", bg="lightyellow").pack()
combo_gender = ttk.Combobox(frame1, values=["Male", "Female", "Other"])
combo_gender.pack()

tk.Label(frame1, text="Phone Number", bg="lightyellow").pack()
entry_phone = tk.Entry(frame1)
entry_phone.pack()

tk.Label(frame1, text="City", bg="lightyellow").pack()
entry_city = tk.Entry(frame1)
entry_city.pack()

tk.Button(
    frame1,
    text="Add Donor",
    bg="green",
    fg="white",
    command=add_donor
).pack(pady=10)

tk.Label(frame1, text="Search Donor ID", bg="lightyellow").pack()
entry_search = tk.Entry(frame1)
entry_search.pack()

result = tk.StringVar()

tk.Label(
    frame1,
    textvariable=result,
    bg="lightyellow",
    fg="blue"
).pack()

tk.Button(
    frame1,
    text="Search Donor",
    command=search_donor
).pack(pady=5)

# -----------------------------
# DONATION TAB
# -----------------------------
frame2 = tk.Frame(notebook, bg="lightcyan")
notebook.add(frame2, text="Donation")

tk.Label(frame2, text="Donor ID", bg="lightcyan").pack()
entry_donor_id = tk.Entry(frame2)
entry_donor_id.pack()

tk.Label(frame2, text="Donation Amount", bg="lightcyan").pack()
entry_amount = tk.Entry(frame2)
entry_amount.pack()

tk.Label(frame2, text="Purpose", bg="lightcyan").pack()
entry_purpose = tk.Entry(frame2)
entry_purpose.pack()

tk.Button(
    frame2,
    text="Add Donation",
    bg="darkblue",
    fg="white",
    command=add_donation
).pack(pady=10)

# -----------------------------
# VIEW TAB
# -----------------------------
frame3 = tk.Frame(notebook, bg="lavender")
notebook.add(frame3, text="View Donations")

donation_text = tk.Text(frame3, width=80, height=25)
donation_text.pack(pady=10)

tk.Button(
    frame3,
    text="View Donations",
    command=view_donations
).pack()

# -----------------------------
# TOTAL TAB
# -----------------------------
frame4 = tk.Frame(notebook, bg="mistyrose")
notebook.add(frame4, text="Total Fund")

tk.Label(
    frame4,
    text="Click Button to Calculate Total Collection",
    bg="mistyrose",
    font=("Arial", 14)
).pack(pady=30)

tk.Button(
    frame4,
    text="Calculate Total Fund",
    bg="purple",
    fg="white",
    command=total_collection
).pack(pady=20)

# -----------------------------
# RUN APPLICATION
# -----------------------------
root.mainloop()