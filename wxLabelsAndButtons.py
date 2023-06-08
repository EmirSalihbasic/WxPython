import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Label and Button Example")
        
        # Create a panel to hold the controls
        panel = wx.Panel(self)
        
        # Create a label
        label = wx.StaticText(panel, label="Hello, World!", pos=(50, 50))
        
        # Create a button
        button = wx.Button(panel, label="Click Me!", pos=(50, 80))
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        
    def on_button_click(self, event):
        print("Button clicked!")

# Create an instance of the application
app = wx.App()

# Create and show the main window
frame = MyFrame()
frame.Show()

# Start the main event loop
app.MainLoop()