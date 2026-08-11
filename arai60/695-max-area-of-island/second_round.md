# 695. Max Area of Island

## Link

https://leetcode.com/problems/max-area-of-island/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1

- 考えたこと
  - 前問の 200. Number of Islands と同じ要領で解けそう。
  - height と width で二重ループを回しながら、さらに BFS か DFS で4方向が島かどうかを判定し、島だったら visited を true にして最大面積を足していく。queue か stack が空になったら最後に全体で持っている最大面積と比較して大きい方を保持する、というようにしたら解けそう。
  - 一旦 DFS で解いてみるか。
  - うーん、解けないな。height と width の二重ループの一時変数として current_max_area_islands を置いているが、離れ小島みたいなものも同じ面積としてカウントしているからだろう。
  - 時間切れになったので一旦 gemini に聞いてみる

```py
# Wrong Answer　11 / 728 testcases passed
class Solution:
    WATER = "0"
    LAND = "1"
    DIRECTIONS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(height)]
        max_area_islands = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == self.WATER or visited[row][col]:
                    continue
                lands_to_visit = [(row, col)]
                current_max_area_islands = 0
                while lands_to_visit:
                    current_row, current_col = lands_to_visit.pop()
                    if not (0 <= current_row < height and 0 <= current_col < width):
                        continue
                    if grid[current_row][current_col] == self.WATER or visited[current_row][current_col]:
                        continue
                    visited[current_row][current_col] = True
                    current_max_area_islands += 1
                    for delta_row, delta_col in self.DIRECTIONS:
                        lands_to_visit.append((delta_row + current_row, delta_col + current_col))
                max_area_islands = max(max_area_islands, current_max_area_islands)
        return max_area_islands
```
- 考えたこと
  - 前問と違って、LAND と WATER が str ではなく int になっていたのに前問に引っ張られてそのまま str で書いてしまっていた、、変えたら AC になった。反省、、
    - 中途半端に case が通るのが余計ややこしい、、
  - 時間がなくて関数に切り出せなかったので、これを機に切り出して整理してみる。
    - 前問同様、訪れるべき LAND かどうかを判定する関数と DFS を行う関数を切り出す
  - また、変数名ももっとやりようがあるので変える。
    - `_islands` は自明なので省いても良さそう。self-explanatory な変数名はいいが、自明なのに長すぎると逆にそこまで長ったらしく説明したい理由とは？と勘ぐりを入れてしまいたくなるだろう。実際の会話と同じだ。
      - `「この前、池袋のカフェに行ってきたの。池袋のカフェのドリンクがすごい美味しかったわ。池袋のカフェがとても寒かったから、池袋のカフェのドリンクにはアイスは入れないように池袋のカフェの店員さんに伝えたわ。」`
      - `「この前、池袋のカフェに行ってきたの。ドリンクがすごい美味しかったわ。とても寒かったから、ドリンクにはアイスを入れないように店員さんに伝えたわ。」`
  - 想定ユースケース
    - 入力のバリデーションは入れていないので、ユーザー入力は前提としない。
    - 社内利用前提の必要に応じて走らせる分析プログラムとかだろうか。
      - と考えると、結構ユースケースの幅は狭いな。
      - バッチ処理として走らせるとしても、入力が m, n ともに 10000 個を超えてくると実行時間が10秒を超す。m が 1000 で固定の場合、ユーザー (n) が一人増えるごとに 0.1ms 遅くなる。時限爆弾感強め。
  - 計算量
    - 時間計算量: O(M * N)
      - Python で毎秒 10^7 steps 実行できると仮定すると、今回の最大実行時間は 50 * 50 / 10^7 = 0.00025s = 0.25ms
      - m, n の最大 len が小さいので、かなり実行時間が短い。
    - 空間計算量: O(M * N)
      - 0.048 + 0.224 + 23 + 274 ≈ 最大300KB
        - int の変数・定数が 6個なので、8B * 6 = 48B = 0.048KB
        - DIRECTIONS は tuple * 4 なので、56B * 4 = 224B = 0.224KB
        - visited は 50行の二重配列なので、行ごとの list header (56B) と要素ポインタ (50 * 8B) から 50 * (56 + 400) = 23KB
        - lands_to_visit は1回 pop して 4方向 append するため分岐がスタックに蓄積され (枠外、訪問済みのセルは pop 後に skip されるとして、慣らすと1 pop あたり1,2回 append されることになる。)、最悪ケース (全入力が LAND) で最大 ~4900 個 (O(M * N)) まで増加する (4900 * 56B ≈ 274KB)。

