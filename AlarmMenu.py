import tkinter as tk


def InitAlarmMainMenu():
    windowmain = tk.Tk()
    windowmain.title('Главное меню')
    windowmain.configure(bg='black')
    windowmain.geometry('600x450')
    windowmain.resizable(width=False, height=False)

    #Фон
    windowmain.image = tk.PhotoImage(file='pictures/logo.png')
    bg_logo = tk.Label(windowmain, image=windowmain.image, bg='black')
    bg_logo.pack()

    #Название
    bg_text = tk.Label(text='Training Alarm',
                       font='PMingLiU 60',
                       foreground="gold2",
                       background="black")
    bg_text.pack()

    #Кнопки
    start_but = tk.Button(windowmain, text='База данных',
                          background="purple",
                          foreground="yellow",
                          padx="40",
                          pady="8",
                          font="60"
                          )

    exit_but = tk.Button(windowmain, text='Выход',
                          background="purple",
                          foreground="yellow",
                          padx="40",
                          pady="8",
                          font="60"
                          )

    start_but.pack(pady=25)
    exit_but.pack()

    windowmain.mainloop()