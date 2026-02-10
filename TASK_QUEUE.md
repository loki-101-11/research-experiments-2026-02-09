# TASK_QUEUE.md - Self-Verification Development Tasks

이 문서는 Opus가 작성하고, Qwen3-coder-next가 실행하는 작업 큐입니다.
각 작업은 짧은 컨텍스트(단일 파일, 단일 기능)로 완료 가능하게 설계됩니다.

## 🎯 목표
LLM 리서치 구현체들에 자체 검증(Self-Verification) 시스템 구축

---

## 📋 작업 큐 (순서대로 실행)

### ✅ COMPLETED
(완료된 작업들이 여기로 이동됩니다)

---

### 🔄 IN_PROGRESS
(현재 진행 중인 작업)

---

### 📝 PENDING

#### TASK-001: 테스트 프레임워크 설정
- **파일**: `tests/conftest.py`, `tests/__init__.py`
- **목표**: pytest 기반 테스트 환경 구축
- **작업 내용**:
  1. `tests/` 디렉토리 생성
  2. `conftest.py`에 공통 fixture 정의
  3. `requirements-test.txt` 생성 (pytest, pytest-cov)
- **검증**: `pytest --collect-only` 실행 성공

#### TASK-002: MTP 모델 유닛 테스트 작성
- **파일**: `tests/test_mtp.py`
- **목표**: MTPModelStub 클래스 테스트
- **작업 내용**:
  1. `test_init()`: 초기화 검증
  2. `test_forward()`: 토큰 예측 출력 형식 검증
  3. `test_distillation_loss()`: 손실 함수 호출 검증
- **검증**: `pytest tests/test_mtp.py -v` 통과

#### TASK-003: RWML 모델 유닛 테스트 작성
- **파일**: `tests/test_rwml.py`
- **목표**: WorldModel 클래스 테스트
- **작업 내용**:
  1. `test_predict_next_state()`: 상태 예측 검증
  2. `test_calculate_reward()`: 보상 계산 검증
  3. `test_train_step()`: 학습 스텝 통합 검증
- **검증**: `pytest tests/test_rwml.py -v` 통과

#### TASK-004: 자동 검증 러너 스크립트
- **파일**: `scripts/run_verification.py`
- **목표**: 모든 테스트를 실행하고 결과를 JSON으로 출력
- **작업 내용**:
  1. pytest를 subprocess로 실행
  2. 결과를 `verification_results.json`에 저장
  3. 실패 시 상세 로그 포함
- **검증**: `python scripts/run_verification.py` 실행 후 JSON 파일 생성

#### TASK-005: CI 파이프라인 설정
- **파일**: `.github/workflows/verify.yml`
- **목표**: Push 시 자동 검증 실행
- **작업 내용**:
  1. Python 3.11 환경 설정
  2. 의존성 설치
  3. 테스트 실행 및 결과 리포트
- **검증**: YAML 문법 검증 통과

#### TASK-006: Horizon Benchmark 테스트 스위트
- **파일**: `tests/test_horizon.py`
- **목표**: 벤치마크 설정 파일 검증
- **작업 내용**:
  1. JSON 스키마 검증
  2. 시나리오 ID 유일성 검증
  3. 필수 필드 존재 검증
- **검증**: `pytest tests/test_horizon.py -v` 통과

#### TASK-007: 코드 커버리지 리포트
- **파일**: `scripts/coverage_report.py`
- **목표**: 커버리지 측정 및 리포트 생성
- **작업 내용**:
  1. pytest-cov로 커버리지 측정
  2. HTML 리포트 생성 (`coverage_html/`)
  3. 커버리지 임계값 체크 (최소 70%)
- **검증**: 커버리지 리포트 파일 생성 확인

#### TASK-008: 통합 테스트 - 전체 파이프라인
- **파일**: `tests/test_integration.py`
- **목표**: 세 모듈 간 통합 동작 검증
- **작업 내용**:
  1. MTP → RWML 데이터 흐름 테스트
  2. Horizon 시나리오 기반 시뮬레이션
  3. End-to-end 실행 검증
- **검증**: `pytest tests/test_integration.py -v` 통과

---

## 📊 진행 상태
- 총 작업: 8개
- 완료: 0개
- 진행 중: 0개
- 대기: 8개

## 🔧 실행 규칙
1. 한 번에 하나의 TASK만 진행
2. TASK 완료 시 COMPLETED로 이동하고 다음 TASK 시작
3. 테스트 실패 시 해당 TASK에서 수정 후 재검증
4. 모든 TASK 완료 시 git commit & push
