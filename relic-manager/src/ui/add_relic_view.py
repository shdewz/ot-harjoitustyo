from tkinter import ttk, constants
from services.relic_service import relic_service
from entities.relic import Relic

class AddRelicView:
    def __init__(self, root, handle_show_relics_view):
        self._root = root
        self._frame = None
        self._handle_show_relics_view = handle_show_relics_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._relic_list_frame = ttk.Frame(master=self._frame)

        title_label = ttk.Label(
            master=self._frame,
            text="Add new relic"
        )

        title_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        add_relic_button = ttk.Button(
            master=self._frame,
            text="Confirm",
            command=self._handle_show_relics_view
        )

        add_relic_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=0)