# 1. Two Sum

## Link

https://leetcode.com/problems/two-sum/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1: [target - num]: index の hashmap を使う

- nums を前から見ていって、[target - num]: index みたいな hashmap に追加していきつつ、num が target - num にヒットしたら、それぞれの index を含めて返せば良さそう
- 最初に思いついた流れ通りに実装した
- diff_to_index という名前はちょっと詰め込みすぎ感があるかも。厳密にいうと、diff_between_target_and_num_to_index なんだけれども長ったらしくなってしまうので略して diff_to_index とした。
- Time Complexity: O(n), Space Complexity: O(n)
- もう1個くらい解法を出したかったが、パッと思いつかなかったので step 2 に進む

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_index = {}
        for i, num in enumerate(nums):
            if num in diff_to_index:
                return [i, diff_to_index[num]]
            diff_to_index[target - num] = i
```

## Step 2

- `if の中のほうが、普通ではない、異常な、変わったことが起きて欲しいという感覚ですね。特に return などでは。ただ、趣味の範囲ではあります。`
  - ああ、確かに。例外を正解として return しているのは確かに驚きがある気がする。
  - https://discord.com/channels/1084280443945353267/1201211204547383386/1207251531041210408
- `たとえば、部屋の中の他に、100mおきに数字が1000個(100 km にわたって)置いてあって、その中から和が target なものを見つける、という課題があって、これをたとえば20人で分担して実行しようとしたら、どういう引き継ぎ資料を作りますかね。一人 5 km ずつ歩いて、数字をノートにメモしていって、ノートをある程度整理した形で引き継いでいかないといけないでしょうね`
  - 「身体性を持った考え方」。ただ変数や値をいじっていくだけに終始しないで、命名やロジックの切り分けを読み手が自然と処理のイメージができるようなものにするべきということと理解。それを考慮すると、自分の step 1はあまりそれができていないな、、
  - https://discord.com/channels/1084280443945353267/1237649827240742942/1249892025948573706
- ああ、step 1 では loop 抜けた後の返り値は何も設定していなかったが、caller 側にとってはエラーが返ってくる方が間違いなく都合がいいだろう。空配列を返すのもいいかもしれないが、この問題のスコープで考えるなら「必ず2つの数字を返す」という前提で空配列が返るのは例外のように思えるのでエラーの方が良さそう。
  - https://github.com/takumihara/leetcode/pull/1#discussion_r1806764103

### 解法1: hashmap 改良版 (key に num を入れる、エラーを返す)

- key に補数を入れるのではなく num を入れるようにした。やっていることは同じなのだが、num を入れておく方が後々応用が効きそうだし何より分かりやすい。diff_to_index という名前がいまいちしっくりこなかったのもこれで改善される
- エラーは入力値がおかしいことを端的に示すために、Exception ではなく ValueError にした

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [i, num_to_index[complement]]
            num_to_index[num] = i
        raise ValueError("nums is invalid. Can't return 2 indices.")
```

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/14/changes の 4th
- https://github.com/olsen-blue/Arai60/pull/11/changes の 3th

### 解法2: 二重ループ

- 選択肢を増やしたいので二重ループでも解けるようにする。
- Space Complexity を1にするとしたらこうするのがいいが、Time Complexity が非効率なので実践的ではないかも。
- Time Complexity: O(n^2), Space Complexity: O(1)

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] + nums[j] != target:
                    continue
                return [i, j]
        raise ValueError("nums is invalid. Can't return 2 indices")
```

#### 参考にした回答

- https://github.com/olsen-blue/Arai60/pull/11/changes の 1st

## Step 3

- 最終的にStep 2 の解法1に以下の変更を加えたものになった
  - if complement in num_to_index を反転させて、答えを happy path 的に返すように
  - num_to_index の命名に合わせる形で、i を index に変更。

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if not complement in num_to_index:
                num_to_index[num] = index
                continue
            return [ index, num_to_index[complement] ]
        raise ValueError("nums is invalid. Can't return the 2 indices.")
```

## Step 4


