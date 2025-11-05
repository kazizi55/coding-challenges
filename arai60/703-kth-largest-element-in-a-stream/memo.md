# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

9 分ほどかかってしまったが、回答は見ずに Python でのインスタンス変数の扱い方や降順での sort 方法を調べながら回答した。LeetCode での実行時間はブレがあるとはいえ、LeetCode 上で実行に平均 2 秒以上かかっていた。

解いた後、ほぼ同じ解き方をしていた方を見つけた。

- add()の時間計算量: $O(m × n \log n)$
  - `add()` 呼出: m 回
  - `sorted()` は Timsort $O(n \log n)$
    - Timsort とはマージソートと挿入ソートを組み合わせたハイブリッドで安定なソートアルゴリズム
      - https://en.wikipedia.org/wiki/Timsort

> `add()` を呼び出すたびに毎回ソートし、 `nums` のリストを生成しているため、 $10^4$ 回呼び出すと実行時間 2000ms 超となっていると想像

$-10^4$ <= nums[i] <= $10^4$ という制約があったことを見落としていた。確かに毎回ソートしてリスト生成をしていたら時間がかかるのも自明と言える。

#### 参考

- https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
- https://docs.python.org/3/library/functions.html#sorted
- https://github.com/skypenguins/coding-practice/pull/23/files

### Step 2

優先度キュー(各要素に優先度を付けて管理する特殊な抽象データ型(データ構造))をヒープを使って実装して解くのが一般的のようだった。優先度キューとヒープの関係は、「抽象データ型とその具体的な実装方法」という関係。ヒープは、優先度付きキューの操作を効率的に実行するための完全二分木のデータ構造。根に常に最小要素（または最大要素）が来ることが保証される。(なお、ヒープ領域の「ヒープ」とは何の関連もない。heap(山)の英単語のイメージを借用した偶然の一致とのこと。) Python ではヒープとして標準で heapq を使うことができる。heapq を使うにしても、init の時に list をどうヒープに変換するかいくつかやり方があるようだった。(for 文で回す、add()を使う、heapify を使うなど)

heapq について理解を深めるために CPython を参考に自前で実装してみる。CPython ではクラスを定義せず一連の関数として定義されているが、他の方がどういう意図で自前実装したのかも合わせて考えたいと思ったので、自分もクラスとして定義する。

#### heapq を自前実装

- X >> 1 は、「X のビット列を右に 1 ビット分ずらす」という意味。「X を 2 で割って整数部分だけ取る」のと同じ。ビット演算の方が早いらしいが、実際はそこまでむしろ//を使う方が早かった (少なくとも Python だと。//といえど、インタプリタが効率的な命令に置き換えていたりして、高速になっている)

```py
>>> print(timeit.timeit('x // 2', setup='x = 123456789', number=10000000))
0.151877292082645
>>> print(timeit.timeit('x >> 1', setup='x = 123456789', number=10000000))
0.19527620798908174
```

- ヒープはよく、こんな感じの木のような図で表される

```
      (0)        <-- 根っこ (一番上)
     /   \
    (1)   (2)      <-- 子供
   / \   / \
 (3)(4) (5)(6)    <-- 孫 (一番下)
```

- CPython の\_siftdown と\_siftup は逆じゃないかと思って調べたら、binary heap の wikipedia によると、`Note that this paper uses Floyd's original terminology "siftup" for what is now called sifting down.`ということで、元々 binary heap を扱う論文において何が up か down かが著者や論文によって異なっていることから発生したものの可能性が高い。個人的には sift up = 要素を正しい位置へ押し上げる、sift down = 要素を正しい位置へ沈めるという理解で調べた限りではそちらの方が多数派のようだったので、CPython の命名とはあえて逆の命名にした

- init では\_sift_down の代わりに\_sift_up を使うこともできるが、range(1, len(self.min_heap))で計算しないといけず、効率が悪いので CPython でも sift_down が使われている (CPython 上だと命名的には sift_up だが、、)

- k 番目に大きい値を返すのに最小ヒープを使って実装されているのはなんでだろうと思ったが、k 個の最小ヒープの一番最初の値 = k 番目に大きい値だからだった。最大ヒープの[-1]を取れば同じことできるのではとも思ったが、そもそも木構造なので、最大ヒープを配列として表すと[100, 60, 50, 10, 20]みたいな感じになる。10 と 20 の順序は保証されないので、最大ヒープの[-1]が最小値にはならない可能性がある。