```py
class Solution:
    WATER = 0
    LAND = 1
    DIRECTIONS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(height)]
        def is_land_required_to_visit(row, col) -> bool:
            return grid[row][col] == self.LAND and not visited[row][col]

        def sum_current_area(start_row, start_col) -> int:
            lands_to_visit = [(start_row, start_col)]
            total_area = 0
            while lands_to_visit:
                row, col = lands_to_visit.pop()
                if not(0 <= row < height and 0 <= col < width):
                    continue
                if not is_land_required_to_visit(row, col):
                    continue
                visited[row][col] = True
                total_area += 1
                for delta_row, delta_col in self.DIRECTIONS:
                    lands_to_visit.append((row + delta_row, col + delta_col))
            return total_area

        max_area = 0
        for row in range(height):
            for col in range(width):
                if not is_land_required_to_visit(row, col):
                    continue
                current_area = sum_current_area(row, col)
                max_area = max(max_area, current_area)
        return max_area
```

## Step 2

- 典型コメント集を見ていても、以前見たなと思うものや意見が一致しているなと思うものが増えてきた気がする。early return/continue、関数に適宜切り出す、命名の工夫など。一方であえてこっちの好みだからこれで行こうと思うものもある。これらこそが感情や審美眼なのだろう。
  - https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.5h10o8wgz7ah
- Python の recursion limit は LeetCode では 550000 に設定されている
  - 知らなかった。デフォルトの 1000 よりもだいぶ上に設定されているのか。reddit にあるように言語差を無くすためだろうという理解。
  - `setrecursionlimit できるような環境ならば設定すればいいわけですが、たとえば、ライブラリーを作っているとすると、これはグローバルに設定を変えることになるので他のところに影響が出る可能性がありますね。`
    - 確かに。迂闊に limit は変えるものではない。
  - https://github.com/olsen-blue/Arai60/pull/18#discussion_r1919805259
- 解法の選択肢としては、前問の 200. Number of Islands と同様のようだった。
  - 再帰/反復 DFS, BFS、Union Find
    - Union Find は前問で書いたのと常識から外れるとのことなので今回は扱わない。
  - 入力を破壊するかしないか
    - 破壊するにしても WATER に置き換えるか、VISITED とするか
  - 入力非破壊の反復 DFS が好みではあるのだが、step1 からあまり変わらなさそうなので、好みとは外れて色々書いてみることにする。

### 解法1: 再帰 DFS (入力を破壊する)

- 参考にした回答
  - https://github.com/olsen-blue/Arai60/pull/18/changes の 4th
  - https://github.com/Fuminiton/LeetCode/pull/18/changes の 1st
- 考えたこと
  - 入力を破壊するにしても、島を海に沈めるのは避けたい気持ち。
    - `0というマジックナンバーが海と訪問済みの二重の意味を持ってしまってるのが気になりました。初めてこのコードを上から読んでいる人からすると自明でない操作かなと`
      - まさにこれ。
      - https://github.com/olsen-blue/Arai60/pull/18/changes#r1921045916
    - なので `VISITED = 2` を定義して区別する。
  - recursion limit はあえて変更しない。グローバルな変更になってしまうのは避けたい。
  - DIRECTIONS を定義しないであえて、+ 1, - 1をベタ書きするのもそれはそれでありかもと思い始めてきた。
    - 可読性はどちらもそこまで変わらないかも。
    - 4方向探索が2方向とか8方向とかに増減する可能性が高そうなら DIRECTIONS で定数で持っておいた方が多少はメンテしやすくなりそう。
    - 趣味の範囲ではあると思う。
    - https://github.com/ryoooooory/LeetCode/pull/21/changes#r1966729356
  - 想定ユースケース
    - 入力を破壊するので、ライブラリの一関数として破壊しますよということを明示して提供するのが良いかも。
    - Python で言うと sort() 的な感じだろうか。
    - もっと実用的にするなら、塗りつぶしを VISITED にするか WATER にするか選べるようになっていると呼び手側が捗るかもしれない。
    - バリデーションを呼び手側に委ねているのは扱いづらいかもな。次の BFS では追加してみる。
  - 計算量
    - 時間計算量: O(M * N)
      - step1 と同じく、最大実行時間は 0.25ms。
    - 空間計算量: O(M * N)
      - 最大 500KB 程度になりそう。
        - int の変数・定数が 6個なので、8B * 6 = 48B = 0.048KB
        - call stack が最大 2500frames なので、2500 * 200B = 500,000B = 500KB
          - call stack のサイズは object によって動的に決まる。
            - https://github.com/python/cpython/blob/main/Objects/frameobject.c#L2038
          - `>>> sys.getsizeof(sys._getframe()) -> 152`
            - 一旦繰り上げて 200B とした。

