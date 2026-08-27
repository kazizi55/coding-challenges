# 323. Number of Connected Components in an Undirected Graph

## Link

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1

- 考えたこと
  - edges を前から見ていって、b か次の a と一致している限り connected と見做して、そうでなかったら components の数を + 1 していく、みたいにしたらできるかなと思ったが、constraints をみるに、edges が昇順などでソートされているわけではないので、`[[0, 1], [2, 3], [1, 2]]`の場合などに本当は1なのに3とカウントされそう。なので sort してからみるべきなのか。
  - うーん、どうやって DFS や BFS を適用すればいいのかわからない。
  - これだと`[[0,1],[0,2],[0,3],[1,4]]`みたいな1つより前の index にいるが隣接しているケースに対応できない。
  - 時間切れ。gemini に聞いてみる。

```py
# Wrong Answer 21 / 41 testcases passed
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_connected_components = 0
        sorted_edges = sorted(edges, key=itemgetter(0))
        previous_edge = []
        for edge in sorted_edges:
            if any(component in previous_edge for component in edge):
                previous_edge = edge
                continue
            num_connected_components += 1
            previous_edge = edge
        return num_connected_components
```

- 考えたこと
  - 先に隣接している node の対応表を作っておき、n 回 loop を回しながら DFS で隣接する node を visited として全て mark する。隣接する node を見切ってもなお、見ていない node が存在する場合は num_connected_components を increment すると言う解法。
    - `先に隣接している node の対応表を作っておき` の部分が肝だと思う。これが思い浮かんでいれば DFS で解けていたなー。
  - 対応表、gemini は以下のような感じで書けると言っていた
    - `adj = {i: [] for i in range(n)}`
    - `for u, v in edges:`
      - `adj[u].append(v)`
      - `adj[v].append(u)`
  - が、命名がわかりづらいのと、対の関係を list で表現しているのがしっくりこなかったので dict に変えて命名もより明示的にした。
  - 最初、`node` と `component` を混同していたが、`node` は点、`edge` は辺、`component` は繋がっている頂点のグループなので明確に区別する必要がある。
  - 想定ユースケース
    - 特に入力のバリデーションは設けていないので社内利用前提。
    - node と辺がともに 10^7 を超えると10秒を超えるので注意書きを添えつつ、バッチ処理か、都度実行してもらうかみたいな感じだろうか。
  - 計算量
    - 入力の n を V とし(vertices なので)、辺の数 len(edges) を E とする。
    - 時間計算量: O(V + E)
      - node_to_connected_nodes に値を追加していくのに、1 * E、その後の外側のループが 1 * V。
      - DFS 内ではその隣接する node も探索するので、2 * E。 
      - なので、定数倍も含めた処理回数の目安としてはおよそ V + 3E 回程度になる。
      - LeetCode の最大入力を考慮し、かつ Python を 10^7step / 秒とすると、最大、(2000 + 3 * 5000) / 10^7 = 0.0017 ≈ 約 2ms かかる。
    - 空間計算量: O(V + E)
      - node_to_connected_nodes に値を追加していくのに key が V 個、value が 2 * E 個。
      - visited が 1 * V 個。
      - DFS のコールスタック: 直線状グラフになる最悪ケースで最大 1 * V。
      - なので、定数倍も含めたメモリの目安としてはおよそ 3V + 2E 程度になる。
      - LeetCode の最大入力を考慮し、整数を 8 Byte として計算すると、3 * 2000 * 8 + 2 * 5000 * 8 = 128000B = 128KB 程度になる。

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_connected_nodes = defaultdict(list)
        for node1, node2 in edges:
            node_to_connected_nodes[node1].append(node2)
            node_to_connected_nodes[node2].append(node1)
        visited = set()
        def traverse_connected_nodes(node: int) -> None:
            for neighbor in node_to_connected_nodes[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                traverse_connected_nodes(neighbor)

        num_connected_components = 0
        for i in range(n):
            if i in visited:
                continue
            num_connected_components += 1
            visited.add(i)
            traverse_connected_nodes(i)
        return num_connected_components
```

## Step 2

- DFS, BFS, UnionFind で解いている人がいた。

### 解法1: UnionFind

- 参考にした回答
  - https://github.com/naoto-iwase/leetcode/pull/28/changes の 2nd
    - 特に最適化に関してめちゃ詳しく書いてくださっている。ありがたい限り。
  - https://github.com/mamo3gr/arai60/pull/56/changes の 2nd
  - https://github.com/h-masder/Arai60/pull/20/changes の 2nd
- 考えたこと
  - union by rank の方が union by size よりも厳密な高さ制御。size が大きいからといって必ずしも高いとは限らないため。
  - path splitting も path halving も node の親を祖父 node に更新するものだが、前者がもれなく更新していくのに対し、後者が1つ飛ばしで更新していく。
  - path compression と union by size を実装している解法が多いな。それで実装してみる。recursion limit を気にしないといけないデータ量だったら、path splitting など他の最適化を使うと言う使い分けができそう。
  - 想定ユースケース
    - これもバリデーションは特に設けていないので社内利用前提。
  - 計算量
    - 入力の n を V とし、辺の数 len(edges) を E とする。
    - 時間計算量: O(V + E * ⍺(V))
      - edges を 1path で探索しながら、union() していくので、1 * E。union find の初期化時に 2 * V かかるのと、union() は逆アッカーマン関数なので ⍺(V)。なので実質 O(V + E)。
      - LeetCode の最大入力を考慮し、かつ Python を 10^7step / 秒とすると、最大、(2 * 2000 + 5000) / 10^7 = 0.0009 ≈ 約 0.9ms かかる。
    - 空間計算量: O(V)
      - parents: 1 * V
      - group_sizes: 1 * V
      - find() の call stack: 
        - union by size により、小さい node を大きい node の下に結合するため、node の深さが 1 増えるときは必ずグループの要素数が 2 倍以上になる (深さ h のとき要素数は 2^h 以上)。
        - 要素数の上限は V なので、node の高さ(深さ)は最大でも log₂(V) に抑えられる (V = 2000 で最大約 11 フレーム)。
        - さらに path compression で参照時に親が根に直接付け替えられて平坦化されるため、実質 O(1)。
      - なので、定数倍も含めたメモリの目安としてはおよそ 2V 程度になる。
      - LeetCode の最大入力を考慮し、整数を 8 Byte として計算すると、2 * 2000 * 8 = 32000B = 32KB 程度になる。

```py
class UnionFind:
    def __init__(self, num_node: int) -> None:
        self.parents = list(range(num_node))
        self.group_sizes = [1] * num_node
        self.num_group = num_node

    def count(self) -> int:
        return self.num_group
    
    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x: int, y: int) -> bool:
        """Return True if the groups gets merged and return False if already merged"""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.group_sizes[root_x] < self.group_sizes[root_y]:
            root_x, root_y = root_y, root_x
        self.parents[root_y] = root_x
        self.group_sizes[root_x] += self.group_sizes[root_y]
        self.num_group -= 1
        return True
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for node1, node2 in edges:
            union_find.union(node1, node2)
        return union_find.count()
