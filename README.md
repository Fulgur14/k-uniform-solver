# k-uniform-solver
A python script to search for k-uniform Euclidean tilings.

This project's aim is to replicate and extend the list of k-uniform Euclidean tilings (can be seen here: https://en.wikipedia.org/wiki/List_of_k-uniform_tilings). With different datasets, the same algorithm can be also used to search various hyperbolic tilings of convex regular polygons. This Euclidean version is a proof of concept.

The program is currently split into 2 scripts. After I made euclidean_solver_mega and ran it (which took about a week to complete with the current settings), I realized that the program creates a huge number of duplicate tilings, which makes it all but impossible to hand-check their true number. And so, the other script, euclidean_pruner was born. The pruner doesn't search for tilings itself, it uses the output file of the solver as an input and eliminates all duplicates, creating a pruned list where every solution only appears once.

Algorithm: The main idea of this solver is combinatorical, not geometrical. Simply said, any periodic planar tiling contains a finite number of tile types such that all tiles of the same type can be projected onto each other by isometry. Each tile, likewise, has a finite number of edges. The edges can be paired up using "Conway symbols", such that, say, edge 0 of tile 0 is always adjacent to edge 2 of tile 1, or to another edge 0 of tile 0, or to edge 3 from mirror image of tile 2, etc.
Of course, not every posible pairing, or "gluing" leads to a valid solution. However, you can follow the sequence of edges and gluings around a vertex and verify that it's valid (angles around it add up to 360 degrees). If all vertices are valid, so is the solution.

Complications:
This is the general way the algorithm works, but there are several details that complicate things a bit.
First of all, the tile can have a symmetry specified. Imagine a square of edge 1, whose edges are labeled 0,1,2,3. If the square doesn't have a symmetry specified, there is actually a second square to be considered, its mirror image. This is indicated by asterisk: an asterisk before an edge label signifies that it's the mirror image of the edge that normally bears this label. So \*0 is the mirror image of the edge 0.
But the square can have axial, and/or rotational symmetry specified, which enforces a global center or axis of symmetry of the whole tiling that projects the square onto itself. If the square has a diagonal axis symmetry, for example, its edges are now labeled 0, \*0, 2, and \*2.
It seems needlessly complicated, but experience has taught me that specified symmetry is a powerful tool.
Second complication (only a minor one) deals with how to verify a vertex as valid. I have said that the angles around it must add up to 360 degrees, but it's actually looser than that -- they merely have to add up to a *factor* of 360. For example, if a sequence around of a vertex adds up to just 180 degrees, the vertex can be completed by repeating that sequence twice. Vertices constructed in this way are centers of global rotational symmetry of the whole tiling.
Finally, there's the third complication: to find k-uniform tilings, we actually want to determine the types of *vertices*, not types of tiles. Thus, this script is actually looking for *duals* of k-uniform tilings, which are then converted into the k-uniform tilings we seek. This limits the possible vertices even further -- in order to form neat regular polygonal tiles, all angles around each vertex of the dual must be equal.

The basic idea of the algorithm is to create and maintain a list of partial solutions to the problem. Partial solutions don't have all their pairings fixed yet, but they also satisfy all necessary constraints. Their vertices might be incomplete, but they can be still completed later (at least in theory).
For each partial solution, the script picks a particular unpaired edge and tries to pair it with all other edges, including, possibly, edges of a completely new tile. If this is possible, it results in one or more new partial solutions which are added to the list. If the script manages to pair off all edges, the solution is deemed complete.

The script outputs a series of files packaging solutions that share number of tiles and specific polygons in the dual k-uniform tiling. For example, a file named 09_34.txt contains solutions with 9 tile types whose k-uniform dual contains only triangles and squares.

The script also creates a directory structure for the solutions, saving each of them as a \*.tes format file. This format is used by the game HyperRogue (http://www.roguetemple.com/z/hyper/), which can load an unlimited variety of tilings. While playing the game on them is a possibility, it can be also used to simply display them with many graphical options.
Note that thanks to the pruner algorithm, the \*.tes functionality can be removed without any loss, as the pruner provides it as well.

However, this "raw" output contains an inordinate number of duplicate solutions. This is where the pruner comes to play. The pruner checks each solution with a two-pronged test:
1) Does the solution contain a "hidden" symmetry? For example, if a k-uniform tiling contains a symmetrical vertex with configuration (3,3,3,4,4), it must contain an axis of symmetry passing through it. On the other hand, if it contains an asymmetrical vertex with this configuration, it should not contain such an axis. If it does, it can be simplified. The first prong of the test only leaves solutions that cannot be simplified.
2) Is the solution identical to another previously seen solution? If so, it is discarded as well.

Altogether, the pruner has been able to exactly replicate numbers listed in the Wikipedia article on k-uniform tilings. This gives me hope that the results for k > 6 are likewise correct, which would allow to extend the knowledge about these tilings significantly.
