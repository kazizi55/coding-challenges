# 98. Validate Binary Search Tree

## Link

https://leetcode.com/problems/validate-binary-search-tree/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- valid BST かどうかを判断する関数を書くという問題。
- 再帰で解けそう。一旦それで解いてみる。node の数が最大 10^4 個なので、実務だと再帰は避けたくなるな。
- 親の val を受け取るヘルパー関数を定義してその中で自身の val と比べるというのを再帰で書いていけば解けそう？

### 解法1: 再帰 (WA)

- 考えたこと
  - 時間切れになってしまった。
  - `root = [5,4,6,null,null,3,7]` の時に false を返すべきなのか。BST の定義について復習しないといけなさそうだな。
    - ああ、`The right subtree of a node contains only nodes with keys strictly greater than the node's key.` は親と子だけではなくて、遡って行った root まで適用されるのか。
    - 3 は 5 の right subtree にあるので、valid ではないということ。

```py
# Wrong Answer 77 / 87 testcases passed
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_valid_bst(node: TreeNode | None, parent_node_val: int, is_left: bool) -> bool:
            if node is None:
                return True
            if is_left and node.val >= parent_node_val:
                return False
            if not is_left and node.val <= parent_node_val:
                return False
            return is_valid_bst(node.left, node.val, True) and is_valid_bst(node.right, node.val, False)
        
        return is_valid_bst(root, -sys.maxsize, False)
```

### 解法1: 再帰

- 考えたこと
  - Gemini と壁打ちをしながら解いた。
  - 最小値と最大値の範囲を node.left か node.right を渡すときに定義すれば子でどちら側の subtree かを意識する必要がなくなる。こちらのほうが処理が素直な感じがして好み。
  - `float("inf")` を使うか `sys.maxsize` を使うかに関しては、後者だと 32 bit platform の場合に問題上の最大値 (`2**31 - 1`)と一致する可能性があるので、前者を採用した。それがなくて、かつ node.val の最大値も低いのなら、type を int で揃えるために `sys.maxsize` を使うかもしれない。
    - `It’s usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.`
      - https://docs.python.org/3/library/sys.html#sys.maxsize
    - https://docs.python.org/3/builtins/functions.html#float
  - 想定ユースケース
    - ロジックが明快で素直な一方、recursion limit を気にする必要があるため、ある程度 depth が浅めの tree しか入力されないことがわかっている場合にはいいかもしれない。
  - 計算量
    - 時間計算量: O(N)
      - N 回 + None の node も call stack に積まれるので、実際は一階層分多く探索することになる。
      - valid bst でないのがわかった時点で早期 return する。
      - 問題の制約を考慮した最大推定所要時間は、(10^4 + 10^4 + 1) / 10^7 = 2ms 程度。
    - 空間計算量: O(N)
      - 1 call stack あたりのオーバーヘッドを 300B とする。
      - skewed tree の場合が最悪ケース。よって、問題の制約を考慮した最大推定消費メモリは、300 * 10^4 = 3MB 程度。

```py
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_valid_bst(node, big_node_val, small_node_val):
            if node is None:
                return True
            if not small_node_val < node.val < big_node_val:
                return False
            return (
                is_valid_bst(node.left, node.val, small_node_val) and 
                is_valid_bst(node.right, big_node_val, node.val)
            )
        
        return is_valid_bst(root, float("inf"), float("-inf"))
```

## Step 2

- かなり選択肢が多い問題だったのだなと周りを見て気づく。これくらいの幅で step1 で見えるようになっていたいな。精進する。
- 周りを見る限りだと、行きがけか帰りがけか、iterative か recursive か、in-order かどうか、子から subtree の情報をもらうか親の node から値の範囲を決めるかどうかが挙げられる。
- `float("inf")` が値として返ってくると呼び出し手的にぎょっとするのはわかる。どうしてもそれをしたいなら JSDoc 的なもので呼び出し側にわかるようにコメントを入れておきたい。それかその場合は明示的にエラーを返すか。後者の方が好み。
  -https://github.com/nittoco/leetcode/pull/35/changes#r1735372624
- `一番小さい数と一番大きい数を表現するために math.inf を使っているのだと思うのですが、値の意味に関する説明がなく、ある種のマジックナンバーになってしまっているように思います`
  - これは確かに。あとこういう境界値は定数として切り出しておいた方が後から変えやすいのでその点でも切り出す方が好み。
  - https://github.com/TORUS0818/leetcode/pull/30/changes#r1712609142
- math.inf と float("inf") は output が同一になる。好みの問題。
  - https://docs.python.org/3/library/math.html#math.inf
