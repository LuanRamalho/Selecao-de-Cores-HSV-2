import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox


def selecionar_cor():
    """Abre o seletor de cores e exibe as informações da cor escolhida."""
    cor = colorchooser.askcolor(title="Selecione uma cor")
    if cor[0]:
        rgb = tuple(map(int, cor[0]))
        hexadecimal = cor[1]
        
        # Atualizar a interface
        frame_cor.configure(bg=hexadecimal)
        entrada_rgb.delete(0, tk.END)
        entrada_rgb.insert(0, f"RGB{rgb}")
        entrada_hex.delete(0, tk.END)
        entrada_hex.insert(0, hexadecimal)


def copiar_rgb():
    """Copia o código RGB para a área de transferência."""
    rgb = entrada_rgb.get()
    if rgb:
        root.clipboard_clear()
        root.clipboard_append(rgb)
        root.update()
        messagebox.showinfo("Copiar RGB", "Código RGB copiado para a área de transferência!")


def copiar_hex():
    """Copia o código hexadecimal para a área de transferência."""
    hexadecimal = entrada_hex.get()
    if hexadecimal:
        root.clipboard_clear()
        root.clipboard_append(hexadecimal)
        root.update()
        messagebox.showinfo("Copiar Hexadecimal", "Código hexadecimal copiado para a área de transferência!")


# Configuração da janela principal
root = tk.Tk()
root.title("Seletor de Cores")
root.geometry("500x500")
root.resizable(False, False)

# Frame principal para exibir a cor
frame_cor = tk.Frame(root, bg="white")
frame_cor.pack(fill="both", expand=True)

# Botão para selecionar a cor
btn_selecionar = tk.Button(frame_cor, text="Selecionar Cor", command=selecionar_cor)
btn_selecionar.pack(pady=10)

# Entrada para o código RGB
frame_rgb = tk.Frame(frame_cor, bg="white")
frame_rgb.pack(pady=5)
entrada_rgb = tk.Entry(frame_rgb, width=30, justify="center")
entrada_rgb.pack(side="left", padx=5)
btn_copiar_rgb = tk.Button(frame_rgb, text="Copiar", command=copiar_rgb)
btn_copiar_rgb.pack(side="right")

# Entrada para o código hexadecimal
frame_hex = tk.Frame(frame_cor, bg="white")
frame_hex.pack(pady=5)
entrada_hex = tk.Entry(frame_hex, width=30, justify="center")
entrada_hex.pack(side="left", padx=5)
btn_copiar_hex = tk.Button(frame_hex, text="Copiar", command=copiar_hex)
btn_copiar_hex.pack(side="right")

# Executa o programa
root.mainloop()
