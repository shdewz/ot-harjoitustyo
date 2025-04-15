from tkinter import ttk, constants
from services.relic_service import relic_service
from entities.relic import Relic

class RelicsView:
    def __init__(self, root, handle_show_add_relic_view):
        self._root = root
        self._frame = None
        self._handle_show_add_relic_field = handle_show_add_relic_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        title_label = ttk.Label(
            master=self._frame,
            text="List of added relics"
        )

        title_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        add_relic_button = ttk.Button(
            master=self._frame,
            text="Add new relic",
            command=self._handle_show_add_relic_field
            # command=self._add_temp_relic
        )

        add_relic_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _add_temp_relic(self):
        relic_service.create("Example Set", "Head", 15, "HP", [("SPD", 6.2), ("ATK%", 8.7), ("EHR%", 11.9), ("ATK", 76)])
        relics = relic_service.get_all()
        self._initialize_relic_table(relics)

    def _initialize_relic_table(self, relics: list[Relic]):
        columns = [
            ("x", 20, "center"),
            ("Set", 200, "w"),
            ("Type", 50, "center"),
            ("Level", 40, "center"),
            ("Mainstat", 100, "w"),
            ("Substat 1", 100, "w"),
            ("Substat 2", 100, "w"),
            ("Substat 3", 100, "w"),
            ("Substat 4", 100, "w"),
            ("Score", 90, "center"),
        ]
        tree = ttk.Treeview(master=self._frame, columns=list(map(lambda x: x[0], columns)), show="headings")

        for (name, width, anchor) in columns:
            tree.heading(name, text=name, command=lambda c=name: sort(tree, c, False))
            tree.column(name, width=width, anchor=anchor)

        for relic in relics:
            substats = list(map(
                lambda i: format_stat(relic.substats[i][0], relic.substats[i][1]),
            range(4)))

            tree.insert("", "end", values=[
                "x",
                relic.relic_set,
                relic.relic_type,
                relic.level,
                format_stat(relic.mainstat, relic.mainstat_value)
            ] + substats + [0])

        tree.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._relic_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        relics = relic_service.get_all()
        self._initialize_relic_table(relics)

        self._relic_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=0)

def format_stat(stat, value):
    percent = "%" if stat[-1] == "%" else ""
    stat_name = stat[:-1] if percent == "%" else stat
    return f"{round(value, 1) if percent == "%" else int(value)}{percent} {stat_name}"

def sort(tree, col, desc):
    data = [(tree.set(item, col), item) for item in tree.get_children("")]
    data.sort(reverse=desc)
    for index, (val, item) in enumerate(data):
        tree.move(item, "", index)
    tree.heading(col, command=lambda: sort(tree, col, not desc))