import model_staff
import model_otdel
import model_post
import model_master
import view
import os

def mode_selection():
    os.system('CLS') 
    mode = view.mode()
    if mode == 1:
        mode_table = view.mode_table()
        if mode_table == 1: model_staff.AddStaff()
        if mode_table == 2: model_otdel.AddOtdel()
        if mode_table == 3: model_post.AddPost()
        if mode_table == 4: model_master.AddMaster()
    elif mode == 2:
        mode_table = view.mode_table()
        if mode_table == 1: model_staff.DelStaff()
        if mode_table == 2: model_otdel.DelOtdel()
        if mode_table == 3: model_post.DelPost()
        if mode_table == 4: print('Данный раздел находится в разработке...')
    elif mode == 3:
        mode_table = view.mode_table()
        if mode_table == 1: model_staff.RemoveStaff()
        if mode_table == 2: model_otdel.RemoveOtdel()
        if mode_table == 3: model_post.RemovePost()
        if mode_table == 4: print('Данный раздел находится в разработке...')
    elif mode == 4:
        print('Данный раздел находится в разработке...')
    elif mode == 5:
        print('Данный раздел находится в разработке...')
    elif mode == 6:
        exit()