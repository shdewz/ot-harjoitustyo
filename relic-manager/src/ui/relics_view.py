from tkinter import ttk, constants

class RelicsView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text="List of added relics"
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        add_relic_button = ttk.Button(
            master=self._frame,
            text="Add new relic",
            command=self._show_add_relic_view
        )

        add_relic_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _show_add_relic_view(self):
        self.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._todo_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()

        self._todo_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=0)