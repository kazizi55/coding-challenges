# 349. Intersection of Two Arrays

## Link

https://leetcode.com/problems/intersection-of-two-arrays/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- これは確か解法がたくさんある問題だったはず。なるべく多く解法を思いつきたいな。

### 解法1: set の & を使う

- まずは nums1 と nums2 をそれぞれ set 化してその intersection を返すのができる。
- https://docs.python.org/3/tutorial/datastructures.html#sets
  - union とかもできる。覚えておく。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)
```

### 解法2: set の intersection を使う

- set の intersection() を使って書くこともできる。かなりシンプルにかける。
  - https://docs.python.org/3/library/stdtypes.html#set.intersection
- この内部実装をどれくらい自分で実装するかで解法にバリエーションが生まれるのでは、という所感。
  - https://github.com/kazizi55/coding-challenges/pull/9/changes のような感じ。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))
```

### 解法3: hashmap を使う

- この問題は hashmap に分類されているので、hashmap を使っても解けるはず。チャレンジしてみる。
- num を key、頻度を value にとり、頻度が2以上のものの key を返すみたいな感じだろうか。
- 一旦実装。Heap 系の解法をほぼそのまま転用して解くことができた。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_frequency = defaultdict(int)
        for num1 in nums1:
            num_to_frequency[num1] = 1
        for num2 in nums2:
            if not num2 in num_to_frequency:
                continue
            num_to_frequency[num2] += 1
        return [ num for num, frequency in num_to_frequency.items() if frequency > 1 ]
```

## Step 2

- `in list は、list を全部確認するので、O(n) の時間がかかります。`
  - 言われてみたら確かに。それなりに高価であることを認識しておく。
  - https://discord.com/channels/1084280443945353267/1201211204547383386/1208701087264280596
  - 一方、`in dict` や `in set` は内部的にハッシュテーブルが使われているため、平均 O(1) の時間で済む。
    - https://wiki.python.org/moin/TimeComplexity
- NaN == NaN は False になる
  - NaN は、0/0,∞ - ∞, √-1 など 色んな計算不可能・未定義なあらゆる結果の placeholder になっている。それらが equal であることを認めてしまうと数学的に正しくないので False になっている。
  - https://en.wikipedia.org/wiki/NaN#Comparison_with_NaN

```py
>>> nan = float("nan")
>>> nan == nan
False
```

### 解法1: Merge Sort の build up 的実装

- `メモリーに乗らないくらい巨大でも、ソートされているならば、両方から取り出して、小さい方を進めていき、同じだったらそれを確保するということです。`
  - 両方の入力がとても巨大でともに sort 済みの場合に有用な解法。
  - https://github.com/Hurukawa2121/leetcode/pull/13#discussion_r1894836342
- nums1 と nums2 を降順 sort した上で、 index をそれぞれ持っておいて、同じ数字が連続しているか一方よりも数字が小さい場合は片方の index を1つ進める、そうでない場合は intersection とみなして両方の index を足すというのを繰り返す解法。
- なんでこれが Merge Sort の変形と言えるのかピンとこなかったが、分割して sort した sub array を build up していく時と全く同じことをしているからかー。Merge Sort の復習にもなる。
- sort() か sorted() を使うか迷ったが、個人的には前者がいいかなと思った。入力が sort されているとしたらという前提で書いているので、そのシミュレーションと考えると sort() を使って意図的に入力を破壊するのも個人的には許容。
- 計算量 (M = len(nums1), N = len(nums2))
  - Time Complexity: O(M log M + N log N)
    - bottleneck は sort 部分。
      - Python の sort は Timsort が使われているのか。これも Merge Sort に似たロジックが用いられているらしい。めちゃ活用されてるな、Merge Sort。
        - https://www.geeksforgeeks.org/dsa/timsort/
    - sort を含めないなら、O(M + N)
  - Space Complexity: O(M + N)
    - sort を含めないなら、O(min(M, N))。output の array 分の space。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        intersection = []
        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if len(intersection) > 0:
                if intersection[-1] == nums1[index1]:
                    index1 += 1
                    continue
                if intersection[-1] == nums2[index2]:
                    index2 += 1
                    continue
            if nums1[index1] < nums2[index2]:
                index1 += 1
                continue
            if nums1[index1] > nums2[index2]:
                index2 += 1
                continue
            intersection.append(nums1[index1])
            index1 += 1
            index2 += 1
        return intersection
```

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/21/changes の 4th

### 解法2: Binary Search を用いた実装

