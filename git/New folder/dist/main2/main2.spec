# -*- mode: python -*-

block_cipher = None


a = Analysis(['main2.py'],
             pathex=['C:\\Users\\trann\\Documents\\New folder'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
	       Tree('C:\\Users\\trann\\Documents\\New folder'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main2')
