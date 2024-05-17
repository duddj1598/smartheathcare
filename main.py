from tkinter import *
import tkinter.font
import tkinter.ttk as ttk
import json

win = Tk()

win.title("SHC")
icon = PhotoImage(file="./img/logo.png")
win.iconphoto(True,icon)
win.geometry("400x500")
win.resizable(False, False)

def restart():
    global win
    try:
        win.destroy()
    finally:
        win = Tk()
        win.title("SHC")
        icon = PhotoImage(file="./img/logo.png")
        win.iconphoto(True,icon)
        win.geometry("400x500")
        win.resizable(False, False)
        win["background"] = "#61779a"

def usr_info_push():
    usr_hight = ent_hight.get()
    usr_weight = ent_weight.get()
    usr_info_list = {"hight":int(usr_hight),"weight":int(usr_weight)}
    with open(f"./data/{usr_id}.json",'r') as f:
        last_list = json.load(f)
        last_list.update(usr_info_list)
    with open(f"./data/{usr_id}.json",'w') as f:
        json.dump(last_list,f,ensure_ascii=False,indent="\t")
    main()
        

def usr_info_input():
    global ent_hight,ent_weight
    restart() #화면 재구성
    lbl_hight = Label(win,text="키 : ",background="#61779a")
    ent_hight = Entry(win,highlightthickness=0)
    lbl_weight = Label(win,text="몸무게 : ",background="#61779a")
    ent_weight = Entry(win,highlightthickness=0)
    push_button = Button(win,text="입력",width=20,command=usr_info_push,highlightbackground="#61779a")
    back_button = Button(win,text="뒤로가기",width=3,height=1,highlightbackground="#61779a",command=main)
    back_button.place(x=320,y=450)
    lbl_hight.place(x=103, y=170)
    ent_hight.place(x=130, y=173)
    lbl_weight.place(x=80, y=220)
    ent_weight.place(x=130, y=223)
    push_button.place(x=98, y=260)

def usr_nutri_push():
    kcal = int(ent_kcal.get())
    carbs = int(ent_carbs.get())
    protein = int(ent_protein.get())
    fat = int(ent_fat.get())
    with open(f"./data/{usr_id}.json",'r') as f:
        last_list = json.load(f)
        last_list["kcal"] += kcal
        last_list["carbs"] += carbs
        last_list["protein"] += protein
        last_list["fat"] += fat
    with open(f"./data/{usr_id}.json",'w') as f:
        json.dump(last_list,f,ensure_ascii=False,indent="\t")
    main()

def usr_nutri_input():
    global ent_kcal,ent_carbs,ent_protein,ent_fat
    restart() #화면 재구성
    lbl_kcal = Label(win,text="칼로리 : ",background="#61779a")
    ent_kcal = Entry(win,highlightthickness=0)
    lbl_carbs = Label(win,text="탄수화물 : ",background="#61779a")
    ent_carbs = Entry(win,highlightthickness=0)
    lbl_protein = Label(win,text="단백질 : ",background="#61779a")
    ent_protein = Entry(win,highlightthickness=0)
    lbl_fat = Label(win,text="지방 : ",background="#61779a")
    ent_fat = Entry(win,highlightthickness=0)
    push_button = Button(win,text="입력",width=20,command=usr_nutri_push,highlightbackground="#61779a")
    back_button = Button(win,text="뒤로가기",width=3,height=1,highlightbackground="#61779a",command=main)
    back_button.place(x=320,y=450)
    lbl_kcal.place(x=82, y=140)
    ent_kcal.place(x=130, y=143)
    lbl_carbs.place(x=70, y=180)
    ent_carbs.place(x=130, y=183)
    lbl_protein.place(x=81, y=220)
    ent_protein.place(x=130, y=223)
    lbl_fat.place(x=92, y=260)
    ent_fat.place(x=130, y=263)
    push_button.place(x=95, y=300)

def usr_compare_input():
    restart()
    with open(f"./data/{usr_id}.json",'r') as f:
        user = json.load(f)
    if(user["gender"] == "여자"):
        standard_weight = pow(user["hight"]/100,2)*21
    elif(user["gender"] == "남자"):
        standard_weight = pow(user["hight"]/100,2)*22
    standard_kcal = standard_weight * 35
    standard_carbs = standard_kcal * 0.5
    standard_protein = standard_kcal * 0.2
    standard_fat = standard_kcal * 0.3
    Label(win,text="\n\n\n",bg="#61779a").pack()
    Label(win,text=f"하루 권장 칼로리는 {standard_kcal:.2f}kcal이고 \n권장 칼로리로부터 {user["kcal"]}kcal만큼 섭취해 \n{standard_kcal-user["kcal"]:.2f}kcal의 차이가 납니다.").pack()
    Label(win,text="\n",bg="#61779a").pack()
    Label(win,text=f"하루 권장 탄수화물은 {standard_carbs/4:.2f}g이고 \n권장 탄수화물로부터 {user["carbs"]}g만큼 섭취해 \n{standard_carbs/4-user["carbs"]:.2f}g의 차이가 납니다.").pack()
    Label(win,text="\n",bg="#61779a").pack()
    Label(win,text=f"하루 권장 단백질는 {standard_protein/4:.2f}kcal이고 \n권장 칼로리로부터 {user["protein"]}g만큼 섭취해 \n{standard_protein/4-user["protein"]:.2f}g의 차이가 납니다.").pack()
    Label(win,text="\n",bg="#61779a").pack()
    Label(win,text=f"하루 권장 지방은 {standard_fat/9:.2f}kcal이고 \n권장 칼로리로부터 {user["fat"]}g만큼 섭취해 \n{standard_fat/9-user["fat"]:.2f}g의 차이가 납니다.").pack()
    back_button = Button(win,text="뒤로가기",width=3,height=1,highlightbackground="#61779a",command=main)
    back_button.place(x=320,y=450)

