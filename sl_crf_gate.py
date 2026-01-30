import numpy as np

class SL_CRF_Gate:
    """
    Sub-Linear Compute Rejection Framework (SL-CRF) 
    Axiomatic Rejection Gate - Version 2.0 (Ontos-V2)
    """
    def __init__(self, tau=0.812, sigma=15.0):
        self.tau = tau
        self.sigma = sigma

    def forward(self, observed_signal, current_state):
        """
        情報を棄却するか受容するかを判定するメインロジック
        """
        # 現在の推測（状態）と観測値の差分を計算
        diff = np.abs(observed_signal - current_state)
        
        # 執着R（Axiomatic Rejection weight）の計算
        # 0.812の相転移点に基づくガウス重み付け
        R = np.exp(-(diff**2) / (2 * (self.sigma**2)))
        
        # 棄却ゲートの適用
        # 0.812以下の寄与度を持つ信号を抑制し、計算リソースを保護する
        if np.mean(R) < self.tau:
            # 信号を低優先度（または棄却）としてマーク
            return (observed_signal - current_state) * R, True
        
        return (observed_signal - current_state) * R, False

# 外部からの呼び出し用サンプル
if __name__ == "__main__":
    print("SL-CRF Gate System Initialized.")
    print(f"Working Axiom: tau = {0.812}")