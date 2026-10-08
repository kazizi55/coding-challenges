# 111. Minimum Depth of Binary Tree

## Link

https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- 前問の 104. Maximum Depth of Binary Tree とほぼ同じ考え方で解けそう。
- が、leaf node までの最短距離を全探索して見たいので、DFS を使うべき？あとは再帰か反復か、あとは call stack か自前 stack かといったところか。
- 問題の制約的には、node がどういうふうに連なるかの記載はない。これも前問と同じ。
- node.left と node.right が ともに None になる == node が leaf node ということになる。
- 全部一通り解いてみる。

### 解法1: 反復 DFS

- 考えたこと
  - depth を stack に持たせるか、変数として定義して loop の中で increment していくやり方があるが、前者の方が node.left と node.right と depth という関係を凝集して表現できている感じがするので好み。
    - 空間計算量をシビアに考えないといけない状況なら後者を選ぶ。
  - これは上から下に探索していっている流れ。
  - 想定ユースケース
    - ライブラリの一関数として提供。
    - Recursion Error を気にしなくていいので安全。深さが事前に予測できない木構造でも対応可能。
  - 計算量
    - 時間計算量: O(N)
      - node が一直線に並んでいるのが最悪ケース。
      - 問題の制約を考慮した Python での推定実行時間は、10^5 / 10^7 = 10ms 程度
    - 空間計算量: O(N)
      - 完全二分木のように横に広がっている場合が最悪ケース。最下層の node 数が最大で N/2 個になるため O(N)。
      - 問題の制約を考慮した Python での推定消費メモリは、10^5 * 8 * 2 / 2 = 800KB 程度

```py
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes_and_depths = [(root, 1)]
        min_depth = sys.maxsize
        while nodes_and_depths:
            node, depth = nodes_and_depths.pop()
            if node.left is None and node.right is None:
                min_depth = min(depth, min_depth)
                continue
            if node.left is not None:
                nodes_and_depths.append((node.left, depth + 1))
            if node.right is not None:
                nodes_and_depths.append((node.right, depth + 1))
        return min_depth
```

### 解法2: 再帰 DFS (call stack)

- 考えたこと
  - traverse_min_depth をそのまま return する形で書けるかなと思ったが、depth と min_depth をどう保持するか考えた時に、traverse_min_depth の引数に min_depth を持たせると、それを上書きして引数を破壊することになるので避けた。
  - 代わりに traverse_min_depth を呼びつつ、min_depth を外側で保持、nonlocal で traverse_min_depth 内で書き換えることを明示した。
  - 想定ユースケース
    - 社内利用の都度実行のスクリプト。
    - デフォルトの max recursion limit は 1000なので、depth が深い可能性がある場合は使わない方がいい。
  - 計算量
    - 解法1とほぼ同じ。
    - プラスで、call stack の分のメモリが積まれる感じになる。
      - 1000 * 300 = 300KB 程度がプラスされる感じだろうか。

```py
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        min_depth = sys.maxsize
        def traverse_min_depth(node: TreeNode | None, depth: int) -> int:
            nonlocal min_depth
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
            if node.left is not None:
                traverse_min_depth(node.left, depth + 1)
            if node.right is not None:
                traverse_min_depth(node.right, depth + 1)

        if root is None:
            return 0
        traverse_min_depth(root, 1)
        return min_depth
```

### 解法3: 再帰 DFS (自前 stack)

