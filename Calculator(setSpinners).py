import wx

class CalculatorFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Simple Calculator")

        # Create a panel to hold the controls
        panel = wx.Panel(self)

        # Create a text entry control to display the calculation and result
        self.calculation_text = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        self.calculation_text.SetValue("0")

        # Create spinners for number input
        self.num_spinner = wx.SpinCtrl(panel, value="0", min=0, max=100)
        self.num_spinner.Bind(wx.EVT_SPINCTRL, self.on_spinner_change)

        # Create buttons for operations
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', 'C', '=', '/'
        ]
        gs = wx.GridSizer(4, 4, 5, 5)
        for label in buttons:
            button = wx.Button(panel, label=label)
            gs.Add(button, 0, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Use a sizer to arrange the controls
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.calculation_text, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.num_spinner, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(gs, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(main_sizer)

        self.current_calculation = ""

    def on_button_click(self, event):
        button = event.GetEventObject()
        label = button.GetLabel()

        if label == 'C':
            self.current_calculation = ""
            self.calculation_text.SetValue("0")
        elif label == '=':
            try:
                result = eval(self.current_calculation)
                self.calculation_text.SetValue(str(result))
                self.current_calculation = str(result)
            except:
                self.calculation_text.SetValue("Error")
                self.current_calculation = ""
        else:
            self.current_calculation += label
            self.calculation_text.SetValue(self.current_calculation)

    def on_spinner_change(self, event):
        value = str(self.num_spinner.GetValue())
        self.calculation_text.SetValue(value)
        self.current_calculation = value


# Create an instance of the application
app = wx.App()

# Create and show the main window
frame = CalculatorFrame()
frame.Show()

# Start the main event loop
app.MainLoop()