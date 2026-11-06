# 102. Binary Tree Level Order Traversal

## Link

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- left to right, level by level で subarray を作り、配列として返すという要件。
- BFS でみていって node.val を level ごとで格納していけば解けそう。
- この解法以外パッと思い浮かばないな。悔しい。

### 解法1: BFS

- 考えたこと
  - level ごとに切り替わる感じを明確にしたいので、next_nodes 的な配列を作る解法でいきたい。
  - 割と素直にかけたかも。
  - ちょっと変数名が長くなってしまった気もするが、`*_per_level` と `next_*` は関心ごとが現在の level なのか次の nodes なのかで違うため、厳密に区別しておきたいので個人的には許容。
  - 想定ユースケース
    - データ分析用のライブラリの一関数として提供。
    - node.val が level ごとでどんな値があるのかを見るだけなら、集計する上で扱いづらい。
    - 関数を拡張していくなら、pre-order や post-order、in-order など並び方を指定できるようにする感じだろうか。その場合は subarray は無くなりそう。
  - 計算量
    - 時間計算量: O(N)
      - node を上から下まで全探索するので N。
      - 問題の制約的には、最大推定所要時間は 2000 / 10^7 = 0.2 ms 程度
    - 空間計算量: O(N)
      - nodes_to_visit は最大 N/2 個格納
      - node_vals は最大 N 個の subarray が格納
      - next_nodes_to_visit は最大 N/2 個格納
      - node_vals_per_level は最大 N/2 個格納
      - よって問題の制約的には、最大推定消費メモリは 2000 * 8 / 2 + 100 + 2000 * (8 + 100) + 100 + 2000 * 8 / 2 + 100 + 2000 * 8 / 2 + 100 = 240KB 程度
        - nodes_to_visit、next_nodes_to_visit には pointer のみが格納される
        - 配列1つあたりのオーバーヘッドを 100B とする
          - `sys.getsizeof([])` の結果は 56B、len が5を超えたあたりからバッファの確保で 120B になった

```py
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        nodes_to_visit = [root]
        node_vals = []
        while nodes_to_visit:
            next_nodes_to_visit = []
            node_vals_per_level = []
            for node in nodes_to_visit:
                node_vals_per_level.append(node.val)
                if node.left is not None:
                    next_nodes_to_visit.append(node.left)
                if node.right is not None:
                    next_nodes_to_visit.append(node.right)
            node_vals.append(node_vals_per_level)
            nodes_to_visit = next_nodes_to_visit
        return node_vals
```

## Step 2

- `「機械の使い方の説明です。まず、青いランプが5つついていることを確認してください。ついている場合、…使い方の説明…。ランプがついていなかった場合は、直ちに使用を中止して事務所に連絡してください。…機械の使い方の続き…。」 ... 「機械の使い方の説明です。まず、青いランプが5つついていることを確認してください。ランプがついていなかった場合は、直ちに使用を中止して事務所に連絡してください。…長い使い方の説明…。」のほうが素直ですよね。`
  - 同意。早期リターンすることで読み手の working memory を減らすことができる。
  - https://discord.com/channels/1084280443945353267/1196472827457589338/1196473479256625233
- `nodes = nodes.flat_map { |node| [node&.left, node&.right] }.compact というようなのもあるでしょう。`
  - Python で同じことをするとしたら、`nodes = [child for node in nodes for child in (node.left, node.right) if child]` のような感じだろうか。可読性を無視して1行で無理に済まそうとしている感じがしてあまり好みではないが、選択肢として持っておいてもいいな。
  - https://github.com/akmhmgc/arai60/pull/22#discussion_r2353951272
- `全体的に、話し方の計算の精度が良すぎるので「くらいの桁」と思ってください。「東京駅から新宿駅まで14分22.23秒かかります。」といわれるとなんかこの人勘違いしていないかと思いませんか。倍位は簡単にずれる計算をしていると思ってください。`
  - 確かに。見積もりでしかないので正確だと思いすぎないようにする。
  - https://github.com/huyfififi/coding-challenges/pull/31#discussion_r2286790129
- 特に再帰 DFS と反復 BFS の deque の解法で、みんなが試行錯誤している感じが伝わってくる。人それぞれ着地するところが少し違くて興味深いですね。

### 解法1: 再帰 DFS

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/32/changes の 2nd
  - https://github.com/nittoco/leetcode/pull/32/changes の 2nd
  - https://github.com/tokuhirat/LeetCode/pull/26/changes の 2nd
  - https://github.com/nanae772/leetcode-arai60/pull/26/changes の 2nd
