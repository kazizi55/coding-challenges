# 200. Number of Islands

## Link

https://leetcode.com/problems/number-of-islands/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1

- 考えたこと
  - 四方を囲まれている島の数を数え上げるというもの。
  - とりあえず分かりやすさのために1と0を定数化するのは覚えている。
  - どうやって解くんだったっけな、、
  - m, n ともに最大の len は300なので、O(n^2)で解いても3 * 10^4 steps 程度。すなわち Python でも0.5sちょいくらいで処理が終わるはず。よし、O(n^2)で解くか。
  - あ、あと DFS で解くんだったな。となると while ループの方がやりやすそう。stack を用意する。
  - が、どうやって stack に値をつめていくんだっけな、、
  - 常に i+1 と j+1 を見てまだ LAND だったら stack に入れていく、ともに WATER だったら num_islands を increment する感じだろうか
  - うーん、時間切れ。gemini に聞きながら答えを作っていく

```py
#  通らない
class Solution:
    LAND = "1"
    WATER = "0"
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        stack = []
        while len(stack) > 0:
```
- 考えたこと
  - gemini に聞きながら完成させた。
  - M と N の二重ループの中でさらに stack を使って隣接する LAND を全て WATER に破壊的変更をする形で DFS をする。
  - イメージで考えると、島の探索隊がいるとして、島の一部を見つけ次第、見つけたという記録をつけて、引き継ぎしながら**その島全体を海に沈める**。そしてまた次の人に引き継ぐ。島が見つからなければどんどん次の人に引き継いでいく。イメージで考えるとなかなかすごいことしてるな、この解法。笑
    - イメージが強烈だと覚えやすいので助かる。
  - 流れはわかりやすいし、in-place で変更するので空間計算量も節約できるが、入力を破壊するのは実務ではそれなりにリスクがあるだろうし用途が限られるだろう。
  - 想定ユースケース
    - 入力を破壊するので、大きな入力を扱う場合かつ元の入力を保持したい場合には向いていない。
    - 入力のバリデーションも特にかけていないので、社内で必要に応じて使う分析用ライブラリとかだろうか。やはり用途は限られる。
  - 計算量
    - 時間計算量: O(M * N)
      - 4重ループに見えるが、実際は `while len(stack) > 0` と `for r_offset, c_offset in self.DIRECTIONS` のなかで隣接する LAND を WATER に塗りつぶしているので、`if grid[r][c] != self.LAND` で skip されるため、O(M * N) になる。
      - M と N も最大 300 なので、最大 3^2 * 10^4 steps とする、さらに4方向の計算も加味してと、Python で実行すると大体 3^2 * 10^4 * 4  / 10^7 = 36ms ほどになる。元の len が少ないので思ったよりも時間はかからない
    - 空間計算量: O(M * N)
      - 入力を in-place で書き換えることで visited 配列のメモリは削減できているが、DFS 用の stack に最大で全セル数 O(M * N) の要素が積まれる可能性があるため、最悪空間計算量は O(M * N) となる。
      - stack 以外の変数も含めて、8 * 9 * 3^2 * 10^4 = 6.48MB 程度だろうか
      - が、stack は pop のたびにメモリが解放され、探索が終わるごとにリセットされるので、実際のピークメモリは最大の島の LAND 数に依存する。

```py
class Solution:
    LAND = "1"
    WATER = "0"
    DIRECTIONS = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != self.LAND:
                    continue
                num_islands += 1
                stack = [(r, c)]
                grid[r][c] = self.WATER
                while len(stack) > 0:
                    current_r, current_c = stack.pop()
                    for r_offset, c_offset in self.DIRECTIONS:
                        next_r = current_r + r_offset
                        next_c = current_c + c_offset
                        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == self.LAND:
                            grid[next_r][next_c] = self.WATER
                            stack.append((next_r, next_c))
        return num_islands
```

## Step 2

- `私の感覚なんですけど、日本語だったらこう表現すると思うんですよ。「root1 と root2 の集団のサイズを比べて、小さい方を大きい方に合流させる。」ここで、「root1 と root2 の集団のサイズを比べて、root1 が root2 よりも大きかった場合は、root2 を root1 に合流させ、そうでなかった場合は、root1 を root2 に合流させる。」とは言わないと思うんですよ。`
  - 自然言語で表現するときに使う言葉を変数に使うとよい
  - https://discord.com/channels/1084280443945353267/1201211204547383386/1213387878734766080
