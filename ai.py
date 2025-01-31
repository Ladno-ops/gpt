from tkinter import *
import openai

key = 'key'

openai.api_key = key

root = Tk()
root.geometry('370x465')
root['bg'] = "#09090d"
root.resizable(width = False , height = False)

def key_handler_function(event):
    txt = entry['text']

    textgpt.configure(state=NORMAL)

    response = openai.Completion.create(
        prompt = txt,
        engine = 'gpt-3.5-turbo-1106',
        max_tokens = 100,
        temperature = 0,
        n = 1,
        timeout = 15
    )
    gptanswer = response.choices[0].text.strip()


    textgpt.insert(1.0, gptanswer)
    textgpt.configure(state=DISABLED)
    entry.delete(0, 'end')

textgpt = Text(root, width=40, height=25, bg = '#13141c', fg = 'white', state=DISABLED)
textgpt.place(x = 20, y = 20)

entry = Entry(root, bg = '#13141c', fg='white', width=53)
entry.place(x = 20, y = 430)

entry.bind("<Return>", key_handler_function)

root.mainloop()