- 考えたこと
  - 104 で nodchip さんから頂いた FB を元に実装を進める (dataclass を使う、参照渡しした値の上書きをやめる)
    - https://github.com/kazizi55/coding-challenges/pull/21#discussion_r4180199346
    - https://github.com/kazizi55/coding-challenges/pull/21#discussion_r4190778511
  - 途中から Gemini に聞きながら書いた。若干実装重め。
  - 行数が多く、一呼吸おきたいところが多かったので、空行を追加してみている。
  - 104 だと、left_depth, right_depth という命名にしていたが、その level での depth というふうにも見えるなと思ったので、明示的に left_min_depth, right_min_depth という名前に変更。「その level での左/右の child から積み上がってきた min_depth」なので。
  - 想定ユースケース
    - ライブラリの一関数として提供という感じ。が、実務ではこのように書くことはないだろう。
  - 計算量
    - 時間計算量: O(N)
      - Big O 上は解法1と同じだが、行き帰りがあるので倍になる。
      - 問題の制約を考慮した Python での推定実行時間は、10^5 / 10^7 * 2 = 20ms 程度
    - 空間計算量: O(N)
      - Big O 上は解法1と同じだが、dataclass を使っているのと、最大 N/2 ではなく N個になるのが違う。
      - 実際にメモリを調べてみたところ、TraverseStatus 1インスタンスあたり約 350B だった。
      - 問題の制約を考慮した Python での推定消費メモリは、10^5 * 350 = 35MB 程度

```py
from dataclasses import dataclass

@dataclass
class TraverseStatus:
    node: Optional[TreeNode]
    parent_traverse_status: Optional[TraverseStatus] = None
    is_left_child: bool = False
    left_min_depth: int = 0
    right_min_depth: int = 0
    visited: bool = False

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        traverse_statuses = [TraverseStatus(node=root)]
        while traverse_statuses:
            status = traverse_statuses[-1]
            if not status.visited:
                status.visited = True
                if status.node.left is not None:
                    traverse_statuses.append(
                        TraverseStatus(
                            node=status.node.left,
                            parent_traverse_status=status,
                            is_left_child=True
                        )
                    )
                if status.node.right is not None:
                    traverse_statuses.append(
                        TraverseStatus(
                            node=status.node.right,
                            parent_traverse_status=status,
                        )
                    )
                continue

            traverse_statuses.pop()
            
            if status.node.left is not None and status.node.right is not None:
                min_depth = min(status.left_min_depth, status.right_min_depth) + 1
            elif status.node.left is not None:
                min_depth = status.left_min_depth + 1
            elif status.node.right is not None:
                min_depth = status.right_min_depth + 1
            else:
                min_depth = 1

            if status.parent_traverse_status is None:
                return min_depth

            if status.is_left_child:
                status.parent_traverse_status.left_min_depth = min_depth
            else:
                status.parent_traverse_status.right_min_depth = min_depth
        return 0
```

```
>>> status = TraverseStatus(node=None)
>>> print(status.__dict__)
{'node': None, 'parent_traverse_status': None, 'is_left_child': False, 'left_min_depth': 0, 'right_min_depth': 0, 'visited': False}
>>> print("Instance base size:", sys.getsizeof(status))
Instance base size: 48
>>> print("Internal dict size:", sys.getsizeof(status.__dict__))
Internal dict size: 296
```

## Step 2

- `木の高さを求めるときには、上から数字を配っていくか、下から集めてくるかの2方向があって、それぞれ再帰で書くか、スタックとループで書くか、がありますね。`
  - 104 でも同じようなコメントを目にした。改めて考えてみると、下から集めてくる再帰パターンはまだ書いていないな。
  - https://discord.com/channels/1084280443945353267/1196472827457589338/1237988315781664770
- `これ、面白い書き方ですね。他の言語でも使えそうですね。`
  - 確かに Python でも使えるかも。
  - https://github.com/Yoshiki-Iwasa/Arai60/pull/25/changes/BASE..0816b5d2268b91c7bcb24881a301f829ae148ba2#r1665958206
- テストコードの書き方
  - https://github.com/usatie/leetcode/pull/4/changes#r1940258085
- 104 ではエラー処理を行なっていなかったので、この問題では意識的に行なってみる。
- あ、確かに BFS でも解けるな。むしろ leaf node の方が early return ができる(leaf node を見つけた時点でそれが答えの min depth になる)ので、パフォーマンスも良さそう。step1 の段階で気づいておくべきだったなー。
- DFS でも「枝刈り」をすると、その時の min_depth より深いところを見なくて済むので効率化できるのか、なるほど。
  - https://github.com/TORUS0818/leetcode/pull/24/changes#diff-7435bbd8ce81e1d7ea48f67dd0e6361c5a0d7edf5f5581e58323b5570d4b483bR162-R167