- `とりあえずは長くて良いので名前をつけてみるので良いと思います。長い命名ができれば短くもできると思うのですが、逆は成り立たないと思います。その上で変数のスコープなどによって長さも調節する感じかなと思います。`
  - 確かに。ベースは長い正式名称みたいなものがあってそれをスコープに応じて短くしていく感じか。
  - 日本 東京都 豊島区 と言うべき時もあるし、東京都からしか言わなくてもいい時もあるし、逆に豊島区とか日本だけしか言わなくてもいい時もある。同じようなものなのだろう。
  - https://github.com/shining-ai/leetcode/pull/17#discussion_r1510212982
- `gridを書き換えるなら、訪問済みを表す値を別で定義して入れたほうが良いと思います '0'はあくまでWATERを表す数なので、デバックがしにくくなるのとコードリーダーは'0'訪問済みをWATERにすることに意味があるように見えてしまうので`
  - 確かに。元から海だったのか島をぶっ壊して海にしたのかは区別しておいた方が次何かする人が作業しやすいだろう
  - https://github.com/Ryotaro25/leetcode_first60/pull/18#discussion_r1676688484
- `visit_island は、メソッド内のとはいえメソッドなので、雑に扱っても構わないものにしておきたい気持ちがあるんです。... そうすると、読む方からすると、こういう条件を満たしている引数で呼んで欲しいのか、と分かるようになりますね。`
  - 同意。呼び出し側に呼び出し条件をいちいち書かせるよりも呼び出し元で guard を書いておいて雑に呼び出せるようにしておいた方が取り回しがいい。Python のライブラリとかも例えばそう言う実装になっているし。
  - https://github.com/sakupan102/arai60-practice/pull/18#discussion_r1582241335
- `私は変数におくというよりは「なぜそのデシジョンがなされたのか」の背景をコメントに書いておくといいと思います。`
  - 「帰結」はコードからわかるが、「動機」はコードからだけでは分かりようがないのでコメントに書くと良い
  - https://github.com/Fuminiton/LeetCode/pull/17#discussion_r1984360256
- `しかし、実際に頼んでいることは、一般的な自然数添字の UnionFind へのお願いですね。もうちょっと楽にしたいことを伝えられるはずなんですよ。`
  - 関数の作り方をお願いの仕方ベースで考える。
  - https://github.com/ichika0615/arai60/pull/9/changes/BASE..d9c2466cb7f298f4aea361af67b4a426d5d6e9b3#r1954436002
- `dfs は名前が悪いので、もうちょっと意味のある名前をつけませんか。いや、なんか、冷蔵庫に「電気」とか「断熱膨張」とかって名前つけないじゃないですか。「冷やす貯蔵庫」ですよね。意味といっているのは、要は、どうやってそれを作っているか動いているかは書いている人は興味があるけれども、読んでいる人、呼び出す人はそれを伝えられたからって困るわけですよ。remove_island とか色々あると思うんですよ。`
  - 今回も例えが興味深い。確かに呼び出し側の気持ちになってみたらどう実装されているかはあんまり興味ないだろう。家電とか車とか身近なもので考えてみると確かに分かりやすい。
  - https://discord.com/channels/1084280443945353267/1183683738635346001/1194347590125367467
- `関数は、理想的には名前だけから呼んだときに何が起きるかが分かることが好まれます。そうすれば、ソースコードを読んでいったときに、その中を見なくても続きが読めるからです。最悪なのは、読んでいくと、正体不明の関数があって前後からは推測できなくて、その中を見ると、そこでも正体不明の関数が呼ばれていて、というのが続くことです。`
  - 上の話の延長で、実務レベルで困ることがこれ。確かに変数が内容を端的に伝えていれば読む負荷はグッと下がる。
  - https://github.com/Hurukawa2121/leetcode/pull/17/changes#r1898583926
