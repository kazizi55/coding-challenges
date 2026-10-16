# 617. Merge Two Binary Trees

## Link

https://leetcode.com/problems/merge-two-binary-trees/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1

- 考えたこと
  - 2つの binary tree が入力として渡され、同じ位置にある node 同士は merge され、そうでない場合は残り続ける。
  - BFS, DFS のどちらでも解ける。全探索する必要があるので、どちらの方が効率的とかはなさそう。
  - 一旦 DFS で解いたが、実装がやや重く、最終的に Gemini に聞きながら完成させた。もっとシンプルに書けそう。
  - 想定ユースケース
    - ライブラリの一関数としての提供。
  - 計算量
    - N を max(len(root1), len(root2))とする
    - 時間計算量: O(N) 
      - tree が片方に偏っていても完全ニ分木でも結局 stack に入れて一個ずつ見ていくので、計算量は変わらなさそう
      - 最悪ケースは root1 と root2 で node が全く被っていない場合。
      - 問題の最大入力を考慮すると推定実行時間は、2000 * 2 / 10^7 = 0.4ms 程度
    - 空間計算量: O(N)
      - TraverseStatus は1 インスタンスにつき、約 330Bだった
      - DFS だと一方の枝を深さ優先で辿り切ってスタックから pop してからもう一方の枝を処理するため、非被りであっても両方のノードが同時にスタックに積まれることはなく、最大の stack の長さは片方の最大深さ分の約 2000 個程度。
      - 問題の最大入力を考慮すると推定消費メモリは、2000 * 330 = 0.6MB 程度

```py
from dataclasses import dataclass

@dataclass
class TraverseStatus:
    node1: Optional[TreeNode]
    node2: Optional[TreeNode]
    new_parent: TreeNode
    left: bool

class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if root1 is None and root2 is None:
            return None
        sentinel = TreeNode(0)
        traverse_statuses = [TraverseStatus(node1=root1, node2=root2, new_parent=sentinel, left=True)]
        while traverse_statuses:
            status = traverse_statuses.pop()
            if status.node1 is None and status.node2 is None:
                continue
            
            node1_left_child, node1_right_child = None, None
            node2_left_child, node2_right_child = None, None

            if status.node1 is not None and status.node2 is not None:
                new_val = status.node1.val + status.node2.val
                node1_left_child, node1_right_child = status.node1.left, status.node1.right
                node2_left_child, node2_right_child = status.node2.left, status.node2.right
            elif status.node1 is not None:
                new_val = status.node1.val
                node1_left_child, node1_right_child = status.node1.left, status.node1.right
            else:
                new_val = status.node2.val
                node2_left_child, node2_right_child = status.node2.left, status.node2.right
            
            new_node = TreeNode(new_val)
            if status.left:
                status.new_parent.left = new_node
            else:
                status.new_parent.right = new_node
            
            traverse_statuses.append(
                TraverseStatus(
                    node1=node1_right_child, node2=node2_right_child,
                    new_parent=new_node,
                    left=False
                )
            )
            traverse_statuses.append(
                TraverseStatus(
                    node1=node1_left_child, node2=node2_left_child,
                    new_parent=new_node,
                    left=True
                )
            )
        return sentinel.left
```

```
>>> print("Instance base size:", sys.getsizeof(status))
Instance base size: 48
>>> print("Internal dict size:", sys.getsizeof(status.__dict__))
Internal dict size: 280
```

## Step 2

- `新しいのを作るか作らないのか、古い入力を壊すのか壊さないのか、共有するのかしないのか(変更しない前提ならばメモリー使用量が減る)、などのオプションがあって、自分がどれを「選択」したかを意識しましょう。`
  - 確かに。どの解法も「絶対に正しい・間違っている」ということはなく、特定のユースケースに有用。今回の問題はこのような選択肢が見えているべきだった。
  - https://github.com/fhiyo/leetcode/pull/25#discussion_r1656461334
- `こういうのは趣味なのですが、基本的に「ある幅を持った選択肢を考えた上で気に入ったものを選んでいる」というプロセスが大事です。ここで、書いた最終出力結果でしか評価されないと思っていると、だいぶそれは違います。要するに、「A と B と C を考慮した上で、A を選んだ」というのと「A で動くことが分かったので A にした」というのだと結果が同じでもまったく違う評価になるということです。`
  - 別視点からの同じ話。問題が解けたというのは全体の3割でしかない、というのはまさにこういうことなのだろう。
  - https://discord.com/channels/1084280443945353267/1200089668901937312/1204638326410448987
- `これ、たとえば、分散処理をして戻ってきたデータをマージするなど、このようなことをしたくなる状況はそこそこあるように思います。`
  - なるほど、こんな感じでユースケースをもっと具体的にしてみてもいいな。
  - https://github.com/irohafternoon/LeetCode/pull/26/changes#r2056460029
- とりあえず、破壊、非破壊でそれぞれ書いてみる。あと step1 (非破壊で反復 DFS) のブラッシュアップもしてみる。
- あとダブルポインタを使った実装もいくつか見つけた。実装してみる。

### 解法1: 非破壊で再帰 DFS

- 参考にした回答
  - https://github.com/fhiyo/leetcode/pull/25/changes の 1st
  - https://github.com/olsen-blue/Arai60/pull/23/changes の 4th
  - https://github.com/hayashi-ay/leetcode/pull/12/changes の 5th
  - https://github.com/goto-untrapped/Arai60/pull/47/changes#r1730325260
  - https://github.com/Fuminiton/LeetCode/pull/23/changes#r1997660435
- 考えたこと
  - 呼び出し側が root1 か root2 を書き換えた時に、出力が勝手に書き換わる可能性があるのが入力非破壊なのに対して一貫性がないと思うので、node が入力と出力で共有されないようにもする。
    - `1. 新しい ListNode を返すか`、`2. copy.deepcopy() を使うか`、`3. 下に流すか`のざっくり3パターンがある
      - `if root1 is None` に対して、`return TreeNode(root2.val, root2.left, root2.right)` か、`return copy.deepCopy(root2)` か、`root1 = TreeNode(0)` とするかという違い。
    - 1は2の自前実装という理解。
    - 1と3は TreeNode の値を同じ loop のどのタイミングで入れるかどうかの違いで処理的には同じことをしている。
    - TreeNode に値をセットする処理をより凝集できている3が好み。
    - copy.deepcopy()
      - 文字通り deep copy する。
      - すでに copy している object を memo として渡すことができるのか。
      - https://docs.python.org/3/library/copy.html#copy.deepcopy
  - 想定ユースケース
    - 分散処理をして戻ってきたデータをマージする関数。ライブラリの1関数という想定。
    - recursion limit がデフォルトだと1000なので、この問題に対応する時点で書き換える必要あり。(LeetCode 上だと50000程度だったと思うのでこの考慮は不要)
      - 常にこの limit を気にしなければならないので、大きな入力の処理には不向きだと思う。
  - 計算量
    - N を max(len(root1), len(root2))とする
    - 時間計算量: O(N)
      - 最大推定所要時間は step1 と同じ。
    - 空間計算量: O(N)
      - step1 と同じく、最大の call stack の長さは片方の最大深さ分の約 2000 個程度。
      - 1 frame あたり 400B。
      - TreeNode 1インスタンスあたり 320B 程度。
      - root1 と root2 が完全に被っていないと最大で4000個 TreeNode インスタンスができる。
        - step1 の計算で TreeNode インスタンスを考慮していないことに気づいた。
      - 最大推定消費メモリは 400 * 2000 + 320 * 4000 = 2MB 程度

```py
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            root1 = TreeNode(0)
        if root2 is None:
            root2 = TreeNode(0)
        new_root = TreeNode(root1.val + root2.val)
        new_root.left = self.mergeTrees(root1.left, root2.left)
        new_root.right = self.mergeTrees(root1.right, root2.right)
        return new_root
```

