from tkinter import ttk
import tkinter as tk
from WorkWithBase import *


class MainWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Главное меню')
        self.configure(bg='black')
        self.geometry('600x450')
        self.resizable(width=False, height=False)

        # Фон
        self.image = tk.PhotoImage(file='pictures/logo.png')
        bg_logo = tk.Label(self, image=self.image, bg='black')

        # Название
        bg_text = tk.Label(text='Training Alarm',
                           font='PMingLiU 60',
                           foreground="gold2",
                           background="black")

        # Кнопки
        start_but = tk.Button(self, text='База данных',
                              background="purple",
                              foreground="yellow",
                              padx="40",
                              pady="8",
                              font="60",
                              command=self.opendatawindow
                              )

        exit_but = tk.Button(self, text='Выход',
                             background="purple",
                             foreground="yellow",
                             padx="40",
                             pady="8",
                             font="60",
                             command=self.destroy
                             )

        # Отрисовка виджетов
        bg_logo.pack()
        bg_text.pack()
        start_but.pack(pady=25)
        exit_but.pack()

    def opendatawindow(self):
        datawindow = DataWin(self)
        datawindow.grab_set()


class DataWin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.resizable(width=False, height=False)

        def edit(event):

            if self.tree.identify_region(event.x, event.y) == 'cell':
                def ok(event):
                    self.tree.set(item, column, entry.get())
                    entry.destroy()
                    RowFilling(self.tree, column, item)

                column = self.tree.identify_column(event.x)
                item = self.tree.identify_row(event.y)
                x, y, width, height = self.tree.bbox(item, column)
                value = self.tree.set(item, column)

            elif self.tree.identify_region(event.x, event.y) == 'nothing':
                column = self.tree.identify_column(event.x)
                x, y, width, height = self.tree.bbox(self.tree.get_children('')[-1], column)
                if event.y > y:

                    def ok(event):
                        item = self.tree.insert("", "end", values=("", ""))
                        self.tree.set(item, column, entry.get())
                        entry.destroy()

                    y += height
                    value = ""
                else:
                    return
            else:
                return
            entry = ttk.Entry(self.tree)
            entry.place(x=x, y=y, width=width, height=height,
                        anchor='nw')
            entry.insert(0, value)

            def DeleteRecord(event):
                print('ok')

            # Связь event с нажатием
            entry.bind('<FocusOut>', lambda e: entry.destroy())
            entry.bind('<Return>', ok)
            entry.bind('<1>', ok)
            entry.bind('<Delete>', DeleteRecord)
            entry.focus_set()

        # Работа с заполненными данными
        def RowFilling(tree, column, row):
            tree.curItem = tree.focus()
            tree.contents = tree.item(tree.curItem)
            if '' not in tree.contents['values'][1:]: DataSave(tree.contents['values'])


        # Таблица
        self.title("База данных")
        columns = ("#0", "#1", "#2", "#3", "#4")
        self.tree = ttk.Treeview(self, show="headings", columns=columns, displaycolumns=columns[1:5])
        self.tree.heading("#1", text="Тип")
        self.tree.column("#1", minwidth=80, width=80)
        self.tree.heading("#2", text="День недели")
        self.tree.column("#2", minwidth=80, width=80)
        self.tree.heading("#3", text="Время")
        self.tree.column("#3", minwidth=50, width=50)
        self.tree.heading("#4", text="Место проведения")
        self.tree.column("#4", minwidth=150)
        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=ysb.set)

        # Чтение Базы и заполнение
        current_base = AlarmBaseReading()
        for row in current_base:
            self.tree.insert('', 'end', values=row)

        # Кнопка
        self.button_exit = tk.Button(self, text="Закрыть", command=self.destroy)

        # Отрисовка
        self.tree.pack(padx=0)
        self.button_exit.pack(pady=5, ipadx=2, ipady=2, side=tk.RIGHT)

        # Присвоение event к клику мыши
        self.tree.bind('<Double-Button-1>', edit)

