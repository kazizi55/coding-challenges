# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

最初は既存の List を変更する形で行なっていたが、重複している node を完全に排除するには新しい List を作る方がすぐできるのではと思い、実装してみたが、時間が足らず 5 分経過。
他の方の回答を見て、新しい List を head の一つ前から作る形で作成し、重複があったら削除していくと解けることがわかった。
一旦「重複を発見したら帰るな」で解いてみた。

- 時間計算量: O(N)
- 空間計算量: O(1)

#### 参考にした回答

https://github.com/olsen-blue/Arai60/pull/4
https://github.com/ryosuketc/leetcode_arai60/pull/4
https://discord.com/channels/1084280443945353267/1195700948786491403/1197102971977211966

### Step 2

まずは「重複したら引き継ぐ」パターンで解いてみた。dummy.next を return する前に previous.next = None と書くのが疑問だったが、最後が重複で終わった時 ([1,2,3,3]の場合など)でも previous.next = current としているため、previous の先には重複がまだ残っていることになるため、必要だと理解した。

- 時間計算量: O(N)
- 空間計算量: O(1)

「重複を発見したら帰るな」の方が処理がスッキリしているように感じたが、「重複したら引き継ぐ」の方が処理が追いやすかった。previous と current を 1 つずつ増加させているからだと思う。

また、step1 で dummy = ListNode(next=head)と定義していたのを、dummy.next = head と定義するようにしてみた。この方が previous.next や current.next と対比して表現できるので良いと感じた。個人的に、同じようなことを複数の対象(今回なら dummy、current、previous)に対して表現したいときはなるべく同じように書くのがいいと思う。

加えて、return する List に含めない値を value_to_remove と定義していたのを value_to_skip に変更した。問題文上は delete と表記されており、他の人の回答では value_to_remove のように と定義されているものもあったが、今回の処理の流れを見ると value_to_skip に値が一致している限り、current を skip しているので、value_to_skip が個人的には最も自然と判断した。

さらに、「重複したら引き継ぐ」パターンで duplicated な node を skip する処理を関数に切り出してみた。こうして関数に切り出すと、while が二重になるので、「重複したら引き継ぐ」のような書き方で「重複を発見したら帰るな」をしている感じになる。value_to_skip という変数をこの関数のローカルスコープに閉じ込めることができ、見通しが良くなるので個人的には好み。

#### 参考にした回答

https://github.com/hayashi-ay/leetcode/pull/23/files
https://discord.com/channels/1084280443945353267/1195700948786491403/1197102971977211966

### Step 3

1 回目は「重複したら引き継ぐ」、2 回目以降は、Step2 の「重複したら引き継ぐ」のような書き方の「重複を発見したら帰るな」で実装してみた。処理の追いやすさや見通しの良さ的にこの 2 回目以降の書き方が一番しっくりきた。

思えば、Step1 の「重複を発見したら帰るな」は current.val != current.next.val という形で正常系を異常系みたいな形で早期 continue で処理していたからわかりづらかったかもしれない。最終的にしっくりきた書き方の方が読み手的にも処理の流れとして自然 (すなわち異常系を早期 continue で処理)なのかなと思う。が、[コードの整え方](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.9kpbwslvv3yv)にもあるように、異常系の方が処理が長くなりそうならむしろ異常系を後ろに持ってくることがよりわかりやすくなる場合もある。とはいえ、その場合もできるだけ関数に切り出して異常系 -> 正常系の流れは崩さないように実装したい。

### Step 4

以下、いただいたフィードバック:
