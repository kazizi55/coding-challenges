# 104. Maximum Depth of Binary Tree

## Link

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1: 反復 BFS

- 考えたこと
  - TreeNode の左右両方が null でない限り、それらを queue に積んでいって depth を increment して、最終的にその depth を返すようにすればいけそう。BFS。再帰でも反復でも解けるな。一旦反復で解いてみる。
  - depth の初期値を 1 にする凡ミスをした、、root を stack に積む限りは 0 にする必要がある。
  - 想定ユースケース
    - ライブラリの一関数として提供。
    - Recursion Error を気にしなくていいので安全。深さが事前に予測できない木構造でも対応可能。
  - 計算量
    - 時間計算量: O(N)
      - node が均等に配置されておらず、一直線に並んでいるのが最悪ケース。その場合のこの問題を考慮した Python の推定最大所要時間は、10^4 / 10^7 ≈ 1ms
    - 空間計算量: O(N)
      - 完全二分木のように横に広がっている場合が最悪ケース。最下層の node 数が最大で N/2 個になるため O(N)。ちなみに一直線に並ぶ場合は各層 1個なので最良ケース O(1) になる。
      - この問題を考慮した Python の推定最大メモリは、10^4 / 2 * 8 ≈ 40KB

```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes = [root]
        depth = 0
        while nodes:
            next_nodes = []
            for node in nodes:
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            nodes = next_nodes
            depth += 1
        return depth
```

### 解法2: 再帰 DFS

- 考えたこと
  - 再帰でも解く。
  - これも node is None の時の depth をどう返すかで最初 WA になってしまった、、これは一番最後の max() が実行されるときも + 1されるため、base case は depth のみを返すのが正しい。
  - 想定ユースケース
    - 社内利用の都度実行のスクリプト。
    - デフォルトの max recursion limit は 1000なので、depth が深い可能性がある場合は使わない方がいい
    - 平衡二分木のように、depth が O(log N) に抑えられているデータの集計が適している
  - 計算
    - 解法1と同じ

```py
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def traverse_max_depth(node: TreeNode | None, depth: int) -> int:
            if node is None:
                return depth
            return max(
                traverse_max_depth(node.left, depth),
                traverse_max_depth(node.right, depth)
            ) + 1

        return traverse_max_depth(root, 0)
```

## Step 2

- `ちょっと全ノードに部下を立たせてみましょう ... 全員がこの仕事やってたら、なんかとにかく無駄って思いません。`
  - アルゴリズムに沿って人に動いてもらう想定で考える手法。自然言語で説明しやすい解法がやはり好み。
  - https://discord.com/channels/1084280443945353267/1226508154833993788/1246313673446653963
- `depthという変数名でノードの深さを表す変数というのは分かるけれど、何のノードの深さなのかというのが文脈依存で意味が変わるので読むのが大変という感じですかね。`
  - なぜ読みづらいのかをここまで言語化できるのが流石だと思った。私も見習っていきたい。
  - https://github.com/nittoco/leetcode/pull/14/changes/BASE..f88affbf9dceed3e6c60711cff87114715631c3e#r1622575220

### 解法1: 再帰 DFS

- 参考にした回答
  - https://github.com/fhiyo/leetcode/pull/23/changes の 1st
  - https://github.com/hayashi-ay/leetcode/pull/22/changes の 3rd
- 考えたこと
  - maxDepth 自体を再帰で呼ぶこともできるのか。そうすることでさらにシンプルになる。
  - 想定ユースケース
    - step1 の解法2 と同じ
  - 計算量
    - step1 の解法2 と同じ

```py
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        ) + 1
```

### 解法2: 反復 BFS

- 参考にした回答
  - https://github.com/fhiyo/leetcode/pull/23/changes の 1st
  - https://github.com/fhiyo/leetcode/pull/23/changes#r1675990961
- 考えたこと
  - deque に (node, depth) を入れる方法は思い浮かばなかった。その方がより BFS っぽくなる感じがある
  - とはいえ、個人的には depth ごとで1ずつ depth を increment するのがわかりやすい next_nodes と nodes を使う解法の方が好みかも。
  - ある高さにある node の数が多ければ多いほどとメモリを消費するのが BFS、 逆に深ければ深いほど消費するのが DFS なのか、言われてみれば確かに。
  - 想定ユースケース
    - step1 の解法1 と同じ
  - 計算量
    - step1 の解法1 と同じ
    - depth を deque の中に持つので空間計算量は若干大きくなる

```py
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        nodes_and_depths = deque([(root, 1)])
        max_depth = 1
        while nodes_and_depths:
            node, depth = nodes_and_depths.popleft()
            max_depth = max(max_depth, depth)
            if node.left is not None:
                nodes_and_depths.append((node.left, depth + 1))
            if node.right is not None:
                nodes_and_depths.append((node.right, depth + 1))
        return max_depth
```

### 解法3: 帰りがけに maxDepth を increment する反復 DFS

