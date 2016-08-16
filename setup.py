import os
import numpy
from Tkinter import *


def run():
    if not os.path.isdir(fileLocation.get() + '\Rabbit-invontory'):
        os.makedirs(fileLocation.get() + '\Rabbit-invontory')
    if not os.path.isdir(r'C:\Program Files' + '\Rabbit-essential'):
        os.makedirs(r'C:\Program Files' + '\Rabbit-essential')
    if not os.path.isdir(fileLocation.get() + '\Rabbit-invontory\Rabbits'):
        os.makedirs(fileLocation.get() + '\Rabbit-invontory\Rabbits')
    if not os.path.isdir(fileLocation.get() + '\Rabbit-invontory\Essential'):
        os.makedirs(fileLocation.get() + '\Rabbit-invontory\Essential')
    numpy.save('C:\Program Files\Rabbit-essential\Directory', fileLocation.get() + '\Rabbit-invontory')

master = Tk()
Label(master, text='Main folder location').grid(row=0)
fileLocation = Entry(master)
fileLocation.grid(row=0, column=1)

Button(master, text='Run', command=run).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text='Cancel', command=master.quit).grid(row=2, column=1, sticky=W, pady=4)
mainloop()