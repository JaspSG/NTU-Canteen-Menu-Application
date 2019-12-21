import json
import calendar

############Jasper##################

#Read file & Create Menu in list format
def create_menu(file):
    with open(file) as myfile:
        mylist = []
        for line in myfile:
                mylist.append(line.strip())

        return mylist

#Save json file into a external file
def save_dict(data, file):
       '''
       Saves dict into json_file
       file = 'nameoffile' (string)
       '''
       if isinstance(data, dict) and isinstance(file, str) is True:
              with open(file, 'w') as outfile:
                     json.dump(data, outfile)
       else:
              print("Enter dictionaries only")

#Load json file into a variable
def load_data(file):
       '''
       file = 'nameoffile' (string)

       '''
       try:
              with open(file, 'r') as infile:
                     data = json.load(infile)
              return data
       except:
              print ("Invalid input, enter : (Filename.txt)")


# Updates default menu with new menu
def updatemenu(key, selection, menu):
    '''
    key: stall of menu to be edited
    selection: Choice of menu to be inserted (default(0),breakfast(1),special(2))
    menu : dictionary menu to be changed
    '''
    allmenu = load_data('all_menu')
    if selection > 2:
        print ("Menu does not exist, try again")
    else:
        newitem = {key: allmenu[key][selection]}
        if len(newitem[key]) == 0:
            return menu
        else:
            del menu[key]
            menu.update(newitem)
            return menu


#Generate menu based on day
def todaymenu(weekday, menu):
        #Special Menu Days
        menu = load_data('default_menu')
        keydays = [2,4,5,6]
        if weekday in keydays:
            if weekday == 5 or weekday == 6:
                menu = {stall:['Store is Closed'] for (stall,menu) in menu.items()}
                return menu
            elif weekday == 2:
                menu = updatemenu('noodles', 2, menu)
                return menu
            elif weekday == 4:
                menu = updatemenu('mala', 2, menu)
                return menu
        else:
            return menu

############Jasper##################


############ Jasper & Haocheng###########
def newmenu(day, time, stall, menu):
    '''
    day = 0-6
    time = 0-23
    stall = choice of stall
    output : {'stall' : menu}
    '''
    newmenu = todaymenu(day, menu)
    if day == 5 or day == 6:
        return newmenu[stall]
    else:
        ophours = load_data('op_hours')
        if time not in range(ophours[stall][0], ophours[stall][1]+1):
            close = ['Store is Closed']
            return close
        elif time in range(ophours[stall][0], ophours[stall][0]+3):
            breakfast = updatemenu(stall, 1, menu)
            return breakfast[stall]
        else:
            
            return newmenu[stall]

############ Jasper & Haocheng###########

################## DATE & TIME FUNCTIONS (HaoCheng) ########################### 
#get current system time as a list with hour followed by minute

def system_time():
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    return hour , minute

#get current system weekday as a integer.0-Monday and 6-Sunday

def system_weekday():
    from datetime import date
    my_date = date.today()
    return my_date.weekday()
    
#check valid weekday input from user, return boolean

def check_weekday(date):
    try:
        date_list = date.split('/')
        week_of_day = calendar.weekday(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return True
    except:
        return False

#check valid time input from user, return boolean

def check_time(time):
    try:
        hour = int(time.split(':')[0])
        minute = int(time.split(':')[1])
        if int(hour) in range(0,24) and int(minute) in range (0,60):
            return True
        else:
            return False
    except:
        return False
################## DATE & TIME FUNCTIONS (HaoCheng) ########################### 
