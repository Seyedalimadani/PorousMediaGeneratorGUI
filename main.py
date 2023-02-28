import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root=customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")


frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label=customtkinter.CTkLabel(master=frame, text="2D Porous Media Generator")
label.pack(pady=12, padx= 10 )

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Threshold")
entry1.pack (pady=12, padx=10)
entry2 = customtkinter.CTkComboBox(master=frame,values=["Raw", "AverageBlur", "Gaussian","MedianBlur"])
entry2.pack (pady=12, padx=10)
button = customtkinter.CTkButton(master=frame, text="Generate")
button.pack (pady=12, padx=10)
checkbox = customtkinter.CTkCheckBox(master=frame, text="Save After Generation")
checkbox.pack (pady=12, padx=10)
root.mainloop()