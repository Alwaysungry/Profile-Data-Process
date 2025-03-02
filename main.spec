# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['E:\\Third'],
             binaries=[
			 
			 ],
             datas=[
			 ('image\\ass.gif')
			 (‘image/downarrow.png’)
			 ("./image/downarrow.png")
			 ("./image/downarrow.png")
			 ("./image/downarrow.png")
			 (".\\image\\refresh.png")
			 ('.\\image\\eraser.png')
			 ("./image/uparrow.png")
			 ("./image/downarrow.png")
			 ("./image/uparrow.png")
			 ("./image/downarrow.png")
			 ("./image/downarrow.png")
			 (".\\image\\plot1.png")
			 ('.\\image\\eraser.png')
			 ("./image/uparrow.png")
			 ("./image/downarrow.png")
			 ("./image/uparrow.png")
			 ("./image/downarrow.png")
			 ("./image/downarrow.png")
			 ('.\\image\\eraser.png')
			 (".\\image\\plot1.png")
			 (".\\image\\plot2.png")
			 (".\\image\\eraser.png")
			 (".\\image\\plot2.png")
			 (".\\image\\eraser.png")
			 ('.\\image\\ouc.png')
			 ('.\\image\\min.png')
			 ('.\\image\\max.png')
			 ('.\\image\\close.png')
			 ('.\\image\\home.png')
			 ('.\\image\\data.png')
			 ('.\\image\\fig.png')
			 ('.\\image\\plot1.png')
			 ('.\\image\\plot1.png')
			 ('.\\image\\plot1.png')
			 ('.\\image\\plot2.png')
			 ('.\\image\\plot2.png')
			 ('.\\image\\help.png')
			 ('.\\image\\icon.png')
			 ],
             hiddenimports=['pkg_resources'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='mit.ico')
