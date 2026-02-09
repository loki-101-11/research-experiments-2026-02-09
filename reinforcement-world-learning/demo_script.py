"""
Reinforcement World Model Learning (RWML) Demo Script
Paper: Reinforcement World Model Learning for LLM-based Agents (arXiv:2602.05842)

이 스크립트는 에이전트가 액션에 따른 다음 텍스트 상태를 예측하고, 
실제 결과와의 차이를 보상으로 사용하여 학습하는 RWML의 핵심 루프를 시뮬레이션합니다.
"""

import time

class WorldModel:
    def __init__(self, model_name="RWML-Agent"):
        self.model_name = model_name

    def predict_next_state(self, current_state, action):
        """
        [핵심 구현]: 액션 조건부 상태 예측 (Action-conditioned Prediction)
        LLM이 현재 상태와 취할 액션을 기반으로 결과 상태를 텍스트로 추론합니다.
        """
        print(f"[{self.model_name}] 현재 상태: '{current_state}', 액션: '{action}' 기반 다음 상태 예측 중...")
        # 실제 구현에서는 LLM 추론이 들어가는 부분
        if "불을 켠다" in action:
            return "방 안이 환해짐"
        return "변화 없음"

def simulate_environment(current_state, action):
    """
    실제 환경(Ground Truth) 시뮬레이션
    """
    if "불을 켠다" in action:
        return "방 안이 환해짐"
    return "변화 없음"

def calculate_reward(predicted, actual):
    """
    [핵심 구현]: Sim-to-Real Gap Reward
    예측과 실제 결과가 일치할수록 높은 보상을 부여하여 월드 모델의 정확도를 높입니다.
    """
    if predicted == actual:
        return 1.0  # 일치함
    return -1.0  # 불일치 (모델 수정 필요)

def train_step(state, action):
    model = WorldModel()
    
    # 1. 월드 모델의 예측
    predicted_state = model.predict_next_state(state, action)
    
    # 2. 실제 환경 실행
    actual_state = simulate_environment(state, action)
    
    # 3. 보상 계산 (Gap 기반)
    reward = calculate_reward(predicted_state, actual_state)
    
    print(f"예측: {predicted_state} | 실제: {actual_state} | 보상: {reward}")
    
    if reward > 0:
        print("-> 월드 모델이 환경을 정확히 이해하고 있습니다.")
    else:
        print("-> Sim-to-Real Gap 발생: 모델 업데이트(Policy Gradient 등)가 필요합니다.")

if __name__ == "__main__":
    print("--- RWML (Reinforcement World Model Learning) 시뮬레이션 시작 ---")
    train_step("어두운 방", "스위치를 눌러 불을 켠다")
    print("--- 시뮬레이션 종료 ---")
