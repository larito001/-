"""双击运行此脚本，打包生成 exe（输出到 Build 文件夹）"""
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
BUILD = os.path.join(ROOT, "Build")

os.chdir(ROOT)

# 安装 PyInstaller
subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller", "-q"])

# 打包 auto_clicker
print("\n===== 打包 auto_clicker.exe =====")
subprocess.run([
    sys.executable, "-m", "PyInstaller",
    "--noconfirm", "--onefile", "--windowed",
    "--name", "auto_clicker",
    "--uac-admin",
    "--distpath", BUILD,
    "--workpath", os.path.join(BUILD, "temp"),
    "--specpath", os.path.join(BUILD, "temp"),
    os.path.join(SRC, "auto_clicker.py"),
])

# 打包 auto_battle
print("\n===== 打包 auto_battle.exe =====")
subprocess.run([
    sys.executable, "-m", "PyInstaller",
    "--noconfirm", "--onefile", "--windowed",
    "--name", "auto_battle",
    "--uac-admin",
    "--distpath", BUILD,
    "--workpath", os.path.join(BUILD, "temp"),
    "--specpath", os.path.join(BUILD, "temp"),
    "--add-data", os.path.join(SRC, "Button.jpg") + ";.",
    "--add-data", os.path.join(SRC, "selectPage.jpg") + ";.",
    os.path.join(SRC, "auto_battle.py"),
])

print("\n===== 完成！exe 在 Build 文件夹中 =====")
input("按回车键退出...")
