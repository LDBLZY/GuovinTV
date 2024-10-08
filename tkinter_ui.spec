# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['tkinter_ui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config/config.ini', 'config'),
        ('config/demo.txt', 'config'),
        ('updates/multicast/multicast_map.json', 'updates/multicast'),
        ('updates/multicast/multicast_region_result.json', 'updates/multicast')
    ],
    hiddenimports=[],
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
    name='update-tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