def reset_button_command():
    with open(f"./data/{usr_id}.json",'r') as f:
        last_list = json.load(f)
        reset_list = {"kcal":0,"carbs":0,"protein":0,"fat":0}
        last_list.update(reset_list)
    with open(f"./data/{usr_id}.json",'w') as f:
        json.dump(last_list,f,ensure_ascii=False,indent="\t")
    main()
    Label(win,text="초기화 되었습니다.",fg="green",background="#61779a").pack()
        

def main():
    restart()
    font = tkinter.font.Font(family="AppleGothic", size=20, weight="bold")
    main_lbl = Label(win,text=f"{usr_id}",font=font,background="#61779a")
    main_lbl.pack()
    usr_info_button = Button(win,text="본인 정보 입력", width=10, height=7,command=usr_info_input)
    usr_nutri_button = Button(win,text="식품 정보 입력", width=10, height=7, command=usr_nutri_input)
    usr_compare_button = Button(win,text="권장량과 비교", width=10, height=7, command=usr_compare_input)
    reset_button = Button(win,text="영양정보 리셋",width=10, height=7, command=reset_button_command)
    usr_info_button.place(x=50, y=80)
    usr_nutri_button.place(x=230, y=80)
    usr_compare_button.place(x=50, y=250)
    reset_button.place(x=230,y=250)
    

def login_button_command():
    global usr_id
    usr_id = ent_id.get()
    usr_password = ent_password.get()
    try:
        with open(f"./data/{usr_id}.json",'r') as f:
            id_list = json.load(f)
        if(usr_password == id_list["password"]):
            main()
        else:
            init()
            error_lbl = Label(win,text="틀린 비밀번호입니다.",fg="red",background="#61779a")
            error_lbl.place(x=155,y=20)
    except FileNotFoundError:
        init()
        error_lbl = Label(win,text="없는 아이디입니다",fg="red",background="#61779a")
        error_lbl.place(x=157,y=20)

def login_command():
    global ent_id, ent_password
    restart() #화면 재구성
    lbl_id = Label(win,text="id : ",background="#61779a")
    ent_id = Entry(win,highlightthickness=0)
    lbl_password = Label(win,text="password : ",background="#61779a")
    ent_password = Entry(win,highlightthickness=0)
    login_button = Button(win,text="로그인",width=20,command=login_button_command,highlightbackground="#61779a")
    back_button = Button(win,text="뒤로가기",width=3,height=1,highlightbackground="#61779a",command=init)
    back_button.place(x=320,y=450)
    lbl_id.place(x=98, y=170)
    ent_id.place(x=130, y=173)
    lbl_password.place(x=50, y=220)
    ent_password.place(x=130, y=223)
    login_button.place(x=98, y=260)

def signup_button_command(gender):
    usr_id = ent_id.get()
    usr_password = ent_password.get()
    usr_gender = gender.get()
    signup_list = {"id":usr_id,"password":usr_password,"gender":usr_gender,"kcal":0,"carbs":0,"protein":0,"fat":0}
    with open(f"./data/{usr_id}.json",'w') as f:
        json.dump(signup_list,f,ensure_ascii=False,indent="\t")
    init()


def signup_command():
    global ent_id, ent_password
    gender = ["남자","여자"]
    restart() #화면 재구성
    lbl_id = Label(win,text="id : ",background="#61779a")
    ent_id = Entry(win,highlightthickness=0)
    lbl_password = Label(win,text="password : ",background="#61779a")
    ent_password = Entry(win,highlightthickness=0)
    lbl_gender = Label(win,text="성별 : ",background="#61779a")
    gender_combo = ttk.Combobox(win,values=gender,state="readonly",width=17)
    signup_button = Button(win,text="회원가입",width=20,command=lambda: signup_button_command(gender_combo),highlightbackground="#61779a")
    back_button = Button(win,text="뒤로가기",width=3,height=1,highlightbackground="#61779a",command=init)
    back_button.place(x=320,y=450)
    lbl_id.place(x=98, y=170)
    ent_id.place(x=120, y=173)
    lbl_password.place(x=50, y=220)
    ent_password.place(x=120, y=223)
    lbl_gender.place(x=87,y=270)
    gender_combo.place(x=122, y=270)
    signup_button.place(x=98, y=310)

    
def init():
    global login
    restart()
    login = Button(win,text="로그인",width=17,command=login_command,highlightbackground="#61779a")
    signup = Button(win,text="회원가입",width=17,command=signup_command,highlightbackground="#61779a")
    login.place(x=110,y=170)
    signup.place(x=110,y=220)

init()
win["background"] = "#61779a"

win.mainloop()