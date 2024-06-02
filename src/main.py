import pyautogui
import numpy as np
import cv2
import keyboard
from rich.console import Console
import os
from time import sleep

keybind = 'q'

def capture_screen(region=None):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

def detect_enemy(screen):
    lower_color = np.array([0, 0, 200])
    upper_color = np.array([50, 50, 255])
    
    mask = cv2.inRange(screen, lower_color, upper_color)
    return np.any(mask)

def activate_tb():
    global keybind
    
    console = Console()
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("TriggerWave", style="cyan")
    
    console.print(f"Hold special keybind ({keybind}) and aim", end=" ")
    console.print("at enemies", style="cyan", end="")
    console.print("!")
    
    console.print("Press", end=" ")
    console.print("Escape", style="cyan", end=" ")
    console.print("to back to menu.")
    while True:
        screen = capture_screen(region=(959, 539, 1, 1))
        if detect_enemy(screen) and keyboard.is_pressed(keybind):
            pyautogui.mouseDown()
        elif keyboard.is_pressed('escape'):
            print_menu(2)
            break
        else:
            pyautogui.mouseUp()
            
def docs():
    console = Console()
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("TriggerDocs", style="cyan")
    
    console.print("Made by:", end=" ")
    console.print("biterolf10 ( https://github.com/biterolf10 )", style="cyan")
    console.print("Made for:", end=" ")
    console.print("everyone", style="hot_pink", end="")
    console.print(".", end="\n\n")
    
    console.print("Working for", end=" ")
    console.print("every", style="cyan", end=" ")
    console.print("game with cursor color changing on enemy hover.", end="\n\n")
    
    console.print("To move down in menu press", end=" ")
    console.print("S or Down Arrow", style="cyan", end="")
    console.print(".",)
    
    console.print("To move up in menu press", end=" ")
    console.print("W or Up Arrow", style="cyan", end="")
    console.print(".")
    
    console.print("To confirm menu choose press", end=" ")
    console.print("Space or Enter", style="cyan", end="")
    console.print(".")
    
    console.print("To cancel menu choose press", end=" ")
    console.print("Escape", style="cyan", end="")
    console.print(".", end="\n\n")
    
    console.print(">", style="cyan", end=" ")
    console.print("Back")
    
    sleep(.2)
    while True:
        if (keyboard.is_pressed('space') or keyboard.is_pressed('enter')):
            print_menu(0)
            break
        
def change_keybind():
    global keybind
    
    console = Console()
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("TriggerCfg", style="cyan")
    
    console.print("Write special", end=" ")
    console.print("keybind", style="cyan", end=" ")
    console.print("that allow trigger bot to shoot.")
    
    console.print("(Press button that you want to use and confirm)")
    console.print("> ", style="cyan", end=" ")
    
    keybind = None
    while keybind is None:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            keybind = event.name
            break
    
    sleep(.2)
    while True:
        if (keyboard.is_pressed('space') or keyboard.is_pressed('enter')):
            print_menu(1)
            break
        
def exit_program():
    console = Console()
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("TriggerExit", style="cyan")
    console.print(">", style="cyan", end=" ")
    console.print("Exit TriggerWave?")
    
    sleep(.2)
    while True:
        if (keyboard.is_pressed('space') or keyboard.is_pressed('enter')):
            exit(0)
        if keyboard.is_pressed('escape'):
            print_menu(3)
            break
    
def print_menu(pointer):
    console = Console()
    os.system('cls' if os.name == 'nt' else 'clear')
    if pointer == 0:
        console.print("TriggerWave", style="cyan")
                    
        console.print(">", style="cyan", end=" ")
        console.print("Docs")
        console.print("Change Keybind")
        console.print("Start TriggerBot")
        console.print("Exit")
    elif pointer == 1:
        console.print("TriggerWave", style="cyan")
                    
        console.print("Docs")
        console.print(">", style="cyan", end=" ")
        console.print("Change Keybind")
        console.print("Start TriggerBot")
        console.print("Exit")
    elif pointer == 2:
        console.print("TriggerWave", style="cyan")
                    
        console.print("Docs")
        console.print("Change Keybind")
        console.print(">", style="cyan", end=" ")
        console.print("Start TriggerBot")
        console.print("Exit")
    elif pointer == 3:
        console.print("TriggerWave", style="cyan")
                    
        console.print("Docs")
        console.print("Change Keybind")
        console.print("Start TriggerBot")
        console.print(">", style="cyan", end=" ")
        console.print("Exit")
            
def menu():
    console = Console()
    pointer = 0
    
    print_menu(pointer)
    while True:
        if (keyboard.is_pressed('down') or keyboard.is_pressed('s')) and pointer < 3:
            pointer += 1
            print_menu(pointer)
            sleep(.2)
        elif (keyboard.is_pressed('up') or keyboard.is_pressed('w')) and pointer > 0:
            pointer -= 1
            print_menu(pointer)
            sleep(.2)
        elif (keyboard.is_pressed('space') or keyboard.is_pressed('enter')):
            if pointer == 0:
                docs()
                sleep(.3)
            elif pointer == 1:
                change_keybind()
                sleep(.3)
            elif pointer == 2:
                activate_tb()
                sleep(.3)
            elif pointer == 3:
                exit_program()
                sleep(.3)
    

def main():
    menu()

if __name__ == "__main__":
    main()