- `m, n はわりと主役級なので、width, height などの名前をつけてしまってもいいかもしれません。`
  - 主役級って言い得て妙だなー。よく出てくる言葉だからこそ分かりやすい命名をする。
  - https://discord.com/channels/1084280443945353267/1200089668901937312/1211344469937360908
- `一回、row, col を const int で宣言してしまってから、書いたほうがいい気がしますね。ここ以下、row col が主役なのに、coordinate.{row,col} で呼んでいるのは冗長です。`
  - 主役級なのに個別の名前を与えないのは冗長になってしまう。
  - https://github.com/colorbox/leetcode/pull/31/changes/BASE..68e00411964489033b4e936e38ca08c80a3a1abd#r1881125966

### 解法1: Union Find を使う

- 参考にした回答
  - https://github.com/tarinaihitori/leetcode/pull/17/changes の 2nd
  - https://github.com/hayashi-ay/leetcode/pull/33/changes の 2nd
  - https://github.com/ichika0615/arai60/pull/9/changes の 2nd, arai60_17_2.md
- 考えたこと
  - Union Find は初見なので調べる。
  - gemini に質問をしてイメージが掴めた。こんな感じだろうか。現実の例で考えると途端にアルゴリズムが生き生きして見えてくる。面白い。
    - 「部屋に人がいっぱいいます。大学サークルの新歓とかで集められた大学一年生たちとか。アイスブレイクのために友達グループを作ってもらいます (init() メソッド)。その後無作為に二人を選んで同じ友達グループに属しているかを判断します。」
    - 「同じ人をリーダーと認識している」と言うのを同じ友達グループに属しているとみなす (Find() メソッド)
    - 「違う友達グループに属している二人が友達になったら、同じ友達グループになります。すると一方のグループのリーダーが別のグループのリーダーをリーダーと認識するようになる」(Merge() メソッド)
    - 効率化のために例えば以下が使われる
      - 「リーダーが誰かを判断するときに、中間リーダーを飛ばせるように、一番トップのリーダーをリーダーと判断するように参照先を更新する」(Path Compression)
      - 「違うグループに属している二人が友達になる時に、常に数が少ない方のリーダーに一番友達数が多いグループのリーダーをリーダーとみなすように言う」(Union By Size)。あるいはランクづけをして、ランクを当てにしてもいい (Union By Rank)。
        - これにより、肥大化してリーダーがリーダーを呼び続けるみたいなことを避けられる
        - これにより、計算量がアッカーマン関数の逆関数になる
          - https://discord.com/channels/1084280443945353267/1183683738635346001/1197738650998415500
          - https://github.com/skypenguins/coding-practice/pull/56#discussion_r3681700856
        - そもそもアッカーマン関数とは、A(m, n)がそれぞれの値に応じて以下のように代入される再帰関数のこと。通常の指数関数よりも時間計算量が急速に増加することで有名。(A(3,1)は13なのに対し、A(4,1)は65533、A(4,2)は 2^65536-3 になるなど)
          - m = 0
            - n + 1
          - m > 0 かつ n = 0
            - A(m - 1, 1)
          - m > 0 かつ n > 0
            - A(m - 1, A(m, n - 1))
        - で、これの逆関数なので、入力がかなり大きくなっていったとしても以下のように時間計算量はかなり緩やかに増加していく。
          - α(1) = 0
          - α(4) = 2
          - α(16) = 3
          - α(65536) = 4
          - α(10^80) <= 4
            - 宇宙全体の粒子の数を入力しても4が出力されるのは恐ろしく増加が緩やかだ。
            - http://web.cs.wpi.edu/~kfisler/Courses/Rice/210/Labs/lab09/univSize.html
    - Path Compression と Union By Rank を使って実装。先達が書いているように、これを面接で書くのは結構大変そう。
  - で、どういう流れかというと、「grid から島の座標だけからなる nodes から union find を作成し、右と下の隣接する node を見て union していく。union が終わったら nodes を再度見て、リーダーを見つけるたびに num_islands を増やしていき、その値を返す」という感じ。
  - 想定ユースケース
    - アッカーマン関数の逆関数なので、大規模な入力にも耐えうる。
    - 社内で使う用のビックデータの分析用プログラムとかだろうか。ユーザー入力を想定せず、不正なデータはこの関数が呼ばれる前に弾かれているか整形されている前提。
  - 計算量
    - 時間計算量: O(M * N)
      - nodes に append していくのに 300^2 = 9 * 10^4 steps
      - UnionFind の init に 9 * 10^4 * 2 = 1.8 * 10^5 steps
      - UnionFind の union の実行に、9 * 10^4 * 2 * 2 (union() 内で find() が2回呼ばれるため。path compression しているのでほぼ O(1) になる) = 3.6 * 10^5 steps
      - num_islands の計算に 9 * 10^4 steps = 9 * 10^4 steps
      - (9 * 10^4 + 1.8 * 10^5 + 3.6 * 10^5 + 9 * 10^4) / 10^7 = 最大72 ms 程度
        - Python の時間あたりの step 実行数を 10^7 steps とする
    - 空間計算量: O(M * N)
      - 9 * 10^4 要素に対して合計約 16 MB 程度
        - tuple
          - 1つ当たり56 bytes
            - `>>> sys.getsizeof((1, 2)) -> 56`
          - 9 * 10^4 * 56 = 5.04 MB
          - https://github.com/python/cpython/blob/main/Include/cpython/tupleobject.h
        - list (nodes): 1要素当たり約 8 bytes (ポインタ配列)
          - 9 * 10^4 * 8 = 0.72 MB
          - https://github.com/python/cpython/blob/main/Include/cpython/listobject.h
        - dict (child_to_parent, node_to_rank): ハッシュテーブルのオーバーヘッド含め 1要素当たり約 50〜60 bytes
          - ハッシュ衝突防止のため、CPython の dict は要素数が容量の 2/3 (USABLE_FRACTION) を超えると 2の n 乗 (2^k) で自動リサイズされる。
            - dict、実装みていくと興味深いな。O(1) でヒットするように工夫が盛り込まれている。
          - 9 * 10^4 * 60 bytes ≈ 5.4 MB / dict 
          - https://github.com/python/cpython/blob/main/Objects/dictobject.c#L45

