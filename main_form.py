import tkinter as tk
from tkinter import messagebox


def validate_numeric_input(P):
    if P.replace('.', '', 1).isdigit() or P == "":
        return True
    else:
        return False

def obtener_datos():
    capital_inicial = capital_inicial_input.get()
    aporte_periodico = aporte_periodico_input.get()
    capital_final = capital_final_input.get()
    numero_periodo = numero_periodo_input.get()

    if not capital_inicial or not aporte_periodico or not capital_final or not numero_periodo:
        messagebox.showerror("Error", "Todos los campos deben estar llenos con valores numéricos.")
        return
    else:
        try:
            capital_inicial = float(capital_inicial)
            aporte_periodico = float(aporte_periodico)
            capital_final = float(capital_final)
            numero_periodo = int(numero_periodo)
        except ValueError:
            messagebox.showerror("Error", "Datos mal llenados.")

    return capital_inicial, aporte_periodico, capital_final, numero_periodo

def main():
    global capital_inicial_input, aporte_periodico_input, capital_final_input, numero_periodo_input, info_text

    root = tk.Tk()
    root.title("Ahorro Semanal")
    root.geometry("400x400")

    vcmd = (root.register(validate_numeric_input), '%P')

    tk.Label(root, text="Capital Inicial:").pack()
    capital_inicial_input = tk.Entry(root, width=50, validate='key', validatecommand=vcmd)
    capital_inicial_input.pack()

    tk.Label(root, text="Aporte periódico:").pack()
    aporte_periodico_input = tk.Entry(root, width=50, validate='key', validatecommand=vcmd)
    aporte_periodico_input.pack()

    tk.Label(root, text="Capital Final:").pack()
    capital_final_input = tk.Entry(root, width=50, validate='key', validatecommand=vcmd)
    capital_final_input.pack()

    tk.Label(root, text="Número de Periodo:").pack()
    numero_periodo_input = tk.Entry(root, width=50, validate='key', validatecommand=vcmd)
    numero_periodo_input.pack()

    obtener_datos_btn = tk.Button(root, text="Obtener Datos", command=obtener_datos)
    obtener_datos_btn.pack(pady=10)

    tk.Label(root, text="Información:").pack()
    info_text = tk.Text(root, width=50, height=10, state='disabled')
    info_text.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
