# Yeh code ek folder ke andar jitne bhi Excel files hain, unme se phone numbers count karega.

import os
import pandas as pd

# Apne folder ka path daal
folder_path = r"E:\whatsapp group no\not edited\phn no. 45 kuchaman"
total_numbers = 0

for file in os.listdir(folder_path):
    if file.endswith(".xlsx") or file.endswith(".xls"):
        file_path = os.path.join(folder_path, file)
        try:
            df = pd.read_excel(file_path)

            # Phone number column me kitni entries hain (rows count)
            total_numbers += df['phone_number'].count()

        except Exception as e:
            print(f"Error in {file}: {e}")

print("Total phone numbers (sab  files mila ke):", total_numbers)

