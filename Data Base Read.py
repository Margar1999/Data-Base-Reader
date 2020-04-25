from tkinter import *
import sqlite3


class Main(Tk):
    def screen_option(self, screen_):
        screen_.geometry('1270x470')
        screen_.config(bg = "blue")
        screen_.title('Data Base Reader')

    # Function to connect data base

    def db_connect(self):
        try:
            dbconnect = sqlite3.connect(str(self.entry_1.get())) # C:\Users\marko\Desktop\new.db
            cursors = dbconnect.cursor()
            cursors.execute(str(self.entry_2.get()))                 # SELECT * FROM Trainings WHERE training_id = 1;
            aadsd = cursors.fetchall()
            for i in aadsd:
                Label(screen, text=i, bg="red").grid()

        except:
            Label(screen, text="Try again", bg="red").grid()

        finally:
            dbconnect.close()

    def db_quiet(self):
        screen.quit()

    # Screen build

    def screen_label(self, window):
        Label(master=window, text="SQL  code", font=10, bg="blue",  width=0 ).grid(row=2, column = 0, sticky ='E')
        Label(master=window, text="DB Path", font=10,   bg = "blue").grid(row=1, column = 0, sticky ='E')

    def screen_entry(self, window):
        self.entry_1 = Entry(master=window, width=40, font=10, bg="green")
        self.entry_2 = Entry(master=window, width=40, font=10, bg="green")
        self.entry_1.grid(row=1, column =1)
        self.entry_2.grid(row=2, column =1)

    def screen_button(self, window):
        Button(master=window, text='Execute', font=10, width=10, padx = 1, pady =1, command=self.db_connect).grid(row=1, column = 3, sticky ='E')
        Button(master=window, text='Quit', font=10, width=10, command=self.db_quiet).grid(row=2, column = 3, sticky ='E')


    def mainloop_f(self, main_screen):
        main_screen.mainloop()

screen = Main()
screen.screen_option(screen_=screen)
screen.screen_label(window=screen)
screen.screen_entry(window=screen)
screen.screen_button(window=screen)
screen.mainloop_f(main_screen=screen)












