## SAT (Satisfiability)

Problem: Given a boolean formula with variables that can be `True` or `False`, determine if there is an assignment of values to variables that makes the formula evaluate to `True`.

Input: A boolean formula in propositional logic (e.g., `(x1 OR ¬x2) AND (x2 OR x3))`.

Output: Yes/No - whether there exists a satisfying assignment.

Notes: This is the first problem proven NP-complete and is the basis for reductions to other NP-complete problems.

## 0-1 Integer Programming

Problem: Find `0-1` values for variables that satisfy a set of linear inequalities.

Input: A set of inequalities such as `a1x1 + a2x2 + ... + anxn ≤ b where xi ∈ {0,1}`.

Output: Yes/No - whether there exists an assignment satisfying all inequalities.

Notes: This is a generalization of Subset Sum and Knapsack.

## Clique

Problem: Given a graph and an integer `k`, determine if there exists a subset of `k` vertices where every pair of vertices is connected.

Input: Graph `G(V, E)`, integer `k`.

Output: Yes/No - does G contain a clique of size `k`?

Notes: A clique is a complete subgraph.

## Vertex Cover

Problem: Find a subset of vertices of `size ≤ k` such that every edge has at least one endpoint in this subset.

Input: Graph `G(V, E)`, integer `k`.

Output: Yes/No - is there a vertex cover of `size ≤ k`?

## Set Packing

Problem: Given a collection of sets and an integer `k`, find `k` mutually disjoint sets.

Input: Family of sets `{S1, S2, …, Sn}`, integer `k`.

Output: Yes/No - can you select `k` sets that have no elements in common?

## Set Covering

Problem: Find `≤ k` sets whose union covers all elements in a universe.

Input: Universe `U` and family of subsets `{S1, S2, …, Sn}`, integer `k`.

Output: Yes/No - is there a subcollection of `≤ k` sets that covers `U`?

## Feedback Node Set

Problem: Remove `≤ k` vertices from a graph to make it acyclic (no cycles).

Input: Graph `G(V, E)`, integer `k`.

Output: Yes/No - can you delete `k` vertices to remove all cycles?

## Feedback Arc Set (or Feedback Edge Set)

Problem: Remove `≤ k` edges from a graph to make it acyclic.

Input: Graph `G(V, E)`, integer `k`.

Output: Yes/No - can you delete `k` edges to remove all cycles?

## Directed Hamiltonian Cycle

Problem: Determine if a directed graph contains a cycle that visits each vertex exactly once.

Input: Directed graph `G(V, E)`.

Output: Yes/No - is there a directed Hamiltonian cycle?

## Undirected Hamiltonian Cycle

Problem: Determine if an undirected graph contains a cycle visiting each vertex exactly once.

Input: Undirected graph `G(V, E)`.

Output: Yes/No - is there a Hamiltonian cycle?

## 3-SAT

Problem: Determine satisfiability of a boolean formula in 3-CNF (conjunction of clauses, each with exactly 3 literals).

Input: Boolean formula like `(x1 OR ¬x2 OR x3) AND …`.

Output: Yes/No - is there an assignment that satisfies all clauses?

## Chromatic Number

Problem: Can a graph be colored with `≤ k` colors so that no adjacent vertices share the same color?

Input: Graph `G(V, E)`, integer `k`.

Output: Yes/No - is there a proper `k`-coloring?

## Clique Cover

Problem: Partition the vertices of a graph into `≤ k` cliques.

Input: Graph `G(V, E)`, integer `k`.

Output: Yes/No - can vertices be divided into `≤ k` complete subgraphs?

## Exact Cover

Problem: Find a subcollection of sets such that every element in the universe appears in exactly one set.

Input: Universe `U`, collection of subsets `{S1, …, Sn}`.

Output: Yes/No - is there a subcollection that covers all elements exactly once?

## Hitting Set

Problem: Find `≤ k` elements that intersect every set in a family.

Input: Family of sets `{S1, …, Sn}`, integer `k`.

Output: Yes/No - is there a set of `≤ k` elements that “hits” every subset?

## Steiner Tree

Problem: Find a minimum-size tree that connects a given subset of nodes (terminals).

Input: Graph `G(V, E)`, terminal nodes `T ⊆ V`, integer `k`.

Output: Yes/No - is there a tree connecting all terminals with `≤ k` edges?

## 3-Dimensional Matching (3DM)

Problem: Given three sets `X`, `Y`, `Z` and a set of triples `T ⊆ X×Y×Z`, does there exist a matching covering all elements?

Input: Sets `X`, `Y`, `Z` of size `n`, triples `T ⊆ X×Y×Z`.

Output: Yes/No - is there a subset of `T` of size `n` such that each element of `X`, `Y`, `Z` appears exactly once?

## Knapsack (0-1)

Problem: Select items with given weights and values to maximize total value without exceeding weight capacity.

Input: Items with weights `w[i]` and values `v[i]`, capacity `W`.

Output: Yes/No - is there a subset of items with `total weight ≤ W` and `total value ≥ target`?

## Partition

Problem: Can a set of integers be partitioned into two subsets with equal sum?

Input: Set of integers `S`.

Output: Yes/No - does there exist a partition `S1 ∪ S2 = S, sum(S1) = sum(S2)`?

## Subset Sum

Problem: Determine if there exists a subset of integers that sums exactly to a target value.

Input: Set of integers `S`, integer target `T`.

Output: Yes/No - is there a subset whose `sum = T`?

## Job Sequencing / Scheduling

Problem: Given a set of `n` jobs `J = {J1, J2, ..., Jn}`, where each job `Ji` has a processing time `p_i`, a deadline `d_i`, and a profit `π_i`, determine a schedule on a single machine that **maximizes total profit** (or achieves a target profit) such that no two jobs overlap and each job is completed by its deadline.

Input: A set of jobs `J = {J1, ..., Jn}`, Processing times `p_i ∈ ℕ⁺`, Deadlines `d_i ∈ ℕ⁺`, Profits `π_i ∈ ℝ⁺`  

Output: Yes/No - does there exist a feasible schedule `σ` such that the total profit `∑_{Ji ∈ σ} π_i` meets or exceeds the target profit and all jobs in the schedule are completed by their deadlines?







## References
- Karp, R. (1972). *Reducibility Among Combinatorial Problems.*  
