# 373. Find K Pairs with Smallest Sums

## Link

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- 2つの昇順で並んだ配列から、もっとも小さい合計になるペアを配列として k 個含めて返すというもの。
- 片方が1つ目から、もう片方が2つ目からになっていたらダブりも OK。
- Kth Largest Element in a Stream や Top K Frequent Elements のように、入力の配列を見ながら、k 個の priority queue を更新していく形で解けそう。
- うーん、example 2の output の[1,1]と[1,1]のように、同じ sum で数字の組み合わせも同じだけど違う index だから許容するみたいなことも考えないといけないのか。
- 15分以内に解けず。解いたのが半年以上前なので忘れているな、、

### 自力解法 (動かない)

- 途中まで。
- nums1 とnums2 の length はそれぞれ10^5まで大きくなりうるので、10^10のオーダーになることを考えると二重ループは避けたいが、パッと思い浮かばなかった、、

```
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sum_to_pair_and_frequency = defaultdict((int, int, int))
        for num1 in nums1:
            for num2 in nums2:
```

## Step 2

- 概観していて、記述量がどうしても多くなる問題だからこそ、関数に適宜切り分け、わかりやすい変数名をつけるべきというコメントを多く見かけた。
- `意図と操作の距離が遠い`。全体を理解して初めて意味がわかるようなものは初めてみる人にはわかりにくい (e.g., `「東京から大阪へ移動する手段に乗る」` vs `「東京から東海道新幹線に乗る」`)。変数名の付け方や関数に適宜切り分けることによって局所的でも意味がわかるように改善することができる。
  - https://github.com/TORUS0818/leetcode/pull/12#discussion_r1698018634
- 自然言語で他の人に何かを説明するときをイメージしてコードを書くと伝わりやすくなる。
  - `大きな目的や全体像は伝えて、それから個々の部分は局所的に分かるようにしますよね。これを足がかりに追加情報を小出しにしていって全体像を伝えます。`
  - `最終的には各部分の操作と全体の意図が噛み合った状態に見えるようになると、理解したと感じますね。`
  - https://github.com/TORUS0818/leetcode/pull/12#discussion_r1703339056
- なるほど、nums1 と nums2 を (x, y) という二次元 grid として捉えることができるのか。(と思ったら半年前の自分も同じことを書いていた。記憶の定着させるためにもっとイメージで覚えないといけないのだなと反省。)

### 解法1: 関数切り出し + set() を使用

- num1 と num2 の index の組み合わせを2次元の表として捉えて、それぞれの値は nums1[i] + nums2[j] にする。答えの配列の要素数が k 個になるまで、min-heap に (nums1[i] + nums2[j], i, j) を追加していき、while ループで1周するたびに、答えの配列に要素数を追加していく、という解法。
- (x - 1, y) in added and (x, y - 1) in added は redundancy guard。add_to_candidates_if_necessary(i + 1, j) と add_to_candidates_if_necessary(i, j + 1) で同じ (x, y) の組み合わせになった時にダブりが起きないようにしている。
- 処理ごとで関数に分けると、明確に認知負荷が下がる感じがする。局所的に意味がわかるようになるからだろう。
- ちなみに visited をただの list にすると TLE になる。そんなに効率性に差があるのかと改めて実感。
- Time Complexity: O(k log k), Space Complexity: O(k)

```py
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = [ (nums1[0] + nums2[0], 0, 0) ]
        visited = set()
        def is_necessary_to_add(x: int, y: int) -> Boolean:
            if x >= len(nums1) or y >= len(nums2):
                return False
            if x == 0 or y == 0:
                return True
            return (x - 1, y) in visited and (x, y - 1) in visited

        def add_to_candidates_if_necessary(x: int, y: int) -> None:
            if is_necessary_to_add(x, y):
                heapq.heappush(candidates, (nums1[x] + nums2[y], x, y))

        pairs = []
        while len(pairs) < k:
            _, i, j = heapq.heappop(candidates)
            pairs.append([nums1[i], nums2[j]])
            visited.add((i, j))
            add_to_candidates_if_necessary(i + 1, j)
            add_to_candidates_if_necessary(i, j + 1)
        return pairs
```

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/66 の　4th
- https://github.com/olsen-blue/Arai60/pull/10/changes

### 解法2: 関数切り出し + set() を使用

- 2次元 grid を左上から塗りつぶしていく感じで、while ループ一周ごとに最小合計を min-heap から pop して答えに加えつつ、下に1つ進み、右に一つ進むという解法。
- 解法1が1マスにつき右と下にとにかく進んで条件合致しなかったら skip みたいなのをやっているのに対し、解法2は律儀に左上からなぞっていく感じ。無駄が少なくて好みだなー。
- が、左上から、一番左の列を起点に探索していくイメージが初見だとつきづらそうとも感じた。その点、解法1は関数で区切ることで局所的にわかるようにしているので分かりやすそう。一方で解法2で関数に区切るのはこれはこれで処理がまとまっていて見やすい説もあるので捨てがたい。どっちも良し悪しがあるなー。
- Time Complexity: O(k log k), Space Complexity: O(k)

```py
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = [ (nums1[0] + nums2[0], 0, 0) ]
        pairs = []

        while len(pairs) < k:
            _, index1, index2 = heapq.heappop(candidates)
            pairs.append([nums1[index1], nums2[index2]])
            if index2 == 0 and index1 + 1 < len(nums1):
                heapq.heappush(candidates, (nums1[index1 + 1] + nums2[index2], index1 + 1, index2))
            if index2 + 1 < len(nums2):
                heapq.heappush(candidates, (nums1[index1] + nums2[index2 + 1], index1, index2 + 1))
        return pairs
```

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/66 の　5th

## Step 3

- 解法1で解いた。記述量は多いが、関数で分けていたり関数名や変数名で可読性を上げている点が好みだったため。
- 記述量は多いが、関数ごとで処理を見直すことができるので、3回連続で書いていても不思議と書き忘れやロジック不備が起きづらかったように思える。

```py
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = [ (nums1[0] + nums2[0], 0, 0) ]
        visited = set()
        def is_necessary_to_add(x: int, y: int) -> Boolean:
            if x >= len(nums1) or y >= len(nums2):
                return False
            if x == 0 or y == 0:
                return True
            return (x - 1, y) in visited and (x, y - 1) in visited

        def add_to_candidates_if_necessary(x: int, y: int) -> None:
            if is_necessary_to_add(x, y):
                heapq.heappush(candidates, (nums1[x] + nums2[y], x, y))

        pairs = []
        while len(pairs) < k:
            _, i, j = heapq.heappop(candidates)
            visited.add((i, j))
            pairs.append([nums1[i], nums2[j]])
            add_to_candidates_if_necessary(i + 1, j)
            add_to_candidates_if_necessary(i, j + 1)
        return pairs
```

## Step 4


