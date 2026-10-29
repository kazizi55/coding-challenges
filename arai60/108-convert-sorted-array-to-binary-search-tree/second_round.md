# 108. Convert Sorted Array to Binary Search Tree

## Link

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- 昇順で並んでいる数字の list を height-balanced tree に変えるという問題
- nums を分割していって、真ん中をとっていく感じか？二分探索？
- 時間切れになってしまったので、とりあえず Gemini に聞きながら形にする。
- 

### 解法1: 再帰 (補助関数なし)

- 考えたこと
  - こんなシンプルに書けるのかー。
  - 再帰関数自体を返さない再帰の解き方が苦手だなと実感。数をこなしていく。
  - `middle = len(nums) // 2` は `(len(nums) - 1) // 2` でも良い。len(nums) が偶数の時の挙動が変わるが、いずれも height-balanced bst になる。
    - 前者だと len(nums) が偶数の時に、右側の index になる (e.g., [1,2,3,4] の 3)
    - 後者だと左側 (e.g., [1,2,3,4] の 2)
  - `list[:index]` と `list[index:]` は右半開区間になるの忘れがち。気をつける。
  - 想定ユースケース
    - ライブラリの一関数。
    - ソート済みデータを一括読み込みして、BST に変換することで、検索・更新性能を O(N) から O(log N) に向上させられる。
    - 再帰で nums の部分配列を渡していくので、空間計算量が大きくなりがち。len(nums) がかなり大きい時は避けたほうが良い。
    - また、recursion limit があるので、呼び出し側にも必要に応じて max を引き上げてもらうなどして調整してもらう必要がある。
  - 計算量
    - 時間計算量: O(N log N)
      - 木の高さ（深さ）が O(log N) であり、各深さレベルでコピーされる部分配列の要素数の合計が常に O(N) となるため、全体で O(N log N)。
      - 問題の最大入力を考慮した最大推定実行時間は、10^4 * log2(10^4) / 10^7 = 13ms 程度。
    - 空間計算量: O(N)
      - node を len(nums) 分作っていくので、O(N)
      - call stack 的には O(log N)
      - O(N) + O(log N) なので Big O 的には O(N)
      - 問題の最大入力を考慮した最大推定消費メモリは、100 * 10^4 + 500 * log2(10^4) + 8 * 10^4 = 1.1MB 程度
        - TreeNode の1インスタンスあたり、100Bytes とする
        - Call stack の1 frame あたり、500Bytes とする
        - stack 上に存在する部分配列の要素合計を 10^4 個とし、1つあたり 8Bytes とする

```py
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        middle = len(nums) // 2
        node = TreeNode(nums[middle])
        node.left = self.sortedArrayToBST(nums[:middle])
        node.right = self.sortedArrayToBST(nums[middle + 1:])
        return node
```

### 解法2: 再帰 (補助関数あり)

- 考えたこと
  - 解法1よりも二分探索っぽくなる。
  - 解法1に合わせて右半開区間を用いて解いているが、閉区間とかでも解ける。
    - 解法1だと Python の list の range の仕様で右半開区間になるが、この解法は渡し方を任意で変えられるので自由度が高くて好み。
  - middle を mid としてみた。どこまで略していいのかいつも迷うが、これは略しても意味が明らかなのかなと思うため。
  - 想定ユースケース
    - 解法1と同じ。
    - が、再帰で pointer を渡すのみなので、空間計算量は比較的抑えられる。
  - 計算量
    - 時間計算量: O(N)
      - 全ての要素を1回ずつ訪れて N 個の node を作成するため、O(N)。
      - 解法1の部分配列コピーが発生せず、ポインタを渡すだけになるので、O(N log N) から O(N) になる。
      - 問題の最大入力を考慮した最大推定実行時間は、10^4 / 10^7 = 1ms 程度。
    - 空間計算量: O(N)
      - Big O 的には解法1と同じだが、stack 上の pointer の合計が log2(N) になる。
      - したがって、問題の最大入力を考慮した最大推定消費メモリは、100 * 10^4 + 500 * log2(10^4) + 8 * log2(10^4) = 1MB 程度。

```py
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build_bst(left, right) -> TreeNode | None:
            if left >= right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_bst(left, mid)
            node.right = build_bst(mid + 1, right)
            return node
        
        return build_bst(0, len(nums))
```

## Step 2

- 変数定義して結局使っていないのでメモリリークになるケース。Python だと GC があるので起きないが一応頭に入れておく。こういうところに C++ の難しさがあるのだろう。
  - https://github.com/irohafternoon/LeetCode/pull/27#discussion_r2060734803
