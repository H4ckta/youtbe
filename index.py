

import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        status_label.config(text="Download completo!")
    except Exception as e:
        status_label.config(text="Erro ao baixar o vídeo.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Baixar Vídeo do YouTube")

# Configuração do grid para centralizar widgets
root.columnconfigure(0, weight=1)  # Coluna central
root.columnconfigure(1, weight=1)  # Coluna à direita
root.columnconfigure(2, weight=1)  # Coluna à esquerda

url_label = tk.Label(root, text="Insira a URL do vídeo do YouTube:")
url_label.grid(row=0, column=1, pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=1, column=1, padx=10)

download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.grid(row=2, column=1, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=1, pady=10)

root.mainloop()
