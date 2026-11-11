# 103. Binary Tree Zigzag Level Order Traversal

## Link

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- level by level で　left to right と right to left で交互に見ていくというもの。
- `102. Binary Tree Level Order Traversal` と同じようなアプローチでいけそう。
- 反復 BFS で level が例えば奇数の時は left to right、そうでないときは right to left で見ていくとすればいけるかな。
- deque を使っても使わなくても解けそうだが、使わない方が素直かも。まずはそれで解いてみる。

### 解法1: 反復 BFS

- 考えたこと
  - 変数が多いのが難点。一方でそれにより level ごとに行う処理が素直に表現できている気はする。
  - level を定義しなくても `len(node_vals) + 1` を参照すれば同じことはできるが、level は主役級なのと、level を1個ずつ進めている感じを出した方が読みやすいと思っているのであえて定義した。
  - 想定ユースケース
    - 計算量的に解法1-3の中で最も軽量かつ、recursion limit を気にする必要もなく、ライブラリの import も不要なので汎用的に対応できる解法だとは思う。
  - 計算量
    - 時間計算量: O(N)
      - 全 node を探索するまで終わらないので N 回
      - `node_vals_per_level.reverse()` が2回に1回走るので、合計 N/2 回
      - 問題の制約を考慮すると、最大推定所要時間は (2000 + 2000/2) / 10^7 = 0.3ms 程度
    - 空間計算量: O(N)
      - nodes_to_visit は最大 N/2 個格納。
      - node_vals は最大 N 個格納。subarray は log2(N) 個とする。
        - 前問で最大 N 個の subarray が格納されているとして、それを元に計算を行っていたが、他の変数と同じタイミングで最大になるわけではない (これのみ skewed tree の場合になる) ので、同一条件下での最大個数に変えている。
      - next_nodes_to_visit は最大 N/2 個格納。
      - node_vals_per_level は最大 N/2個格納。
      - 問題の制約を考慮すると、最大推定消費メモリは 2000 / 2 * 8 + 100 + 2000 * 8 + 100 * log2(2000) + 2000 / 2 * 8 + 100 + 2000 / 2 * 8 + 100 = 40KB 程度

```py
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes_to_visit = [root]
        node_vals = []
        level = 1
        while nodes_to_visit:
            next_nodes_to_visit = []
            node_vals_per_level = []
            for node in nodes_to_visit:
                node_vals_per_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is None:
                        continue
                    next_nodes_to_visit.append(child)
            nodes_to_visit = next_nodes_to_visit
            if level % 2 == 0:
                node_vals_per_level.reverse()
            node_vals.append(node_vals_per_level)
            level += 1
        return node_vals
```

### 解法2: 反復 BFS で deque を使う

- 考えたこと
  - deque を使って実装。
  - 偶数だったら subarray の頭に、そうでなかったら末尾に追加するというロジックの実装のためだけに、deque を node_vals に追加するのはあんまり気に入っていない。
  - 想定ユースケース
    - node が非同期に入力されてくるか、stream で 1つずつ入力されてくる場合に有用。例えば node の数がかなり多くて並行で処理している時などだろうか。その場合はまとまった nodes として処理できないので、この解法のように1つずつ node をみて最初か最後に追加していく必要がある。
  - 計算量
    - 時間計算量: O(N)
      - `reverse()` がないが、代わりに最後に list に変換するとき 最大 N 個分探索する必要がある。
      - 問題の制約を考慮すると、最大推定所要時間は 2000 * 2 / 10^7 = 0.4ms 程度
    - 空間計算量: O(N)
      - nodes_and_levels には最大 N/2 個格納。
      - node_vals は最大 N 個格納。subarray も最大 N 個。
      - 問題の制約を考慮すると、最大推定消費メモリは skewed tree の場合になる。よって、1 * (8 * 2 + 50) + 800 + 2000 * (8 + 800) + 100 = 1.6MB 程度。
        - `sys.getsizeof(deque([]))` を手元で実行すると 760B だった。ここでは1つあたり 800B として計算。

