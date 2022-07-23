import tkinter as tk


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
        bg_logo.pack()

        # Название
        bg_text = tk.Label(text='Training Alarm',
                           font='PMingLiU 60',
                           foreground="gold2",
                           background="black")
        bg_text.pack()

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

        start_but.pack(pady=25)
        exit_but.pack()

    def opendatawindow(self):
        datawindow = DataWin(self)
        datawindow.grab_set()


class DataWin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        #############################

        self.button = tk.Button(self, text="Закрыть", command=self.destroy)

        self.button.pack(pady=5, ipadx=2, ipady=2)
