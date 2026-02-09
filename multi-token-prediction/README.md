# Multi-Token Prediction via Self-Distillation

이 연구는 기존의 순차적인 토큰 생성 방식(Autoregressive)의 속도 한계를 극복하기 위해, 하나의 모델이 한 번에 여러 토큰을 예측하도록 온라인 자기 증류(Self-Distillation) 기법을 사용하여 학습하는 방법을 다룹니다.

## 핵심 개념
- **Beyond Speculative Decoding**: 별도의 보조 모델(Draft Model) 없이, 메인 모델 자체가 멀티 토큰 예측 능력을 갖추도록 학습합니다.
- **Online Self-Distillation**: 이미 학습된 Autoregressive 모델을 Teacher로 삼아, 여러 위치의 토큰을 동시에 예측하도록 Student(자기 자신)를 증류 학습시킵니다.
- **Inference Speedup**: 한 번의 Forward pass로 N개의 토큰을 생성할 수 있어 추론 속도가 획기적으로 향상됩니다.

## 구현 상세 (model_stub.py)
- `MTPDistiller` 클래스: 표준 다음 토큰 예측(Next Token Prediction) 헤드 외에 추가적인 멀티 토큰 예측 헤드를 시뮬레이션합니다.
- `distillation_loss`: Teacher 모델의 확률 분포와 Student의 멀티 토큰 예측 분포 사이의 차이를 최소화하는 로직.
- **Paper Reference**: [arXiv:2602.06019](https://arxiv.org/abs/2602.06019)
