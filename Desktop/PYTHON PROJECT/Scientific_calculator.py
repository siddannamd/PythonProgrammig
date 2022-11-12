root = Tk()

# sets the name on the top of the gui
root.title("Scientific Calculator")

# sets the background color of the calculator
# as white
root.configure(background = 'white')

# fixed the width and height of the gui,
# hence can't be expanded/stretched
root.resizable(width=False, height=False)

# sets the geometry
root.geometry("480x568+450+90")

# holds the buttons in the calculator,
# act as a container for numbers and operators
calc = Frame(root)

# create a grid like pattern of the frame
# i.e buttons
calc.grid()
