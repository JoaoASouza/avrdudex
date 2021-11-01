from tkinter import *
from tkinter import ttk

def createProgrammerFrame():
    programmer_frame = ttk.Frame(root)
    programmer_frame['padding'] = (5, 5, 5, 5)
    programmer_frame['borderwidth'] = 2
    programmer_frame['relief'] = 'ridge'

    programmer = StringVar()
    port = StringVar()
    baudrate = StringVar()
    bitclock = StringVar()

    lbl_programmer = ttk.Label(programmer_frame, text='Programmer')
    box_programmer = ttk.Combobox(programmer_frame, textvariable=programmer, width=50)
    box_programmer['values'] = ('Arduino uno', 'AVR', 'Arduino Due')
    box_programmer.state(['readonly'])

    lbl_port = ttk.Label(programmer_frame, text='Port')
    box_port = ttk.Combobox(programmer_frame, textvariable=port)
    box_port['values'] = ('dev0', '/dev1', '/dev2')
    box_port.state(['readonly'])

    lbl_baudrate = ttk.Label(programmer_frame, text='Baud rate')
    txt_baudrate = ttk.Entry(programmer_frame, textvariable=baudrate)

    lbl_bitclock = ttk.Label(programmer_frame, text='Bit clock')
    txt_bitclock = ttk.Entry(programmer_frame, textvariable=bitclock)

    lbl_programmer.grid(row=0, column=0)
    box_programmer.grid(row=1, column=0, columnspan=3, sticky=(W, E))
    lbl_port.grid(row=2, column=0)
    box_port.grid(row=3, column=0)
    lbl_baudrate.grid(row=2, column=1)
    txt_baudrate.grid(row=3, column=1)
    lbl_bitclock.grid(row=2, column=2)
    txt_bitclock.grid(row=3, column=2)

    programmer_frame.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

def createMCUFrame():
    MCU_frame = ttk.Frame(root)
    MCU_frame['padding'] = (5, 5, 5, 5)
    MCU_frame['borderwidth'] = 2
    MCU_frame['relief'] = 'ridge'

    MCU = StringVar()

    lbl_MCU = ttk.Label(MCU_frame, text='MCU')

    box_MCU = ttk.Combobox(MCU_frame, textvariable=MCU)
    box_MCU['values'] = ('atmega', 'atmini')
    box_MCU.state(['readonly'])

    lbl_MCU_flash = ttk.Label(MCU_frame, text='Flash:\t32kB\t1E950F')

    lbl_MCU_EEPROM = ttk.Label(MCU_frame, text='EEPROM:\t1kB')

    lbl_MCU.grid(row=0)
    box_MCU.grid(row=1, sticky=(W, E))
    lbl_MCU_flash.grid(row=2, sticky=(W, E))
    lbl_MCU_EEPROM.grid(row=3, sticky=(W, E))

    MCU_frame.grid(row=0, column=3, columnspan=1, padx=5, pady=5)

def createFlashFrame():
    flash_frame = ttk.Frame(root)
    flash_frame['padding'] = (5, 5, 5, 5)
    flash_frame['borderwidth'] = 2
    flash_frame['relief'] = 'ridge'

    flash = StringVar()
    flash_mode = StringVar()
    flash_format = StringVar()

    lbl_flash = ttk.Label(flash_frame, text='Flash')

    txt_flash = ttk.Entry(flash_frame, textvariable=flash)

    btn_flash_file_browse = ttk.Button(flash_frame, text="...")

    rad_flash_write = ttk.Radiobutton(flash_frame, text='Write', variable=flash_mode, value='write')
    rad_flash_read = ttk.Radiobutton(flash_frame, text='Read', variable=flash_mode, value='read')
    rad_flash_verify = ttk.Radiobutton(flash_frame, text='Verify', variable=flash_mode, value='verify')

    btn_flash_go = ttk.Button(flash_frame, text="Go")

    lbl_flash_format = ttk.Label(flash_frame, text='Format')

    box_flash_format = ttk.Combobox(flash_frame, textvariable=flash_format)
    box_flash_format['values'] = ('auto', 'manual')
    box_flash_format.state(['readonly'])

    lbl_flash.grid(row=0, column=0)
    txt_flash.grid(row=1, column=0, columnspan=5, sticky=(W, E))
    btn_flash_file_browse.grid(row=1, column=5, columnspan=1)
    rad_flash_write.grid(row=2, column=0)
    rad_flash_read.grid(row=2, column=1)
    rad_flash_verify.grid(row=2, column=2)
    btn_flash_go.grid(row=2, column=3)
    lbl_flash_format.grid(row=2, column=4)
    box_flash_format.grid(row=2, column=5)

    flash_frame.grid(row=1, column=0, columnspan=3, sticky=(W, E), padx=5, pady=5)

def createEEPROMFrame():
    EEPROM_frame = ttk.Frame(root)
    EEPROM_frame['padding'] = (5, 5, 5, 5)
    EEPROM_frame['borderwidth'] = 2
    EEPROM_frame['relief'] = 'ridge'

    EEPROM = StringVar()
    EEPROM_mode = StringVar()
    EEPROM_format = StringVar()

    lbl_EEPROM = ttk.Label(EEPROM_frame, text='EEPROM')

    txt_EEPROM = ttk.Entry(EEPROM_frame, textvariable=EEPROM)

    btn_EEPROM_file_browse = ttk.Button(EEPROM_frame, text="...")

    rad_EEPROM_write = ttk.Radiobutton(EEPROM_frame, text='Write', variable=EEPROM_mode, value='write')
    rad_EEPROM_read = ttk.Radiobutton(EEPROM_frame, text='Read', variable=EEPROM_mode, value='read')
    rad_EEPROM_verify = ttk.Radiobutton(EEPROM_frame, text='Verify', variable=EEPROM_mode, value='verify')

    btn_EEPROM_go = ttk.Button(EEPROM_frame, text="Go")

    lbl_EEPROM_format = ttk.Label(EEPROM_frame, text='Format')

    box_EEPROM_format = ttk.Combobox(EEPROM_frame, textvariable=EEPROM_format)
    box_EEPROM_format['values'] = ('auto', 'manual')
    box_EEPROM_format.state(['readonly'])

    lbl_EEPROM.grid(row=0, column=0)
    txt_EEPROM.grid(row=1, column=0, columnspan=5, sticky=(W, E))
    btn_EEPROM_file_browse.grid(row=1, column=5, columnspan=1)
    rad_EEPROM_write.grid(row=2, column=0)
    rad_EEPROM_read.grid(row=2, column=1)
    rad_EEPROM_verify.grid(row=2, column=2)
    btn_EEPROM_go.grid(row=2, column=3)
    lbl_EEPROM_format.grid(row=2, column=4)
    box_EEPROM_format.grid(row=2, column=5)

    EEPROM_frame.grid(row=2, column=0, columnspan=3, sticky=(W, E), padx=5, pady=5)

root = Tk()
root.title('AVRDUDEX')

createProgrammerFrame()
createMCUFrame()
createFlashFrame()
createEEPROMFrame()

root.mainloop()
