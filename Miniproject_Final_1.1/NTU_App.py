import tkinter as tk
from functions import *
from database import *
import calendar

menu = load_data('default_menu')

#####Jasper / Haocheng / Khin ###########
class NTUCanteen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("NTU FOODIES")
        self.iconbitmap(r'icon.ico')
        self.geometry('400x400')
        self.resizable(False, False)

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


############Jasper###############
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.title = tk.Label(self, fg="#9b716c", font="fixedsys", text="Welcome To NTU Canteen!")
        self.title.pack(pady=15)

        # Widget
        self = tk.Frame(self)
        self.view_all = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="View All Menu",
                                  command=lambda: master.switch_frame(All_stores))
        self.time = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="View By Date & Time", command=lambda: master.switch_frame(Date))

        self.time.pack()
        self.pack(padx=10, pady=50)
        self.view_all.pack(fill='both', pady=10)

        ############################Khin##################################
        self.ophr = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="View Operating Hours",command=lambda: master.switch_frame(OpHours))
        self.ophr.pack(pady=5)

############Jasper###############
class All_stores(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.configure(bg = 'red')

        self.chickenrice = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Chicken Rice",
                                     command=lambda: master.switch_frame(Chickenrice))
        self.chickenrice.pack(fill='both', pady=10)
        self.muslim = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Malay Food", command=lambda: master.switch_frame(Muslim))
        self.muslim.pack(fill='both', pady=10)
        self.western = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Western", command=lambda: master.switch_frame(Western))
        self.western.pack(fill='both', pady=10)
        self.noodles = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Noodles", command=lambda: master.switch_frame(Noodles))
        self.noodles.pack(fill='both', pady=10)
        self.mala = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Mala", command=lambda: master.switch_frame(Mala))
        self.mala.pack(fill='both', pady=10)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(StartPage))
        self.back.pack(pady=20)


############Jasper###############
class Chickenrice(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.name = tk.Label(self, fg="#9b716c", font="fixedsys", text="Chicken Rice")
        self.name.pack(pady=15)

        for menus in  all_menu['chickenrice']:
            for item in menus:
                self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=item)
                self.foodlabel.pack(pady=2)


        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(All_stores))
        self.back.pack()

############Jasper###############
class Muslim(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.name= tk.Label(self, fg="#9b716c", font="fixedsys", text="Malay Food")
        self.name.pack(pady=15)

        for menus in  all_menu['muslim']:
            for item in menus:
                self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=item)
                self.foodlabel.pack(pady=2)


        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(All_stores))
        self.back.pack()

############Jasper###############
class Western(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.name= tk.Label(self, fg="#9b716c", font="fixedsys", text="Western")
        self.name.pack(pady=15)

        for menus in  all_menu['western']:
            for item in menus:
                self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=item)
                self.foodlabel.pack(pady=2)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(All_stores))
        self.back.pack()

############Jasper###############
class Noodles(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.name= tk.Label(self, fg="#9b716c", font="fixedsys", text="Noodles")
        self.name.pack(pady=15)

        for menus in  all_menu['noodles']:
            for item in menus:
                self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=item)
                self.foodlabel.pack(pady=2)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(All_stores))
        self.back.pack()

############Jasper###############
class Mala(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.name= tk.Label(self, fg="#9b716c", font="fixedsys", text="Mala")
        self.name.pack(pady=15)

        for menus in  all_menu['mala']:
            for item in menus:
                self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=item)
                self.foodlabel.pack(pady=2)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(All_stores))
        self.back.pack()

##############Haocheng##############

