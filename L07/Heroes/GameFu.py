import tkinter as tk
import Display
import Add
import Insert
import Remove
import Sort
import Exits
window = tk.Tk()
window.title('Function Heroes')
window.minsize(500,500)

titleLabel = tk.Label(master=window,
                      text ='Select Function Heroes\n1.Display Heroes Function\n2.Add Heroes Function\n3.Insert Heroes Function\n4.Remove Heroes Function\n5.Display Sorted Heroes Function\n6.Exist Funtion')
titleLabel.pack()

textInput = tk.Entry(master=window)
textInput.pack()


okButton = tk.Button(master=window, text ="Okay",command=Display.heroes)
okButton.pack()


output = tk.Label(master=window,text = Display.heroes )
output.pack()









window.mainloop()