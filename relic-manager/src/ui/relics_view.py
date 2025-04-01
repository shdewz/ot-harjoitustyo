from tkinter import ttk, constants
from services.relic_service import relic_service

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

    def _initialize_relic_table(self, relics):
        columns = [("Set", 140, "w"), ("Type", 30, "center"), ("Level", 20, "center"), ("Main", 40, "center"), ("Sub1", 40, "center")]
        tree = ttk.Treeview(master=self._frame, columns=list(map(lambda x: x[0], columns)), show="headings")

        for (name, width, anchor) in columns:
            tree.heading(name, text=name, command=lambda c=name: sort(tree, c, False))
            tree.column(name, width=width, anchor=anchor)

        for relic in relics:
            tree.insert('', 'end', values=[relic["relic_set"], relic["type"], relic["level"], f"10 {relic["mainstat"]}", f"{relic["substat1value"]} {relic["substat1"]}"])

        tree.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _show_add_relic_view(self):
        self.destroy()

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


def sort(tree, col, desc):
    data = [(tree.set(item, col), item) for item in tree.get_children("")]
    data.sort(reverse=desc)
    for index, (val, item) in enumerate(data):
        tree.move(item, "", index)
    tree.heading(col, command=lambda: sort(tree, col, not desc))