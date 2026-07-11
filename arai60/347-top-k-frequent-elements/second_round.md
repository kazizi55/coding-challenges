# 347. Top K Frequent Elements

## Link

https://leetcode.com/problems/top-k-frequent-elements/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- 最頻値を上から順に k 個返すというもの
- Kth Largest Element in a Stream と同じような考え方を使って解けるか？
  - 要素数が k 個の min-heap を持っておく。内容は頻度を格納する。
  - とするとどうやって各数字を格納すれば良いだろう。dict 型？どうやって解いたんだっけな。
- うーん、一旦愚直に heapq は使わずに dict を使って解いてみる。

### 解法1

- 各数字と頻度の dict を作成し、その dict を頻度の降順で sort したのちに、上から k 個の keys の配列を返すもの。
- 時間計算量: O(n), 空間計算量: O(n)
- これはこれでスッキリしている気はするが、`その dict を頻度の降順で sort したのちに`の部分のコードがちょっと強引感があるなー。命名は最大限わかりやすくしたつもりだが、それでもワーっとやりたいことをその1行に凝縮している感じがあって、あんまり好きではない。
- 肝心の Heap を使う解法はパッと思い浮かばなかった。他の方の回答を見てみる。

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = {}
        for num in nums:
            if num in num_to_frequency:
                num_to_frequency[num] += 1
                continue
            num_to_frequency[num] = 1
        num_to_frequency_ordered_by_desc = dict(sorted(num_to_frequency.items(), key=lambda item: item[1], reverse=True))
        return list(num_to_frequency_ordered_by_desc)[:k]
```

## Step 2

- [典型コメント](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0)を概観していると、この問題ではおおよそ以下の種類の解法が頭に浮かぶことが求められているのではという感想を持った。特に[このメッセージ](https://discord.com/channels/1084280443945353267/1183683738635346001/1185972070165782688)を見て思った。
  - priority queue
  - quick select
  - 単純に sort する (step 1で自分が使用)

### 解法1: Priority Queue

- Counter を使う方法でもいろんな解き方があるようだった。どこまで自前実装したいかによってバリデーションがあるように見える。
- Counter は dict の subclass なのかー。
  - iterable でも mapping でも keyword args でも渡して初期化できる。
  - 存在しない key で参照すると、0が返るのか。
  - https://docs.python.org/3/library/collections.html#collections.Counter

#### most_common を使う

- かなり楽に書けるが、もはや内部ロジックを全く知らないで書けてしまう。
- 内部ロジック的には、n が渡されなかったら、最頻値順に降順で sort、渡されていたら heapq.nlargest を使うという流れ。
  - https://github.com/python/cpython/blob/d610d821fd210dce63a1132c274ffdf8acc510bc/Lib/collections/__init__.py#L619

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [ num for num, _ in Counter(nums).most_common(k) ]
```

#### heapq.nlargest を使う

- `len(counter) == k` の guard を設けることで余分な heapq.nlargest の呼び出しを避ける。
- lambda: x: x[1] は itemgetter(1) と書き換えられる。
  - https://discord.com/channels/1084280443945353267/1337642831824814192/1371893051823358046