```py
import sys, inspect
def check_frame(root1, root2):
    f = inspect.currentframe()
    frame_sz = sys.getsizeof(f)
    locals_sz = sys.getsizeof(f.f_locals)
    print(f'Frame object: {frame_sz} bytes')
    print(f'Locals dict:  {locals_sz} bytes')
    print(f'Total frame:  {frame_sz + locals_sz} bytes')

check_frame(None, None)
# Frame object: 216 bytes
# Locals dict:  184 bytes
# Total frame:  400 bytes
```

```
>>> node = TreeNode(0)
>>> sys.getsizeof(node)
48
>>> sys.getsizeof(node.__dict__)
288
```

### 解法2: 破壊で再帰 DFS

- 参考にした回答
  - https://github.com/tarinaihitori/leetcode/pull/23/changes の 2nd
  - https://github.com/hayashi-ay/leetcode/pull/12/changes の 5th
- 考えたこと
  - 書いていて危なっかしくなるな、、
    - root1.val を破壊している
    - root2 の参照を root1 に渡すようにしているため、マージ後の木(root1) の val を書き換えたら、root2 の対応する val が書き換わる可能性がある
  - 空間計算量が節約できるとはいえ、限られた状況下以外ではまず実務では使わないだろう。
  - 想定ユースケース
    - 入力を破壊してもよい使い捨ての集計用 script が適していそう。
    - 入力が大きくても消費メモリをかなり抑えられるので、メモリ上限が厳しい状況に有用そう。
    - ただし Recursion Limit は変わらず気にする必要がある。
  - 計算量
    - M を min(N1, N2) とする
      - root1 か root2 が None の時に None じゃない方を返しているため min() になる。
    - 時間計算量: O(M)
      - 最大推定所要時間は step1, step2 の解法1と同じ。
      - が、root1, root2 のうち、どちらが極端に長い時はこの解法の方が効率がいい。
    - 空間計算量: O(M)
      - in-place の書き換えなので heap memory は 0
      - 最大推定メモリは 2000 * 500 = 1MB 程度

```py
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
```

### 解法3: 非破壊で反復 BFS

- 参考にした回答
  - https://github.com/fhiyo/leetcode/pull/25/changes の 3rd
  - https://github.com/olsen-blue/Arai60/pull/23/changes の 2nd
- 考えたこと
  - step1 のブラッシュアップをしたい。ただし BFS を代わりに使ってみる。
  - queue にいれる前に、merge をすることによって、queue に その node が左右の子供どちらかどうかを持つ必要がなくなるのか
  - merge の際に copy.deepcopy(node) を返すのではなく TreeNode(0) を node に代入するようにすると、node1 か node2 のいずれかが None の場合でも queue に積む必要がある。残りの子孫を辿ってノードを1つずつ生成し続ける必要があるため、片方だけでも子が存在すれば queue に積むという感じ。
    - copy.deepcopy(node) を使う場合は、片方が None の時点で、もう片方の子孫を全て copy するので queue に積む必要がない。したがって、両方の子が存在する場合（node1.left is not None and node2.left is not None）のみ queue に積めばよい（right も同様）。
    - step2 の解法1のように TreeNode(0) を返すようにしてもロジックの凝集はされずにむしろ冗長な部分が増えるように思われ、copy.deepcopy() は定数倍のオーバーヘッドがある程度大きいものの今回は制約をある程度気にしないユースケースにしたので、copy.deepcopy() を選択。
      - Python の copy.deepcopy() は、循環参照を防ぐためのメモ化辞書の管理（各ノードの id 検索・登録）や、型検査・`__dict__` のリフレクション探索を動的に行うため、直接 TreeNode を生成する手動コピーに比べて定数倍のオーバーヘッドが大きくなる。
  - 想定ユースケース
    - step2 の解法1のように、ライブラリの一関数。
    - 入力の木の偏りが大きく、かつ木があまり深くないもの (copy.deepcopy() 内部でも再帰が走るので Recursion Limit を気にする必要あり)
  - 計算量
    - M を min(N1, N2) とする
    - 時間計算量: O(N)
      - 重なる部分(最大 M 個 node)は while ループで走査
      - 重なり合わない残りの部分木は copy.deepcopy によって全ノードが1度ずつ複製される。
      - したがって全ノードの訪問回数は最大でも O(N)。
      - 最大推定所要時間は step1 と同じ。
    - 空間計算量: O(N)
      - マージ後の新しいツリーの構築に O(N) のヒープメモリが必要。
        - このヒープメモリを step1 で考慮していなかった、、次回から考慮する。
      - BFS queue のメモリ消費量は木の最大幅に依存し、完全二分木で最大 O(M) 程度。
      - 全体の空間計算量は新しい木を含めて O(N)。
      - 推定消費メモリ
        - TreeNode 1つ（インスタンス＋`__dict__`）: 320B 程度
        - マージ後の木（完全非重複で最大 4000ノード）: 4000 * 320B = 1.3MB 程度
        - BFS queue（完全二分木で最大幅 1000個、1タプル約 100B）: 1000 * 100B = 0.1MB 程度
        - deepcopy 内部のメモ化辞書・コールスタック: 約 0.5MB
          - `./measure_memo.py` にて確認
        - 合計で最大 1.5MB 〜 2MB 程度に収まる