```py
class Solution:
    WATER = 0
    LAND = 1
    VISITED = 2
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        def is_land_necessary_to_visit(row, col) -> bool:
            return grid[row][col] == self.LAND

        def sum_current_area(row, col) -> int:
            if not (0 <= row < height and 0 <= col < width):
                return 0
            if not is_land_necessary_to_visit(row, col):
                return 0
            grid[row][col] = self.VISITED
            return (
                1 + sum_current_area(row+1, col)
                + sum_current_area(row, col+1)
                + sum_current_area(row-1, col)
                + sum_current_area(row, col-1)
            )
            
        max_area = 0
        for row in range(height):
            for col in range(width):
                if not is_land_necessary_to_visit(row, col):
                    continue
                current_area = sum_current_area(row, col)
                max_area = max(max_area, current_area)
        return max_area
```

### 解法2: BFS (入力を破壊しない)

- 参考にした回答
  - https://github.com/olsen-blue/Arai60/pull/18/changes の 5th
  - https://github.com/ryoooooory/LeetCode/pull/21/changes の 2nd
  - https://github.com/miyataka/coding-practice/pull/18#discussion_r3447746027
- 考えたこと
  - `この「地面か」と「訪問済みか」を同時に評価されているのを見ると、この２つの変数に関係性があるのかと思ってしまうので分けたほうが良さそうです。`
    - これは同意。が、今回の場合だと私はその二つに関係性を見出しているので同時に評価している。
    - 関係性をより明示的にしたいなら関数に切り分けるのがいいのだろう。関数にすることでどう言う関係性かを名前で表現することができるので可読性が上がると言う側面もあるのだろう。step1 と step2 の解法1で関数切り分けしているのでこの解法ではあえて分けないことにしてみる。
    - https://github.com/olsen-blue/Arai60/pull/18/changes#r1921049036
  - `引数の中での関数呼び出しは重要そうな操作には思えない`
    - これも確かに。主人公級の関数なら変数で名前をつけてあげないと展開がわかりづらくなる。
    - 何を持って重要とみなすかは結構人によると思うので好みと言えば好み。
    - https://github.com/olsen-blue/Arai60/pull/18/changes#r1986280759
    - https://github.com/ryoooooory/LeetCode/pull/21/changes#r1966727423
  - queue から pop した時に visited に追加するか、queue 追加時に visited に追加するか。前者だと同じ LAND が複数 queue に入る可能性がある。DFS ならすぐに pop() されて visited に追加されるので、ダブってもせいぜい数個だが、BFS の場合は FIFO である都合上、visited に追加されるまでに時間がかかるため、ダブった値がどんどん入っていく。LeetCode 上でも TLE になる。なので BFS の場合は後者の方針で進める。
    - https://github.com/olsen-blue/Arai60/pull/18/changes#r1919718798
    - https://github.com/olsen-blue/Arai60/pull/18/changes#r1934084846
  - 想定ユースケース
    - バリデーションを追加してユーザー入力前提にしてみた。入力が m, n ともに 10000 個を超えてくると実行時間が10秒を超すのは変わらず。
    - 島と海を自由にドットでマッピングできる web アプリとかかな。そこで最大面積をマッピングのたびに表示するイメージ。マッピングに際し、1000 * 1000 くらいの上限を設けておけば最大1秒くらいで計算が終わるので UX も悪くはなさそう。
  - 計算量
    - 時間計算量: O(M * N)
      - 他と同じく、最大実行時間は 0.25ms。
    - 空間計算量: O(M * N)
      - 0.048 + 0.224 + 153 + 6 ≈ 最大160KB 程度
        - int の変数・定数が 6個なので、8B * 6 = 48B = 0.048KB
        - DIRECTIONS は tuple * 4 なので、56B * 4 = 224B = 0.224KB
        - visited (set) は最悪ケース (全セルが LAND) で 2500 個の (row, col) tuple を保持:
          - tuple オブジェクト (48B * 2500 = 120KB) + set ハッシュテーブル配列 (4096 枠 * 8B ≈ 33KB) で約 153KB
        - lands_to_visit (deque): O(min(M, N)) — 約 6KB
          - BFS は現在探索中の一番外側のセルのみを queue に保持するため、最悪ケース (50 × 50) でも同時に入るのは最大 50〜100 個程度。
          - tuple オブジェクト: (row, col) の 48B × 100 個 = 約 4.8KB
          - deque 構造体・ブロック: 64B + 2 ブロック × 512B ≈ 約 1.1KB
          - 合計: 4.8KB + 1.1KB ≈ 約 6KB


