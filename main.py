import os
import sys
import time
import pyautogui
import ctypes

from termcolor import colored
from colorant import Colorant
from other import Settings

class Main:
    os.system('color')
    KEY_NAMES = {
        0x01: "Tombol Kiri Mouse", 0x02: "Tombol Kanan Mouse", 0x04: "Tombol Tengah Mouse", 0x05: "Tombol X1 Mouse", 
        0x06: "Tombol X2 Mouse", 0x08: "Backspace", 0x09: "Tab", 0x0D: "Enter", 0x10: "Shift", 
        0x11: "Ctrl", 0x12: "Alt", 0x14: "CapsLock", 0x1B: "Esc", 0x20: "Spasi", 0x25: "Kiri", 
        0x26: "Atas", 0x27: "Kanan", 0x28: "Bawah", 0x30: "0", 0x31: "1", 0x32: "2", 0x33: "3", 
        0x34: "4", 0x35: "5", 0x36: "6", 0x37: "7", 0x38: "8", 0x39: "9", 0x41: "A", 0x42: "B", 
        0x43: "C", 0x44: "D", 0x45: "E", 0x46: "F", 0x47: "G", 0x48: "H", 0x49: "I", 0x4A: "J", 
        0x4B: "K", 0x4C: "L", 0x4D: "M", 0x4E: "N", 0x4F: "O", 0x50: "P", 0x51: "Q", 0x52: "R", 
        0x53: "S", 0x54: "T", 0x55: "U", 0x56: "V", 0x57: "W", 0x58: "X", 0x59: "Y", 0x5A: "Z", 
        0x70: "F1", 0x71: "F2", 0x72: "F3", 0x73: "F4", 0x74: "F5", 0x75: "F6", 
        0x76: "F7", 0x77: "F8", 0x78: "F9", 0x79: "F10", 0x7A: "F11", 0x7B: "F12"}

    def __init__(self):
        self.settings = Settings()
        self.monitor = pyautogui.size()
        self.CENTER_X, self.CENTER_Y = self.monitor.width // 2, self.monitor.height // 2
        self.XFOV = self.settings.get_int('Settings', 'X-FOV')
        self.YFOV = self.settings.get_int('Settings', 'Y-FOV')
        self.colorant = Colorant(
            self.CENTER_X - self.XFOV // 2, self.CENTER_Y - self.YFOV // 2,
            self.XFOV, self.YFOV)
    
    def cmd(self, width, height):
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
            style &= ~0x00040000
            style &= ~0x00010000
            ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)
        STD_OUTPUT_HANDLE_ID = ctypes.c_ulong(0xFFFFFFF5)
        windll = ctypes.windll.kernel32
        handle = windll.GetStdHandle(STD_OUTPUT_HANDLE_ID)
        rect = ctypes.wintypes.SMALL_RECT(0, 0, width - 1, height - 1)
        windll.SetConsoleScreenBufferSize(handle, ctypes.wintypes._COORD(width, height))
        windll.SetConsoleWindowInfo(handle, ctypes.c_int(True), ctypes.pointer(rect))

    def print_logo(self):
        os.system(f"title Colorant")
        print(colored('''
                (          (    )    ) :   ( (  
                )\  ( (  : )\  ((.  ()))(  )\)\ 
               (_() )\)\  (_() ))\ ()(())\((_)_)
               /   \_((_)((_)()(_))/ _` | | || |
               | - | '  \/ _` | ' \)__. | |\_. |
               |_|_|_|_|_|__/_|_||_|___/|_||__/ 

                                                Cheese Calorant\n''', 'cyan'))

    def print_info(self):
        try:
            print(colored('[', 'white') + colored('Pengaturan Tombol', 'cyan') + colored(']', 'white'))
            print(colored('[', 'white') + colored('●', 'light_grey') + colored(']', 'white') +
                  colored(f' Tahan {self.KEY_NAMES[self.colorant.AIMBOT_KEY]}', 'light_grey') + colored(' → Aimbot', 'blue'))
            print(colored('[', 'white') + colored('●', 'light_grey') + colored(']', 'white') +
                  colored(f' Tekan {self.KEY_NAMES[self.colorant.TOGGLE_KEY]}', 'light_grey') + colored(' → Toggle ON/OFF', 'blue'))
            print()
            print(colored('[', 'white') + colored('Informasi', 'cyan') + colored(']', 'white'))
            print(colored('[', 'white') + colored('●', 'light_grey') + colored(']', 'white') +
                  colored(f' Ini adalah aimbot sumber terbuka gratis yang dibuat untuk tujuan pendidikan, jika seseorang mencoba menjualnya kepada Anda,\nAnda sedang ditipu.', 'blue'))
            print(colored('[', 'white') + colored('●', 'light_grey') + colored(']', 'white') +
                  colored(f' Colorant menggunakan deteksi warna hsv dan beberapa jenis alat tangkap layar untuk berinteraksi dengan warna yang ditentukan di layar, tanpa memodifikasi memori atau file game.', 'blue'))
            print(colored('[', 'white') + colored('●', 'light_grey') + colored(']', 'white') +
                  colored(f' Pembaruan terakhir → 23 MEI 2023.', 'blue'))
            print(colored('[', 'white') + colored('●', 'light_grey') + colored(']', 'white') +
                  colored(f' Temukan saya di sini: {colored("https://github.com/AmangLy6666", "cyan", attrs=["underline"])}', 'blue'))
            print()
        except:
            os.system('cls')
            print(colored('[Error]', 'red'), colored('Nilai tidak valid ditemukan dalam settings.ini', 'white'))
            time.sleep(10)
            sys.exit()

    def run(self):
        self.cmd(125,30)
        self.print_logo()
        self.print_info()
        self.colorant.listen()

if __name__ == '__main__':
    Main().run()