#### heapq を使う version (init で add する)

- 時間計算量
  - init: $O(n \log k)$
  - add: $O(\log k)$
- 空間計算量
  - $O(k)$

#### heapq を使う version (init で heapify する)

- 時間計算量
  - init: $O(n)$
  - add:
    - 初回: $O(\log n + (n - k) \log n)$
      - add が最初に呼ばれたとき、top_k_nums のサイズは n なので、heappush に$O(\log n)$かかる
      - while ループはヒープサイズが k になるまで実行される。n > k の場合はループは(n + 1) - k 実行される
      - ループ内の heappop はヒープサイズが n から k + 1 のの間で行われるため、$O(\log n)$
    - 2 回目以降: $O(\log k)$
- 空間計算量
  - $O(k)$

初回の add が暗黙的に時間計算量が多くなるのが個人的には微妙。
が、https://github.com/fuga-98/arai60/pull/9/files/ff640247249d04747823950128d4255b03a12b57#r1966684301 でも言及されているように、init と add 以外のところで、万が一 k ＋ 2 個以上になってしまった場合でもこの解法のように add の中で while を使って pop しておけエラーにならず問題なく計算できるというのも納得。どこまで考慮するかという話と理解した。

#### insort を使う version

- 時間計算量
  - init: $O(n \log n)$
  - add: $O(n + c)$
    - c は add の総呼び出し回数
- 空間計算量
  - $O(n + c)$

計算量的には遅いが、Python ではネイティブコードとして動くので速い (先に挙げたビット演算と//の話にも通ずるところがある)

#### 参考

- https://en.wikipedia.org/wiki/Priority_queue
- https://www.reddit.com/r/leetcode/comments/1g5xs2d/%F0%9D%90%8C%F0%9D%90%B2_%F0%9D%90%87%F0%9D%90%9E%F0%9D%90%9A%F0%9D%90%A9%F0%9D%90%AC_%F0%9D%90%83%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%AD_%F0%9D%90%8B%F0%9D%90%A2%F0%9D%90%9E_%F0%9D%90%8E%F0%9D%90%AB_%F0%9D%90%87%F0%9D%90%A8%F0%9D%90%B0_%F0%9D%90%93%F0%9D%90%A8_%F0%9D%90%92%F0%9D%90%A8%F0%9D%90%A5%F0%9D%90%AF%F0%9D%90%9E_%F0%9D%90%80%F0%9D%90%A7%F0%9D%90%B2_%F0%9D%90%8F%F0%9D%90%AB%F0%9D%90%A2%F0%9D%90%A8%F0%9D%90%AB%F0%9D%90%A2%F0%9D%90%AD%F0%9D%90%B2/
- https://stackoverflow.com/questions/1699057/why-are-two-different-concepts-both-called-heap
- https://en.wikipedia.org/wiki/Binary_heap#:~:text=Note%20that%20this%20paper%20uses%20Floyd%27s%20original%20terminology%20%22siftup%22%20for%20what%20is%20now%20called%20sifting%20down.
- https://docs.python.org/3/library/heapq.html
- https://docs.python.org/3.13/library/heapq.html#heapq.heappushpop
- https://github.com/python/cpython/blob/main/Lib/heapq.py
- https://stackoverflow.com/questions/55375312/why-is-siftup-and-siftdown-just-the-opposite-in-python
- https://docs.python.org/3/library/bisect.html#bisect.insort_right
- https://github.com/skypenguins/coding-practice/pull/23/files
- https://github.com/Fuminiton/LeetCode/pull/8/files
- https://github.com/tokuhirat/LeetCode/pull/8/files
- https://github.com/hayashi-ay/leetcode/pull/54/files
- https://github.com/potrue/leetcode/pull/8/files
- https://github.com/fuga-98/arai60/pull/9/files

### Step 3

Step 2 で色々みてきた中で、heapq を使う version (init で add する)で解いた。計算量的にも効率的な上にシンプルに書けるためだ。なお、個人的には、k が負の値になったらどうするか、異常値が来たらどうするかというこの問題の範囲外の話はそれが想定された時にガード節を追加した対応すれば良いのではないか派だ。そういった時に柔軟な対応ができるように、なるべくシンプルに処理を書き切ることがメンテ性の高いコードを書くということなのかなと考えている。

### Step 4

以下、いただいたフィードバック:
