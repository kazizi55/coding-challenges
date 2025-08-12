import time
import statistics

execution_times = []
for _ in range(10):
  start_time = time.perf_counter()

  # 計測したい関数を追加

  end_time = time.perf_counter()
  execution_times.append(end_time - start_time)

print(f"各実行時間: {execution_times}")
print(f"実行時間の中央値: {statistics.median(execution_times)}")