- 参考にした回答
  - https://github.com/fhiyo/leetcode/pull/23/changes の 2nd
  - https://discord.com/channels/1084280443945353267/1227073733844406343/1236235351140339742
  - https://github.com/goto-untrapped/Arai60/pull/45/changes の 2nd
  - https://github.com/sakupan102/arai60-practice/pull/21/changes の 2nd
- 考えたこと
  - `二つの DFS は対応しておらず、上から配るのと下から上げてくるのの差があることは認識できますか?`
    - 私の解法だと、step1 の解法2が「下から上げてくるもの」(帰りがけに maxDepth を increment)に該当する。stack を使った反復 DFS をただ step1 の解法1みたく解けば「上から配るもの」(行きがけに maxDepth を increment)になる。
    `つまり、良いかはともかく、こういう選択肢もあります。`で挙げているコードは、再帰 DFS だが「上から配るもの」として実装している。
    - https://discord.com/channels/1084280443945353267/1227073733844406343/1236235351140339742
  - *_ref が list なのは mutable のため。int だと immutable なので参照渡しがができず、left_depth_ref や right_depth_ref を ret_depth_ref 経由で上書きすることができなくなってしまう。
  - left_depth_ref[0] と right_depth_ref[0] の参照を通して、下から上げてくる動きが見えて面白い。再帰 DFS の call stack も似たような動きをしている。
  - 行きと帰りを表現するために、stack に定数を積んでいる解法もいくつかあったが、関数として切り出して動作を自然言語で表現する方が好みなのでそのように実装した。
  - 想定ユースケース
    - step1 の解法2、step2 の解法1と同じ
    - が、メンテナンス性を考慮した時には実務では使わないと思う。
  - 計算量
    - step1 の解法2、step2 の解法1と同じ
    - ここまで来て call stack 分の空間計算量を今までの計算で考慮していないことがわかった。次から含める。

```py
class Solution:
    def is_going_forward(self, left_depth_ref, right_depth_ref):
        return left_depth_ref[0] == None and right_depth_ref[0] == None
    
    def maxDepth(self, root: TreeNode | None) -> int:
        res_depth_ref = [None]
        # (node, ret_depth_ref, left_depth_ref, right_depth_ref)
        traverse_statuses = [(root, res_depth_ref, [None], [None])]
        while traverse_statuses:
            node, ret_depth_ref, left_depth_ref, right_depth_ref = traverse_statuses[-1]
            if node is None:
                ret_depth_ref[0] = 0
                traverse_statuses.pop()
                continue
            if self.is_going_forward(left_depth_ref, right_depth_ref):
                traverse_statuses.append((node.left, left_depth_ref, [None], [None]))
                traverse_statuses.append((node.right, right_depth_ref, [None], [None]))
                continue
            ret_depth_ref[0] = max(left_depth_ref[0], right_depth_ref[0]) + 1
            traverse_statuses.pop()
        return res_depth_ref[0]
```

## Step 3

- 考えたこと
  - 反復の解法を選択。RecursionLimit を気にしなくていいのと、1個ずつ処理しているのがより直感的にわかって好みのため。
  - tree が横に長ければ BFS、縦に長ければ DFS を選択するのが良いと思うのだが、問題上では明示されていないので、勉強のために step1 で思いつかなかった BFS を選択。

```py
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        nodes_and_depths = deque([(root, 1)])
        max_depth = 1
        while nodes_and_depths:
            node, depth = nodes_and_depths.popleft()
            max_depth = max(depth, max_depth)
            if node.left is not None:
                nodes_and_depths.append((node.left, depth + 1))
            if node.right is not None:
                nodes_and_depths.append((node.right, depth + 1))
        return max_depth
```

## Step 4

- step2 の解法3を改善
  - tuple の要素数が多くてそれぞれが何なのかわかりづらかったので、dataclass を使うように
  - 帰りがけに親の左と右の depth を上書きしていくのをわかりやすくした
  - is_going_forward を visited に置き換え

```py
from dataclasses import dataclass

@dataclass
class TraverseStatus:
    node: Optional[TreeNode]
    parent_traverse_status: Optional["TraverseStatus"] = None
    is_left_child: bool = False
    left_depth: int = 0
    right_depth: int = 0
    visited: bool = False

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        traverse_statuses = [TraverseStatus(node=root)]
        while traverse_statuses:
            status = traverse_statuses[-1]
            if not status.visited:
                status.visited = True
                if status.node.right is not None:
                    traverse_statuses.append(
                        TraverseStatus(
                            node=status.node.right,
                            parent_traverse_status=status
                        )
                    )
                if status.node.left is not None:
                    traverse_statuses.append(
                        TraverseStatus(
                            node=status.node.left,
                            parent_traverse_status=status,
                            is_left_child=True
                        )
                    )
                continue
            traverse_statuses.pop()
            max_depth = max(status.left_depth, status.right_depth) + 1
            if status.parent_traverse_status is None:
                return max_depth
            if status.is_left_child:
                status.parent_traverse_status.left_depth = max_depth
            else:
                status.parent_traverse_status.right_depth = max_depth
        return 0
```