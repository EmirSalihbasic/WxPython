
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Text Entry Controls Example")

        # Create a panel to hold the controls
        panel = wx.Panel(self)

        # Create a single-line text entry control
        single_line_text = wx.TextCtrl(panel, pos=(50, 50))

        # Create a multi-line text entry control
        multi_line_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(50, 100), size=(200, 100))

        # Create a button to retrieve the entered text
        button = wx.Button(panel, label="Get Text", pos=(50, 220))
        button.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, event):
        single_line_text = self.FindWindowById(1)
        multi_line_text = self.FindWindowById(2)

        single_line_text_value = single_line_text.GetValue()
        multi_line_text_value = multi_line_text.GetValue()

        print("Single-line text: ", single_line_text_value)
        print("Multi-line text: ", multi_line_text_value)

# Create an instance of the application
app = wx.App()

# Create and show the main window
frame = MyFrame()
frame.Show()

# Start the main event loop
app.MainLoop()