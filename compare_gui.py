"""
So sánh trực quan giữa giao diện cũ và mới
Chạy file này để mở 2 cửa sổ cạnh nhau
"""

import subprocess
import sys
import time

def run_old_gui():
    """Chạy giao diện cũ"""
    try:
        subprocess.Popen([sys.executable, "-c", """
import tkinter as tk
from creategui_P230 import create_gui_P230

def dummy_func():
    pass

create_gui_P230(dummy_func, dummy_func, dummy_func)
"""])
        print("✓ Đã mở giao diện CŨ")
    except Exception as e:
        print(f"❌ Lỗi mở giao diện cũ: {e}")

def run_new_gui():
    """Chạy giao diện mới"""
    try:
        subprocess.Popen([sys.executable, "test_P230_new.py"])
        print("✓ Đã mở giao diện MỚI")
    except Exception as e:
        print(f"❌ Lỗi mở giao diện mới: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("SO SÁNH GIAO DIỆN P230")
    print("=" * 60)
    print("\nĐang mở 2 cửa sổ để so sánh...")
    print()
    
    # Chạy giao diện cũ
    run_old_gui()
    time.sleep(1)
    
    # Chạy giao diện mới
    run_new_gui()
    
    print()
    print("📌 Tips:")
    print("  - Kéo 2 cửa sổ cạnh nhau để so sánh")
    print("  - Test cùng PBA ID trên cả 2 để thấy sự khác biệt")
    print("  - Để ý phần Result Card không đẩy Log ở giao diện mới")
    print()
    print("✨ Giao diện mới có:")
    print("  ✓ Result card cố định không đẩy log")
    print("  ✓ Layout ngang chuyên nghiệp")
    print("  ✓ Badge status với màu sắc")
    print("  ✓ Icons cho mọi thông tin")
    print("  ✓ Thống kê và history rõ ràng hơn")
