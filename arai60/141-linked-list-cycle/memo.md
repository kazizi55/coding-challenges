# 141. Linked List Cycle

## Link

https://leetcode.com/problems/linked-list-cycle/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

初回トライでは、走査した ListNode を dict に格納して ({ListNode: Bool} の形を想定)、 head.Next() を loop で回しながら dict と照合させるのがいいと思って進めていたが、そもそも Python でどうやって dict を作るのかや loop を回したらいいかがパッと出てこなく、調べていたら 5 分経ってしまっていた。本協会に入るまで Python に触ったことはほぼなく、入会後に LearnPython を数日でサッとこなした程度の習熟度だったのが要因と考えている。

2 回目のトライで 5 分以内に正解にできた。LeetCode の[こちらの回答](https://leetcode.com/problems/linked-list-cycle/solutions/3999014/99-68-two-pointer-hash-table/)を参考にした。Code Two-Pointer と Code Hash Table の 2 パターンがあったが、Code Two-Pointer は時間計算量こそ小さいが直感的でないと感じた (Floyd's Tortoise and Hare Algorithm に則ったものらしい。([記事](https://medium.com/@anudeepballa7/floyds-tortoise-and-hare-algorithm-6d439cdefde5)) ) ので、Code Hash Table の方を選択した。今回の目的は既出の ListNode と照らし合わせることが目的だったので元々考えていた dict は冗長だったことに気づけた。
また、解答例はなぜ list() ではなく set()なのかと思ったが、前者は ordered、後者は unordered な collection で前者の方がオーバーヘッドがあるためと理解した。現に、LeetCode で list()に書き換えて提出してみたら、時間計算量に大きな違いがあり、興味深かった。(set()が Runtime: 36ms に対して、list()が Runtime: 843ms)

https://docs.python.org/3/library/stdtypes.html#list
https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

### Step 2

#### General

- 単語から文字を削って変数名につけると、読み手にとって認知負荷が上がる場合がある
  - https://github.com/skypenguins/coding-practice/pull/9#discussion_r2174656692
  - 例えば Go だと scope によって変数名の長さも柔軟に変えていこうという思想が一定あるが、言語やチームによるものと理解した (そもそも読みやすさに絶対的な指標があるわけでもない)
    - https://google.github.io/styleguide/go/decisions.html#variable-names
- ボトルネックではないところを最適化しない
  - 「東京からニューヨークまで行くのに、飛行機の飛び方を最適化することは意味があっても、駅の降りる速さを最適化してもあまり意味がない」
  - https://github.com/t0hsumi/leetcode/pull/1#discussion_r1852645483

#### Tortoise and Hare Algorithm

- is not と!=の違いについて。自分も今回は is が妥当だと思ったので採用
  - https://github.com/ryosuketc/leetcode_arai60/pull/1#discussion_r2083814842
  - is をメモリアドレス比較にしているのは CPython の特徴。Python 公式 doc には id check と表記
    - CPython はこの辺り
      - https://github.com/python/cpython/blob/481d5b54556e97fed4cf1f48a2ccbc7b4f7aaa42/Objects/object.c#L3259-L3264
    - https://github.com/skypenguins/coding-practice/pull/9#discussion_r2175268156
- コメント集。このアルゴリズムは常識ではないが、有名ではあるとのこと
  - https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.2k4z0wt6ytf9

#### Set()

- current という名前は previous, next などと対比的に使わない場合はあまり推奨されていない。言われてみれば、current と見ると対比される何かを想起させるし、そうでなければ冗長に感じる。
  - https://github.com/Apo-Matchbox/LeetCode_Practice/pull/4#discussion_r2222205254
  - https://github.com/Mike0121/LeetCode/pull/7#discussion_r1587660995

### Step 3

set()を使う方法で実装。3 回実装してみて大きく内容は変わらなかったが、3 回目で問題文に出てくる語彙を使う方が読み手側にとってより直感的かなと思い、visited_nodes から reached_nodes という名前に変えてみた。

### Step 4

- None などの singleton との比較には is か is not を使うようにする
  - https://peps.python.org/pep-0008/#programming-recommendations
  - singleton はただ一つしか存在しない特別なオブジェクトなので、どの変数に None を代入しても常に同じメモリ上の None オブジェクトを指す
  - == は値が正しいかどうかを比較する (等価性 / equality)のに対し、is は同じメモリ上のオブジェクトかどうかを比較する (同一性 / identity)
- 条件文に括弧をつけるかどうかは統一する
  - PEP8 には記載がなかった。つけなくていいものを毎回つけるのは冗長に思うので、基本括弧をつけない方向で統一することにし、条件が複雑なときには括弧を使うようにする
- 時間計算量は入力データのサイズに対し、計算ステップ数がどのように変化するかを表す式。一方で実行時間は実行に掛かった実際の時間を表す。
  - https://discord.com/channels/1084280443945353267/1196498607977799853/1270740093220687903
- set()は hashable なので探索が短い step で済む
  - cpython だと hash 化して、9 個の連続したエントリを探索・その後はランダムに探索している
    - https://github.com/python/cpython/blob/481d5b54556e97fed4cf1f48a2ccbc7b4f7aaa42/Objects/setobject.c#L79-L121
- 平均計算量と最悪計算量
  - 平均計算量で見ると、list も set も要素の追加は O(1)になり、検索だと list が O(n)、set が O(1)になる
  - 一方で最悪検索量で見てみても、要素の追加は list でも set でも O(n)になり(配列のリサイズ・コピーが必要になる場合。ただし set は稀)、検索だと list も set も O(n)になる (set はハッシュ値の衝突が発生した場合。こちらも稀)。
- LeetCode の実行時間はブレがあるため、あまり信用しないほうがよい。計測したい場合は、手元で何度か実行して中央値を取るのがいい
- reach だと特定のゴールに到達と言うニュアンスになるので、reached_nodes というよりは visited_nodes の方が意味的にフィットする
  - https://dictionary.cambridge.org/us/dictionary/english/reach