```

### 解法2: 反復型 DFS

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/37/changes の 4th
  - https://github.com/naoto-iwase/leetcode/pull/28/changes の 1st
- 考えたこと
  - 隣接 node を list で管理することもできる。
    - `nが大きく、疎のノードが多い場合には空間計算量の点でdictがベターな選択肢になることもあるかもしれません。`
      - 確かに。defaultdict を使うと edge があって append するときに初めて追加するので、最初に全 node 分を確保する list よりもこの場合少なくなる。コメントの通り、今回の問題では制約上あり得ないが。
      - https://github.com/naoto-iwase/leetcode/pull/28/changes#r2442726171
    - `i が 0～n-1 のため、 list[list[int]] 型にもできます。こちらのほうがハッシュの計算などが省略でき、軽くなるかもしれません。`
      - 確かに index accessing の方がハッシュ計算の必要がなくて処理が軽くなりそう。visited も同じ。
      - https://github.com/h-masder/Arai60/pull/20/changes#r3109854179
  - visited も合わせて list で管理するのが一貫性があって好み。
  - list で管理するのと、反復型で解いているの以外は step1 と同じ流れ。
  - 想定ユースケース
    - step1 同様、特に入力のバリデーションは設けていないので社内利用前提。
  - 計算量
    - 入力の n を V とし、辺の数 len(edges) を E とする。
    - 時間計算量: O(V + E)
      - adjacent_nodes の初期化に 1 * V、値を追加していくのに、1 * E、その後の外側のループが 1 * V。
      - DFS 内ではその隣接する node も探索するので、2 * E。 
      - なので、定数倍も含めた処理回数の目安としてはおよそ 2V + 3E 回程度になる。
      - LeetCode の最大入力を考慮し、かつ Python を 10^7step / 秒とすると、最大、(2 * 2000 + 3 * 5000) / 10^7 = 0.0019 ≈ 約 2ms かかる。
    - 空間計算量: O(V + E)
      - adjacent_nodes の初期化に 1 * V 個、値を追加していくと 2 * E 個。
      - visited が 1 * V 個。
      - nodes_to_visit: 直線状グラフになる最悪ケースで最大 1 * V。
      - なので、定数倍も含めたメモリの目安としてはおよそ 3V + 2E 程度になる。
      - LeetCode の最大入力を考慮し、整数を 8 Byte として計算すると、3 * 2000 * 8 + 2 * 5000 * 8 = 128000B = 128KB 程度になる。 

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_nodes = [[] for _ in range(n)]
        for node1, node2 in edges:
            adjacency_nodes[node1].append(node2)
            adjacency_nodes[node2].append(node1)
        visited = [False] * n
        def visit_connected_components(start_node: int) -> None:
            nodes_to_visit = [start_node]
            visited[start_node] = True
            while nodes_to_visit:
                node = nodes_to_visit.pop()
                for neighbor in adjacency_nodes[node]:
                    if visited[neighbor]:
                        continue
                    nodes_to_visit.append(neighbor)
                    visited[neighbor] = True

        num_connected_components = 0
        for node in range(n):
            if visited[node]:
                continue
            visit_connected_components(node)
            num_connected_components += 1
        return num_connected_components
```