- 考えたこと
  - ヘルパー関数で level を受け取るようにして1始まりにするか、depth を受け取るようにして0始まりにするか。
    - level を受け取るようにする方が好み。
    - 個人的には depth という言葉は問題文に存在せず、初期値として0を渡すための実装都合上のものという認識。
    - 似たような言葉が乱立すると可読性が落ちるので可能な限り数を絞りたい派。
  - `while level > len(node_vals)` か `if level > len(node_vals)` か。
    - while の方が好み。
    - if を使うと若干危なっかしい感じがする。探索していく時に1より大きい値を level に足すだけで IndexError になるため。
  - `while level > len(node_vals)` か `while len(node_vals) < level` か。
    - より主役を左辺に置きたい気持ち。level はヘルパー関数の引数なので主役寄りと判断。
  - level - 1 や level + 1 などの主役の調整は目が滑ると境界を見誤るので最小限にしたい。なので、`while level - 1 >= len(node_vals)` よりも `while level > len(node_vals)` の方が好み。
  - 想定ユースケース
    - skewed tree でない限りはメモリ効率が BFS よりもいい。なのである程度入力が complete binary tree であることが保証されており、設定されている RecursionLimit を超えない見立てがある場合はこの解法が適していそう
  - 計算量
    - 時間計算量: O(N)
      - step1 と同じ。
    - 空間計算量: O(N)
      - skewed tree で node がまっすぐ並んでいる場合が最悪ケース。
      - node_vals には最大 N 個の subarray が格納。
      - call stack が最大 N 個連なる。
      - call stack 1つあたりのオーバーヘッドを 300B とする。
        - `sys.getsizeof(sys._getframe())` は LeetCode 上だと 232B、手元だと 168B だった。やっぱりばらつきがあるなー。
      - 問題の制約的には、最大推定消費メモリは 2000 * (8 + 100) + 100 + 300 * 2000 = 800KB 程度。

```py
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        node_vals = []

        def traverse_node_vals(node: TreeNode | None, level) -> None:
            if node is None:
                return
            while level > len(node_vals):
                node_vals.append([])
            node_vals[level - 1].append(node.val)
            traverse_node_vals(node.left, level + 1)
            traverse_node_vals(node.right, level + 1)
        
        traverse_node_vals(root, 1)
        return node_vals
```

### 解法2: 反復 BFS で deque を使う

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/32/changes の 2nd
  - https://github.com/nittoco/leetcode/pull/32/changes の 1st
  - https://github.com/TORUS0818/leetcode/pull/28/changes#r1693269335
  - https://github.com/sakupan102/arai60-practice/pull/27/changes#r1597353212
  - https://github.com/ryosuketc/leetcode_arai60/pull/26/changes の 2nd
- 考えたこと
  - deque に node だけ保持するか、node と level の両方を保持するか。
    - 後者の方が可読性が高いと思うので好み。
    - 前者だと `range(len(nodes))` でループを回しているのに node の数がどんどん変わっていくのに若干驚きがあるため。
    - `range(len(nodes)) でループを回している中に nodes.popleft() や node.append() のように nodes に変更を与えるような処理があるのがわかりにくいと感じました`
      - 同意。
      - https://github.com/nittoco/leetcode/pull/32/changes#r1703441822
  - 想定ユースケース
    - 基本的には step1 と同じ。
    - 中間リストの入れ替えや多重ループを避け、単一の while ループで明示的に level を追跡したい場合に適している。
  - 計算量
    - 時間計算量: O(N)
      - step1, step2 の解法1と同じ。
    - 空間計算量: O(N)
      - nodes_and_levels には最大 N/2 個格納。
      - node_vals には最大 N 個の subarray が格納。
      - 問題の制約的には、最大推定消費メモリは 2000 * (8 * 2 + 100) / 2 + 2000 * (8 + 100) + 100 = 330KB 程度。

```py
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        nodes_and_levels = deque([(root, 1)])
        node_vals = []
        while nodes_and_levels:
            node, level = nodes_and_levels.popleft()
            if level > len(node_vals):
                node_vals.append([])
            node_vals[level - 1].append(node.val)
            for child in [node.left, node.right]:
                if child is None:
                    continue
                nodes_and_levels.append((child, level + 1))
        return node_vals
```

## Step 3

- 考えたこと
  - step1 で思い浮かばなかった、かつメモリ消費量が相対的に抑えられている、反復 BFS で deque を使う解法を練習する。
  - `for child in [node.left, node.right]` という書き方が好み。node.left と node.right に同じ処理をするときは割と使っている

```py
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        nodes_and_levels = deque([(root, 1)])
        node_vals = []
        while nodes_and_levels:
            node, level = nodes_and_levels.popleft()
            if level > len(node_vals):
                node_vals.append([])
            node_vals[level - 1].append(node.val)
            for child in [node.left, node.right]:
                if child is None:
                    continue
                nodes_and_levels.append((child, level + 1))
        return node_vals
```

## Step 4