### 解法1: 反復 BFS

- 参考にした回答
  - https://github.com/olsen-blue/Arai60/pull/22/changes の step3
  - https://github.com/hayashi-ay/leetcode/pull/26/changes の step4
  - https://github.com/Yoshiki-Iwasa/Arai60/pull/25/changes の step3
- 考えたこと
  - node と depth を tuple で管理するやり方に慣れていたので、それぞれを別管理にする解法にも改めて慣れてみる。
  - node.left と node.right を child として loop で回すのはいいかどうかは場合によるなー。早期 continue もできるし、同じ処理をまとめられている感じがする一方で、`if node.left is None and node.right is None` も child にしたくなってチグハグ感がある。`is_leaf_node(node)` みたいな関数を定義すれば、チグハグ感は薄れるが、そこまでするかなという感じ。
  - error message をただ "unreachable" としている方が多かったが、呼び出し側としてはもう少し情報があった方がわかりやすいと思ったので足した。
  - 想定ユースケース
    - ライブラリの一関数として提供。
  - 計算量
    - 時間計算量: O(N)
      - node が一直線に並んでいるのが最悪ケースなのは DFS と同じ。推定実行時間は step1 の解法1と同じ。
      - だが、それ以外で完全二分木でない限りは leaf node がある一番浅い depth で early return されるので効率的になる。
    - 空間計算量: O(N)
      - 完全二分木のように横に広がっている場合が最悪ケースなのも DFS と同様。推定メモリは step1 の解法1と同じ。

```py
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        nodes = [root]
        depth = 1
        while nodes:
            nodes_in_next_depth = []
            for node in nodes:
                if node.left is None and node.right is None:
                    return depth
                for child in [node.left, node.right]:
                    if child is None:
                        continue
                    nodes_in_next_depth.append(child)
            nodes = nodes_in_next_depth
            depth += 1
        raise RuntimeError(
            "Unreachable: binary tree contains no leaf nodes"
        )
```

### 解法2: 再帰 DFS (下から集めてくる)

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/26/changes の 1st
  - https://github.com/TORUS0818/leetcode/pull/24/changes の 1st
- 考えたこと
  - step1 の解法3 と大枠の流れは同じだが call stack を使う解法。
  - `if root.left is None and root.right is None` がないと、`if root.left is None` で左右両方の child がないときも拾うことになり、暗黙的だなと思ったので、明示的にした。
  - 下から集めてくる方法にしようとすると、DFS になるのだな。
  - 再帰で枝刈りをしたい場合は min_depth を別に定義し、step1 の解法2のように helper 関数を定義する必要がある。
  - 想定ユースケース
    - step1 の解法2と同じ。
  - 計算量
    - step1 の解法2と同じ。

```py
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        ) + 1
```

## Step 3

- 考えたこと
  - 反復 BFS が好み。
    - 枝刈りをせずとも early return されるので、自然と leaf node がある一番浅い depth までの処理になるように最適化されるため。
    - node と depth を tuple で一緒に持つか、別で管理するかは好みだなー。両方書いてみたが、書き心地は同じ感じ。強いて言えば tuple で一緒に持つ方が depth の increment を忘れない感じがして若干好み。
    - が、tuple の方が depth を queue に積む分、空間計算量が増えるので場合による。

```py
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        nodes = [root]
        depth = 1
        while nodes:
            nodes_in_next_depth = []
            for node in nodes:
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    nodes_in_next_depth.append(node.left)
                if node.right is not None:
                    nodes_in_next_depth.append(node.right)
            nodes = nodes_in_next_depth
            depth += 1
        raise RuntimeError("Unreachable: binary tree has no leaf nodes")
```

```py
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        nodes_and_depths = deque([(root, 1)])
        while nodes_and_depths:
            node, depth = nodes_and_depths.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                nodes_and_depths.append((node.left, depth + 1))
            if node.right is not None:
                nodes_and_depths.append((node.right, depth + 1))
        raise RuntimeError("Unreachable: binary tree has no leaf nodes")
```

## Step 4


