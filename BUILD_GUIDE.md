# 📦 BUILD GUIDE - PBA Function Checker

## 🎯 Yêu cầu trước khi build:

1. **Python 3.x** đã được cài đặt
2. **Tất cả dependencies** đã được cài:
   ```bash
   pip install pillow cx_Oracle pyodbc
   ```
3. **PyInstaller** (sẽ tự động cài nếu chưa có)

## 🚀 Cách 1: Build bằng BAT file (Khuyên dùng)

### Bước 1: Chạy script
```bash
build_main.bat
```

### Bước 2: Chờ build hoàn tất
- Script sẽ tự động clean, build và copy files
- Thời gian build: ~2-3 phút

### Bước 3: Kiểm tra output
Sau khi build xong, kiểm tra folder `dist/`:
```
dist/
├── PBA_Function_Checker.exe  ← File chính
├── config.json                ← Configuration
├── version.txt                ← Version info
├── Resource/                  ← Images (OK.png, NG.png)
└── Logo/                      ← Logo files
```

## 🐍 Cách 2: Build bằng Python script

### Bước 1: Chạy script
```bash
python build_main.py
```

### Bước 2: Chờ build hoàn tất
Same as Cách 1

## ⚙️ Build thủ công (Advanced)

Nếu muốn build thủ công:

```bash
# 1. Clean previous build
rmdir /s /q build dist

# 2. Build với PyInstaller
pyinstaller Main.spec --clean --noconfirm

# 3. Copy files manually
xcopy /E /I /Y Resource dist\Resource\
xcopy /E /I /Y Logo dist\Logo\
copy config.json dist\
copy version.txt dist\
```

## 📋 Checklist sau khi build:

- [ ] File `PBA_Function_Checker.exe` tồn tại trong `dist/`
- [ ] Chạy thử exe để kiểm tra:
  - [ ] Giao diện hiển thị đúng
  - [ ] Images load được (OK.png, NG.png)
  - [ ] Kết nối database hoạt động
  - [ ] Settings window mở được
- [ ] File `config.json` có trong `dist/`
- [ ] Folder `Resource/` có đầy đủ images

## 🐛 Troubleshooting:

### Lỗi: "Module not found"
**Giải pháp:** Cài đặt module bị thiếu:
```bash
pip install <module_name>
```

### Lỗi: "Images not loading"
**Giải pháp:** Đảm bảo folder `Resource/` đã được copy vào `dist/`

### Lỗi: "cx_Oracle.DatabaseError"
**Giải pháp:** 
- Cài đặt Oracle Instant Client
- Kiểm tra config trong `config.json`

### Lỗi: "pyodbc connection failed"
**Giải pháp:**
- Cài đặt ODBC Driver 17 for SQL Server
- File `ODBC17.msi` có sẵn trong project

### Build thành công nhưng exe không chạy
**Giải pháp:**
1. Chạy với console mode để xem lỗi:
   - Sửa `Main.spec`: `console=True`
   - Build lại
2. Kiểm tra Windows Defender/Antivirus

## 📦 Deployment:

Sau khi build thành công, copy toàn bộ folder `dist/` vào:
```
C:\PBA_CHECK\
```

Cấu trúc triển khai:
```
C:\PBA_CHECK\
├── PBA_Function_Checker.exe
├── config.json
├── version.txt
├── update_script.exe (nếu có)
├── Resource\
│   ├── Ok.png
│   ├── NG.png
│   └── background.jpg
└── Logo\
    └── (logo files)
```

## 🔄 Update workflow:

1. Build exe mới
2. Đẩy lên FTP server theo config trong `config.json`:
   - Server: `ftp_server`
   - Path: `update_path`
3. Update file `version.txt` trên FTP
4. Chương trình sẽ tự động check và update

## 📝 Notes:

- Build size: ~50-100MB (tùy dependencies)
- Console mode: Set `console=True` trong `Main.spec` để debug
- Icon: Đặt file `logo.ico` trong folder `Logo/` để thêm icon
- Optimize: Có thể giảm size bằng cách exclude modules không dùng

---

**Happy Building! 🚀**
