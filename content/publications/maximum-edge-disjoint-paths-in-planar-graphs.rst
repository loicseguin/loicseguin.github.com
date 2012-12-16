Maximum Edge-Disjoint Paths in Planar Graphs with Congestion 2
==============================================================

:date: 2011-10-15
:fileurl: https://dl.dropbox.com/u/1459172/Maths/Seguin-Charbonneau_Shepherd-2011-MEDP-in-Planar-Graphs.pdf
:filesize: 608 Ko
:summary: Algorithme d'approximation pour la maximisation des chemins
          disjoints.
:tags: maths
:type: compte-rendu de conférence

We study the maximum edge-disjoint path problem (MEDP) in planar graphs. We are
given a set of terminal pairs and wish to find a maximum routable subset of
demands. That is, a subset of demands that can be connected by edge-disjoint
paths. It is well-known that there is an integrality gap of order square root
of the number of nodes for this problem even on a grid-like graph, and hence in
planar graphs (Garg et al.). In contrast, Chekuri et al. show that for planar
graphs, if LP is the optimal solution to the natural linear programming
relaxation for MEDP, then there is a subset of size OPT over the logarithm of
the number of nodes which is routable with congestion 2. Subsequently they
showed that it is possible to get within a constant factor of the optimal
solution with congestion 4 instead of 2. We strengthen this latter result to
show that a constant approximation is possible also with congestion 2 (and this
is tight via the integrality gap grid example). We use a basic framework from
work by Chekuri et al. At the heart of their approach is a 2-phase algorithm
that selects an Okamura-Seymour instance. Each of their phases incurs a factor
2 congestion. It is possible to reduce one of the phases to have congestion 1.
In order to achieve an overall congestion 2, however, the two phases must share
capacity more carefully. For the Phase 1 problem, we extract a problem called
rooted clustering that appears to be an interesting problem class in itself.