- `最後のポインターは「を保存する先」という意味になりますね`
  - こう言い換えるとダブルポインタもわかりやすいな。
  - ダブルポインタでも解けるのか。それで解いてみる。
  - https://github.com/colorbox/leetcode/pull/38#discussion_r1939049518
- `left`, `right` は `middle` が index なので類推でわかるかなと思い、型ヒントはつけていなかったが、上から読んでいったとしたら確かに一見して node か index かわからないな。型ヒントをつける
  - https://github.com/olsen-blue/Arai60/pull/24/changes#r1934899506
- `あれ、nodeよりrootの方が良くないか？と気付く。middleで選んでるノードを根ノードにしてるので。`
  - うーん、悩ましい。再帰のだと小さな tree を連結している感じがよりあるので root でもいいが、そこに強い意図があるように見えてしまう感じがあるので、node の方が好み。
  - https://github.com/olsen-blue/Arai60/pull/24/changes#r1934899958
- `要するに再帰をある種の分業だと思ったときに、どこまでを上がやってどこからを下がやるかの境目の調整をしていることに相当しているはずです。人間が集まってこの作業を手でするとして、どういうマニュアルを書くか、どこを仕事の境界にするかに対応しているでしょう。`
  - 再帰の解法を思いつくのが苦手なので参考になる。どうやってみんなで分業するか、一人当たりどんなことをしてもらうかを考える。
  - https://github.com/hroc135/leetcode/pull/23/changes#r1797743801
- Go は部分配列を作る際にコピーをしない
  - `Slicing does not copy the slice’s data. It creates a new slice value that points to the original array.`
    - https://go.dev/blog/slices-intro
  -  https://github.com/hroc135/leetcode/pull/23/changes#diff-a22f439c4a0d211a142d80216200ad8509fb3cec4f3ec537e965a9f6a90d6968R177-R178
- `endにするとexclusive([start, end)の半開区間)だと思ってしまうかもしれないという意見をいくつか見かけました。 ... リーダブルコードによると、両側を含む閉区間には(first, last)の対を提案されていました。`
  - C++ の慣習的には end は exclusive な範囲を表すとのこと。
  - https://github.com/naoto-iwase/leetcode/pull/23/changes#r2434280798
- `seattrは実務的にはあまり使わないほうが良いそうです。 ... 自由度が高くて強力な道具は使わないほうがいいことが多いです。eval などと同じ部類と思ってください。`
  - 確かに、実務でこのようなオブジェクトを破壊するコードがたくさん使われていたら局所的にコードを読んでもわかりづらいだろう
  - https://github.com/naoto-iwase/leetcode/pull/23/changes#r2434245689
- いろんな方の解法を見ていて、行きがけ/帰りがけに tree を完成させるか、再帰/反復かで実装できることがわかった。
  - step1 は両方とも帰りがけ・再帰だった。

### 解法1: 行きがけ・反復

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/29/changes の 2nd
  - https://github.com/hroc135/leetcode/pull/23/changes の 2nd
  - https://github.com/naoto-iwase/leetcode/pull/23/changes#r2434250555
- 考えたこと
  - `ListNodeの場合と違いTreeNodeの場合は今回のようにdummyの左右どっちがrootかを把握しておく必要があるため、dummyを使わずに書いた方が分かりやすくなりそうです。`
    - これは同意。left, right かどうかに意味があるように見えるし、どちらに繋げたかを覚えておく必要があるのもあまり好みではない。
    - https://github.com/naoto-iwase/leetcode/pull/23/changes#r2434259090
  - `親側で「子のノードを作っておく（値は子に入れさせる）」までしておくとparentの引数を減らすこともできそうです。`
    - この方法が好みだなー。"left" や "right" を tuple に含めたり、setattr をしたりする必要もなくなる。
    - https://github.com/naoto-iwase/leetcode/pull/23/changes#r2434250555
  - `nodes_and_lefts_and_rights` という変数名、やや長いが中に何が入っているかを明示したいのでギリ許容かなという感じ。tuple 1個あたりの個数が4を超えたら traverse_statuses とかの抽象的な名前に変えるかなーという感じ。
  - 想定ユースケース
    - ライブラリの一関数
    - recursion limit を気にしなくていいので、node の depth が深すぎないか recursion limit を調整するかどうかを考える必要がなくなり、呼び出し手にやや親切かなと思っている。
  - 計算量
    - 時間計算量: O(N)
      - step1 の解法2と同じく、問題の最大入力を考慮した最大推定実行時間は、10^4 / 10^7 = 1ms 程度。
    - 空間計算量: O(N)
      - 問題の最大入力を考慮すると、nodes_and_lefts_and_rights には最大同時に N/2 個格納される。
      - 最大消費メモリは 100 * 10^4 + 100 * 10^4 / 2 = 1.5MB 程度
        - TreeNode 1インスタンスあたり 100B とする
        - deque 内の 3-tuple 1つあたり、100B とする
          - 3-tuple 自体は 64Bytes 程度の想定。(ヘッダ 40B + ポインタ (8B) x 3)
          - deque のスロット: 10B 程度
          - left, right の int オブジェクト: 0-56B (1024以下はキャッシュされるが、それ以上は 28B x 2 となる)
            - https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong

```py
from collections import deque

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        root = TreeNode()
        nodes_and_lefts_and_rights = deque([(root, 0, len(nums))])
        while nodes_and_lefts_and_rights:
            node, left, right = nodes_and_lefts_and_rights.popleft()
            mid = (left + right) // 2
            node.val = nums[mid]
            if left < mid:
                node.left = TreeNode()
                nodes_and_lefts_and_rights.append((node.left, left, mid))
            if mid + 1 < right:
                node.right = TreeNode()
                nodes_and_lefts_and_rights.append((node.right, mid + 1, right))
        return root
```

### 解法2: 先に tree を作ってから、in-order で書き換える (帰りがけ・再帰)

- 参考にした回答
  - https://github.com/hroc135/leetcode/pull/23#issuecomment-2418322326
- 考えたこと
  - in-order は DFS の1つで、left -> root -> right の順に探索していくこと。
    - 他にも以下がある
      - pre-order: root -> left -> right
      - post-order: left -> right -> root
    - 今まで DFS というと、pre-order 前提で考えていたことに気づいた。これからは DFS でもどの順番で探索しているか意識的になってみる。
    - 一方 BFS はlevel-order しかないのも興味深い。
    - https://www.geeksforgeeks.org/dsa/tree-traversals-inorder-preorder-and-postorder/
  - 以下の条件を満たすとき、complete binary tree と言える。
    - 一番下以外、全ての level が　nodes で埋まっている
    - 一番下が、左から右に隙間を開けず nodes で埋まっている
    - 他にも似たようなものとして以下がある。勉強になるな。
      - perfect binary tree: 全ての level が nodes で埋まっている
      - full binary tree: 全ての node が 0 か 2個の子を持っている (左か右かは問わない)
    - https://www.geeksforgeeks.org/dsa/complete-binary-tree/
  - set_values_for_nodes、popleft()、set_values_for_nodes の順で書いているのは in-order で node.val がセットされるようにするため。順番を変えると、pre-order や post-order になるので動かなくなる。
  - 想定ユースケース
    - ライブラリの一関数。
    - recursion limit を気にする必要あり。
    - 時間計算量が 2N になるので、他の解法より効率は悪い。
    - が、in-order, pre-order, post-order で node.val をセットするように自由に変えられるので、そのカスタマイズ性を持たせておきたいときに有用。
    - 木構造を作成する関数と、値をセットする関数が分かれているのも責務が分離されていて、拡張しやすい感じがあって好み。
  - 計算量
    - 時間計算量: O(N)
      - 部分配列コピーはしていないので、O(N)、また木構造を作成するのと値をセットするのでそれぞれ nums を探査するので、2N
      - 問題の最大入力を考慮した最大推定実行時間は、10^4 * 2 / 10^7 = 2ms 程度。
    - 空間計算量: O(N)
      - nums_to_visit には最大 N 個格納され、call stack は complete binary tree の高さ分保持(log2(N))。
      - 最大消費メモリは 100 * 10^4 + 10 * 10^4 + 500 * log2(10^4) = 1.1MB 程度
        - TreeNode 1インスタンスあたり 100B とする
        - deque 内のポインタスロット1つあたり 10B とする
        - call stack 1フレームあたり 500B とする

```py
from collections import deque
from typing import Optional

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build_tree(index) -> Optional[TreeNode]:
            if index >= len(nums):
                return None
            node = TreeNode()
            node.left = build_tree(2 * index + 1)
            node.right = build_tree(2 * index + 2)
            return node
        
        nums_to_visit = deque(nums)
        def set_values_for_nodes(node: Optional[TreeNode]) -> None:
            if node is None:
                return None
            set_values_for_nodes(node.left)
            node.val = nums_to_visit.popleft()
            set_values_for_nodes(node.right)
        
        root = build_tree(0)
        set_values_for_nodes(root)
        return root
```

### 解法3: 帰りがけ・反復

- 参考にした回答
  - https://github.com/naoto-iwase/leetcode/pull/23/changes#r2440407669
