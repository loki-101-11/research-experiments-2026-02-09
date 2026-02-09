# Horizon Benchmark for Long-term Planning

Horizon(또는 OdysseyBench, LORE 등)은 LLM 에이전트가 단기적인 질의응답을 넘어, 수십 단계의 복잡한 절차와 장기적인 계획(Long-term Planning)이 필요한 작업을 얼마나 잘 수행하는지 측정하는 벤치마크입니다.

## 핵심 개념
- **Long-Horizon Tasks**: 수백 개의 단계를 거쳐야 하거나, 수 시간 이상의 실행 시간이 필요한 복잡한 워크플로우를 평가합니다.
- **Reasoning over Time**: 작업이 진행됨에 따라 변화하는 환경을 인지하고, 초기 계획을 동적으로 수정하는 능력을 검증합니다.
- **Real-world Tool Use**: 단순한 텍스트 생성이 아닌, 실제 파일 시스템, API, 웹 브라우저 등을 복합적으로 사용하는 능력을 측정합니다.

## 구현 상세 (benchmark_config.json)
- 벤치마크의 평가 항목(Metric), 시나리오(Scenario), 그리고 에이전트가 사용할 수 있는 도구(Tools) 정의.
- **Success Criteria**: 최종 목표 달성 여부뿐만 아니라 효율성(Step count), 비용(Token usage) 등을 종합 평가합니다.
- **Reference**: OpenAI/Anthropic의 최근 에이전트 평가 프레임워크와 유사한 구조를 가집니다.
