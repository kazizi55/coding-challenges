# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

#### Set()

時間計算量: O(N)
空間計算量: O(N)

141. Linked List Cycle とほとんど変わらなかった (変わったのは返り値が bool 値か node かという程度)ので、 答えを見ずに 2 分程度で解くことができた。

141 でいただいたフィードバックをそのままコードに落とし込むことができてご意見を血肉にできている感覚を得れた。!=と is not の違い、命名の仕方などだ。
https://github.com/kazizi55/coding-challenges/pull/1/files#diff-0ac89d0fb94529b2b9ec468c4157cfdfc6e0406d959283f2e8307878c7a1a213R59-R79

#### Hare and Tortoise

時間計算量: O(N)
空間計算量: O(1)

一方で、LeetCode に `Follow up: Can you solve it using O(1) (i.e. constant) memory?`とあったので、Hare and Tortoise を使って解き直してみたが、5 分以内に AC にできなかったので、答えを見て解いた。
最初の答え(141 と同様に fast と slow が同一になった時点で return する手法)はあくまでも合流点か開始点を return するものだったので合流点が return されたときに fail していた。

ntanaka1984 さんの図を見て、開始点から分岐点までの長さ == 合流点から分岐点までの長さということが明瞭になり、コードが腑に落ちた。
https://github.com/ntanaka1984/leetcode/pull/2#issuecomment-3106759861
oda さんの hare と tortoise を合流点から後ろ向きに歩かせてみる解説も、開始点から分岐点までの長さ == 合流点から分岐点が直感的にわかり、なるほどなと思った。
https://discord.com/channels/1084280443945353267/1246383603122966570/1252209488815984710

### Step 2

#### Set()

今回は自然に node と書いていたが、current_node にするのは previous や next などの変数が存在していて、current であることを強調したい時のみ使う。
https://github.com/skypenguins/coding-practice/pull/10/files#r2188608249
https://github.com/potrue/leetcode/pull/2/files#r2072453473

再帰を使って解くこともできる。
https://github.com/Fuminiton/LeetCode/pull/2#discussion_r1948034553

#### Hare and Tortoise

関数化する方法もある。以下のケースは衝突点を返す関数を作成している。fast、slow という概念を関数内に隠蔽できるので、開始点を特定するときのノイズを減らすことができる (開始点を探す時点では fast、slow という概念は不要)
https://github.com/hayashi-ay/leetcode/pull/18/files#diff-97a2b5510d65cd5c736cab9a3675eb2122bfe5e9ccbe491032aad6fee9d3f74dR133-R152

while True という形で無限ループを使うことで None を早期 return できる。
https://github.com/olsen-blue/Arai60/pull/2/files#diff-2d9cbcab205d34e01955561fc8d084614d1d817a33b81d59bdbf2096fb2bd565R149-R156

関数化しない場合、2 つ目の while で fast, slow を使い回すのではなくて、origin という新しい変数に代入することもできる。が、origin というと個人的に何かの起源を思い浮かべるのと、origin なのは最初だけでどんどん探査していくことから、finder を使うのが適切だと判断した。
https://github.com/olsen-blue/Arai60/pull/2/files#diff-2d9cbcab205d34e01955561fc8d084614d1d817a33b81d59bdbf2096fb2bd565R158-R163

### Step 3

#### Set()

平均 1 分で 3 回とも AC。
step2 で関数化して再起する方法もあることを知ったが、結局 step1 が一番直感的だと感じた。なぜなら Hare and Tortoise と違って処理が 1 段階のみで簡潔に記述できるからだ。(その証左として node や visited など変数名を簡潔にすることができる)
処理が簡潔なのに関数化をする必要はないという判断。

また、step1 では if node in visited の後に else 節を書いていたが、早期 return するので冗長だなと思い削除した。

#### Hare and Tortoise

平均 2 分で 3 回とも AC。
Set()と違い、処理が 2 段階あるので、1 つ目を関数化して slow や fast など、2 段階目の処理ではノイズになる変数を関数スコープの変数にした。

また、step2 では get_catchup_node という変数名にしていたが、取得するのではなく探索するので find_catchup_node の方が直感的だと思い、変更した。

Hare and Tortoise、勉強にはなるものの、Set()の方がすぐ書ける上に読みやすく、少なくとも時間計算量はほぼ変わらないので、業務で使うとしたら空間計算量の制約が余程厳しくない限りは Set()を使うと思う。

### Step 4

以下、いただいたフィードバック:
