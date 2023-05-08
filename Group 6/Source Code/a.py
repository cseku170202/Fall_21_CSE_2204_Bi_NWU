import tkinter as tk
import math
import time
from tkinter import Canvas
from tkinter import ttk


class Graph:
    node = []
    edges = []
    flag = 0
    prev = -1

    INF = 10 ** 9

    def __Root_Window(self):
        self.root = tk.Tk()  # first line
        self.root.title("Graph ADT")

        # Code to align Window in the middle of the screen irrespective of the screen dimention
        self.window_width = 1000
        self.window_height = 700

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        self.root.geometry('{0}x{1}+{2}+{3}'.format(self.window_width, self.window_height, self.center_x,
                                                    self.center_y))  # Window Dimension

        self.root.resizable(True, True)  # Resizability of the Window is restricted

    def __canva(self):
        # canva is where nodes and edges are displayed
        self.canva_width = 700
        self.canva_height = 700

        self.canva = Canvas(self.root, width=self.canva_width, height=self.canva_height)

        self.canva.create_rectangle(5, 5, self.canva_width, self.canva_height - 5, width=3)
        self.canva.pack(side="right")

    def __left_side(self):
        # Heading
        self.Heading = ttk.Label(self.root, width=self.window_width - self.canva_width,
                                 text="Graph Visualizer", foreground="black", anchor=tk.CENTER,
                                 font=("Helvetica", 20))
        self.Heading.pack()

        # Display
        self.no_of_nodes = ttk.Label(self.root, width=self.window_width - self.canva_width,
                                     text="No of Nodes : 0", foreground="black", anchor=tk.W,
                                     font=("Helvetica", 15))
        self.no_of_nodes.pack(padx=10, pady=10)

        self.no_of_edges = ttk.Label(self.root, width=self.window_width - self.canva_width,
                                     text="No of Edges : 0", foreground="black", anchor=tk.W,
                                     font=("Helvetica", 15))
        self.no_of_edges.pack(padx=10, pady=10)

    def __draw(self):
        def add_node(event):
            node_id = len(self.node) + 1
            x = event.x
            y = event.y
            r = 30
            self.node.append([node_id, x, y])

            self.canva.create_oval(x - r, y - r, x + r, y + r, tags='del', width=3)
            self.canva.create_text(x, y, text="{0}".format(node_id), fill="black", tags="del",
                                   font=('Helvetica 25 bold'))

            self.no_of_nodes['text'] = "No of Nodes : {0}".format(len(self.node))  # Update No of node count

        def add_edge(event):
            if (len(self.node) == 0):
                return

            x = event.x
            y = event.y

            closest_node = -1
            closest_dist = self.INF

            for i in self.node:
                dist = math.sqrt((x - i[1]) ** 2 + (y - i[2]) ** 2)
                if (dist < closest_dist):
                    closest_node = i[0]
                    closest_dist = dist

            if (self.flag == 0):
                self.prev = closest_node

                x1, y1 = self.node[closest_node - 1][1], self.node[closest_node - 1][2]
                self.canva.create_text(x1, y1, text="{0}".format(closest_node), fill="red", tags="del",
                                       font=('Helvetica 25 bold'))

                self.flag = 1
            else:
                x1, y1 = self.node[self.prev - 1][1], self.node[self.prev - 1][2]
                x2, y2 = self.node[closest_node - 1][1], self.node[closest_node - 1][2]

                dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                # Add a popup window to get the path distance from the user
                popup_window = tk.Toplevel(self.root)
                popup_window.geometry("300x100")
                popup_window.title("Path Distance")
                tk.Label(popup_window, text="Enter the path distance: ").pack(pady=10)
                entry = tk.Entry(popup_window)
                entry.pack(pady=10)
                tk.Button(popup_window, text="OK", command=lambda: on_submit()).pack()

                def on_submit():
                    nonlocal dist
                    try:
                        new_dist = int(entry.get())
                        if new_dist <= 0:
                            raise ValueError
                        dist = new_dist
                    except ValueError:
                        tk.messagebox.showerror("Error", "Invalid distance value! Please enter a positive integer.")
                    else:
                        popup_window.destroy()
                        if (self.prev != closest_node):
                            self.edges.append([self.prev, closest_node, dist])
                            self.edges.append([closest_node, self.prev, dist])
                            self.canva.create_line(x1, y1, x2, y2,
                                                   width=5, tags="del", fill='#999999')

                            self.canva.create_text(x1, y1, text="{0}".format(self.prev), fill="black", tags="del",
                                                   font=('Helvetica 25 bold'))
                            self.canva.create_text(x2, y2, text="{0}".format(closest_node), fill="black", tags="del",
                                                   font=('Helvetica 25 bold'))
                            self.canva.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="{0}".format(dist), fill="red",
                                                   tags="del", font=('Helvetica 15 bold'))

                            edge_count = []
                            for i in self.edges:
                                if (i[0], i[1]) not in edge_count:
                                    edge_count.append((i[0], i[1]))
                            self.no_of_edges['text'] = "No of Edges : {0}".format(len(edge_count))
                        self.flag = 0

        def clear(event):
            self.node = []
            self.edges = []
            self.flag = 0
            self.prev = -1
            self.canva.delete('del')

            self.no_of_nodes['text'] = "No of Nodes : {0}".format(len(self.node))  # Updating No of Node Count to 0
            self.no_of_edges['text'] = "No of Edges : 0"  # Updating No of Edge Count to 0

        self.canva.bind('<Button-1>', add_node)
        self.canva.bind('<Button-3>', add_edge)
        self.root.bind('<x>', clear)

    def path(self, n1, n2, c, tag):  # Node_1 Node_2 colour tags
        x1, y1 = self.node[n1 - 1][1], self.node[n1 - 1][2]
        x2, y2 = self.node[n2 - 1][1], self.node[n2 - 1][2]

        self.canva.create_line(x1, y1, x2, y2,
                               width=5, tags=tag, fill=c)
        self.canva.update()

    def __algo(self):
        def DFS(event):

            adj_list = {}
            for i in self.node:
                adj_list[str(i[0])] = []

            for i in self.edges:
                if (str(i[0]) not in adj_list[str(i[1])]):
                    adj_list[str(i[0])] += [str(i[1])]
                    adj_list[str(i[1])] += [str(i[0])]

            # start = 0, source = n
            n = str(len(self.node))
            s = '1'
            vis = []

            def dfs(s, n):

                if (s == n):
                    time.sleep(5)
                    return

                vis.append(s)
                for i in adj_list[s]:
                    if (i not in vis):
                        self.path(int(s), int(i), "red", "algo")
                        time.sleep(0.5)
                        dfs(i, n)
                        self.path(int(s), int(i), "#999999", "algo")
                        time.sleep(0.2)

            dfs(s, n)

            self.canva.delete("algo")

        self.root.bind("dfs", DFS)

    def __init__(self):
        self.__Root_Window()
        self.__canva()
        self.__left_side()
        self.__draw()
        self.__algo()
        self.root.mainloop()


g = Graph()
