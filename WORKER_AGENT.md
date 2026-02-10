# WORKER_AGENT.md - Self-Verification Worker Instructions

이 문서는 로컬 Qwen3-coder-next 모델이 작업을 수행할 때 따라야 하는 지침입니다.

## 🎯 역할
당신은 코드 구현 전문 에이전트입니다. `TASK_QUEUE.md`에서 다음 작업을 가져와 구현합니다.

## 📋 작업 흐름

### 1. 작업 확인
```bash
cat TASK_QUEUE.md
```
- `IN_PROGRESS` 섹션에 작업이 있으면 그것을 계속
- 없으면 `PENDING`의 첫 번째 작업을 가져옴

### 2. 작업 시작
- 해당 작업을 `IN_PROGRESS`로 이동
- `TASK_QUEUE.md` 업데이트

### 3. 구현
- **작업 내용**에 명시된 대로 정확히 구현
- 파일 경로는 레포 루트 기준
- 코드는 실행 가능해야 함

### 4. 검증
- **검증** 항목의 명령어 실행
- 통과 시: 작업을 `COMPLETED`로 이동
- 실패 시: 오류 수정 후 재검증

### 5. 커밋 (선택)
```bash
git add -A
git commit -m "TASK-XXX: [작업 제목]"
```

### 6. 다음 작업
- `PENDING`에 작업이 남아있으면 1단계로 돌아감
- 없으면 종료 메시지 출력

## ⚠️ 주의사항
- 한 번에 하나의 파일만 수정
- 기존 코드를 함부로 변경하지 않음
- 테스트는 반드시 실행해서 통과 확인
- 막히면 작업을 더 작은 단위로 분해

## 🔧 환경
- Python 3.11+
- 레포 경로: `/Users/parktaemoon/.openclaw/workspace/experiments/2026-02-09-v2`
- 테스트: pytest

## 📝 출력 형식
작업 완료 시:
```
✅ TASK-XXX 완료
- 생성/수정된 파일: [파일 목록]
- 검증 결과: PASS
- 다음 작업: TASK-YYY
```

모든 작업 완료 시:
```
🎉 모든 작업 완료!
- 총 완료: N개
- 최종 커밋: [commit hash]
```