```py
class UnionFind:
    def __init__(self, nodes):
        self.child_to_parent = {node: node for node in nodes}
        self.node_to_rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.child_to_parent[node] != node:
            self.child_to_parent[node] = self.find(self.child_to_parent[node])
        return self.child_to_parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 is root2:
            return
        if self.node_to_rank[root1] > self.node_to_rank[root2]:
            self.child_to_parent[root2] = root1
            return
        if self.node_to_rank[root1] < self.node_to_rank[root2]:
            self.child_to_parent[root1] = root2
            return
        self.child_to_parent[root2] = root1
        self.node_to_rank[root1] += 1
    
class Solution:
    LAND = "1"
    DIRECTIONS = [(0, 1), (1, 0)]
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        nodes = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == Solution.LAND:
                    nodes.append((i, j))
        union_find = UnionFind(nodes)
        for r, c in nodes:
            for delta_r, delta_c in self.DIRECTIONS:
                next_r = r + delta_r
                next_c = c + delta_c
                if (next_r, next_c) in union_find.child_to_parent:
                    union_find.union((r, c), (next_r, next_c))
        num_islands = 0
        for node in nodes:
            if union_find.find(node) != node:
                continue
            num_islands += 1
        return num_islands
```

### 解法2: DFS を使う (入力非破壊)

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/33/changes の 2nd
  - https://github.com/olsen-blue/Arai60/pull/17/changes の 4th
  - https://github.com/quinn-sasha/leetcode/pull/18/changes の 3rd
- 考えたこと
  - 入力を破壊する・しないなど DFS にしてもいろんな解法があるのか。
  - 入力を破壊する場合でも VISITED と第三の定数を置いて破壊した入力を明示的にするものがあった。
  - 個人的には入力を破壊する時点でユースケースがだいぶ限られると感じるので、space complexity を抑えなければならなかったり入力が極端に大きかったりする場合を除いて、基本的に入力非破壊にしたいなと思うようになった。
  - 再帰 DFS にするか 反復 DFS にするか。せっかくなので両方書く。
  - 個人的には再帰だと call stack の上限を気にしないといけないので、入力の大きさにある程度幅を持たせられる反復 DFS の方が好みではある。
    - デフォルトの上限は1000
      - `>>> sys.getrecursionlimit() -> 1000`
  - いずれにせよ流れとしては、「grid が島と水以外の不正な値かを確認しつつ、水かすでに見ている島だったらスキップして、num_islands の値を一度増やしたら隣接する島をひたすら捜索するのを繰り返す。最後に num_islands を返す」という感じになる。
  - 想定ユースケース
    - 島の数を判定するライブラリの一関数として提供するとかだろうか
    - 不正な入力を弾くバリデーションを入れたので呼び出し側でよしなにハンドリングできるようになっている
  - 計算量
    - 時間計算量: O(M * N)
      - step1 と同じく、最大36 ms 程度になる見込み。
    - 空間計算量: O(M * N)
      - step1 とほぼ同じだが、visited 分も含める必要があるので、6.48MB + 9 * 10^4 * 8B = 6.48 + 0.72 = 7.2MB 程度だろうか

```py
# A worst-case grid full of land requires a recursion depth of up to 90000 frames.
sys.setrecursionlimit(90000)

class Solution:
    WATER = "0"
    LAND = "1"
    DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(height)]
        def is_valid(row, col) -> bool:
            return grid[row][col] == self.WATER or grid[row][col] == self.LAND

        def should_be_skipped(row, col) -> bool:
            return grid[row][col] == self.WATER or visited[row][col]

        def mark_land_as_visited(row, col) -> None:
            if not (0 <= row < height and 0 <= col < width):
                return
            if should_be_skipped(row, col):
                return
            visited[row][col] = True
            for delta_row, delta_col in self.DIRECTIONS:
                mark_land_as_visited(delta_row + row, delta_col + col)

        num_islands = 0
        for row in range(height):
            for col in range(width):
                if not is_valid(row, col):
                    raise ValueError(
                        "Input should be either a land or water.",
                        f"Input: {grid[row][col]}"
                        )
                if should_be_skipped(row, col):
                    continue
                num_islands += 1
                mark_land_as_visited(row, col)
        return num_islands
```

```py
class Solution:
    WATER = "0"
    LAND = "1"
    DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(height)]
        def is_valid(row, col) -> bool:
            return grid[row][col] == self.WATER or grid[row][col] == self.LAND

        def should_be_skipped(row, col) -> bool:
            return grid[row][col] == self.WATER or visited[row][col]

        def mark_land_as_visited(start_row, start_col) -> None:
            lands_to_visit = [(start_row, start_col)]
            while lands_to_visit:
                row, col = lands_to_visit.pop()
                if not (0 <= row < height and 0 <= col < width):
                    continue
                if should_be_skipped(row, col):
                    continue
                visited[row][col] = True
                for delta_row, delta_col in self.DIRECTIONS:
                    lands_to_visit.append((delta_row + row, delta_col + col))

        num_islands = 0
        for row in range(height):
            for col in range(width):
                if not is_valid(row, col):
                    raise ValueError(
                        "Input should be either a land or water.",
                        f"Input: {grid[row][col]}"
                        )
                if should_be_skipped(row, col):
                    continue
                num_islands += 1
                mark_land_as_visited(row, col)
        return num_islands
```

### 解法3: BFS を使う (入力非破壊)

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/33/changes の 2nd
  - https://github.com/quinn-sasha/leetcode/pull/18/changes の 3rd
- 考えたこと
  - DFS と同様に、入力非破壊の方が好みなのでそれで実装してみる。
  - 想定ユースケース
    - 解法2と同じく、島の数を判定するライブラリの一関数として提供するとかになりそう
  - 計算量は解法2と同じという認識

