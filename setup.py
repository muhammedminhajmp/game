import cx_Freeze
from cx_Freeze import setup, Executable
import os
import pygame

# Dependencies for the game
# include_files = [
#     # Add paths to game assets (images, sounds) if you have them
#     # ("path_to_assets_folder", "assets"),  # For example: assets folder
# ]
include_files = [("assets", "assets")]

# Add pygame to the packages list (required for cx_Freeze)
packages = ["pygame"]

# Base setting for Windows
base = None
if os.name == 'nt':  # If running on Windows
    base = "Win32GUI"  # Prevents the console window from appearing

# Executable configuration
executables = [
    Executable("pygame3.py", base=base, target_name="MyPlatformerGame.exe", shortcut_name="ZIZO",
        shortcut_dir="DesktopFolder",icon=r"D:\trogon\pratice\python-game\assets\kneepad.ico",)
]

# Setup function
setup(
    name="Platformer Game",
    version="1.0",
    description="A 2D Platformer Game built with Pygame",
    options={
        "build_exe": {
            "packages": packages,
            "include_files": include_files
        }
    },
    executables=executables
)
