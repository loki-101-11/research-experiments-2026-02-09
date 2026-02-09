# Reinforcement World Model Learning for LLM-based Agents (RWML)

이 연구는 LLM 기반 에이전트가 텍스트 환경에서 액션에 따른 다음 상태를 예측하는 '월드 모델'을 스스로 학습하는 프레임워크를 다룹니다.

## 핵심 개념
- **Action-Conditioned Prediction**: 에이전트가 특정 액션을 취했을 때 월드가 어떻게 변할지(Next State)를 예측합니다.
- **Sim-to-Real Gap Rewards**: 단순히 다음 토큰을 예측하는 SFT 방식에서 벗어나, 실제 환경의 피드백과 모델의 예측 사이의 차이를 보상으로 사용하여 모델을 최적화합니다.
- **Textual States**: 모든 상태와 액션은 텍스트로 정의되며, 이는 LLM이 복잡한 추론을 월드 모델링에 활용할 수 있게 합니다.

## 구현 상세 (demo_script.py)
- `WorldModel` 클래스: 상태(state)와 액션(action)을 입력받아 다음 상태를 예측하는 LLM 기반 모델 구조.
- `train_step`: 예측된 상태와 실제 환경 상태 사이의 차이를 계산하여 보상을 생성하고, 이를 통해 모델을 업데이트하는 로직(의사 코드 포함).
- **Paper Reference**: [arXiv:2602.05842](https://arxiv.org/abs/2602.05842)