```py
class Solution:
    WATER = 0
    LAND = 1
    DIRECTIONS = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = set()
        def validate_cell(row, col) -> None:
            if grid[row][col] == self.LAND or grid[row][col] == self.WATER:
                return
            raise ValueError(
                "Input should only contain 0 or 1",
                f"input: {grid[row][col]}"
            )

        def is_land_necessary_to_visit(row, col) -> bool:
            return grid[row][col] == self.LAND and (row, col) not in visited
        
        max_area = 0
        for row in range(height):
            for col in range(width):
                validate_cell(row, col)
                if not is_land_necessary_to_visit(row, col):
                    continue
                current_area = 0
                lands_to_visit = deque([(row, col)])
                visited.add((row, col))
                while lands_to_visit:
                    current_area += 1
                    current_row, current_col = lands_to_visit.popleft()
                    for delta_row, delta_col in self.DIRECTIONS:
                        next_row = delta_row + current_row
                        next_col = delta_col + current_col
                        if not (0 <= next_row < height and 0 <= next_col < width):
                            continue
                        validate_cell(next_row, next_col)
                        if not is_land_necessary_to_visit(next_row, next_col):
                            continue
                        lands_to_visit.append((next_row, next_col))
                        visited.add((next_row, next_col))
                max_area = max(max_area, current_area)
        return max_area
```

## Step 3

- 考えたこと
  - 反復 DFS で入力非破壊で解く。
  - step 2 を経て、「stack から pop した時に visited に追加するか、stack 追加時に visited に追加するか」と言う選択肢が見えるようになった。
    - 前者だと stack にダブった値が追加されるが、visited の追加処理が1回で済む、後者だとダブった値は追加されないが、visited の追加処理は複数書く必要あり、と言う次第。
    - 後者の方が好み。DFS <-> BFS をデータ構造を変えるだけで実現できるため。
  - やっぱり current_area を DFS で探索しながら合計していく処理は関数に切り出した方が見通しが良くて好み。
  - visited は list よりも set の方が 座標を保持する lands_to_visit とより対になるように見えて好み。
    - `visited[row][col] = True` と `visited.add((row, col))` に対して、`lands_to_visit.append((row, col))`なので。
    - より座標感が出るのが set と言う所感。

```py
class Solution:
    LAND = 1
    DIRECTIONS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def is_land_necessary_to_visit(row, col) -> bool:
            return grid[row][col] == self.LAND and (row, col) not in visited

        height = len(grid)
        width = len(grid[0])
        def sum_current_area(start_row, start_col) -> int:
            current_area = 0
            lands_to_visit = [(start_row, start_col)]
            visited.add((start_row, start_col))
            while lands_to_visit:
                current_area += 1
                row, col = lands_to_visit.pop()
                for delta_row, delta_col in self.DIRECTIONS:
                    next_row = row + delta_row
                    next_col = col + delta_col
                    if not (0 <= next_row < height and 0 <= next_col < width):
                        continue
                    if not is_land_necessary_to_visit(next_row, next_col):
                        continue
                    lands_to_visit.append((next_row, next_col))
                    visited.add((next_row, next_col))
            return current_area
        
        max_area = 0
        for row in range(height):
            for col in range(width):
                if not is_land_necessary_to_visit(row, col):
                    continue
                current_area = sum_current_area(row, col)
                max_area = max(max_area, current_area)
        return max_area
```

## Step 4