```py
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        nodes_and_levels = deque([(root, 1)])
        node_vals = []
        while nodes_and_levels:
            node, level = nodes_and_levels.popleft()
            if level > len(node_vals):
                node_vals.append(deque([]))
            if level % 2 == 0:
                node_vals[level - 1].appendleft(node.val)
            else:
                node_vals[level - 1].append(node.val)
            for child in [node.left, node.right]:
                if child is None:
                    continue
                nodes_and_levels.append((child, level + 1))
        return [list(node_val_group) for node_val_group in node_vals]
```

### 解法3: 再帰 DFS

- 考えたこと
  - 再帰 DFS でも解く。
  - 内容はほぼ解法2と変わらず。
  - 想定ユースケース
    - tree の高さよりも幅が大きい場合に BFS よりもメモリ消費量を抑えることができる。
    - ただし、recursion limit は気にしないといけない。
  - 計算量
    - 時間計算量: O(N)
      - node が None でも call stack に積んで探索しているので、2N 分の探索になる。
      - 問題の制約を考慮すると、最大推定所要時間は 2000 * 2 * 2 / 10^7 = 0.8ms 程度
    - 空間計算量: O(N)
      - node_vals は最大 N 個格納。subarray も最大 N 個。
      - call stack 1つあたりのオーバーヘッドを 300B とする。
      - 問題の制約を考慮すると、最大推定消費メモリは skewed tree の場合になる。2000 * (8 + 800) + 100 + 300 * 2000 = 2.2MB 程度。


```py
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        node_vals = []

        def traverse_node_vals(node: TreeNode | None, level: int) -> None:
            if node is None:
                return
            if level > len(node_vals):
                node_vals.append(deque([]))
            if level % 2 == 0:
                node_vals[level - 1].appendleft(node.val)
            else:
                node_vals[level - 1].append(node.val)
            traverse_node_vals(node.left, level + 1)
            traverse_node_vals(node.right, level + 1)

        traverse_node_vals(root, 1)
        return [list(node_val_group) for node_val_group in node_vals]
```

## Step 2

- `return [list(nodes) for nodes in nodes_ordered]と掛けなくはないのですが、少し指しすぎかもしれません。`
  - 個人的にはこれくらいなら許容レベルだった。こう思う方もいると認識しておく。
  - https://github.com/hayashi-ay/leetcode/pull/35#discussion_r1504207832
- `リフレクション的な機能は極力使用しないほうが良いと思います。理由は、コンパイル時の静的な解析でエラーを特定することが難しくなる場合があるためです。`
  - 確かに。getattr や setattr は黒魔術という話は前にもみたな。
  - https://github.com/hayashi-ay/leetcode/pull/35#discussion_r1504201369
- `Reflection is then the ability to make modifications at runtime by making use of introspection`
  - Reflection という言葉を初めて聞いたのでメモ。Introspection とセットで覚える。
  - https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful
- getattr を使う解法はちょっと黒魔術感があるなー。
  - https://github.com/hayashi-ay/leetcode/pull/35/changes#diff-8408720477e1fa6f21dd1fc886a99aa3a937252dddfe9a431516bbb8e258e6fdR32-R35
- `オープンワールドのゲームの RTA みたいな感じを受けていますが、大事なのは、 ... 移り変わり、みたいなものを上で特に表現してみました。`
  - これを普段から意識しているつもりだが改めて。早く効率的な解法を書けることだけで満足してはならない。
  - https://discord.com/channels/1084280443945353267/1206101582861697046/1208473290881110117
- `私の意図は「無価値」というよりは、「専門家が行動することよりも広い範囲で考えていることがある。学習の際には、報酬を得るポイントはある程度多いほうがよいので、考えていることを広く一致させたほうがよい。」というようなことです。`
  - 考えていることも含めて一致させるように普段から学習する。
  - https://github.com/olsen-blue/Arai60/pull/27#discussion_r1937955131
- `深さ (英: depth) とは、逆に、あるノードについて、そのノードから根ノードまでのエッジ数のこと。根ノードの深さは 0 である。`
  - なので初期値は depth は 0、level は 1 となる。
  - https://github.com/olsen-blue/Arai60/pull/27#discussion_r1957344202
