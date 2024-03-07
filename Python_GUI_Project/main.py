import wx

class TicTacToeGUI(wx.Frame):
    def __init__(self, parent, title):
        super(TicTacToeGUI, self).__init__(parent, title=title, size=(800, 600))
        self.board = [' '] * 9  
        self.current_player = 'X' 
        self.initialize_ui()
        self.Centre()
        self.Show()
    
    def initialize_ui(self):
        panel = wx.Panel(self)
        grid = wx.GridSizer(3, 3, 10, 10)
        
        # Modern font and rounded buttons setup
        modern_font = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        button_color = "#FFFFFF"  # White color for buttons
        hover_color = "#e0e0e0"  # Light grey for hover effect
        
        self.buttons = []
        for position in range(9):
            button = wx.Button(panel, id=position, label='', size=(100, 100), style=wx.BORDER_NONE)
            button.SetFont(modern_font)
            button.SetBackgroundColour(button_color)
            button.SetForegroundColour("#000000")  # Black color for text
            
            # Rounded corners are not directly supported, so this is a placeholder for the concept.
            # In practice, you might use images or custom drawing to achieve this effect.
            
            self.buttons.append(button)
            grid.Add(button, 0, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.on_button_clicked)
            button.Bind(wx.EVT_ENTER_WINDOW, lambda event: self.on_hover(event, hover_color))
            button.Bind(wx.EVT_LEAVE_WINDOW, lambda event: self.on_hover(event, button_color))
        
        panel.SetSizer(grid)

    def on_hover(self, event, color):
        event.GetEventObject().SetBackgroundColour(color)
        event.GetEventObject().Refresh()

    def on_button_clicked(self, event):
        button_id = event.GetEventObject().GetId()
        if self.board[button_id] == ' ':
            self.board[button_id] = self.current_player
            self.buttons[button_id].SetLabel(self.current_player)
            if self.current_player == 'X':
                self.buttons[button_id].SetForegroundColour('#007bff')  # Blue for X
            else:
                self.buttons[button_id].SetForegroundColour('#28a745')  # Green for O
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            wx.MessageBox('This cell is already taken!', 'Info', wx.OK | wx.ICON_INFORMATION)
        self.check_game_status()  # Assuming check_game_status is defined as previously discussed


    
    def check_game_status(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                wx.MessageBox(f'{self.board[a]} wins!', 'Game Over', wx.OK | wx.ICON_INFORMATION)
                self.reset_game()
                return
        if ' ' not in self.board:
            wx.MessageBox('The game is a draw!', 'Game Over', wx.OK | wx.ICON_INFORMATION)
            self.reset_game()

    
    def reset_game(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        for button in self.buttons:
            button.SetLabel('')


if __name__ == "__main__":
    app = wx.App(False)
    frame = TicTacToeGUI(None, 'Tic Tac Toe')
    app.MainLoop()
