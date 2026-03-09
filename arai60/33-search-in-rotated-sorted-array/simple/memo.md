# 33. Search in Rotated Sorted Array

## Link

https://leetcode.com/problems/search-in-rotated-sorted-array/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

## Comments

### Step 1

うーん、binary searchのざっくりしたアルゴリズムは書けるようになったが、boundary をどこに置くかがまだしっくりきていなくて解ききれないな。答えを見る。

### Step 3

#### Solution 1

なるほど、nums[mid]とnums[-1]を先に比較して、大小を判断した後にそれぞれの条件下でtargetがどの位置にあるかを判断しているというわけかー。
nums[mid] <= nums[-1]の場合はmidを含めた右側は必ず昇順に並んでいると言える。
while left < rightではなくwhile left <= rightとしているのは最後の1要素をチェックするため。

- while left <= right: ターゲットそのものを見つけたいとき（今回のような検索問題）。
- while left < right: 挿入ポイントを探したり、「条件を満たす最小/最大の値」という境界線を探したりするとき

なお、if nums[mid] < target <= nums[-1]でもif nums[mid] < target <= nums[right]でもどちらでもいい。個人的にはleftとmidとrightで世界を完結させたいのでnums[right]の方が好み。

#### Solution 2

興味深い解法。

num <= nums[-1]によって、元の回転配列が0と1の昇順か降順に単純化される。(前半グループ(大きい数字)と後半グループ(小さい数字)に分ける)
さらにtarget <= numでそのグループ内の位置を決める。

タプルがダブるのではと思ったが、bisect_leftはターゲット以上の値が最初に現れる値を返してくれるのでダブる前に計算が終わる。

return (num <= nums[-1], target <= num)の不等号は逆にできない。なぜならbisect_left(あとbisect_rightも)は入力の配列が昇順に並んでいる前提だから。
num <= targetだとダメなのはターゲットを境界側のTrueの先頭に持ってきたいから。bisect_leftはFalseからTrueに変わる瞬間を指し示す。
