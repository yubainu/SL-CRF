# demo_numeric.py
import numpy as np
import matplotlib.pyplot as plt
from ontos_stub import ONTOS  # さっき作ったスタブを読み込む

def run_test():
    monitor = ONTOS(alert_threshold=0.25)
    
    # テストデータの生成（最初は安定、後半に崩壊する数値列）
    stable = np.random.normal(0.1, 0.02, 40)
    drift = np.linspace(0.1, 0.4, 20)
    data = np.concatenate([stable, drift])

    idis = []
    alerts = []

    for v in data:
        result = monitor.step(v)
        idis.append(result["idi"])
        if result["report"]:
            alerts.append(result["report"])

    # 結果の可視化
    plt.figure(figsize=(10, 5))
    plt.plot(data, label="Input Data Stream", alpha=0.5)
    plt.plot(idis, label="ONTOS IDI (Structural Friction)", color='red', linewidth=2)
    plt.axhline(0.25, color='gray', linestyle='--', label="Alert Threshold")
    plt.title("ONTOS V12.3: Structural Discontinuity Detection")
    plt.legend()
    plt.show() # 図が表示される

    print("\n".join(alerts[:5])) # 最初のアラートを表示

if __name__ == "__main__":
    run_test()
