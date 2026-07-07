# gui.py

import tkinter as tk
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
import os

from campus import get_buildings, get_building_info
from astar import a_star



class CampusGuideGUI:


    def __init__(self, root):

        self.root = root

        self.root.title(
            "University of Haripur - Virtual Campus Tour Guide"
        )

        self.root.geometry("700x500")

        self.root.resizable(False, False)


        # Heading

        title = tk.Label(
            root,
            text="University of Haripur\nVirtual Campus Tour Guide",
            font=("Arial", 20, "bold")
        )

        title.pack(pady=20)



        # Frame

        frame = tk.Frame(root)

        frame.pack(pady=10)



        buildings = get_buildings()



        # Start Location

        tk.Label(
            frame,
            text="Starting Location:",
            font=("Arial", 12)
        ).grid(row=0, column=0, padx=10, pady=10)


        self.start_box = ttk.Combobox(
            frame,
            values=buildings,
            width=25
        )

        self.start_box.grid(
            row=0,
            column=1
        )

        self.start_box.current(0)



        # Destination

        tk.Label(
            frame,
            text="Destination:",
            font=("Arial", 12)
        ).grid(row=1, column=0, padx=10, pady=10)


        self.destination_box = ttk.Combobox(
            frame,
            values=buildings,
            width=25
        )

        self.destination_box.grid(
            row=1,
            column=1
        )

        self.destination_box.current(1)



        # Button

        find_button = tk.Button(
            root,
            text="Find Shortest Route",
            font=("Arial", 12, "bold"),
            command=self.find_route,
            width=25
        )

        find_button.pack(pady=20)



        # Result Area

        self.result = tk.Text(
            root,
            height=10,
            width=70,
            font=("Arial", 12)
        )

        self.result.pack(pady=10)

        # Campus Map Display
        base_dir = os.path.dirname(__file__)
        map_path = os.path.join(
            base_dir,
            "assets",
            "campus_map.png"
        )

        if os.path.exists(map_path):

            image = Image.open(map_path)

            image = image.resize(
                (400,250)
            )


            self.map_image = ImageTk.PhotoImage(
                image
            )


            map_label = tk.Label(
                self.root,
                image=self.map_image
            )


            map_label.pack(
                pady=10
            )


        else:

            map_label = tk.Label(
                self.root,
                text="Campus Map Not Found"
            )

            map_label.pack()

    def find_route(self):

        start = self.start_box.get()

        destination = self.destination_box.get()


        if start == destination:

            messagebox.showwarning(
                "Warning",
                "Start and destination cannot be same!"
            )

            return



        route = a_star(
            start,
            destination
        )


        self.result.delete(
            "1.0",
            tk.END
        )


        if route:

            self.result.insert(
                tk.END,
                "Shortest Route:\n\n"
            )

            self.result.insert(
                tk.END,
                " → ".join(route)
            )


            self.result.insert(
                tk.END,
                "\n\nDestination Information:\n"
            )

            self.result.insert(
                tk.END,
                get_building_info(destination)
            )


        else:

            self.result.insert(
                tk.END,
                "No route available."
            )



# Run GUI

if __name__ == "__main__":

    window = tk.Tk()

    app = CampusGuideGUI(window)

    window.mainloop()