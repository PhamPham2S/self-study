# 전이 학습(Transfer Learning) 및 PEFT 기법 성능/효율성 심층 비교 분석

## 1. 프로젝트 개요 (Overview)

본 프로젝트는 **[특정 도메인, 예: 금융/법률]** 텍스트 데이터를 활용하여, 다양한 전이 학습(Transfer Learning) 기법과 최신 경량화 튜닝(PEFT) 방법론의 성능과 자원 효율성을 비교 분석합니다.
전통적인 Fine-tuning부터 최신 LoRA, Prompt Tuning까지 단계별로 적용하며, **모델 성능(Accuracy)과 컴퓨팅 비용(Memory, Time) 간의 Trade-off**를 규명하는 것을 목표로 합니다.

* **진행 기간:** 202X.XX.XX ~ 202X.XX.XX
* **수행 환경:** Google Colab Pro+ (GPU: A100/V100), VS Code
* **사용 언어 및 라이브러리:** Python, PyTorch, Hugging Face Transformers, PEFT, Datasets

## 2. 데이터셋 (Dataset)

* **데이터 명:** [데이터셋 이름, 예: KR-FinBert-SC]
* **출처:** [링크 또는 출처 기재]
* **데이터 크기:** 학습(Train) `[ ]`건, 검증(Validation) `[ ]`건, 테스트(Test) `[ ]`건
* **Task:** [예: 문장 다중 분류 (Sentiment Analysis)]

## 3. 실험 방법론 (Methodology)

본 프로젝트는 동일한 Backbone 모델(`[예: KLUE-RoBERTa-large 또는 Llama-3-8b]`)을 기준으로 아래 4가지 방식의 학습 전략을 적용했습니다.

### Experiment 1: Baseline & Traditional Transfer Learning

* **Feature Extraction (Frozen Backbone):** 모델의 가중치를 고정하고(Freeze), Classifier Head만 학습.
* **Full Fine-tuning:** 모델의 모든 파라미터를 업데이트.

### Experiment 2: Domain Adaptation (Continued Pretraining)

* Task 수행 전, 도메인 특화 코퍼스(Unlabeled Text)를 사용하여 **MLM(Masked Language Modeling)** 방식으로 추가 사전 학습을 진행.
* 이후 Downstream Task에 대해 Fine-tuning 수행하여 성능 변화 관찰.

### Experiment 3: Parameter-Efficient Fine-Tuning (PEFT)

적은 수의 파라미터만 학습하여 효율성을 극대화하는 기법들을 적용.

* **LoRA / QLoRA:** Low-Rank Adaptation 적용 (Rank `r=[ ]` 설정).
* **Soft Prompts (Prompt Tuning):** 입력 임베딩 층에 학습 가능한 가상 토큰 추가.
* **Adapter:** Transformer 레이어 사이에 Adapter Layer 삽입. (선택 사항)
* **Prefix-Tuning:** 각 레이어의 Key, Value에 Prefix 벡터 추가. (선택 사항)

## 4. 실험 결과 (Experimental Results)

각 방법론에 따른 학습 파라미터 수, 자원 소모량, 최종 성능 비교표입니다.

| 실험 기법 (Method) | 학습 파라미터 수 (Trainable Params) | GPU 메모리 사용량 (Peak Memory) | 학습 소요 시간 (Training Time) | 정확도 (Accuracy) | F1 Score |
| --- | --- | --- | --- | --- | --- |
| **Feature Extraction** | `[ ]` | `[ ]` GB | `[ ]` min | `[ ]` | `[ ]` |
| **Full Fine-tuning** | `[ ]` | `[ ]` GB | `[ ]` min | `[ ]` | `[ ]` |
| **Continued Pretraining + FT** | `[ ]` | `[ ]` GB | `[ ]` min | `[ ]` | `[ ]` |
| **LoRA (PEFT)** | `[ ]` | `[ ]` GB | `[ ]` min | `[ ]` | `[ ]` |
| **Prompt Tuning (PEFT)** | `[ ]` | `[ ]` GB | `[ ]` min | `[ ]` | `[ ]` |

> *참고: 학습 파라미터 수는 전체 모델 파라미터 대비 약 `[ ]`% 수준으로 감소함.*

### 학습 곡선 (Learning Curve)

*Loss 및 Accuracy 변화 그래프 이미지 삽입 예정*
`![Learning Curve Plot](./assets/learning_curve_placeholder.png)`

## 5. 분석 및 고찰 (Analysis & Conclusion)

### 5.1. 성능 관점 (Performance)

* Full Fine-tuning 대비 PEFT 기법들의 성능 하락폭이 `[크다/작다/거의 없다]`.
* 특히 `[특정 기법]`의 경우 도메인 지식이 필요한 상황에서 가장 우수한 성능을 보였다.
* Continued Pretraining을 수행했을 때 `[ ]`%의 성능 향상이 있었으며, 이는 도메인 적응의 중요성을 시사한다.

### 5.2. 효율성 관점 (Efficiency)

* LoRA를 적용했을 때 메모리 사용량이 `[ ]`% 절감되어 Colab 무료 버전에서도 구동 가능함을 확인했다.
* 학습 속도 면에서는 `[Feature Extraction]`이 가장 빨랐으나, 성능과의 균형(Trade-off)을 고려하면 `[추천하는 기법]`이 가장 합리적인 선택지로 보인다.

## 6. 디렉토리 구조 (Directory Structure)

```bash
.
├── assets/                 # 결과 이미지 및 그래프 저장
├── data/                   # 데이터셋 (Git ignore 처리됨)
├── notebooks/              # Google Colab 실습 노트북 (.ipynb)
│   ├── 01_feature_extraction.ipynb
│   ├── 02_full_finetuning.ipynb
│   ├── 03_continued_pretraining.ipynb
│   └── 04_peft_lora_tuning.ipynb
├── src/                    # 전처리 및 유틸리티 스크립트 (.py)
├── results/                # 모델 체크포인트 및 로그
└── README.md

```

## 7. 참고 문헌 (References)

* [Paper] LoRA: Low-Rank Adaptation of Large Language Models
* [Paper] The Power of Scale for Parameter-Efficient Prompt Tuning
* [Link] Hugging Face PEFT Documentation

---

### 작성 팁 (Tip)

1. **결과 채우기:** 실습을 진행하면서 위 표의 빈칸을 하나씩 채워 나가는 것을 목표로 하십시오.
2. **`notebooks` 폴더:** Colab에서 작업한 파일은 기능별(01, 02, 03...)로 나누어 저장한 뒤, VS Code를 통해 이 폴더에 정리해서 올리면 깔끔합니다.
3. **이미지:** Colab에서 `plt.savefig()` 등으로 저장한 그래프 이미지를 `assets` 폴더에 넣고 경로를 연결하면 됩니다.