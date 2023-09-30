import tkinter as tk 

def change_text():
    label.config(text='обновить надпись')

root = tk.Tk ()
root.title("наша праграма")
root.geometry('500x200')
label= tk.Label(root , text= 'надпись')
label.pack()
button=tk.Button(root , text= 'изменить текст',command=change_text)
button.pack()
root.mainloop()
 
import tkinter as tk 
import tkinter.ttk as ttk 
root = tk.Tk ()
root.geometry('500x200')
root.title("наша праграма")
def count_words_chars():
    sentence=sentence_entry.get('1.0','end-1c')
    words=len(sentence.split())
    chars=len(sentence)
    words_label.config(text=f'колличество слов={words}')
    chars_label.config(text=f'колличество символов={chars}')
sentence_entry=tk.Text(root,height=3,wrap='word')
words_label=ttk.Label(root)
chars_label=ttk.Label(root)
count_butten=ttk.Button(root,text="подсчитать",command=count_words_chars)
sentence_entry.pack()
words_label.pack()
chars_label.pack()
count_butten.pack()

root.mainloop()