- `たとえば、追加質問で考えられるのは、「片方がとても大きくて、片方がとても小さいときには、大きい方を set にするのは大変じゃないでしょうか、特に大きいほうが sort 済みのときにはどうしますか。」とかです。`
  - この観点はなかった。確かにその条件だと set() を使うのは非効率に思える。
  - https://github.com/katataku/leetcode/pull/12#discussion_r1893968021
- 計算量 (M = len(nums1), N = len(nums2))
  - Time Complexity: O(M log M + N log M)
    - sort を含めないなら、O(N log M)
  - Space Complexity: O(min(M, N) + M)
    - sort を含めないなら、O(min(M, N))。output の array 分の space。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        intersections = set()
        for num in nums2:
            if num in intersections:
                continue
            left = 0
            right = len(nums1)
            while left < right:
                middle = (left + right) // 2
                if nums1[middle] == num:
                    intersections.add(num)
                    break
                if nums1[middle] < num:
                    left = middle + 1
                else:
                    right = middle
        return list(intersections)
```

#### 参考にした回答

- https://github.com/katataku/leetcode/pull/12#discussion_r1894597448
  - in list は O(N) の時間がかかってしまうので、set() を使って O(1) とした
  - 開区間で書かれているのは、index に+1せずに境界を意識しないように済むためと理解。が、個人的には bisect_left に合わせて右半開区間で書く方が好み
    - https://docs.python.org/3/library/bisect.html#bisect.bisect_left
- https://github.com/olsen-blue/Arai60/pull/13/changes の 4th

### 解法3: set() を使わず Direct Address Table を使う

- `私はStep1で nums1 を舐めつつ、辞書を構築しており、このとき1以上の頻度のカウントを与えることが意味がなくてモヤモヤしてました`
  - これは確かに。
  - さらに自分の step 1 は num_to_frequency というのも nums1 の num を何個重複があっても1としか数えないので変数として厳密にいうと間違っている。nums1 で出てきた値かというのを bool 値でもつのがスッキリしていて分かりやすいかも。
  - https://github.com/quinn-sasha/leetcode/pull/13/changes#r1966664625
- Direct Address Table とはインデックス番号そのものを数字として扱う手法のこと。
  - https://www.geeksforgeeks.org/dsa/direct-address-table/
- その table に nums1 の値が見つかったら True と書き込み、nums2 でも見つかったら答えの配列に追加していくという解法。
- LeetCode の制約に忠実に沿うならこの解法が一番好み。だが、seen_in_nums1 の要素数が固定されていたりするなど、よく言えば必要最小限、悪く言えば小回りが効かない感もあるので、場合による。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen_in_nums1 = [False] * 1001
        for num1 in nums1:
            seen_in_nums1[num1] = True
        intersections = []
        for num2 in nums2:
            if not seen_in_nums1[num2]:
                continue
            intersections.append(num2)
            seen_in_nums1[num2] = False
        return intersections
```

#### 参考にした回答

- https://github.com/quinn-sasha/leetcode/pull/13/changes の 3rd

## Step 3

- 入力がかなり大きいとか sort されているなどの条件がなく、LeetCode の制約に則るなら、Direct Access Table を使う解法が素直である程度自前実装もする上に必要最小限感があるので好み。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen_in_nums1 = [False] * 1001
        for num1 in nums1:
            seen_in_nums1[num1] = True
        intersections = []
        for num2 in nums2:
            if not seen_in_nums1[num2]:
                continue
            intersections.append(num2)
            seen_in_nums1[num2] = False
        return intersections
```

## Step 4

### 解法1: seen_in_nums1 の length を nums1 と nums2 の max の値にする

- step3 よりも LeetCode の制約を超えて対応できるのでそれが良さではある。
- が、seen_in_nums1 の個数がなぜ max(nums2) も考慮しなければならないのかが後続処理を見ないとわからないのが若干可読性が悪いかも。

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen_in_nums1 = [False] * (
            max(
                max(nums1),
                max(nums2)
            )+1
        )
        for num1 in nums1:
            seen_in_nums1[num1] = True
        intersection = []
        for num2 in nums2:
            if not seen_in_nums1[num2]:
                continue
            intersection.append(num2)
            seen_in_nums1[num2] = False
        return intersection
```

### 解法2: 片方だけ Set にする

- step1 の解法2の intersection() を自前実装した version

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums1 = set(nums1)
        intersection = []
        for num2 in nums2:
            if not num2 in unique_nums1:
                continue
            intersection.append(num2)
            unique_nums1.remove(num2)
        return intersection
```