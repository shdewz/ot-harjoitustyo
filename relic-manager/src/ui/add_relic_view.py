from tkinter import ttk, constants, StringVar
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

        title_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.EW)

        # current_var = StringVar()
        # combobox = ttk.Combobox(master=self._frame, textvariable=current_var, values=["1", "2", "3"])

        # combobox.grid(
        #     row=1,
        #     column=1,
        #     padx=5,
        #     pady=5,
        #     sticky=constants.EW
        # )

        row_index = 1

        set_label = ttk.Label(master=self._frame, text="Relic Set:")
        set_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        set_var = StringVar()
        set_entry = ttk.Combobox(master=self._frame, textvariable=set_var, values=["1", "2", "3"])
        set_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        type_label = ttk.Label(master=self._frame, text="Type:")
        type_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        type_var = StringVar()
        type_entry = ttk.Combobox(master=self._frame, textvariable=type_var, values=["Head", "Hands", "Body", "Feet"])
        type_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        level_label = ttk.Label(master=self._frame, text="Level:")
        level_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        level_entry = ttk.Entry(master=self._frame)
        level_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        sub1_label = ttk.Label(master=self._frame, text="Substat 1:")
        sub1_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        sub1_entry = ttk.Entry(master=self._frame)
        sub1_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
        sub1_entry_val = ttk.Entry(master=self._frame)
        sub1_entry_val.grid(row=row_index, column=2, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        add_relic_button = ttk.Button(master=self._frame, text="Confirm", command=self._handle_show_relics_view)
        add_relic_button.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
