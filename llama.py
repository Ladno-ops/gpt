from tkinter import *
import requests

url = "http://localhost:11434/v1/chat/completions"

root = Tk()
root.geometry('370x465')
root['bg'] = "#09090d"
root.resizable(width = False , height = False)

def key_handler_function(event):
    global entry
    txt = entry.get()

    textgpt.configure(state=NORMAL)

    textgpt.delete(1.0, END)

    data = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": txt}] 
    }
    
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        gptanswer = result["choices"][0]["message"]["content"].strip()
    else:
        gptanswer = f"Ошибка: {response.status_code}, {response.text}"

    textgpt.insert(1.0, gptanswer)
    textgpt.configure(state=DISABLED)
    entry.delete(0, 'end')

textgpt = Text(root, width=40, height=25, bg = '#13141c', fg = 'white', state=DISABLED)
textgpt.place(x = 20, y = 20)

entry = Entry(root, bg = '#13141c', fg='white', width=53)
entry.place(x = 20, y = 430)

entry.bind("<Return>", key_handler_function)

root.mainloop()