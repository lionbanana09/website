from tkinter import *
import tkinter.colorchooser
from PIL import ImageGrab
from datetime import datetime

class PixelApp:
    
    def __init__(self, root):
        self.root =root
        self.root.title("Pixel Art")
        
        self.entry_length = StringVar()
        self.entry_height = StringVar()
       
        self.cell_length = 50
        self.grid_width = 20
        self.grid_height = 10
       
       
        self.colour_chooser = tkinter.colorchooser.Chooser(self.root)
        self.chosen_colour = None
        self.is_pen_selected = False
        self.is_eraser_selected = False

        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column= 0, row=0, sticky=(N,E,S,W))
        
        self.cells = []
        for x in  range(0,self.grid_width):
            for y in range(0,self.grid_height):
                self.cell = Frame(self.drawing_grid, width= self.cell_length, height= self.cell_length,bg="white", highlightbackground="black",highlightcolor="black",highlightthickness=1)
                self.cell.grid(column=x,row=y)
                self.cell.bind('<Button-1>', self.tap_cell)
                self.cells.append(self.cell)
                
        control_frame = Frame(self.root,height= self.cell_length)
        control_frame.grid(column=0, row= 1, sticky=(N,E,S,W))
        
        new_button = Button(control_frame, text="New", command=self.press_new_button)
        new_button.grid(column=0, row=0,columnspan=2, sticky=(N,E,S,W),padx=5,pady=5)
        
        enter_width =Entry(control_frame, textvariable= self.entry_length)
        enter_width.grid(column=4, row=0,columnspan=1, sticky=(N,E,S,W),padx=5,pady=5)
        
        enter_height =Entry(control_frame, textvariable= self.entry_height)
        enter_height.grid(column=2, row=0,columnspan=1, sticky=(N,E,S,W),padx=5,pady=5)
        
        save_button = Button(control_frame, text="Save",command=self.press_save_button)
        save_button.grid(column=5, row =0,columnspan=2, sticky=(N,E,S,W),padx=5,pady=5)
        
        self.pen_image = PhotoImage(file="pencil.png").subsample(2,3)
        pen_button = Button(control_frame, text= "pen",image =self.pen_image,command=self.press_pen_button)
        pen_button.grid(column=8, row = 0,columnspan=2, sticky=(N,E,S,W),padx=5,pady=5)
        
        self.erase_image = PhotoImage(file="eraser.png").subsample(2,3)
        erase_button = Button(control_frame, text="erase",image=self.erase_image,command=self.press_erase_button)
        erase_button.grid(column=10, row =0,columnspan=2, sticky=(N,E,S,W),padx=5,pady=5)
        
        self.selected_colour_box = Frame(control_frame, borderwidth=2, relief="raised", bg ="white")
        self.selected_colour_box.grid(column=13,row=0, sticky=(N,E,S,W),padx=7,pady=7)
        
        pick_colour_button = Button(control_frame, text="Pick Colour",command= self.press_pick_button)
        pick_colour_button.grid(column=14, row=0,columnspan=3, sticky=(N,E,S,W),padx=5,pady=5)
        
        cols, rows = control_frame.grid_size()
        for col in range(0, cols):
            control_frame.columnconfigure(col, minsize=self.cell_length)        
        control_frame.rowconfigure(0,minsize=self.cell_length)
        
        
        
    def tap_cell(self,event):
        widget = event.widget
        index = self.cells.index(widget)
        selected_cell = self.cells[index]
        if self.is_eraser_selected:
            selected_cell["bg"] = "white"
        if self.is_pen_selected and self.chosen_colour != None:
            selected_cell["bg"] =self.chosen_colour
        
    def clearFrame(self):
        # destroy all widgets from frame
        for widget in self.drawing_grid.winfo_children():
            widget.destroy()
    
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        self.drawing_grid.pack_forget()
    
    def press_new_button(self):
        
        self.clearFrame()
        self.cells.clear
        
        self.grid_height = int(self.entry_height.get())
        self.grid_width = int(self.entry_length.get())
        
        for x in  range(0,int(self.entry_length.get())):
            for y in range(0,int(self.entry_height.get())):
                self.cell = Frame(self.drawing_grid, width= self.cell_length, height= self.cell_length,bg="white", highlightbackground="black",highlightcolor="black",highlightthickness=1)
                self.cell.grid(column=x,row=y)
                self.cell.bind('<Button-1>', self.tap_cell)
                self.cells.append(self.cell) 
        self.chosen_colour = None
        self.is_pen_selected = False
        self.is_eraser_selected = False
        self.selected_colour_box["bg"] = "white"
        
    def press_save_button(self):
        x= self.root.winfo_rootx() +self.drawing_grid.winfo_x()
        y= self.root.winfo_rooty() + self.drawing_grid.winfo_y() 
        
        
        width = (self.grid_width * self.cell_length)
        height = (self.grid_height * self.cell_length) 
        scale = 1
        width = x + (width * scale)
        height = y + (height * scale)
        
        image_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S" + ".png")
        _ = ImageGrab.grab(bbox=(x,y,width,height)).save(image_name)
        
    def press_pen_button(self):
        self.is_pen_selected = True
        self.is_eraser_selected = False
        
    def press_erase_button(self):
        self.is_pen_selected = False
        self.is_eraser_selected = True
        
    def press_pick_button(self):
        colour_info = self.colour_chooser.show()
        chosen = colour_info[1]
        if chosen != None:
            self.chosen_colour = chosen
            self.selected_colour_box["bg"] = self.chosen_colour
    
    
root = Tk()
PixelApp(root)
root.mainloop()