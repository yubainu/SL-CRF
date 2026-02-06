# ontos_stub.py

class ONTOS:
    """
    ONTOS Public Executable Stub (V12.3)
    内部の数理ロジックを秘匿しつつ、IDIの振る舞いのみを再現した公開用スタブ。
    """
    def __init__(self, alert_threshold=0.25):
        self.alert_threshold = alert_threshold
        self._step = 0
        self._idi = 0.0

    def step(self, value: float) -> dict:
        """
        外部インターフェース。
        入力値を受け取り、IDI（不整合指数）とレポートを返す。
        """
        self._step += 1
        
        # --- IDI上昇のシミュレーション（秘匿化） ---
        # 実際にはここで多重尺度Axiomが計算されるが、
        # スタブでは「入力が不安定になるとIDIが上がる」挙動をエミュレートする
        if value > 0.15:
            drift = (value - 0.15) * 0.8
            self._idi += drift
        
        report = ""
        if self._idi > self.alert_threshold:
            report = f"[ONTOS ALERT] Structural Inconsistency Detected (IDI: {self._idi:.3f})"

        return {
            "idi": self._idi,
            "report": report,
            "idi_map": {}  # 詳細なインバリアント・マップは非公開
        }