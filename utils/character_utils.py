class Characters:
    def __init__(self, nerd_font=False):
        self.nerd_font = nerd_font
    
    def default_players(self):
        if self.nerd_font:
            return ["", "󰄛", "", ""]
        else:
            return ["$", "#", "@", "%"]
    def current_player(self):
        if self.nerd_font:
            return ""
        else:
            return ">"
    def unknown_question(self):
        if self.nerd_font:
            return ""
        else:
            return "?"