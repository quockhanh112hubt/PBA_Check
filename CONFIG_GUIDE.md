# Configuration Management Guide

## 📋 Tổng quan

Chương trình hiện đã hỗ trợ quản lý cấu hình thông qua file `config.json` và giao diện Settings.

## 🎯 Các thay đổi chính

### 1. File cấu hình mới
- **config.json**: Lưu trữ tất cả cấu hình
- **config_manager.py**: Module quản lý config

### 2. Giao diện Settings
- Truy cập: Click nút **⚙️ Settings** ở góc dưới bên phải màn hình chính
- Chức năng:
  - Cấu hình thông số Update (FTP, Version URL)
  - Cấu hình SQL Server Database
  - Cấu hình Oracle Database
  - Reset về mặc định
  - Lưu cấu hình

### 3. Cấu trúc config.json

```json
{
    "update": {
        "program_directory": "C:\\PBA_CHECK",
        "ftp_base_url": "ftp://update:update@192.168.110.12/...",
        "version_url": "ftp://update:update@192.168.110.12/.../version.txt"
    },
    "database": {
        "sql_server": {
            "driver": "ODBC Driver 17 for SQL Server",
            "server": "192.168.35.32",
            "port": "1433",
            "database": "ITMV_KTNG_DB",
            "username": "ITMV_KTNG",
            "password": "!itm@semi!12"
        },
        "oracle": {
            "host": "192.168.35.20",
            "port": "1521",
            "service_name": "ITMVPACKMES",
            "username": "mighty",
            "password": "mighty"
        }
    }
}
```

## 🔧 Cách sử dụng

### Thay đổi cấu hình qua GUI

1. Khởi động chương trình
2. Click nút **⚙️ Settings** ở màn hình chính
3. Chỉnh sửa các thông số cần thiết
4. Click **💾 Save Settings**
5. Restart chương trình để áp dụng thay đổi

### Thay đổi cấu hình qua file

1. Mở file `config.json`
2. Chỉnh sửa các giá trị cần thiết
3. Save file
4. Restart chương trình

### Reset về mặc định

1. Mở Settings window
2. Click **🔄 Reset to Default**
3. Confirm
4. Restart chương trình

## 📝 Lưu ý quan trọng

1. **Backup config**: Nên backup file `config.json` trước khi thay đổi
2. **Restart required**: Phải restart chương trình sau khi thay đổi config
3. **Password security**: Mật khẩu được lưu dạng plain text trong config.json
4. **File location**: File `config.json` phải ở cùng thư mục với Main.py

## 🔐 Bảo mật

⚠️ **Quan trọng**: 
- File `config.json` chứa thông tin nhạy cảm (passwords)
- Không chia sẻ file này lên internet/repository
- Nên thêm `config.json` vào `.gitignore`
- Cân nhắc mã hóa passwords trong tương lai

## 🚀 Files đã được cập nhật

1. **Main.py** - Thêm Settings window và load config
2. **config_manager.py** - Module quản lý config (mới)
3. **config.json** - File cấu hình (mới)
4. **creategui_P1_new.py** - Sử dụng config thay vì hard-code
5. **creategui_P230_new.py** - Sử dụng config thay vì hard-code
6. **creategui_P4_new.py** - Sử dụng config thay vì hard-code

## 📞 Hỗ trợ

Liên hệ IT Team nếu gặp vấn đề với cấu hình.