- 考えたこと
  - 最初の探索で子から親への参照と val、2回目の探索でそれらを元に tree を作るという解法。こうすれば帰りがけ・反復で解けるのか、面白いな。
    - 最初の探索は DFS でも BFS でも問題ない。2回目の探索では子から親の順で遡っていく必要があるので、pop() して後ろから取り出していく必要がある。
    - pop() ではあるが、最初の探索 が DFS だったら post-order DFS、BFS だったら reverse-order BFS になる。
  - 参照元コードは queue の tuple に要素を積む方針をとっているが、個人的には dataclass にした方が可読性が上がって好み。
  - getter を定義することで getattr() を使わないで済むのはいいな。
  - 想定ユースケース
    - ライブラリの一関数。
    - recursion limit を気にする必要なし。
    - nums から tree を作るための要素が入った配列に変換する関数と、それを tree に変換する関数に分けることができるので、コードが大きくなってきた場合の責務分離としての一つの解なのだろうか。解法2とは違う責務分離の方法で興味深い。
  - 計算量
    - 時間計算量: O(N)
      - nums への探索を2回行うので、2N
      - 問題の最大入力を考慮した最大推定実行時間は、10^4 * 2 / 10^7 = 2ms 程度。
    - 空間計算量: O(N)
      - TraverseStatus は DFS なので最大深さ分の log2 N 個程度が格納、 BuildStatus が N 個分格納。
      - それぞれ1インスタンスあたり 100B とする
      - また、BuildStatus内の left_pointer と right_pointer をそれぞれ 50B とする
      - 最大消費メモリは、100 * log2(10^4) + (100 + 50 * 2) * 10^4 = 2MB 程度。

```py
from collections import deque
from typing import List
from dataclasses import dataclass

@dataclass
class TraverseStatus:
    left_index: int
    right_index: int
    self_pointer: List[TreeNode]

@dataclass
class BuildStatus:
    val: int
    left_pointer: List[TreeNode]
    right_pointer: List[TreeNode]
    self_pointer: List[TreeNode]

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode | None:
        def pointer_to_node(pointer: List[TreeNode]) -> TreeNode | None:
            if not pointer:
                return None
            return pointer[0]
        
        if not nums:
            return None
        root_pointer = []
        traverse_statuses = [
            TraverseStatus(
                left_index=0,
                right_index=len(nums),
                self_pointer=root_pointer
            )
        ]
        build_statuses = []
        while traverse_statuses:
            status = traverse_statuses.pop()
            mid_index = (status.left_index + status.right_index) // 2
            left_pointer = []
            right_pointer = []
            build_statuses.append(
                BuildStatus(
                    val=nums[mid_index],
                    left_pointer=left_pointer,
                    right_pointer=right_pointer,
                    self_pointer=status.self_pointer
                )
            )
            if status.left_index < mid_index:
                traverse_statuses.append(
                    TraverseStatus(
                        left_index=status.left_index,
                        right_index=mid_index,
                        self_pointer=left_pointer
                    )
                )
            if status.right_index > mid_index + 1:
                traverse_statuses.append(
                    TraverseStatus(
                        left_index=mid_index + 1,
                        right_index=status.right_index,
                        self_pointer=right_pointer
                    )
                )

        while build_statuses:
            status = build_statuses.pop()
            node = TreeNode(
                val=status.val,
                left=pointer_to_node(status.left_pointer),
                right=pointer_to_node(status.right_pointer)
            )
            status.self_pointer.append(node)
        return pointer_to_node(root_pointer)
```

## Step 3

- 考えたこと
  - ロジックのシンプルさと処理効率性のバランス的に、帰りがけ・再帰で補助関数を使うものが好み。(step1 の解法2)
  - 書き方は変わっていないが、いろいろな解法を見てみて、より処理が腑に落ちるようになった気がする。

```py
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build_bst(left, right) -> TreeNode | None:
            if left >= right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_bst(left, mid)
            node.right = build_bst(mid + 1, right)
            return node

        return build_bst(0, len(nums))
```

## Step 4

### 解法1: step2 の解法2 の build_tree で要素の個数を受け取る

- 要素の個数を受け取るように変更することで個人的には処理が直感的になった。こっちの方が好みかも。
- 元の解法だとせっかく index を受け取っているのにそれを index として使うことがないので少し驚きがあると思う
- また、len(nums) を引数として注入するようになったので、この解法の方が build_tree を汎用化しやすい

```py
from collections import deque

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build_tree(count) -> TreeNode | None:
            if count <= 0:
                return None
            node = TreeNode()
            left_count = (count - 1) // 2
            right_count = (count - 1) - left_count
            node.left = build_tree(left_count)
            node.right = build_tree(right_count)
            return node

        nodes_to_visit = deque(nums)
        def set_values_for_nodes(node: TreeNode | None) -> None:
            if node is None:
                return None
            set_values_for_nodes(node.left)
            node.val = nodes_to_visit.popleft()
            set_values_for_nodes(node.right)

        root = build_tree(len(nums))
        set_values_for_nodes(root)
        return root
```
