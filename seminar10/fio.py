import tkinter as tk


def lib(x, y, z):
    with open('/Users/pest/Documents/study/python/seminar10/library.txt', 'a', encoding='utf-8') as l:
        l.write(f'Фамилия: {x} Имя: {y} Отчество: {z}\n')


window = tk.Tk()
window.title('ФИО')
window.geometry('250x130')

first_name = tk.Label(text="Фамилия")
first_name.grid(column=0, row=0)
first_name = tk.Entry(width=15)
first_name.grid(column=1, row=0)
first_name.focus()

person_name = tk.Label(text="Имя")
person_name.grid(column=0, row=1)
person_name = tk.Entry(width=15)
person_name.grid(column=1, row=1)

second_name = tk.Label(text="Отчество")
second_name.grid(column=0, row=2)
second_name = tk.Entry(width=15)
second_name.grid(column=1, row=2)

button = tk.Button(text="добавить в файл >>>", width=13, height=1,
                   command=lambda: lib(first_name.get(), person_name.get(), second_name.get()))
button.grid(column=1, row=3)

window.mainloop()
