import ttkbootstrap as tb
from ttkbootstrap.constants import *

class mainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Konverter Suhu")
        self.root.geometry("500x400")

        frame = tb.Frame(self.root)
        frame.pack(padx=20, pady=20)
        
     
        user_info_frame = tb.LabelFrame(
            frame, 
            text="Konversi Suhu",
            bootstyle="primary"
        )
        user_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
  
        tb.Label(
            user_info_frame, 
            text="Masukkan Suhu:",
            font=("Helvetica", 10)
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.suhu_entry = tb.Entry(
            user_info_frame, 
            width=10,
            bootstyle="primary"
        )
        self.suhu_entry.grid(row=0, column=1, padx=10, pady=10)
        
  
        self.satuan_awal = tb.Combobox(
            user_info_frame, 
            values=["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Reamur (°R)"],
            width=12,
            state="readonly",
            bootstyle="primary"
        )
        self.satuan_awal.current(0)
        self.satuan_awal.grid(row=0, column=2, padx=10, pady=10)
        
      
        tb.Label(
            user_info_frame, 
            text="Konversi ke:",
            font=("Helvetica", 10)
        ).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
     
        self.satuan_tujuan = tb.Combobox(
            user_info_frame, 
            values=["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Reamur (°R)"],
            width=12,
            state="readonly",
            bootstyle="primary"
        )
        self.satuan_tujuan.current(1)
        self.satuan_tujuan.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        
       
        button = tb.Button(
            user_info_frame, 
            text="Konversi Suhu", 
            command=self.konversi_suhu,
            bootstyle="success"
        )
        button.grid(row=2, column=0, columnspan=3, padx=10, pady=15)
        
      
        result_frame = tb.LabelFrame(
            frame, 
            text="Hasil Konversi",
            bootstyle="info"
        )
        result_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.result_label = tb.Label(
            result_frame, 
            text="",
            font=("Helvetica", 12, "bold"),
            bootstyle="inverse-info"
        )
        self.result_label.pack(padx=20, pady=20, fill="both", expand=True)
        
        note_frame = tb.Frame(frame)
        note_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        tb.Label(
            note_frame, 
            text="Rumus konversi:",
            font=("Helvetica", 8)
        ).pack(anchor="w")
        
        tb.Label(
            note_frame, 
            text="°F = (°C × 9/5) + 32 | K = °C + 273.15 | °R = °C × 4/5",
            font=("Helvetica", 7),
            foreground="gray70"
        ).pack(anchor="w")

    def konversi_suhu(self):
        try:
            suhu = float(self.suhu_entry.get())
            satuan_awal = self.satuan_awal.get()
            satuan_tujuan = self.satuan_tujuan.get()
            
          
            if "Celsius" in satuan_awal:
                celsius = suhu
            elif "Fahrenheit" in satuan_awal:
                celsius = (suhu - 32) * 5/9
            elif "Kelvin" in satuan_awal:
                celsius = suhu - 273.15
            elif "Reamur" in satuan_awal:
                celsius = suhu * 5/4
                
            
            if "Celsius" in satuan_tujuan:
                hasil = celsius
                simbol = "°C"
            elif "Fahrenheit" in satuan_tujuan:
                hasil = (celsius * 9/5) + 32
                simbol = "°F"
            elif "Kelvin" in satuan_tujuan:
                hasil = celsius + 273.15
                simbol = "K"
            elif "Reamur" in satuan_tujuan:
                hasil = celsius * 4/5
                simbol = "°R"
                
         
            hasil_formatted = f"{hasil:.2f}" if abs(hasil) >= 0.01 else f"{hasil:.4f}"
            
         
            self.result_label.config(
                text=f"{suhu} {satuan_awal.split(' ')[-1]} = {hasil_formatted} {simbol}"
            )
            
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid!")

# Main program dengan tema minty
if __name__ == "__main__":
    root = tb.Window(themename="minty")
    app = mainApp(root)
    root.mainloop()