- 色んな回答を見て、探索自体を zigzag に行うかどうか、レベルごとに左か右から探索するか、subarray 挿入時に反転させるかどうか、再帰か反復か、などの選択肢があったのだなと知る。step1 で解法は3つ浮かんだが、選択肢としてそれぞれの特徴や良し悪しを考えるところまではパッとは行けなかったので精進する。

### 解法1: zigzag に探索

- 参考にした回答
  - https://github.com/TORUS0818/leetcode/pull/29/changes の 2nd
  - https://github.com/fhiyo/leetcode/pull/29/changes の 3rd
  - https://github.com/Mike0121/LeetCode/pull/10/changes の 3rd
  - https://github.com/sakupan102/arai60-practice/pull/28/changes#r1597349140
- 考えたこと
  - from_left などの flag を持たせて level ごとで queue にいれる順番を反転する方法か、level か depth 的な変数が偶数かどうかでその順番を反転させる方法かで大きく2通りある感じだった。
  - どちらも同じくらい好みなので、今まで書いてこなかった前者で書いてみる。
  - BFS なのに、level では LIFO で探索するのか。最後に挿入した node から次の level で探索するようにしたいため。面白いな。
  - nodes に append する処理を append_if_exists として定義。同じ処理が3つ以上あると関数に切り出したくなる。
  - ネストしている `while nodes_to_visit` は `for node in reversed(nodes)` と書いてもいい。好みの問題だと思う。
  - 想定ユースケース
    - 定数倍レベルで他の解法よりも早いので、より高速な処理が求められる場合に適している
    - 問題の制約上やらないが、generator として yield node.val というように実装するようにすれば、1つずつ node を返していくような streaming 処理ができるようになる。
  - 計算量
    - 時間計算量: O(N)
      - reverse() も list への変換もないので、N 回探索するのみで OK。
      - 問題の制約を考慮すると、最大推定所要時間は 2000 / 10^7 = 0.2ms 程度
    - 空間計算量: O(N)
      - step1 の解法1 と同じ。

```py
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        def append_if_exists(nodes: list[TreeNode], node: TreeNode | None) -> None:
            if node is None:
                return
            nodes.append(node)

        if root is None:
            return []
        nodes_to_visit = [root]
        node_vals = []
        from_left = True
        while nodes_to_visit:
            next_nodes_to_visit = []
            node_vals_per_level = []
            while nodes_to_visit:
                node = nodes_to_visit.pop()
                node_vals_per_level.append(node.val)
                if from_left:
                    append_if_exists(next_nodes_to_visit, node.left)
                    append_if_exists(next_nodes_to_visit, node.right)
                    continue
                append_if_exists(next_nodes_to_visit, node.right)
                append_if_exists(next_nodes_to_visit, node.left)
            nodes_to_visit = next_nodes_to_visit
            node_vals.append(node_vals_per_level)
            from_left = not from_left
        return node_vals
```

## Step 3

- 考えたこと
  - 思いつかなかった step2 の解法を練習。
  - 基本的な流れは step1 の解法1とほぼ同じなので覚えやすい。

```py
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        def append_if_exists(nodes: list[TreeNode], node: TreeNode | None) -> None:
            if node is None:
                return
            nodes.append(node)
        
        if root is None:
            return []
        nodes_to_visit = [root]
        node_vals = []
        from_left = True
        while nodes_to_visit:
            next_nodes_to_visit = []
            node_vals_per_level = []
            while nodes_to_visit:
                node = nodes_to_visit.pop()
                node_vals_per_level.append(node.val)
                if from_left:
                    append_if_exists(next_nodes_to_visit, node.left)
                    append_if_exists(next_nodes_to_visit, node.right)
                    continue
                append_if_exists(next_nodes_to_visit, node.right)
                append_if_exists(next_nodes_to_visit, node.left)
            nodes_to_visit = next_nodes_to_visit
            node_vals.append(node_vals_per_level)
            from_left = not from_left
        return node_vals
```

## Step 4


