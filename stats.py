import pandas as pd

# File paths
total_root = r"C:\Users\HP\Downloads\D. E. Shaw__SummerInternship__2026 Batch (1).xlsx"
selected_root = r"C:\Users\HP\Downloads\FowardedToStudents_StudentDetails-TIETPatiala.xlsx"

# Read Excel files
total = pd.read_excel(total_root)
selected = pd.read_excel(selected_root)

totalx = total["Name"]
selectedx = set(selected["Name"])

for index,member in enumerate(totalx):
    if member not in selectedx:
        print(member)


        
