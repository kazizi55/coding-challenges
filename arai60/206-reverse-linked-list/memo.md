# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

配列の反転メソッドがわからず時間がかかったが、答えを見ずに 7 分で解いた。 141. Linked List Cycle と 20. Valid Parentheses を組み合わせたような問題だった。一つの関数としてまとめて書いてしまったが、関数に分けることもできそう。が、全体を通してシンプルな処理なので分けると逆に冗長になるかもなとも思う。

### Step 2

- 共通
  - `「直径 1 m 金属の輪っか」に 2 m の鎖が生えていてその先に「南京錠」がついているとすると、LinkedList とは、これを一直線に並べて、南京錠を隣の輪っかにつなげていったもの`
- RecursiveSolutionWithTail
  - `再帰というのは、リストの頭を担当する部下が、何かを下流にお願いして、仕事が返ってきて、自分も何かをすると、全体のリストが逆順になるというもの`
  - `依頼内容は、「自分よりも下流を逆順にして、頭と尻尾の輪っかを渡してください」になる`
  - `端っこの処理は次の担当がいなかったときに、次の担当に部下を一人用意して考えるか、あるいは自分で処理しちゃうかになる`
    - 元の list の端っこの時は if node.next is None の時で次の担当に部下を一人用意している
    - reversed_list の端っこの時は tail.next = node の時で自分で処理している
  - oda さんの例えもあり、処理が追いやすかった
  - node, \_ = reverse_list_helper(head)という形で top level で 2 つ目の返り値が無駄になってしまうのが気になった
- RecursiveSolutionWithoutTail
  - `よく見ると tail は node.next に相当する`
  - RecursiveSolutionWithTail の tail.next = node を node.next.next = node に変えただけ
  - 処理の無駄は無くなったが、コードを読み解くのにメタ的な視点を用いないといけなくなる (再帰で reverse_list_helper が最後に返してくるのは node.next になることを読みとる必要がある)ので、個人的には RecursiveSolutionWithTail の方が処理が追いやすかった
- RecursiveSolutionPassingRest
  - `考え方としては、5番目の人が6番目の人に、何を渡して、何を返してもらうか`
  - `頭から5番目までひっくり返した物を渡して、全部がひっくり返ったものを返してもらう。`
  - かなりシンプルに記述することができ、他の再帰と比べて特別な処理が必要なのは元の list の端っこに到達した時だけなので、処理の流れもわかりやすかった
- IterativeSolution
  - stack や再帰を使わないでも 1 loop するだけでも書くことができた
  - 処理が追いやすく、空間計算量も他の解法と比べて stack を積まないので少なくできる (O(n)が O(1)にできる)
  - 一方で問題が比較的シンプルだからこそ、IterativeSolution が読みやすいのだと思う。例えば区間指定の reverse list を実装するとなったら途端に処理が追いづらくなるだろう。この問題を解くことだけを考えれば空間計算量はこの解法がベストと言えるが、将来的な保守性などを考えたとしたら他の解法の方に軍配が上がるとも言える

#### 参考にした回答

- 共通
  - https://discord.com/channels/1084280443945353267/1231966485610758196/1239417493211320382
- RecursiveSolutionWithTail
  - https://discord.com/channels/1084280443945353267/1231966485610758196/1239417493211320382
  - https://github.com/TORUS0818/leetcode/pull/9/files#r1598170316
- RecursiveSolutionWithoutTail
  - https://github.com/goto-untrapped/Arai60/pull/27#discussion_r1641596128
- RecursiveSolutionPassingRest
  - https://github.com/goto-untrapped/Arai60/pull/27#discussion_r1641789968
- IterativeSolution
  - https://github.com/potrue/leetcode/pull/7/files#diff-e89fbdab352f3f200bf092970a6bf3570b455964a1b6a81c7060abf5a41101c2R70-R82

### Step 3

RecursiveSolutionWithTail を 2 回、RecursiveSolutionPassingRest を 1 回解いた。空間計算量などの効率性よりも読みやすさや保守性の高さなどを考慮してそれらを書くことを選択した。RecursiveSolutionWithTail の方が引き継ぎの例えが頭に残っており、スムーズに書けた。

### Step 4

以下、いただいたフィードバック:
