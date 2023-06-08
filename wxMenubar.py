import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()  # Create a menu bar

        file_menu = wx.Menu()  # Create a File menu
        open_item = file_menu.Append(wx.ID_OPEN, 'Open', 'Open a file')
        exit_item = file_menu.Append(wx.ID_EXIT, 'Exit', 'Exit the application')
        self.Bind(wx.EVT_MENU, self.OnOpen, open_item)
        self.Bind(wx.EVT_MENU, self.OnExit, exit_item)

        help_menu = wx.Menu()  # Create a Help menu
        about_item = help_menu.Append(wx.ID_ABOUT, 'About', 'About the application')
        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)

        menubar.Append(file_menu, '&File')  # Add the File menu to the menu bar
        menubar.Append(help_menu, '&Help')  # Add the Help menu to the menu bar

        self.SetMenuBar(menubar)  # Set the menu bar for the frame

        self.SetSize((300, 200))
        self.Center()

    def OnOpen(self, event):
        # Open file logic
        pass

    def OnExit(self, event):
        self.Close()

    def OnAbout(self, event):
        # Show about dialog logic
        pass

app = wx.App()
frame = MyFrame(None, 'Simple Menu Bar')
frame.Show()
app.MainLoop()