```py
class Solution:
    WATER = "0"
    LAND = "1"
    DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(height)]
        def is_valid(row, col) -> bool:
            return grid[row][col] == self.WATER or grid[row][col] == self.LAND

        def should_be_skipped(row, col) -> bool:
            return grid[row][col] == self.WATER or visited[row][col]

        def mark_land_as_visited(start_row, start_col) -> None:
            lands_to_visit = deque([(start_row, start_col)])
            while lands_to_visit:
                row, col = lands_to_visit.popleft()
                if not (0 <= row < height and 0 <= col < width):
                        continue
                if should_be_skipped(row, col):
                        continue
                visited[row][col] = True
                for delta_row, delta_col in self.DIRECTIONS:
                    lands_to_visit.append((delta_row + row, delta_col + col))

        num_islands = 0
        for row in range(height):
            for col in range(width):
                if not is_valid(row, col):
                    raise ValueError(
                        "Input should be either a land or water.",
                        f"Input: {grid[row][col]}"
                        )
                if should_be_skipped(row, col):
                    continue
                num_islands += 1
                mark_land_as_visited(row, col)
        return num_islands
```

- このような形で queue から取り出したあとで visited を True にすると、複数回同じものが queue に入ってしまう。visited と mark される前の land が queue に入ってさらにその隣接している land が queue に追加されるので、時間計算量は大体 4^n になる。LeetCode 上も TLE になる。
  - https://github.com/quinn-sasha/leetcode/pull/18/changes#r1997515140
- ちなみに DFS だと stack から取り出した後に visited を True にしても TLE にはならない。同じものが複数 stack に入るのは変わらないが、LIFO なので、1つの land につき最大4回までしか stack に追加されないので、時間計算量も M * N * 4 程度に収まる。
```py
...
        def mark_land_as_visited(start_row, start_col) -> None:
            lands_to_visit = deque([(start_row, start_col)])
            while lands_to_visit:
                row, col = lands_to_visit.popleft()
                visited[row][col] = True
                for delta_row, delta_col in self.DIRECTIONS:
                    next_row = delta_row + row
                    next_col = delta_col + col
                    if not (0 <= next_row < height and 0 <= next_col < width):
                        continue
                    if should_be_skipped(next_row, next_col):
                        continue
                    lands_to_visit.append((next_row, next_col))
...
```

## Step 3

- 考えたこと
  - 解法2のように入力非破壊で反復 DFS にするのが好み。
  - 前述の通り、入力非破壊の方が実務で呼び出し側的に取り回しが効きやすそうで、再帰を使わない分、recursion limit を気にしなくてもいいからだ
  - union find は勉強にはなったが、常識からは外れるとのことなので、一旦 step 3では扱わない。
  - BFS か DFS かという点だと、この問題に限っていえば前述のような visited を true にするタイミングが違うと時間計算量が爆発的に増加するようなことが起きえない DFS の方がメンテナンス性が高いとも言えるので、DFS を選んだ。
  - step2 で `not (0 <= row < height and 0 <= col < width)` を should_be_skipped に含めていなかったことに気づき (mark_lands_as_visited の中でしか用いられない guard なので含めなかった)、含めないことの正当性を示すために、`is_land_necessary_to_visit` という関数名に変えた。cell が訪問するべき島かどうかを判断する関数なので、境界値チェックは含めない、というふうに多少は示せたとは思う。
  - また、should_be_skipped -> mark_lands_as_visited にリネームするに従い、条件を反転させた。なんとなく肯定系の方が内容がスッと入ってくる感じがある (not をつけた時に否定しているのね、と自然に判断できるため)。好みの範疇だろう。


```py
class Solution:
    LAND = "1"
    DIRECTIONS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = [[False] * width for _ in range(height)]
        def is_land_necessary_to_visit(row, col) -> bool:
            return grid[row][col] == self.LAND and not visited[row][col]
        
        def mark_lands_as_visited(start_row, start_col) -> None:
            lands_to_visit = [(start_row, start_col)]
            while lands_to_visit:
                row, col = lands_to_visit.pop()
                if not (0 <= row < height and 0 <= col < width):
                    continue
                if not is_land_necessary_to_visit(row, col):
                    continue
                visited[row][col] = True
                for delta_row, delta_col in self.DIRECTIONS:
                    lands_to_visit.append((delta_row + row, delta_col + col))

        num_islands = 0
        for row in range(height):
            for col in range(width):
                if not is_land_necessary_to_visit(row, col):
                    continue
                num_islands += 1
                mark_lands_as_visited(row, col)
        return num_islands
```

## Step 4


