from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from math import floor as ceil
from tkinter import *
from tkinter.ttk import *

device = AudioUtilities.GetSpeakers()
interface = device.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def get():
    return volume.GetMasterVolumeLevelScalar() * 100

def set(vol: float = 50):
    volume.SetMasterVolumeLevelScalar(vol / 100, None)
    stat.config(text=f"Select Volume Level ({ceil(get())}):")

master = Tk()
master.geometry("560x300")
master.title("Worst Volume Control Have Ever Made To The Public Using Python (v1.0)")
COLUMNS = 8
v = IntVar(master, value=ceil(get()))

for c in range(COLUMNS):
    master.grid_columnconfigure(c, weight=1)

stat = Label(master, text=f"Select Volume Level ({ceil(get())}):")
stat.grid(row=0, column=0, columnspan=COLUMNS, sticky="w", pady=5)

values = {f"{i}%": i for i in range(1, 101)}

for idx, (text, value) in enumerate(values.items()):
    row = idx // COLUMNS
    col = idx % COLUMNS
    Radiobutton(
        master,
        text=text,
        variable=v,
        value=value,
        command=lambda val=value: set(val)
    ).grid(row=row + 1, column=col, sticky="w")

mainloop()
