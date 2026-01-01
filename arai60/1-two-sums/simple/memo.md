# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/11/files

## Comments

### Step 1

dict を作成して、target - nums[i] を key にして i を value して for 文をまわせばうまくいくかなと思ったが時間切れ。
あとで見返してみて、`if num_dict[nums[i]]`だと 0 の時に False 判定されるからダメだと分かった、、
なので、if nums[i] in num_dict とすればいい。

### Step 3

#### Solution 1

Step 1 と同じ解法だが、Step 1 だと命名のわかりやすさが欠けていたと感じるので、num_to_index や complement などを使うことによって改善したと思う。

#### Solution 2

二重ループを使う解法。直感的だが、Time Complexity は On^2 なので実戦向きではない。
