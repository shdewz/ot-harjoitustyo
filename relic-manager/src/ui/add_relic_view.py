from tkinter import ttk, constants, StringVar
from services.relic_service import relic_service
from entities.relic import Relic, relic_mainstats, relic_substats, relic_types, relic_sets

class AddRelicView:
    def __init__(self, root, handle_show_relics_view):
        self._root = root
        self._frame = None
        self._handle_show_relics_view = handle_show_relics_view
        self._substat_fields = {}
        self._relic_group = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_substat_entry(self, index, row_index):
        row_index = row_index + (index - 1)
        self._substat_fields[f"sub{index}_label"] = ttk.Label(master=self._frame, text=f"Substat {index}:")
        self._substat_fields[f"sub{index}_label"].grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)

        self._substat_fields[f"sub{index}_entry_type_var"] = StringVar()
        self._substat_fields[f"sub{index}_entry_type"] = ttk.Combobox(master=self._frame,
                                                                      textvariable=self._substat_fields[f"sub{index}_entry_type_var"],
                                                                      values=list(map(lambda x: x[0], relic_substats.values()))
                                                                      )
        self._substat_fields[f"sub{index}_entry_type"].grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)

        self._substat_fields[f"sub{index}_entry_val"] = ttk.Entry(master=self._frame)
        self._substat_fields[f"sub{index}_entry_val"].grid(row=row_index, column=2, padx=5, pady=5, sticky=constants.EW)

    def _validate_relic(self):
        _relic_set = self._set_entry.get()
        if not _relic_set:
            return False
        _relic_type = self._type_entry.get()
        if not _relic_type:
            return False
        _relic_level = self._level_entry.get()
        if not _relic_level.isnumeric():
            return False
        _relic_mainstat_full = self._mainstat_entry.get()
        _relic_mainstat = {v[0]: k for k, v in relic_mainstats.items()}.get(_relic_mainstat_full)
        if not _relic_mainstat:
            return False
        _relic_substats = []
        for i in range(4):
            substat_type_full = self._substat_fields[f"sub{i + 1}_entry_type"].get()
            substat = {v[0]: k for k, v in relic_substats.items()}.get(substat_type_full)
            try:
                substat_value = float(self._substat_fields[f"sub{i + 1}_entry_val"].get())
                _relic_substats.append((substat, substat_value))
            except ValueError:
                return False
        self._add_relic()

    def _add_relic(self):
        _relic_set = self._set_entry.get()
        _relic_type = self._type_entry.get()
        _relic_level = int(self._level_entry.get())
        _relic_mainstat_full = self._mainstat_entry.get()
        _relic_mainstat = {v[0]: k for k, v in relic_mainstats.items()}.get(_relic_mainstat_full)
        _relic_substats = []
        for i in range(4):
            substat_type_full = self._substat_fields[f"sub{i + 1}_entry_type"].get()
            substat = {v[0]: k for k, v in relic_substats.items()}.get(substat_type_full)
            substat_value = float(self._substat_fields[f"sub{i + 1}_entry_val"].get())
            _relic_substats.append((substat, substat_value))

        relic_service.create(_relic_set, _relic_type, _relic_level, _relic_mainstat, _relic_substats)
        self._handle_show_relics_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._relic_list_frame = ttk.Frame(master=self._frame)

        title_label = ttk.Label(master=self._frame, text="Add new relic")

        title_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.EW)

        row_index = 1

        set_label = ttk.Label(master=self._frame, text="Relic Set:")
        set_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        set_var = StringVar()
        self._set_entry = ttk.Combobox(master=self._frame, textvariable=set_var, values=list(relic_sets.keys()))
        self._set_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        type_label = ttk.Label(master=self._frame, text="Type:")
        type_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        type_var = StringVar()
        self._type_entry = ttk.Combobox(master=self._frame, textvariable=type_var, values=list(relic_types.keys()))
        self._type_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        level_label = ttk.Label(master=self._frame, text="Level:")
        level_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        self._level_entry = ttk.Entry(master=self._frame)
        self._level_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        mainstat_label = ttk.Label(master=self._frame, text="Mainstat:")
        mainstat_label.grid(row=row_index, column=0, padx=5, pady=5, sticky=constants.E)
        mainstat_var = StringVar()
        self._mainstat_entry = ttk.Combobox(master=self._frame, textvariable=mainstat_var, values=list(map(lambda x: x[0], relic_mainstats.values())))
        self._mainstat_entry.grid(row=row_index, column=1, padx=5, pady=5, sticky=constants.EW)

        sub_val_label = ttk.Label(master=self._frame, text="Substat values:")
        sub_val_label.grid(row=row_index, column=2, padx=5, pady=5, sticky=constants.EW)
        row_index += 1

        self._add_substat_entry(1, row_index)
        self._add_substat_entry(2, row_index)
        self._add_substat_entry(3, row_index)
        self._add_substat_entry(4, row_index)
        row_index += 4

        add_relic_button = ttk.Button(master=self._frame, text="Confirm", command=self._validate_relic)
        add_relic_button.grid(row=row_index, column=2, padx=5, pady=5, sticky=constants.EW)

