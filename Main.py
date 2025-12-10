import urllib.request
import subprocess
import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from creategui_P230_new import create_gui_P230
from creategui_P4_new import create_gui_P4
from creategui_P1_new import create_gui_P1
from utils import get_current_version
from PIL import Image, ImageTk

# Đường dẫn tới thư mục chứa các file chương trình
PROGRAM_DIRECTORY = "C:\\PBA_CHECK"
UPDATE_SCRIPT_EXECUTABLE = os.path.join(PROGRAM_DIRECTORY, "update_script.exe")

# Đường dẫn tới FTP Server
FTP_BASE_URL = "ftp://update:update@192.168.110.12/KhanhDQ/Update_Program/PBA_CHECK/"
VERSION_URL = FTP_BASE_URL + "version.txt"


def login():
    selected_option = option_var.get()
    root.destroy()
    
    if selected_option == "ECIGA-P1 4.0":
        create_gui_P1(create_login_ui, create_gui_P230, create_gui_P4)
    elif selected_option == "ECIGA-P2 3.0":
        create_gui_P230(create_login_ui, create_gui_P1, create_gui_P4)
    elif selected_option == "ECIGA-P4":
        create_gui_P4(create_login_ui, create_gui_P1, create_gui_P230)
    elif selected_option == "ECIGA-P2 4.0(Coming Soon)":
        Plant_Comming_Soon()


def Plant_Comming_Soon():
    messagebox.showinfo("Thông báo", "Plant đang trong quá trình phát triển!")
    create_login_ui()

def get_latest_version():
    try:
        with urllib.request.urlopen(VERSION_URL) as response:
            latest_version = response.read().decode('utf-8').strip()
        return latest_version
    except Exception as e:
        print(f"Không thể lấy phiên bản mới nhất: {e}")
        return None

def check_for_updates():
    current_version = get_current_version()
    latest_version = get_latest_version()
    
    if latest_version and latest_version > current_version:
        initiate_update()

def initiate_update():
    print("Đang chuẩn bị cập nhật và khởi động lại chương trình...")
    process = subprocess.Popen([UPDATE_SCRIPT_EXECUTABLE])
    print(f"Đã khởi chạy {UPDATE_SCRIPT_EXECUTABLE}, PID: {process.pid}")
    sys.exit()

def cancel():
    root.destroy
    sys.exit()

def create_login_ui():
    global root, option_var

    root = tk.Tk()
    root.title(f"PBA Function Data Checker Version {get_current_version()}")
    root.geometry("660x600")
    root.configure(bg='#00a99d')
    root.resizable(False, False)

    # Tải ảnh nền
    background_image = Image.open("Resource/background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    canvas = tk.Canvas(root, width=200, height=250)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Frame chính giữa
    frame = tk.Frame(root, bg='#003366', bd=0)
    frame.place(relx=0.5, rely=0.5, anchor='center', width=500, height=300)

    # Icon người dùng
    user_name = tk.Label(frame, bg='#003366', text="PBA FUNCTION DATA CHECKER", fg='#66CCFF', font=("Arial Black", 18))
    user_name.place(relx=0.5, y=25, anchor='center')
    user_icon = tk.Label(frame, bg='#003366', text="ITM Semiconductor Vietnam", fg='#66CCFF', font=("Cascadia Mono SemiBold", 9))
    user_icon.place(relx=0.5, y=50, anchor='center')

    # Tiêu đề đăng nhập
    title = tk.Label(frame, text="Select Production Model", fg='#66CCFF', bg='#003366', font=("Arial Black", 16))
    title.place(relx=0.5, y=100, anchor='center')

    # Tạo combobox cho các lựa chọn
    option_var = tk.StringVar()
    option_frame = tk.Frame(frame, bg='#e0f7fa', bd=1, relief='solid')
    option_frame.place(relx=0.5, y=150, anchor='center', width=300, height=40)
    combo = ttk.Combobox(option_frame, textvariable=option_var, font=("Arial", 12), state="readonly")
    combo['values'] = ("ECIGA-P1 4.0", "ECIGA-P2 3.0", "ECIGA-P4", "ECIGA-P2 4.0(Coming Soon)")
    combo.place(relx=0.5, rely=0.5, anchor='center', width=240, height=30)
    combo.current(1)

    # Nút đăng nhập
    login_button = tk.Button(frame, text="START", command=login, bg='#00796b', fg='#003366', font=("Arial", 14))
    login_button.place(relx=0.5, y=200, anchor='center', width=150, height=40)
    root.bind('<Return>', lambda event: login())

    root.mainloop()


if __name__ == "__main__":
    check_for_updates()
    create_login_ui()