class Date(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def user_weekday():
            global week_of_day
            if check_weekday(self.entry.get()):
                date = self.entry.get()
                date_list = date.split('/')
                week_of_day = calendar.weekday(int(date_list[0]), int(date_list[1]), int(date_list[2]))
                master.switch_frame(Time)
                return week_of_day
            else:
                self.warning = tk.Label(self, bg="#7fcbaf", fg="#003866", font="fixedsys", text='Invalid Input, Please enter again')
                self.warning.after(5000, self.warning.destroy)
                self.warning.pack(fill='both', pady=10)


        def system_datetime():
            global week_of_day
            global hour
            week_of_day = system_weekday()
            hour = system_time()[0]
            master.switch_frame(NewStores)

        self.label = tk.Label(self, fg="#003866", font="fixedsys", text='Please input date(YYYY/MM/DD):')
        self.label.pack(fill='both', pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(fill='both', pady=10)

        self.btn = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text='submit', command=lambda: user_weekday())
        self.btn.pack(fill='both', pady=10)

        self.btn2 = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text='Use system date and time', command=lambda: system_datetime())
        self.btn2.pack(fill='both', pady=10)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(StartPage))
        self.back.pack(fill='both', pady=10)



############Haocheng############
class Time(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def user_time():
            global hour
            if check_time(self.entry.get()):
                time = self.entry.get()
                hour = int(time.split(':')[0])
                minute = int(time.split(':')[1])
                master.switch_frame(NewStores)
                return hour, minute

            else:
                self.warning = tk.Label(self, bg="#7fcbaf", fg="#003866", font="fixedsys", text='Invalid Input, Please enter again')
                self.warning.after(5000, self.warning.destroy)
                self.warning.pack(fill='both', pady=10)

        self.label = tk.Label(self, fg="#003866", font="fixedsys", text='Please input time in 24 hours format(HH:MM): ')
        self.label.pack(fill='both', pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(fill='both', pady=10)

        self.btn = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text='submit', command=lambda: user_time())
        self.btn.pack(fill='both', pady=10)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(StartPage))
        self.back.pack(fill='both', pady=10)

#################Haocheng&Jasper#####################
class NewStores(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self = tk.Frame(self)
        self.pack(pady=20)

        self.chickenrice = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Chicken Rice",
                                     command=lambda: master.switch_frame(NewChickenrice))
        self.chickenrice.pack(fill='both', pady=10)
        self.muslim = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Malay Food", command=lambda: master.switch_frame(NewMuslim))
        self.muslim.pack(fill='both', pady=10)
        self.western = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Western", command=lambda: master.switch_frame(NewWestern))
        self.western.pack(fill='both', pady=10)
        self.noodles = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Noodles", command=lambda: master.switch_frame(NewNoodles))
        self.noodles.pack(fill='both', pady=10)
        self.mala = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Mala", command=lambda: master.switch_frame(NewMala))
        self.mala.pack(fill='both', pady=10)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(StartPage))
        self.back.pack(pady=20)


###############Haocheng###################
class NewChickenrice(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        global menu
        new_menu = newmenu(week_of_day, hour, 'chickenrice', menu)

        def select():
            global sel 
            sel = 1
            master.switch_frame(Waitingtime_1)


        for i in new_menu:
            self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=i)
            self.foodlabel.pack(pady=2)

        if new_menu != ['Store is Closed']:
        ###############Khin###############
            self.waitingtime = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Calculate Waiting Time",command=lambda: select())
            self.waitingtime.pack(pady=5)
        ###

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(NewStores))
        self.back.pack()


###############Haocheng###################
class NewMuslim(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global menu
        new_menu = newmenu(week_of_day, hour, 'muslim', menu)

        def select():
            global sel 
            sel = 2
            master.switch_frame(Waitingtime_1)


        for i in new_menu:
            self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=i)
            self.foodlabel.pack(pady=2)

        if new_menu != ['Store is Closed']:
        ###############Khin###############
            self.waitingtime = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Calculate Waiting Time",command=lambda: select())
            self.waitingtime.pack(pady=5)
        ###

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(NewStores))
        self.back.pack()


