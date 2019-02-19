# -*- mode: python -*-

block_cipher = None


a = Analysis(['guest.py','product.py'],
             pathex=['D:\\Python37-32\\lab\\ProductManager'],
             binaries=[],
             datas=[('D:\\Python37-32\\lab\\ProductManager\\data','data'),('D:\\Python37-32\\lab\\ProductManager\\icon','icon'),
                   ('D:\\Python37-32\\lab\\ProductManager\\guest','guest')],
             hiddenimports=['sqlite3','PyQt5'],
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
          name='guest',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='guest')
