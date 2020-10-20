
# Without GUI (GRAPHICAL USER INTERFACE)
import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\Student7\Desktop\img1.png')


# With GUI
import pyautogui
import tkinter as tk

root= tk.Tk()
root.title('CapTuRe')

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def capture():
    
    capture = pyautogui.screenshot()
    capture.save(r'C:\Users\Student7\Desktop\img1.png')

myButton = tk.Button(text='Take Screenshot', command=capture, bg='green',fg='white',font= 15)
canvas1.create_window(150, 150, window=myButton)

if __name__ == '__main__':
  root.mainloop()
