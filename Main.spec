# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('Resource', 'Resource'),
        ('Logo', 'Logo'),
        ('config.json', '.'),
        ('config_manager.py', '.'),
        ('utils.py', '.'),
        ('creategui_P1_new.py', '.'),
        ('creategui_P230_new.py', '.'),
        ('creategui_P4_new.py', '.'),
    ],
    hiddenimports=[
        'tkinter',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'cx_Oracle',
        'pyodbc',
        'config_manager',
        'utils',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PBA_Function_Checker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Logo\\logo.ico' if os.path.exists('Logo\\logo.ico') else None,
)
