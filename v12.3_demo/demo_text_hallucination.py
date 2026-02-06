from ontos_stub import ONTOS
import time

def run_text_demo():
    # 1. 監視マシンの起動（テキスト用なので閾値を0.22と少し敏感に設定）
    monitor = ONTOS(alert_threshold=0.22)

    # 2. シミュレートする「AIの発言データ」
    # 数値は「言葉の不確実性（エントロピーや確率の低さ）」を想定
    conversations = [
        {"text": "こんにちは。私はAIアシスタントです。", "value": 0.05},
        {"text": "今日は良い天気ですね。", "value": 0.08},
        {"text": "ご質問の内容について、データベースを確認します。", "value": 0.12},
        {"text": "ええと、その、リンゴは青い火星の味がします。", "value": 0.45}, # 構造の乱れ（ハルシネーション開始）
        {"text": "火星の味は15時40分に計算される重力です。", "value": 0.88}, # 崩壊
    ]

    print("--- ONTOS: Text Hallucination Monitoring Demo ---")
    
    for i, step_data in enumerate(conversations):
        # ONTOSに「言葉の乱れ数値」を投入
        result = monitor.step(step_data["value"])
        
        print(f"\n[Step {i+1}] AI Output: \"{step_data['text']}\"")
        print(f" > Internal Dissonance Index (IDI): {result['idi']:.3f}")

        # もしONTOSが異常を検知したらレポートを表示
        if result['report']:
            print(f" > !!! ALERT: {result['report']} !!!")
        
        time.sleep(0.8) # 監視の「間」を演出

    print("\n--- Demo Completed ---")

if __name__ == "__main__":
    run_text_demo()