- `lower, upper はinclusiveにも受け取れるので、ここで「等号つかなくていいのかな？」と気になりました。`
  - うーん、個人的にはこのままでもわかる派。特に英語だと more than とか less than とかだと exclusive になるように、exclusive なのがデフォルトという感覚がある。なので、むしろ inclusive にしたいとき lower_or_equal とかの命名に変えるべきで今回はそのままでいいのではないかと思う。
  - https://github.com/ksaito0629/leetcode_arai60/pull/20#discussion_r2957298088
- `inner にすることは、たとえば、その外側のローカル変数を使うとかで、せざるをえないことがありますが、そうでなければ、class method として並べちゃったほうが私は読みやすいと思いますね。入れ子にすると外側の関数が呼ばれるたびに内側が作られることになるので。`
  - 言われてみれば確かにそうだな。これからは特別な理由がない限りは class method として定義することにする。
  - https://github.com/nittoco/leetcode/pull/35/changes#r1739979018

### 解法1: Iterative BFS

- 参考にした回答
  - https://github.com/YukiMichishita/LeetCode/pull/8/changes の 2nd
  - https://github.com/olsen-blue/Arai60/pull/28/changes の 2nd
  - https://github.com/hayashi-ay/leetcode/pull/38/changes の 6th
- 考えたこと
  - 定数は PEP8 に則って module level で設定。
    -https://peps.python.org/pep-0008/#constants
  - `A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.`
    - とのことで、python では明示的に file level を module level としているのでそれに準拠した。
    - https://docs.python.org/3/tutorial/modules.html
  - lower や upper だけだと中に入っているのか node なのか node.val なのかが名前だけだとわかりづらいと思うので、`_val`をつけた。
  - 想定ユースケース
    - BFS なので、skewed tree か、違反している node が root 側にある可能性が高い場合に有用。
  - 計算量
    - 時間計算量: O(N)
      - これは None の場合は deque に追加しないのでそのぶん探索回数が少なくて済む。
      - 問題の制約を考慮した最大推定所要時間は、10^4 / 10^7 = 1ms 程度。
    - 空間計算量: O(N)
      - これは complete tree の時が最悪ケース
      - deque のインスタンスのオーバーヘッドを 200B、append する tuple を 50B とする。
      - 問題の制約を考慮した最大推定消費メモリは、200 + 50 * 10^4 / 2 = 250KB 程度。

```py
from collections import deque
import math


MIN_VALUE = -math.inf
MAX_VALUE = math.inf

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        nodes_to_visit = deque([(root, MIN_VALUE, MAX_VALUE)])
        while nodes_to_visit:
            node, lower_val, upper_val = nodes_to_visit.popleft()
            if not (lower_val < node.val < upper_val):
                return False
            if node.left is not None:
                nodes_to_visit.append((node.left, lower_val, node.val))
            if node.right is not None:
                nodes_to_visit.append((node.right, node.val, upper_val))
        return True
```

### 解法2: Recursive DFS (in-order)

- 参考にした回答
  - https://github.com/nittoco/leetcode/pull/35/changes の 3rd
  - https://github.com/YukiMichishita/LeetCode/pull/8/changes の 2nd
  - https://github.com/olsen-blue/Arai60/pull/28/changes の 4th
- 考えたこと
  - in-order で並べた list を探索する解法。
  - generator を使うやり方と使わないやり方、また nonlocal を使うやり方もある。
  - `Generator + 再帰、強力ですね。pros cons の cons としては、再帰の深さの限界があること、走りかけの Generator を木の深さ分だけ作るのでそこそこ重いことがありそうですね。`
    - `tracemalloc` を使って手元で計測してみたら、generator を使う再帰がそうでない再帰の10倍くらいメモリを確保していた。確かに重い。
    - https://github.com/nittoco/leetcode/pull/35/changes#r1739978684
  - node.val との比較用の初期値を None にするのいいな。より実態に沿っていると感じる。
  - 一番思い浮かばなそうな generator を使うやり方で練習。
  - 想定ユースケース
    - 探索ロジックと判定ロジックを明確に分離できているように思うので、メンテ性を重視する場合には有用。
    - 一方で skewed tree の場合、yield from で O(N^2) かかるので、大きい入力には向かない。
  - 計算量
    - 時間計算量: O(N^2)
      - skewed tree の場合が最悪ケース。
      - さらに、None かどうかにかかわらず 子に対して yield from を行うのと、previous_val との比較をするのに都度下から上に yield を上げていかないといけない (= `走りかけの Generator を木の深さ分だけ作る`)。
        - 少し見やすいということ以外にメリットがない気がしてきたので、今後はできるだけ None の場合は子を探索しないようにしてみる。
      - なので、(1 + 2) + (2 + 2) + ... + (N + 2) = N(N + 1) / 2 + 2N 回探索することになる。
      - よって問題の制約を考慮した最大推定時間は (10^4 * (10^4 + 1) / 2 + 2 * 10^4) / 10^7 = 5s 程度。だいぶ重いな。
      - https://peps.python.org/pep-0380/#optimisations
    - 空間計算量: O(N)
      - 手元で測ってみて、1 generator あたり 200B 程度だった
      - こちらも skewed tree の場合が最悪ケースなので、問題の制約を考慮した最大確保メモリは、200 * (10^4 + 1) = 2MB 程度