###############Haocheng###################
class NewWestern(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global menu
        new_menu = newmenu(week_of_day, hour, 'western', menu)

        def select():
            global sel 
            sel = 3
            master.switch_frame(Waitingtime_1)


        for i in new_menu:
            self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=i)
            self.foodlabel.pack(pady=2)

        if new_menu != ['Store is Closed']:
        ###############Khin###############
            self.waitingtime = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Calculate Waiting Time",command=lambda: select())
            self.waitingtime.pack(pady=5)


        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(NewStores))
        self.back.pack()


###############Haocheng###################
class NewMala(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global menu
        new_menu = newmenu(week_of_day, hour, 'mala', menu)

        def select():
            global sel 
            sel = 5
            master.switch_frame(Waitingtime_1)


        for i in new_menu:
            self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=i)
            self.foodlabel.pack(pady=2)

        if new_menu != ['Store is Closed']:
        ###############Khin###############
            self.waitingtime = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Calculate Waiting Time",command=lambda: select())
            self.waitingtime.pack(pady=5)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(NewStores))
        self.back.pack()


###############Haocheng###################
class NewNoodles(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        global menu
        new_menu = newmenu(week_of_day, hour, 'noodles', menu)

        def select():
            global sel 
            sel = 4
            master.switch_frame(Waitingtime_1)


        for i in new_menu:
            self.foodlabel = tk.Label(self, fg="#003866", font="fixedsys", text=i)
            self.foodlabel.pack(pady=2)

        if new_menu != ['Store is Closed']:
        ###############Khin###############
            self.waitingtime = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Calculate Waiting Time",command=lambda: select())
            self.waitingtime.pack(pady=5)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="back", command=lambda: master.switch_frame(NewStores))
        self.back.pack()


###############Khin###################
class Waitingtime_1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def current():
            try:
                if int(self.number.get()) >= 0:
                    no = int(self.number.get())
                    if sel == 1:
                        no *= 1
                    elif sel == 2:
                        no *= 2
                    elif sel == 3:
                        no *= 3
                    elif sel == 4:
                        no *= 4
                    elif sel == 5:
                        no *= 5
                else:
                    raise ValueError
                self.number.delete(0, tk.END)
                self.label = tk.Label(self, bg="#7fcbaf", fg="#003866", font="fixedsys",
                                      text=("The waiting time is: " + str(no) + "mins"))
                self.label.after(5000, self.label.destroy)
                self.label.pack()
                return no

            except ValueError:
                self.number.delete(0, tk.END)
                self.label = tk.Label(self, bg="#7fcbaf", fg="#003866", font="fixedsys", text=("Please enter a valid number"))
                self.label.after(2000, self.label.destroy)
                self.label.pack()


        self.title = tk.Label(self, fg="#003866", font="fixedsys", text=
        "Enter number of people in the queue currently:")
        self.title.pack()

        # input box
        self.number = tk.Entry(self, text="fixedsys")
        self.number.pack(pady=15)

        # event button to calculate and display output
        self.current_button = tk.Button(self, bg="white", fg="#003866", font="fixedsys", text="Calculate",
                                        command=lambda: current())
        self.current_button.pack(pady=5)

        self.back = tk.Button(self, bg="white", fg="#003866", font="fixedsys", text="back", command=lambda: master.switch_frame(StartPage))
        self.back.pack( pady=10)


###############Khin###################
class OpHours(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.frame = tk.Frame(self)
        self.frame.pack(pady=50)
        for i in op_hours:
            self.stallname = tk.Label(self.frame,
                                      text=(i + " : " + str(op_hours[i][0]) + ":00 to " + str(op_hours[i][1]) + ":00"))
            self.stallname.pack(pady=2)

        self.back = tk.Button(self, bg="white", fg="#9b716c", font="fixedsys", text="Back", command=lambda: master.switch_frame(StartPage))
        self.back.pack(pady=20)




if __name__ == "__main__":
    app = NTUCanteen()
    app.mainloop()