- source code に`Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]` と書かれていたので、あえて heapq.nlargest を使う意義はなんだろうと思ったが、空間計算量が O(n) -> O(k) ([このコード](https://github.com/python/cpython/blob/3.14/Lib/heapq.py#L579)あたりや heapify()のおかげ)、時間計算量が O(n log n) -> O(n log k) ([このコード](https://github.com/python/cpython/blob/3.14/Lib/heapq.py#L588)あたりのおかげ)という感じで最適化されるのが意義と理解。データ量が多くなった時に真価を発揮するのかも。

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        if len(counter) == k:
            return [ num for num, _ in counter.items() ] 
        top_k = heapq.nlargest(k, counter.items(), key=itemgetter(1))
        return [ num for num, _ in top_k ]
```

#### Counter ではなく defaultdict を使う

- 上の解法に比べるとだいぶ手触り感がある。Step 1 の単純にソートするのと流れはほぼ変わらない (min-heap を使っているかどうかという程度)

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        top_k_frequent = []
        for num, frequency in num_to_frequency.items():
            heapq.heappush(top_k_frequent, (frequency, num))
            if len(top_k_frequent) > k:
                heapq.heappop(top_k_frequent)
        return [ num for _, num in top_k_frequent ]
```

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/60/changes の 2nd と 4th
- 

### 解法2: Quick Select

- Quick Select とは？
  - Quick Sort を途中までやるアルゴリズム
  - そもそも Quick Sort とは？
    - 配列の中で Pivot となる要素を決めて(決め方は色々あるとのこと。最初の要素、最後の要素、ランダムなど)、Pivot よりも小さいものを左、そうでないものを右に移動。分かれた2つのサブ配列にも同じ探査をするのを再帰的に行っていって、最終的に要素の数が一つになるまで行う、というアルゴリズム。
    - https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/
  - Quick Select では再帰的探査を両方のサブ配列に行うのではなく、kth smallest (largest) element が含まれている方のみを見ていくというもの。おー、まさにこの問題のためのようなアルゴリズムだ。
    - https://www.geeksforgeeks.org/dsa/quickselect-algorithm/
- 最悪計算量
  - O(n^2)
  - sort されている配列で常に最初か最後の要素を pivot として選択し続けていった場合にこれになる。
- 平均計算量
  - O(n)
  - pivot が常に配列の真ん中あたりの要素である前提。
- 末尾再帰最適化
  - 関数の最後の処理として自分自身を呼び出す（末尾再帰）場合に、コンパイラや実行環境が新しいスタックフレームを積まずに、ループ処理（ジャンプ命令）に変換して実行する最適化手法。これをサポートしている言語は再帰の空間計算量を O(1) に抑えることができる。Python はサポートしていないので、再帰の代わりに while などを使って O(1) にすることができる。
  - https://github.com/tarinaihitori/leetcode/pull/9/changes#r1816991686
- ピボット選択
  - Quick Sort / Quick Select の性能はこの選択に強く依存
  - 先頭・末尾選択
    - 常に配列の先頭や末尾の要素を選ぶ
    - 配列がソート済みの場合に計算量が O(n^2) になるので実用上避けられる
  - ランダム選択
    - 配列からランダムに一つの要素を選ぶ
    - 配列の状態によらず時間計算量を平均値 (Quick Select なら O(n))に確率的にならせる
  - 3値の中央値
    - 先頭・中央・末尾の3つの要素の中から中央値を選ぶ
    - 実装がシンプルなのに計算量が O(n^2) になるのを効率的に回避できるのでライブラリで広く使われている
  - 中央値の中央値
    - 配列を5要素ずつのグループに分け、それぞれの中央値の中央値を取る
    - 決定論的に最悪時間計算量を O(n) に抑えられる
    - 定数項が大きいので、ランダム選択や3値の中央値の方が高速
- Merge Sort とは
  - 配列を均等に2つに分け続けて、分けられないところまで分割する
  - サブ配列を sort しながら merge していく
  - 1つの配列になるまで続ける
  - https://www.geeksforgeeks.org/dsa/merge-sort/
- Merge Sort とのプロコン
  - 最悪時間計算量
    - Quick Sort
      - O(n^2)
      - pivot 選択が偏った場合
    - Merge Sort
      - O(n log n)
      - 常に保証
  - 空間計算量
    - Quick Sort
      - O(log n)
      - in-place で sort 可能
    - Merge Sort
      - O(n)
      - マージ用の一時配列が必要
  - 安定性
    - Quick Sort
      - 不安定ソート
      - 要素を大きくジャンプさせてスワップするため、同値の要素の順序が崩れる可能性がある
    - Merge Sort
      - 安定ソート
      - 順序が維持される
  - キャッシュ効率
    - Quick Sort
      - 連続したメモリ領域にアクセスするので、キャッシュヒット率が高い
    - Merge Sort
      - 一時配列へのコピーや走査がが発生するため、オーバーヘッドがある
  - 外部ソート (メモリ上に一度に展開できない場合に外部ストレージを活用して行うソート)
    - Quick Sort
      - メモリ上に展開できない巨大なデータには不向き
    - Merge Sort
      - データを順番に読み込んでマージできるので適している
- quick_select や _partition の引数を全て frequency_to_num と表現しているが、Tuple の第二要素に参照することは一度もないので、参照元のように、array と表現するのもありなのかもしれない。一方で、ずっと frequency_to_num を参照し続けているのも事実で、どちらかというとそっちを強調して全ての箇所で frequency_to_num と書く方が好みかも。書くのが若干大変だが、、
- 流れはわかりやすいが、実装は重めという印象。特に境界値の判定が多いので間違えそうになる。右半開区間にもっと慣れるべきなのかもしれない。

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def quick_select(frequency_to_num: List[Tuple[int, int]], left: int, right: int, k: int) -> None:
            if left >= right:
                return
            pivot_index = _partition(frequency_to_num, left, right)
            if pivot_index == k:
                return
            if k < pivot_index:
                quick_select(frequency_to_num, left, pivot_index, k)
            else:
                quick_select(frequency_to_num, pivot_index + 1, right, k)
                

        def _partition(frequency_to_num: List[Tuple[int, int]], left: int, right: int) -> int:
            pivot_index = random.randrange(left, right)
            pivot = frequency_to_num[pivot_index]
            _swap(frequency_to_num, pivot_index, right - 1)
            store_index = left
            for i in range(left, right - 1):
                if frequency_to_num[i] > pivot:
                    _swap(frequency_to_num, i, store_index)
                    store_index += 1
            _swap(frequency_to_num, store_index, right - 1)
            return store_index

        def _swap(frequency_to_num: List[Tuple[int, int]], i: int, j: int) -> None:
            frequency_to_num[i], frequency_to_num[j] = frequency_to_num[j], frequency_to_num[i]

        num_to_frequency = defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        frequency_to_num = [ (frequency, num) for num, frequency in num_to_frequency.items() ]
        quick_select(frequency_to_num, 0, len(frequency_to_num), k)
        return [ num for frequency, num in frequency_to_num[:k] ]
```

#### 参考にした回答

- https://github.com/tokuhirat/LeetCode/pull/9/changes#r2074951611
- https://github.com/hayashi-ay/leetcode/pull/60/changes の 4th

## Step 3

- Counter ではなく defaultdict を使い、 heapq を使う形で解いた。
- 流れが直感的で追いやすく、記述量も少なく、また step 1 の sorted を使うよりも空間計算量が抑えられるため好み。

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        top_k_frequency_to_num = []
        for num, frequency in num_to_frequency.items():
            heapq.heappush(top_k_frequency_to_num, (frequency, num))
            if len(top_k_frequency_to_num) > k:
                heapq.heappop(top_k_frequency_to_num)
        return [ num for _, num in top_k_frequency_to_num ]
```

## Step 4

### 解法 1: Step 1 と同じ流れでタプルの num のみを返す

- Step 1と同じ流れだが、num_to_frequency.items() の返り値のタプルのうちの num をそのまま答えの配列に含める感じ。
- 流れがスッキリして分かりやすい。そもそも step 1でやっていたような、答えの配列を作るタイミングで dict に変換するのは冗長だなと気づいた。

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        num_and_frequency_ordered_by_desc = sorted(num_to_frequency.items(), key=itemgetter(1), reverse=True)
        return [ num for num, _ in num_and_frequency_ordered_by_desc[:k] ]
```