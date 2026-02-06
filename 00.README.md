# ONTOS Engine V12.3  
**Detecting Discontinuous Hallucinations via Structural Inconsistency**

---

## Overview

**ONTOS (Structural Inconsistency Detection Engine)** is a multi-scale monitoring system designed to detect *structural discontinuities* in data streams.

Unlike conventional anomaly detection—which reacts to surface-level output changes—ONTOS focuses on **logical topology**:  
it detects *when internal structure begins to break*, **before** observable failure occurs.

ONTOS computes a leading indicator called the **Inherent Discrepancy Index (IDI)**, which measures friction between multiple abstraction scales.

This repository demonstrates that **LLM-style hallucinations can be detected as structural events**, not semantic classification problems.

---

## Key Insight

> Hallucination is not an error in output.  
> It is a **collapse of cross-scale structural consistency**.

---

## Experimental Results

### 1. Numerical “Ghost Drift” Test

- Input signal remains statistically stable
- Baseline delta fails to detect anomalies
- **ONTOS IDI rises gradually**
- Structural erosion detected **5–10 steps before collapse**

**Conclusion:**  
ONTOS acts as a *leading indicator*, not a reactive alarm.

---

### 2. Textual Hallucination Test

- Simulated semantic entropy stream
- Stable narrative → logic drift → discontinuous hallucination
- **IDI crosses threshold before semantic failure is explicit**

**Conclusion:**  
Logical leaps in text manifest as *structural discontinuities*, detectable without labels.

---

## Technical Features

- **Multi-Scale Probing**  
  Polynomial Axioms (degree 1–5) monitor structure at different abstraction levels.

- **Topological Invariants**  
  Cross-scale consistency is tracked to expose “quiet contradictions” invisible to single-scale models.

- **Leading Indicator Design**  
  IDI reacts to *structural friction*, not magnitude or variance.

---

## Usage / How to Run

### Requirements

- Python 3.9+  
- NumPy  
- Matplotlib  

```bash
pip install numpy matplotlib
```

### 1. Numerical Ghost Drift Test
```bash
python demo_numeric.py
```

Expected behavior:  
	•	Baseline delta stays inconclusive  
	•	ONTOS IDI increases smoothly  
	•	Alert triggers before visible collapse  

Outputs:  
	•	ontos_diagnostic_data.txt  
	•	ontos_v12_3_final_polish.png  


### 2. Textual Hallucination Detection Test
```bash
python demo_text_hallucination.py
```

Expected behavior:    
	•	Structural erosion detected before hallucination  
	•	IDI exceeds threshold prior to semantic breakdown  

Outputs:  
	•	ontos_text_hallucination_diagnostic.txt  
	•	ontos_text_test_visual.png  


### Understanding the Output

Each step() returns:

{  
    "idi": float,        # Global structural instability  
    "report": str,      # Diagnostic message (empty if stable)  
    "idi_map": dict     # Per-invariant IDI (abstracted)  
}

Interpretation:  
	•	IDI < threshold → structurally coherent  
	•	IDI rising → hidden erosion  
	•	IDI > threshold → discontinuity detected


### About the Public Stub

This repository exposes a behavior-preserving stub of ONTOS.

Guaranteed:  
	•	Same public interface  
	•	Comparable IDI dynamics  
	•	Reproducible detection timing  

Intentionally hidden:  
	•	Internal belief mechanics  
	•	Structural memory rules  
	•	Exact invariant topology  

Reproducibility without reversibility



### Reproducibility Statement

All results in this repository can be reproduced by running the provided scripts.

While the ONTOS core is not release,
the behavioral claims, timing, and detection characteristics are independently verifiable.

This repository is suitable for:  
	•	Independent validation  
	•	Safety research  
	•	Alignment discussion  
	•	Industrial feasibility review  

## Future Work
	•	Dataset purification via structural filtering  
	•	Training cost reduction by excluding high-belief samples  
	•	Real-time detection of structural mislearning in LLM training loops  


# ONTOS Engine V12.3 不連続ハルシネーションの構造検知エンジン

## 概要
ONTOS（Structural Inconsistency Detection Engine）は、
データストリームの背後にある論理構造の不連続性を検知する多重尺度エンジンです。

従来の異常検知が「結果」に反応するのに対し、
ONTOSは構造が壊れ始めた瞬間を捉えることを目的としています。

その指標が IDI（Inherent Discrepancy Index） です。

## 核心的な考え方
ハルシネーションは「間違い」ではない。
抽象度間の整合性が崩壊した構造イベントである。

## 実験結果
### 1. 数値的ゴースト・ドリフト試験
•入力は統計的に安定  
•ベースラインでは異常検知不可  
•IDIが先行的に上昇  
•崩壊の5〜10ステップ前に検知

### 2. 言語的ハルシネーション試験
•安定文脈 → 論理ドリフト → 不連続ジャンプ  
•意味破綻の前にIDIが閾値を突破

## 技術的特徴
•多重尺度プロービング  
 1次〜5次の構造Axiomが同時監視  
•トポロジカル・インバリアント  
 尺度間の矛盾を直接検知  
•先行指標設計  
 統計量ではなく構造摩擦に反応

## 使い方

### 必要環境
•Python 3.9+  
•NumPy  
•Matplotlib  

```bash
pip install numpy matplotlib
```

### 数値テスト

```bash
python demo_numeric.py
```


### テキストハルシネーション検証

```bash
python demo_text_hallucination.py
```


### 公開スタブについて

このリポジトリは 再現可能なスタブ実装 を提供します。
•振る舞いは再現可能
•内部構造は非公開
•解析耐性を保持

再現性はあるが、逆解析はできない設計です。

### 再現性について
本リポジトリの全ての主張は
付属スクリプトの実行により検証可能です。

### 今後の展望  
•学習データの構造的浄化  
•再学習コストの削減  
•LLM学習中の誤学習リアルタイム検知  