```py
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        def merge(node1, node2) -> TreeNode | None:
            if node1 is None and node2 is None:
                return None
            if node1 is None:
                return copy.deepcopy(node2)
            if node2 is None:
                return copy.deepcopy(node1)
            return TreeNode(node1.val + node2.val)
        
        merged_root = merge(root1, root2)
        if root1 is None or root2 is None:
            return merged_root
        nodes1_and_nodes2_and_merged = deque([(root1, root2, merged_root)])
        while nodes1_and_nodes2_and_merged:
            node1, node2, merged = nodes1_and_nodes2_and_merged.popleft()
            merged.left = merge(node1.left, node2.left)
            if node1.left is not None and node2.left is not None:
                nodes1_and_nodes2_and_merged.append((
                    node1.left,
                    node2.left,
                    merged.left
                ))
            merged.right = merge(node1.right, node2.right)
            if node1.right is not None and node2.right is not None:
                nodes1_and_nodes2_and_merged.append((
                    node1.right,
                    node2.right,
                    merged.right
                ))
        return merged_root
```

- TreeNode(0) を返すようにすると以下のようなコードになる。

```py
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        def merge(node1: TreeNode | None, node2: TreeNode | None) -> TreeNode | None:
            if node1 is None and node2 is None:
                return None
            if node1 is None:
                node1 = TreeNode(0)
            if node2 is None:
                node2 = TreeNode(0)
            return TreeNode(node1.val + node2.val)

        if root1 is None and root2 is None:
            return None
        merged_root = merge(root1, root2)
        nodes1_and_nodes2_and_merged = deque([(root1, root2, merged_root)])
        while nodes1_and_nodes2_and_merged:
            node1, node2, merged = nodes1_and_nodes2_and_merged.popleft()
            node1_left = node1.left if node1 is not None else None
            node2_left = node2.left if node2 is not None else None
            if node1_left is not None or node2_left is not None:
                merged.left = merge(node1_left, node2_left)
                nodes1_and_nodes2_and_merged.append((node1_left, node2_left, merged.left))
            node1_right = node1.right if node1 is not None else None
            node2_right = node2.right if node2 is not None else None
            if node1_right is not None or node2_right is not None:
                merged.right = merge(node1_right, node2_right)
                nodes1_and_nodes2_and_merged.append((node1_right, node2_right, merged.right))
        return merged_root
```

```
% python3 arai60/617-merge-two-binary-trees/measure_memo.py
============================================================
deepcopy 内部のメモ化辞書・コールスタック: 計測
============================================================
1. メモ化辞書 (memo dict):
   - 登録エントリ数: 4001 件 (TreeNode 2000個 + __dict__ 2000個 + root)
   - メモリサイズ:   147544 bytes (0.14 MB)

2. コールスタック (call stack):
   - 1フレームあたり: 360 bytes (frame object + locals dict)
   - 最大1000フレーム: 360000 bytes (0.34 MB)

3. 合計 (メモ化辞書 + コールスタック):
   - 147544 B + 360000 B = 507544 bytes
   - 約 0.48 MB  ->  【約 0.5MB】
============================================================
```

### 解法4: setattr と getattr を使って実装 (反復 DFS)

- 参考にした回答
  - https://github.com/hroc135/leetcode/pull/22#discussion_r1795257023
  - https://github.com/Yoshiki-Iwasa/Arai60/pull/66#discussion_r1777943015
  - https://github.com/tarinaihitori/leetcode/pull/23/changes#r1919824481
- 考えたこと
  - `わりとこの関数の動作は、自然言語で表現すると複雑になる感じを受けています。「node1, node2 が両方 nil でない場合は Val のみ初期化するが、片方 nil の場合は nil でない方を流用することによって答えを作り、両方とも nil ならば nil を返す。」ですよね。stack を引数に与えると、「node1.Left と node2.Left をマージして、続きがあれば stack に足しておく(左側の処理)。」くらいまで圧縮できるはずです。`
    - step2 の解法3の merge() がその関数にあたる
    - 言われてみると確かに自然言語で表現しづらいな
    - できるだけ圧縮できるように処理を書く視点をこれから持つようにする
  - stack から pop() してから merge() をするので、stack に node を積む時点で子がいるかどうかわからない。親への参照を stack に積むことで、後からその子を追加することができる
    - C++、Go、Rust などだと、double pointer で `merged **TreeNode` などのように定義して、merged node への参照を stack に積める
    - Python だと double pointer は使えないので、setter (setattr) か親 node を stack に積む形になる。勉強のために double pointer にできる限り寄せたいので、前者を選択。
      - https://docs.python.org/3/builtins/functions.html#setattr
  - partial() が必要なのは、setattr が第3引数の val を必須としているため。
  - ` If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.`
    - filter() の挙動。便利。
    - https://docs.python.org/3/builtins/functions.html#filter
  - `partial(setattr, ...)` で setattr をカリー化して後から部分適用していくの関数型みたいで興味深い。
  - 想定ユースケース
    - ライブラリの一関数としての提供。
  - 計算量
    - N を max(len(root1), len(root2))とする
    - 時間計算量: O(N)
      - Big O 的には Step1 と同じだが、`nodes = list(filter(None, nodes))` と `total_val = sum(n.val for n in nodes)` でそれぞれ N 個分の探索がプラスされる。
    - 空間計算量: O(N)
      - traverse_statuses の tuple は1つあたり 300B 程度
        - tuple: 50B 程度 (40 + 8 * len(traverse_statuses[i]))
        - partial object とその args: 170B 程度 (object * 2 + pointer = 80 * 2 + 8)
        - inner list: 100B (list + pointers = 80 + 2 * 8)
      - 問題の制約的に最大推定消費メモリは 2000 * 300 + 300 = 600300 = 600KB 程度

```py
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        dummy = TreeNode()
        traverse_statuses = [(partial(setattr, dummy, "left"), [root1, root2])]
        while traverse_statuses:
            write_node, nodes = traverse_statuses.pop()
            nodes = list(filter(None, nodes))
            if not nodes:
                continue
            total_val = sum(n.val for n in nodes)
            new_node = TreeNode(total_val)
            write_node(new_node)
            for child in ["left", "right"]:
                traverse_statuses.append((
                    partial(setattr, new_node, child),
                    [getattr(n, child) for n in nodes]
                ))
        return dummy.left
```

## Step 3

- 考えたこと
  - 問題の制約内で考えるなら、非破壊の再帰 DFS がシンプルかつ呼び出し側の驚きも少ないので好み。

```py
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            root1 = TreeNode(0)
        if root2 is None:
            root2 = TreeNode(0)
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged
```

## Step 4


