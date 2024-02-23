import PyInstaller.__main__

options = ['--onefile', '--console']
script_file = 'rota.lua'

PyInstaller.__main__.run([*options, script_file])
