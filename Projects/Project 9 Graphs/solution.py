"""
CSE 331 FS22 (Onsay)
Graph Project
"""

import math
import queue
import time
import csv
from typing import TypeVar, Tuple, List, Set, Dict

import numpy as np

T = TypeVar('T')
Matrix = TypeVar('Matrix')  # Adjacency Matrix
Vertex = TypeVar('Vertex')  # Vertex Class Instance
Graph = TypeVar('Graph')  # Graph Class Instance


class Vertex:
    """
    Class representing a Vertex object within a Graph.
    """

    __slots__ = ['id', 'adj', 'visited', 'x', 'y']

    def __init__(self, id_init: str, x: float = 0, y: float = 0) -> None:
        """
        DO NOT MODIFY
        Initializes a Vertex.
        :param id_init: [str] A unique string identifier used for hashing the vertex.
        :param x: [float] The x coordinate of this vertex (used in a_star).
        :param y: [float] The y coordinate of this vertex (used in a_star).
        :return: None.
        """
        self.id = id_init
        self.adj = {}  # dictionary {id : weight} of outgoing edges
        self.visited = False  # boolean flag used in search algorithms
        self.x, self.y = x, y  # coordinates for use in metric computations

    def __eq__(self, other: Vertex) -> bool:
        """
        DO NOT MODIFY.
        Equality operator for Graph Vertex class.
        :param other: [Vertex] vertex to compare.
        :return: [bool] True if vertices are equal, else False.
        """
        if self.id != other.id:
            return False
        if self.visited != other.visited:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex visited flags not equal: self.visited={self.visited},"
                  f" other.visited={other.visited}")
            return False
        if self.x != other.x:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex x coords not equal: self.x={self.x}, other.x={other.x}")
            return False
        if self.y != other.y:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex y coords not equal: self.y={self.y}, other.y={other.y}")
            return False
        if set(self.adj.items()) != set(other.adj.items()):
            diff = set(self.adj.items()).symmetric_difference(set(other.adj.items()))
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex adj dictionaries not equal:"
                  f" symmetric diff of adjacency (k,v) pairs = {str(diff)}")
            return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        Constructs string representation of Vertex object.
        :return: [str] string representation of Vertex object.
        """
        lst = [f"<id: '{k}', weight: {v}>" for k, v in self.adj.items()]
        return f"<id: '{self.id}'" + ", Adjacencies: " + "".join(lst) + ">"

    __str__ = __repr__

    def __hash__(self) -> int:
        """
        DO NOT MODIFY
        Hashes Vertex into a set. Used in unit tests.
        :return: [int] Hash value of Vertex.
        """
        return hash(self.id)

    # ============== Modify Vertex Methods Below ==============#

    def deg(self) -> int:
        """
        Returns the number of outgoing edges from this vertex
        :return: number of outgoing edges from vertex
        """
        return len(self.adj)

    def get_outgoing_edges(self) -> Set[Tuple[str, float]]:
        """
        Returns set of tuples representing all outgoing edges from vertex
        :return: number of outgoing edges from this vertex
        """
        return self.adj.items()

    def euclidean_dist(self, other: Vertex) -> float:
        """
        Returns euclidian distance between this vertex and another
        :param other: vertex to which we are calculating distance
        :return: euclidian distance between this vertex and other
        """
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**(1/2)

    def taxicab_dist(self, other: Vertex) -> float:
        """
        Returns taxicab distance between this vertex and another
        :param other: vertex to which we are calculating distance
        :return: taxicab distance between this vertex and other
        """
        return abs(self.x-other.x) + abs(self.y-other.y)


class Graph:
    """
    Class implementing the Graph ADT using an Adjacency Map structure.
    """

    __slots__ = ['size', 'vertices', 'plot_show', 'plot_delay']

    def __init__(self, plt_show: bool = False, matrix: Matrix = None, csvf: str = "") -> None:
        """
        DO NOT MODIFY
        Instantiates a Graph class instance.
        :param plt_show: [bool] If true, render plot when plot() is called; else, ignore plot().
        :param matrix: [Matrix] Optional matrix parameter used for fast construction.
        :param csvf: [str] Optional filepath to a csv containing a matrix.
        :return: None.
        """
        matrix = matrix if matrix else np.loadtxt(csvf, delimiter=',', dtype=str).tolist() \
            if csvf else None
        self.size = 0
        self.vertices = {}

        self.plot_show = plt_show
        self.plot_delay = 0.2

        if matrix is not None:
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix)):
                    if matrix[i][j] == "None" or matrix[i][j] == "":
                        matrix[i][j] = None
                    else:
                        matrix[i][j] = float(matrix[i][j])
            self.matrix2graph(matrix)

    def __eq__(self, other: Graph) -> bool:
        """
        DO NOT MODIFY
        Overloads equality operator for Graph class.
        :param other: [Graph] Another graph to compare.
        :return: [bool] True if graphs are equal, else False.
        """
        if self.size != other.size or len(self.vertices) != len(other.vertices):
            print(f"Graph size not equal: self.size={self.size}, other.size={other.size}")
            return False
        for vertex_id, vertex in self.vertices.items():
            other_vertex = other.get_vertex_by_id(vertex_id)
            if other_vertex is None:
                print(f"Vertices not equal: '{vertex_id}' not in other graph")
                return False

            adj_set = set(vertex.adj.items())
            other_adj_set = set(other_vertex.adj.items())

            if not adj_set == other_adj_set:
                print(f"Vertices not equal: adjacencies of '{vertex_id}' not equal")
                print(f"Adjacency symmetric difference = "
                      f"{str(adj_set.symmetric_difference(other_adj_set))}")
                return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        Constructs string representation of graph.
        :return: [str] String representation of graph.
        """
        return "Size: " + str(self.size) + ", Vertices: " + str(list(self.vertices.items()))

    __str__ = __repr__

    def plot(self) -> None:
        """
        DO NOT MODIFY
        Creates a plot a visual representation of the graph using matplotlib.
        :return: None.
        """
        if self.plot_show:
            import matplotlib.cm as cm
            import matplotlib.patches as patches
            import matplotlib.pyplot as plt

            # if no x, y coords are specified, place vertices on the unit circle
            for i, vertex in enumerate(self.get_all_vertices()):
                if vertex.x == 0 and vertex.y == 0:
                    vertex.x = math.cos(i * 2 * math.pi / self.size)
                    vertex.y = math.sin(i * 2 * math.pi / self.size)

            # show edges
            num_edges = len(self.get_all_edges())
            max_weight = max([edge[2] for edge in self.get_all_edges()]) if num_edges > 0 else 0
            colormap = cm.get_cmap('cool')
            for i, edge in enumerate(self.get_all_edges()):
                origin = self.get_vertex_by_id(edge[0])
                destination = self.get_vertex_by_id(edge[1])
                weight = edge[2]

                # plot edge
                arrow = patches.FancyArrowPatch((origin.x, origin.y),
                                                (destination.x, destination.y),
                                                connectionstyle="arc3,rad=.2",
                                                color=colormap(weight / max_weight),
                                                zorder=0,
                                                **dict(arrowstyle="Simple,tail_width=0.5,"
                                                                  "head_width=8,head_length=8"))
                plt.gca().add_patch(arrow)

                # label edge
                plt.text(x=(origin.x + destination.x) / 2 - (origin.x - destination.x) / 10,
                         y=(origin.y + destination.y) / 2 - (origin.y - destination.y) / 10,
                         s=weight, color=colormap(weight / max_weight))

            # show vertices
            x = np.array([vertex.x for vertex in self.get_all_vertices()])
            y = np.array([vertex.y for vertex in self.get_all_vertices()])
            labels = np.array([vertex.id for vertex in self.get_all_vertices()])
            colors = np.array(
                ['yellow' if vertex.visited else 'black' for vertex in self.get_all_vertices()])
            plt.scatter(x, y, s=40, c=colors, zorder=1)

            # plot labels
            for j, _ in enumerate(x):
                plt.text(x[j] - 0.03 * max(x), y[j] - 0.03 * max(y), labels[j])

            # show plot
            plt.show()
            # delay execution to enable animation
            time.sleep(self.plot_delay)

    def add_to_graph(self, begin_id: str, end_id: str = None, weight: float = 1) -> None:
        """
        Adds to graph: creates start vertex if necessary,
        an edge if specified,
        and a destination vertex if necessary to create said edge
        If edge already exists, update the weight.
        :param begin_id: [str] unique string id of starting vertex
        :param end_id: [str] unique string id of ending vertex
        :param weight: [float] weight associated with edge from start -> dest
        :return: None
        """
        if self.vertices.get(begin_id) is None:
            self.vertices[begin_id] = Vertex(begin_id)
            self.size += 1
        if end_id is not None:
            if self.vertices.get(end_id) is None:
                self.vertices[end_id] = Vertex(end_id)
                self.size += 1
            self.vertices.get(begin_id).adj[end_id] = weight

    def matrix2graph(self, matrix: Matrix) -> None:
        """
        Given an adjacency matrix, construct a graph
        matrix[i][j] will be the weight of an edge between the vertex_ids
        stored at matrix[i][0] and matrix[0][j]
        Add all vertices referenced in the adjacency matrix, but only add an
        edge if matrix[i][j] is not None
        Guaranteed that matrix will be square
        If matrix is nonempty, matrix[0][0] will be None
        :param matrix: [Matrix] an n x n square matrix (list of lists) representing Graph
        :return: None
        """
        for i in range(1, len(matrix)):  # add all vertices to begin with
            self.add_to_graph(matrix[i][0])
        for i in range(1, len(matrix)):  # go back through and add all edges
            for j in range(1, len(matrix)):
                if matrix[i][j] is not None:
                    self.add_to_graph(matrix[i][0], matrix[j][0], matrix[i][j])

    def graph2matrix(self) -> Matrix:
        """
        Given a graph, creates an adjacency matrix of the type described in construct_from_matrix.
        :return: [Matrix] representing graph.
        """
        matrix = [[None] + list(self.vertices)]
        for v_id, outgoing in self.vertices.items():
            matrix.append([v_id] + [outgoing.adj.get(v) for v in self.vertices])
        return matrix if self.size else None

    def graph2csv(self, filepath: str) -> None:
        """
        Given a (non-empty) graph, creates a csv file containing data necessary to reconstruct.
        :param filepath: [str] location to save CSV.
        :return: None.
        """
        if self.size == 0:
            return

        with open(filepath, 'w+') as graph_csv:
            csv.writer(graph_csv, delimiter=',').writerows(self.graph2matrix())

    # ============== Modify Graph Methods Below ==============#

    def unvisit_vertices(self) -> None:
        """
        Resets visited flags to False of all vertices within the graph
        :return: None
        """
        for v_id in self.vertices:
            self.vertices[v_id].visited = False

    def get_vertex_by_id(self, v_id: str) -> Vertex:
        """
        Returns vertex associated with given vertex id
        """
        return self.vertices.get(v_id)

    def get_all_vertices(self) -> Set[Vertex]:
        """
        PLEASE FILL OUT DOCSTRING
        """
        vSet =set()
        for v_id in self.vertices:
            vSet.add(self.get_vertex_by_id(v_id))
        return vSet

    def get_edge_by_ids(self, begin_id: str, end_id: str) -> Tuple[str, str, float]:
        """
        Returns the edge connecting the vertex with id begin_id to the vertex with id end_id in
         a tuple form, None if edge or either vertices does not exist
        :param begin_id: source vertex
        :param end_id: destination vertex
        :return: tuple of the two vertex ids and edge weight, None if non-existent
        """
        v = self.vertices.get(begin_id)
        if v is None:
            return None
        weight = v.adj.get(end_id)
        if weight is None:
            return None
        return (begin_id,end_id,weight)

    def get_all_edges(self) -> Set[Tuple[str, str, float]]:
        """
        Returns a set of tuples representing all edges within the graph
        :return: set of tuples representing all edges within the graph
        """
        eSet = set()
        for v_id in self.vertices:
            vertex = self.get_vertex_by_id(v_id)
            v_edges = vertex.get_outgoing_edges()
            for dest,weight in v_edges:
                eSet.add((v_id,dest,weight))
        return eSet

    def _build_path(self, back_edges: Dict[str, str], begin_id: str, end_id: str) \
            -> Tuple[List[str], float]:
        """
        Reconstructs the path from start_id to end_id and computes the total distance
        :param back_edges: dict of vertex ids to predecessor vertex ids
        :param begin_id: path source vertex
        :param end_id: path destination vertex
        :return: tuple form ([path], distance], None if path does not exist
        """
        dist = 0
        curr = end_id
        pred = back_edges.get(end_id)
        if pred is None:
            return None
        path = [end_id]
        while pred:
            dist += self.get_edge_by_ids(pred,curr)[2]
            path.append(pred)
            curr = pred
            pred = back_edges.get(pred)

        if path[-1] != begin_id:
            return None
        return (list(reversed(path)), dist)

    def bfs(self, begin_id: str, end_id: str) -> Tuple[List[str], float]:
        """
        Performs a breadth-first search beginning at vertex with id begin_id and terminating at vertex with id end_id
        :param begin_id: starting vertex
        :param end_id: destination vertex
        :return: Tuple of form ([path],distance), where path is list of vertex ids and distance is sum of edge weights along path
        """
        forest = {}
        for v_id in self.vertices:
            if v_id not in forest:
                forest[v_id] = None
                q = queue.SimpleQueue()
                q.put(v_id)
                while not q.empty():
                    u = q.get()
                    if u == begin_id:
                        forest[u] = None
                    v = self.get_vertex_by_id(u)
                    for adj_vert, weight in v.adj.items():
                        if adj_vert not in forest:
                            forest[adj_vert] = u
                            q.put(adj_vert)
                        elif u == begin_id:
                            forest[adj_vert] = u

        path = self._build_path(forest, begin_id, end_id)
        if path is None:
            return ([], 0)
        return path

    def dfs(self, begin_id: str, end_id: str) -> Tuple[List[str], float]:
        """
        Performs a depth-first search starting at vertex id begin_id and terminating at vertex id end_id
        Wrapper function for dfs_inner
        :param begin_id: source id to start search
        :param end_id: destination id
        :return: Tuple of form ([path],distance), where path is list of vertex ids and distance is sum of edge weights along path
        """
        if begin_id not in self.vertices or end_id not in self.vertices:
            return ([],0)
        def dfs_inner(current_id: str, end_id: str, path: List[str]) -> Tuple[List[str], float]:
            """
            Performs the recursive work of depth-first search by searching for a path from vertex with id current_id to vertex with id end_id
            Inner function for dfs
            :param current_id: vertex id of the current node
            :param end_id: vertex id of the destination node
            :param path: current list of vertex ids to reach destination
            :return: Tuple of form ([path],distance), where path is list of vertex ids and distance is sum of edge weights along path
            """
            self.vertices.get(current_id).visited = True
            if current_id==end_id:
                return ([end_id],0)
            for adjV in self.vertices[current_id].adj:
                if self.vertices.get(adjV).visited is False:
                    path,dist = dfs_inner(adjV,end_id,path)
                    if len(path)>0:
                        path.append(current_id)
                        return path, dist + self.get_vertex_by_id(current_id).adj.get(adjV)
            return ([],0)

        path,dist = dfs_inner(begin_id,end_id,[])
        return list(reversed(path)),dist




    def topological_sort(self) -> List[str]:
        """
        Performs topological sort on the graph, returning a possible topological ordering as a list of vertex ids.
        :return: list of string vertex ids after the topological sort
        """
        topo = []

        def topological_sort_inner(topo:List[str],current_id: str) -> List[str]:
            """
            Performs a depth-first search starting at vertex id current_id
            inner function for topological_sort
            :param topo: current topologically sorted list of vertex ids
            :param current_id: current vertex id being searched from
            :return: list of string vertex ids after the topological sort
            """
            self.vertices.get(current_id).visited = True
            for adjV in self.vertices[current_id].adj:
                if self.vertices.get(adjV).visited is False:
                    topological_sort_inner(topo,adjV)
            topo.append(current_id)
        for v_id in self.vertices:
            v = self.get_vertex_by_id(v_id)
            if v.visited is False:
                inner = topological_sort_inner(topo,v_id)
                if inner:
                    topo.append(inner)
        return list(reversed(topo))


    def friends_recommender(self, current_id: str) -> List[str]:
        """
        Creates a sorted list of recommended friends based on given vertex
        :param current_id: given id of vertex to recommend to a friend
        :return: list of names of recommended vertices sorted by friend score
        """