### 解法3: 再帰型 BFS

- 参考にした回答
  - https://github.com/h-masder/Arai60/pull/20/changes の 2nd
- 考えたこと
  - BFS って再帰でも解けるのか。知らなかった。
  - next_nodes を再帰で渡すようにして、FIFO で実行されるようにすればできるのか。
  - 呼び出し側にとって都合がいいように、type hint 上から読み取れないバリデーションを追加してみた。
  - 各 edge は必ず2個でないといけない、ダブりがないようにしないといけない、って改めて見ると結構厳しい制約だな。
  - level ごとに next_nodes をまとめて次の再帰関数を呼ぶので、call stack は DFS の時 よりも少なくなる
  - 想定ユースケース
    - ライブラリの一関数として提供。
  - 計算量
    - 入力の n を V とし、辺の数 len(edges) を E とする。
    - 時間計算量: O(V + E)
      - step1 と同じく、最大約 2ms かかる。
    - 空間計算量: O(V + E)
      - step1 と同じく、最大 128KB 使う。
    
```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_adjacent_nodes = defaultdict(list)
        for edge in edges:
            if len(edge) != 2:
                raise ValueError(
                    "Each edge must contain exactly 2 nodes."
                )
            node1, node2 = edge
            if node1 == node2:
                raise ValueError(
                    f"Self-loops are not allowed: ({node1}, {node2})."
                )
            node_to_adjacent_nodes[node1].append(node2)
            node_to_adjacent_nodes[node2].append(node1)
        visited = set()
        def visit_adjacent_nodes(nodes: List[int]) -> None:
            if not nodes:
                return
            next_nodes = []
            for node in nodes:
                visited.add(node)
                for neighbor in node_to_adjacent_nodes[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    next_nodes.append(neighbor)
            visit_adjacent_nodes(next_nodes)

        num_connected_components = 0
        for node in range(n):
            if node in visited:
                continue
            num_connected_components += 1
            visit_adjacent_nodes([node])
        return num_connected_components
```

## Step 3

- 考えたこと
  - 常識の範囲内である DFS の反復型で解いてみる。
  - わかりやすさのために、adjacent_nodes (connected_nodes) を neighbors に統一した。
  - また、nodes_to_visit は、厳密にいうと、`nodes whose neighbors should be visited` になるので、名が体を成していないと思った (nodes_to_visit に追加した直後に visited に追加するのはかなり驚きだろう)。 なので、nodes_to_expand にリネームした。
  - 可読性を重視するなら、neighbors と visited は list よりも dict で管理する方が対の感じをより表現できる感じがして好み。

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_neighbors = defaultdict(list)
        for node1, node2 in edges:
            node_to_neighbors[node1].append(node2)
            node_to_neighbors[node2].append(node1)
        visited = set()
        def visit_neighbors(start_node: int) -> None:
            nodes_to_expand = [start_node]
            visited.add(start_node)
            while nodes_to_expand:
                node = nodes_to_expand.pop()
                for neighbor in node_to_neighbors[node]:
                    if neighbor in visited:
                        continue
                    nodes_to_expand.append(neighbor)
                    visited.add(neighbor)
        
        num_connected_components = 0
        for node in range(n):
            if node in visited:
                continue
            visit_neighbors(node)
            num_connected_components += 1
        return num_connected_components
```

## Step 4


