from functions import*
######## Jasper #######
#Menu Creation
chickenrice = create_menu('m_chickenrice.txt')
muslim = create_menu('m_muslim.txt')
western = create_menu('m_western.txt')
noodles = create_menu('m_noodles.txt')
mala = create_menu('m_mala.txt')

#Breakfast
b_muslim = create_menu('b_muslim.txt')
b_western = create_menu('b_western.txt')

#Special
s_noodles = create_menu('s_noodles.txt')
s_mala = create_menu('s_mala.txt')

#Collection of menus & Operating Hours
all_menu = {'chickenrice': [chickenrice, [], []],
            'muslim': [muslim, b_muslim, []], 
            'western': [western, b_western, []],
            'noodles': [noodles, [], s_noodles], 
            'mala' : [mala, [], s_mala]}

default_menu = {'chickenrice': chickenrice, 'muslim': muslim, 'western': western,
            'noodles': noodles, 'mala' : mala}

######## Jasper #######

############Khin / Jasper / HaoCheng ##########
op_hours ={'chickenrice': (8,16), 'western': (8,16), 'noodles': (8,17), 'muslim': (8,17), 'mala': (10,17)}

#Save to File
save_dict(default_menu, 'default_menu')
save_dict(all_menu, 'all_menu')
save_dict(op_hours, 'op_hours')

    

