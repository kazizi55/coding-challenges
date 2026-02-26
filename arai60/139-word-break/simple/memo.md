# 139. Word Break

## Link

https://leetcode.com/problems/word-break/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

## Comments

### Step 1

パッと見て再帰でシンプルに解けそうだなと思った。wordListを見てsを刈り取って残りを次に渡す、空文字になったらその時点でtrueを返す、何もヒットしなかったらfalseを返すと言う方針で解く。
うーん、見た目は問題なさそうだけど18 / 48 testcases passedだなー。なんでだろう。答えを見る。
あー、wordDictに入っているか判定のところで辞書の中の単語にヒットしたらその後の単語で固定して探していたからダメだったのかー。
あと、cacheする関数の名前がいけてないな。もっと意味のある名前をつけるように心がける。
あと、range(x, y)とs[:x]が指す範囲がごちゃごちゃになっていた。

### Step 3

#### Solution 1

Step1と方針は同じだが、再帰関数にスライスではなくindexを渡すことで空間計算量を節約。スライスだと新しい文字列を作成してしまうので。

ちなみにstartswith()を使わないで書くと以下のようになる:

```py
            for word in wordDict:
                target_end = from_index + len(word)
                if target_end <= len(s) and s[from_index:target_end] == word:
                    if is_breakable(target_end):
                        return True
```

#### Solution 2

なるほど、そもそもこのアルゴリズムでは 「インデックス = 文字の数（長さ）」 として扱っているのかー。

len(s) + 1 にする理由は以下の 3 点に集約される：

1. スタート地点の確保: 「何もしていない状態（インデックス0）」を True にするため。
2. ゴール地点の確保: 「全文字（インデックス len(s)）終わった状態」を記録するため。
3. 計算の簡略化: 現在の位置 + 単語の長さ をそのままインデックスとして使えるようにするため（IndexError 防止）。

直前の値を使いつづけて積み重ねていく、というよりはTrueとFalseで歯抜けにする (Trueと言う旗を立てるイメージの方が適切か)と言う感じ。

index_to_segmentableをis_breakable_at_lengthという変数名に変えるだけでグッと理解しやすくなった。だってこれは厳密にいうとindexじゃないじゃんという。