```py
class Solution:
    def traverse_nodes_in_order(self, node: TreeNode | None) -> TreeNode | None:
        if node is None:
            return
        yield from self.traverse_nodes_in_order(node.left)
        yield node
        yield from self.traverse_nodes_in_order(node.right)

    def isValidBST(self, root: TreeNode | None) -> bool:
        previous_val = None
        for node in self.traverse_nodes_in_order(root):
            if previous_val is not None and node.val <= previous_val:
                return False
            previous_val = node.val
        return True
```

### 解法3: Iterative DFS (in-order)

- 参考にした回答
  - https://github.com/YukiMichishita/LeetCode/pull/8/changes の 2nd
  - https://github.com/naoto-iwase/leetcode/pull/33/changes の 2nd
  - https://github.com/fhiyo/leetcode/pull/30/changes の 3rd
  - https://github.com/TORUS0818/leetcode/pull/30/changes の 2nd
- 考えたこと
  - 左側の child を探索しきって stack に追加し、pop() して一つずつ見ていく中で、右側の child も合わせて追加するというもの
  - in-order なので必ず左側を先に探索するようにする。右側の child を探索するときもその child は左から見る必要がある。
  - 最初はあまりピンとこなかったが、図を書いてみたらわかった。
    - 再帰だけ解いても処理の流れが頭のなかで図解できていなかったと反省。
    - 今後は同じ考え方で解くものがあったらできるだけ再帰と反復で解こうと思う。
  - 周りを見る限りだと、左側の child を追加する関数を別で定義するかしないか、while ループの書き方をどうするか、stack 内の要素のデータ構造をどうするかでバリデーションがありそう
  - 個人的には関数に切り出したほうが素直な感じがするので、その方が好み。切り出さないで 1つの while 内で表現しようとすると、while 内の node が一意でなくなってしまうので可読性が下がると思ったため (左側の child を探索している途中の node と stack から pop() した node)。
  - 想定ユースケース
    - 推定所要時間と推定確保メモリとロジックの素直さのバランスが一番いいように思えた。実務で使うならこの解法かも。
  - 計算量
    - 時間計算量: O(N)
      - step1 の解法1 と同じく None の場合は探索しないので、問題の制約を考慮した最大推定所要時間は、10^4 / 10^7 = 1ms 程度。
    - 空間計算量: O(N)
      - left-skewed tree の時が最悪ケース。
      - list のインスタンスのオーバーヘッドを 100B とする。
      - 問題の制約を考慮した最大推定確保メモリは、100 + 8 * 10^4 = 80KB 程度。 

```py
class Solution:
    def append_current_and_left_children(self, nodes: list[TreeNode], node: TreeNode) -> None:
        while node is not None:
            nodes.append(node)
            node = node.left

    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        nodes_to_visit = []
        self.append_current_and_left_children(nodes_to_visit, root)
        previous_val = None
        while nodes_to_visit:
            node = nodes_to_visit.pop()
            if previous_val is not None and node.val <= previous_val:
                return False
            previous_val = node.val
            if node.right is not None:
                self.append_current_and_left_children(nodes_to_visit, node.right)
        return True
```

### 解法4: Iterative DFS (帰りがけ)

- 参考にした回答
  - https://github.com/naoto-iwase/leetcode/pull/33/changes#r2479195403
- 考えたこと
  - 帰りがけで iterative で実装するときは、dataclass に切り出すのが好み。通常の tuple だと引数が4つあって渡す時にどれがどれか混乱するため。今回は内容を変更したく default 値も設定したいので、typing.NamedTuple や typing.TypedDict は選択肢から外れる。
  - dataclass で mutable type の property に default 値を設定したい場合は field() を使う必要がある。
    - https://docs.python.org/3/library/dataclasses.html#mutable-default-values
  - 想定ユースケース
    - 行きと帰りで行う処理を明確に分けたい時や探索の metadata を見たい時に有用。
    - 確保メモリは他の解法に比べてかなり多いのでそれが許容できる場合に限る。
  - 計算量
    - 時間計算量: O(N)
      - 帰りがけに valid BST かどうかの判定をするので、True だった場合に 2N 分探索する必要がある。これが最悪ケース。
      - 問題の制約を考慮した最大推定所要時間は、10^4 * 2 / 10^7 = 2ms 程度。
    - 空間計算量: O(N)
      - 1 TraverseStatus あたり 500B とする
        - 1 list あたり 50B とする
        - `sys.getsizeof(TraverseStatus(node=TreeNode())` が 56B
        - `sys.getsizeof(TraverseStatus(node=TreeNode().__dict__))` が 288B
      - skewed tree の時が最悪ケース。
      - 問題の制約を考慮した最大推定確保メモリは、10^4 * 500 = 5MB 程度

```py
from dataclasses import dataclass, field


@dataclass
class TraverseStatus:
    node: TreeNode
    val_bounds: list[int] = field(default_factory=list)
    left_val_bounds: list[int] = field(default_factory=list)
    right_val_bounds: list[int] = field(default_factory=list)

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        traverse_statuses = [TraverseStatus(node=root)]
        while traverse_statuses:
            status = traverse_statuses[-1]
            if not status.left_val_bounds and status.node.left is not None:
                traverse_statuses.append(TraverseStatus(
                    val_bounds=status.left_val_bounds,
                    node=status.node.left
                ))
                continue
            if not status.right_val_bounds and status.node.right is not None:
                traverse_statuses.append(TraverseStatus(
                    val_bounds=status.right_val_bounds,
                    node=status.node.right
                ))
                continue
            if status.left_val_bounds and status.left_val_bounds[1] >= status.node.val:
                return False
            if status.right_val_bounds and status.right_val_bounds[0] <= status.node.val:
                return False
            val_range = status.left_val_bounds + [status.node.val] + status.right_val_bounds
            status.val_bounds += [min(val_range), max(val_range)]
            traverse_statuses.pop()
        return True
```

## Step 3

- 考えたこと
  - 浮かばなかった解法のうち、好みだったものを練習。
  - 5個解法を作ってみて選択肢が比較的多いのと、step1 で WA したので、3つ選んで定着を試みる。

### 解法1: Recursion DFS

- 考えたこと
  - node.val と型を揃えたくなってきたので、MIN_VALUE などの初期値に sys.maxsize を使うようにした
  - MIN_VALUE などの初期値を None にするかは考えたが、lower_val と upper_val が None の可能性を考慮すると条件文が若干増えてしまうのがあまり素直でないなと思ったので、sys.maxsize を使うようにした。

```py
import sys

MIN_VALUE = -sys.maxsize
MAX_VALUE = sys.maxsize


class Solution:
    def is_valid_bst_helper(self, node: TreeNode | None, lower_val: int, upper_val: int) -> bool:
        if node is None:
            return True
        if not (lower_val < node.val < upper_val):
            return False
        return (
            self.is_valid_bst_helper(node.left, lower_val, node.val)
            and self.is_valid_bst_helper(node.right, node.val, upper_val)
        )

    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.is_valid_bst_helper(root, MIN_VALUE, MAX_VALUE)
```

### 解法2: Iterative BFS

```py
import sys
from collections import deque

MIN_VALUE = -sys.maxsize
MAX_VALUE = sys.maxsize


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        nodes_to_visit = deque([(root, MIN_VALUE, MAX_VALUE)])
        while nodes_to_visit:
            node, lower_val, upper_val = nodes_to_visit.popleft()
            if not (lower_val < node.val < upper_val):
                return False
            if node.left is not None:
                nodes_to_visit.append((node.left, lower_val, node.val))
            if node.right is not None:
                nodes_to_visit.append((node.right, node.val, upper_val))
        return True
```

### 解法3: Iterative DFS (in-order)

- 考えたこと
  - これも MIN_VALUE を最初に previous_value に渡す方が None の考慮をする必要がなくなって好み。

```py
import sys

MIN_VALUE = -sys.maxsize


class Solution:
    def append_left_children(self, nodes: list[TreeNode], node: TreeNode) -> None:
        while node is not None:
            nodes.append(node)
            node = node.left

    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        nodes_to_visit = []
        self.append_left_children(nodes_to_visit, root)
        previous_val = MIN_VALUE
        while nodes_to_visit:
            node = nodes_to_visit.pop()
            if previous_val >= node.val:
                return False
            previous_val = node.val
            self.append_left_children(nodes_to_visit, node.right)
        return True
```

## Step 4


