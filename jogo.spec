# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['jogo.py'],
    pathex=[],
    binaries=[],
    datas=[('monkey.png', '.'), ('maca.png', '.'), ('inimigo.png', '.'), ('Paparazzi.mp3', '.'), ('fundo1.png', '.'), ('fundo2.png', '.'), ('fundo3.png', '.')],
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
    name='jogo',
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
)
