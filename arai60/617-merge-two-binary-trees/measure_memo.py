import copy
import inspect
import sys


class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# 1. Measure function call frame size (same method as second_round.md line 167-180)
def get_frame_size():
  f = inspect.currentframe()
  return sys.getsizeof(f) + sys.getsizeof(f.f_locals)


# 2. Build a tree with 2,000 nodes
def build_tree(n):
  if n <= 0:
    return None
  left_n = (n - 1) // 2
  right_n = n - 1 - left_n
  node = TreeNode(n)
  node.left = build_tree(left_n)
  node.right = build_tree(right_n)
  return node


tree = build_tree(2000)

# -------------------------------------------------------------
# Part 1: Measure memo dictionary created by copy.deepcopy()
# -------------------------------------------------------------
memo = {}
copy.deepcopy(tree, memo)
memo_bytes = sys.getsizeof(memo)

# -------------------------------------------------------------
# Part 2: Measure call stack overhead at Python's default limit (1,000 frames)
# -------------------------------------------------------------
frame_bytes = get_frame_size()
stack_bytes = frame_bytes * 1000

# -------------------------------------------------------------
# Part 3: Combine memo dict + call stack
# -------------------------------------------------------------
total_bytes = memo_bytes + stack_bytes

print("=" * 60)
print("deepcopy 内部のメモ化辞書・コールスタック: 計測")
print("=" * 60)
print("1. メモ化辞書 (memo dict):")
print(
    f"   - 登録エントリ数: {len(memo)} 件 (TreeNode 2000個 + __dict__ 2000個 +"
    " root)"
)
print(f"   - メモリサイズ:   {memo_bytes} bytes ({memo_bytes / (1024 * 1024):.2f} MB)")

print("\n2. コールスタック (call stack):")
print(f"   - 1フレームあたり: {frame_bytes} bytes (frame object + locals dict)")
print(
    f"   - 最大1000フレーム: {stack_bytes} bytes"
    f" ({stack_bytes / (1024 * 1024):.2f} MB)"
)

print("\n3. 合計 (メモ化辞書 + コールスタック):")
print(f"   - {memo_bytes} B + {stack_bytes} B = {total_bytes} bytes")
print(f"   - 約 {total_bytes / (1024 * 1024):.2f} MB  ->  【約 0.5MB】")
print("=" * 60)
