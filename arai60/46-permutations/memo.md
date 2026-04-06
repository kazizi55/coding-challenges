# 46. Permutations

## Link

https://leetcode.com/problems/permutations/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/51

## Comments

### Step 1
- inputの順列を返すと言うもの。nums.lengthが6までなら愚直に計算してもいけるか？最大でも6!分くらいしか計算しないので、、
- 再帰でも解けそう。固定する数字と回転させる数字をそれぞれ引数で渡す形で。あーでもどう返り値に含めるかが大変か。
- 返り値の配列を持っておいて、回転させたものをどんどん放り込んでいく感じになる。順列の数が幾つになるかはわかるので、例えば while len(permutations) < math.factorial(len(nums)) みたいな感じでひたすら計算していくのだろうか
- 時間切れ。答えを見る。

### Step 3

#### Solution 1

- なるほど、順列の各数字を1個ずつ固定させつつstackを積み、再帰で回していけばできるのか。
- next_rest_nums = rest_nums[:index] + rest_nums[index + 1:] を使えば、今回の数字以外を抜き出して次の再帰関数に渡すことができる。

#### Solution 2

- Solution 1と考え方は同じでこっちは stack を自前で実装する version。
- このPRのauthorの方はSolution 1の方が直感的でいいと言っていたけど、それは納得。Solution 1 は先頭から順番にpermutationを完成させていくのに対し、2は末尾から完成させていく。どっちもDFSではあるのが面白い。
- 2を1の順番で回したかったらrangeをreversedにするといい
