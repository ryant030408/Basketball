import tkinter as tk
import tkinter.ttk as ttk
import graph_gui_functions as gf


def get_top_gui(self):
    # year combobox and label
    self.years_l = tk.Label(self.top_frame, text='Year')
    self.years_c = ttk.Combobox(self.top_frame, textvariable=self.year_to_use, values=gf.year_creator())
    self.years_c.current(1)  # set initial value
    self.player_list = gf.get_player_list(self)

    self.years_l.grid(row=0, column=0)
    self.years_c.grid(row=0, column=1)

    # team combobox and label
    self.teams_l = tk.Label(self.top_frame, text="Teams")
    self.teams_c = ttk.Combobox(self.top_frame, values=gf.get_team_abbr(), textvariable=self.team_name)

    self.teams_l.grid(row=0, column=2)
    self.teams_c.grid(row=0, column=3)

    # player combobox and label
    self.players_l = tk.Label(self.top_frame, text='Player')
    self.players_c = ttk.Combobox(self.top_frame, values=self.player_list['DISPLAY_FIRST_LAST'].tolist(),
                                  textvariable=self.player_name)

    self.players_l.grid(row=0, column=4)
    self.players_c.grid(row=0, column=5)

    # radio buttons
    self.team_r = tk.Radiobutton(self.top_frame, text='Team', variable=self.player_team_radio_val, value=1,
                                 command=lambda: gf.selection(self, 1))
    self.player_r = tk.Radiobutton(self.top_frame, text='Player', variable=self.player_team_radio_val,
                                   value=2, command=lambda: gf.selection(self, 2))

    self.team_r.grid(row=0, column=6)
    self.player_r.grid(row=0, column=7)

    # clear button
    self.clear_b = tk.Button(self.top_frame, text='Clear', command=lambda: gf.clear_plot(self, full=1))

    self.clear_b.grid(row=0, column=8)

