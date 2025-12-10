"""
Script để apply giao diện mới cho tất cả 3 models: P1, P4, P230
Backup files cũ trước khi thay thế
"""

import shutil
import os
from datetime import datetime

def backup_and_replace(old_file, new_file, model_name):
    """Backup và thay thế một file"""
    backup_dir = "backup"
    
    # Tạo thư mục backup nếu chưa có
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Backup file cũ
    if os.path.exists(old_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f"{os.path.basename(old_file)}_{timestamp}.bak")
        shutil.copy2(old_file, backup_file)
        print(f"  ✓ Backed up {model_name}: {backup_file}")
        
        # Xóa file cũ
        os.remove(old_file)
    
    # Copy file mới thành file chính
    if os.path.exists(new_file):
        shutil.copy2(new_file, old_file)
        print(f"  ✓ Applied new GUI for {model_name}")
        return True
    else:
        print(f"  ❌ New file not found: {new_file}")
        return False

def apply_all_updates():
    """Apply updates cho tất cả models"""
    print("=" * 70)
    print("APPLY NEW GUI FOR ALL MODELS")
    print("=" * 70)
    print()
    
    updates = [
        ("creategui_P230.py", "creategui_P230_new.py", "P230"),
        ("creategui_P1.py", "creategui_P1_new.py", "P1"),
        ("creategui_P4.py", "creategui_P4_new.py", "P4")
    ]
    
    success_count = 0
    
    for old_file, new_file, model_name in updates:
        print(f"\n📋 Processing {model_name}...")
        if backup_and_replace(old_file, new_file, model_name):
            success_count += 1
    
    print()
    print("=" * 70)
    print(f"✨ Completed! {success_count}/{len(updates)} models updated successfully")
    print("=" * 70)
    print()
    print("📝 Notes:")
    print("  - Old files backed up to 'backup/' folder")
    print("  - All models now have:")
    print("    ✓ Modern UI with fixed Result Card")
    print("    ✓ Statistics panel")
    print("    ✓ Connection status indicators")
    print("    ✓ Recent History with filter feature")
    print("    ✓ Activity Log")
    print()
    print("🚀 Ready to use! Restart your application.")
    print()

if __name__ == "__main__":
    print()
    response = input("⚠️  This will replace P1, P4, and P230 GUI files. Continue? (yes/no): ")
    
    if response.lower() in ['yes', 'y']:
        apply_all_updates()
    else:
        print("\n❌ Operation cancelled.")
