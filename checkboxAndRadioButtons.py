import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Checkbox and Radio Buttons Example")

        # Create a panel to hold the controls
        panel = wx.Panel(self)

        # Create a checkbox
        checkbox = wx.CheckBox(panel, label="Enable Feature", pos=(50, 50))
        checkbox.Bind(wx.EVT_CHECKBOX, self.on_checkbox_toggle)

        # Create a static text to display the radio button selection
        self.selection_label = wx.StaticText(panel, label="", pos=(50, 80))

        # Create a group of radio buttons
        radio_box = wx.RadioBox(panel, label="Options", pos=(50, 110), choices=["Option 1", "Option 2", "Option 3"])
        radio_box.Bind(wx.EVT_RADIOBOX, self.on_radio_button_select)

    def on_checkbox_toggle(self, event):
        checkbox = event.GetEventObject()
        if checkbox.GetValue():
            print("Feature enabled!")
        else:
            print("Feature disabled!")

    def on_radio_button_select(self, event):
        radio_box = event.GetEventObject()
        selection = radio_box.GetStringSelection()
        self.selection_label.SetLabel(f"Selected: {selection}")

# Create an instance of the application
app = wx.App()

# Create and show the main window
frame = MyFrame()
frame.Show()

# Start the main event loop
app.MainLoop()