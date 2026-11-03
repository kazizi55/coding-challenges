# 112. Path Sum

## Link

https://leetcode.com/problems/path-sum/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- root から leaf まで足していって、targetSum にあるかどうかを探索し、あったら True、なかったら False を返す問題
- BFS か DFS かで探索しつつ、leaf かつ 累積和が targetSum と一致していたら True を返すとすれば解けそう。
- queue なり stack に node と prefix_sum を積むのがいいかも
- 再帰か反復かで解ける。行きがけで完成させるか、帰りがけで完成させるかも選べる。

### 解法1: 反復 DFS

- 考えたこと
  - 一旦反復で解く。
  - node.left と node.right に対して同じような処理をするときは `for child in [node.left, node.right]` にしてまとめるのが好み。
  - 一旦 DFS にしてみた。queue に変えれば BFS になる。
  - 想定ユースケース
    - 空間計算量的に、DFS は O(height)、BFS は O(width) になるので、横に長い tree の場合 (完全木など)は DFS の方が適している。
  - 計算量
    - 時間計算量: O(N)
      - 最悪ケースは targetSum が node のどの合計とも一致しない場合。
      - 問題の最大入力を考慮すると、最大 5000 / 10^7 = 0.5ms 程度かかる見込み。
    - 空間計算量: O(N)
      - 最悪ケースは、ほぼ skewed tree だが child が2つ必ずある場合。N/2 個になる。(図を参照)
      - 問題の最大入力を考慮すると、最大 5000 / 2 * 74 = 185KB 程度になる見込み。
        - nodes_and_prefix_sums の tuple 1つあたり、50 + 8 * 2 = 66B とする。自身への pointer 分も考慮し、74B。

```py
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        nodes_and_prefix_sums = [(root, root.val)]
        while nodes_and_prefix_sums:
            node, prefix_sum = nodes_and_prefix_sums.pop()
            if node.left is None and node.right is None:
                if prefix_sum != targetSum:
                    continue
                return True
            for child in [node.left, node.right]:
                if child is None:
                    continue
                nodes_and_prefix_sums.append((child, prefix_sum + child.val))
        return False
```

```
    (Root)
   /      \
[L1]      (R1)
         /    \
      [L2]    (R2)
             /    \
          [L3]    (R3)
                 /    \
              [L4]    (R4)
                      ...
                     /    \
                 [Lk]     (Rk)
```

### 解法2: 再帰 DFS

- 考えたこと
  - 再帰でも解く。
  - ヘルパー関数を使わずに再帰で解く場合は、targetSum から node.val を引いていって0になった時かつ node が leaf の時に True を返すようにする必要がある。
  - 問題の制約上は node の最大数が5000になっているので、Python のデフォルトの recursion limit (1000)は容易に越してしまうので注意が必要
  - 確か LeetCode だと上限がかなり高めに設定されていた気がする
    - `print(sys.getrecursionlimit())` を問題で実行したら550000だった。かなり高いなあ。ここまでの上限が設定されているのは特殊だと捉えるべきだと思う。
  - 想定ユースケース
    - recursion limit を考えなくていい場合なので、入力の閾値が明確に決まっている場合やある程度 skewed tree でないことが保証されている場合に適していそう
  - 計算量
    - 時間計算量: O(N)
      - 解法1と同じ。
    - 空間計算量: O(N)
      - skewed tree の場合が最悪ケース。再帰の深さが最大 N になる。
      - 問題の最大入力を考慮すると、最大 5000 * 200B = 1MB 程度になる見込み。
        - call stack frame 1つあたり 200B とする。ローカル変数などの overhead や allocator とかも含めると実際はもう少し大きいかもしれない。

```py
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        rest = targetSum - root.val
        if root.left is None and root.right is None and rest == 0:
            return True
        return self.hasPathSum(root.left, rest) or self.hasPathSum(root.right, rest)
```

## Step 2

- `これ、引き算先にしちゃって、 ... のほうが素直ではないでしょうか。`
  - 同意。step1 の解法2でこれで解いていた。素直という表現、いいな。
  - https://github.com/SuperHotDogCat/coding-interview/pull/37#discussion_r1665891252
- `あ、でも、targetSum っていうのは、目標の数値という意味がありそうなので、これは変数ではなく、固定値であって欲しいという気持ちが湧いてきた`
  - これは同意。leaf node に向かって合計の val を積み上げていって、targetSum と一致するかを見る流れの方がやりたいこと的に自然に思う。
  - https://github.com/olsen-blue/Arai60/pull/25/changes#diff-b4b5f9e02019847ced4bcdf2e9c797122a98fdca815f1def17c05e23c0d8f21aR28
- leaf node まで来たら `return sum == targetSum` するのが自然に思えてきた。条件文にそれを入れて True を返すのは冗長に思える。
- `sys.setrecursionlimit()` は関数スコープではなくグローバルな変更になる。取扱注意。
  - https://github.com/olsen-blue/Arai60/pull/25/changes#r2000464040
- 反復の解法の場合、累積和に現在の node.val を足してから list に積むか、取り出してから足すかの2パターンある。取り出して足すパターンだと、取り出した値を何か別のことに使う感じがして冗長なので、前者が好み。
  - https://github.com/hayashi-ay/leetcode/pull/30/changes#diff-b4b5f9e02019847ced4bcdf2e9c797122a98fdca815f1def17c05e23c0d8f21aR79-R98
- `更新していく変数は多いですから明示する必要なければわざわざ言わないことの方が多いですね`
  - 同意。文脈で分かるのなら明示する必要はない。
  - https://github.com/quinn-sasha/leetcode/pull/24/changes#r2172989694
- `node.left is None and node.right is None` を is_leaf 関数として切り出している解法を何個か見つけたが、それと node.right is not None とかの条件を並べた時に対称性があまり見えなくなるので切り出さない方が好み。`node.left is None and node.right is None`を何個も書かないといけない状況だったら関数に切り出すかもしれない。
  - https://github.com/nanae772/leetcode-arai60/pull/25/changes#diff-73d2c961668b0fe9bdd4ed93d8145f4c3c5277b9ece69d0e206e62a46add847dR2-R4

### 解法1: 再帰 DFS (ヘルパー関数あり)

- 参考にした回答
  - https://github.com/olsen-blue/Arai60/pull/25/changes の 1st
  - https://github.com/quinn-sasha/leetcode/pull/24/changes の 3rd
  - https://github.com/nanae772/leetcode-arai60/pull/25/changes の 1st
- 考えたこと
  - nonlocal を使うか使わないかの選択肢がある。上書きの可能性を関数外でも考慮しなければならなくなり、可読性が落ちるので、使わないで解けるなら使わないでいきたい派。
  - traverse_path_sum の local name の total を上書きしてしまっているが、ヘルパー関数なので呼び出し側の都合は考慮しなくていいこと、current_total などの別の変数を定義するとかえって可読性が落ちる (わざわざ2つ定義する意味はない、current と聞くと previous を想像するが引数名を previous とするのも違和感があるなど) ので、今回は良しとした。
  - 想定ユースケース
    - step1 の解法2と同様。
  - 計算量
    - 時間計算量: O(N)
      - step1 と同じ。
    - 空間計算量: O(N)
      - step1 の解法2と同じ。

```py
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def traverse_path_sum(node: TreeNode | None, total: int) -> bool:
            if node is None:
                return False
            total += node.val
            if node.left is None and node.right is None:
                return targetSum == total
            return traverse_path_sum(node.left, total) or traverse_path_sum(node.right, total)

        return traverse_path_sum(root, 0)
```

## Step 3

- 考えたこと
  - 再帰の解法を思いつくのが苦手なので定着させる。
  - 再帰の解法だと、total を足し合わせていって targetSum と一致するかを見る方が自然に思えるので、それが実現できる helper 関数ありの解法を選択。

```py
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def traverse_has_path_sum(node: TreeNode | None, total: int) -> bool:
            if node is None:
                return False
            total += node.val
            if node.left is None and node.right is None:
                return total == targetSum
            return traverse_has_path_sum(node.left, total) or traverse_has_path_sum(node.right, total)
        
        return traverse_has_path_sum(root, 0)
```

## Step 4


