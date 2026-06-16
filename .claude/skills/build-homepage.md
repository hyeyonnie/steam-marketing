---
name: build-homepage
description: version04 홈페이지 업데이트 작업을 homepage-builder 에이전트에게 위임한다. 워크트리(worktree-homepage-update 브랜치)에서 실행해야 한다.
---

<skill>
# build-homepage 스킬

이 스킬은 `.claude/agents/homepage-builder.md` 에이전트를 사용해 version04 홈페이지 업데이트를 수행합니다.

## 사용 에이전트

| 에이전트 | 역할 |
|---|---|
| `homepage-planner` | 기획: 섹션 구성·소스 데이터·확정 의사결정 관리, 기획안 md 작성 (코드 없음) |
| `homepage-builder` | 구현: 마크업·스타일·i18n 기술 구현 (HTML/CSS/JS), 기획안을 따름 |
| `english-copywriter` | 영어 마케팅 카피 작성·교정 (index.html + app.js의 en 블록) |
| `korean-copywriter` | 한국어 마케팅 카피 작성·교정 (app.js의 ko 블록) |

> 역할 분리: **기획(planner) → 구현(builder) → 카피(copywriter)**. planner가 작성한
> `version04/홈페이지_업데이트_기획안.md`가 단일 출처(SSOT)이며, builder/copywriter는 이를 참조한다.

## 실행 방법

1. 현재 워크트리(`worktree-homepage-update`)에 있는지 확인
2. (기획 변경이 있으면) `homepage-planner` 에이전트로 기획안(`version04/홈페이지_업데이트_기획안.md`)을 갱신
3. `homepage-builder` 에이전트를 `version04/` 디렉토리 기준으로 호출해 기획안대로 구조/마크업/스타일/i18n 골격을 구현
4. 골격이 완성되면 카피 다듬기:
   - `english-copywriter` 에이전트로 영어 카피 교정 (index.html 기본값 ↔ app.js en 블록 동기화 유지)
   - `korean-copywriter` 에이전트로 한국어 카피 교정 (app.js ko 블록, en과 1:1 키 정합성 유지)
5. 각 에이전트 정의파일(`.claude/agents/*.md`)의 지시문을 따름

## 작업 범위

에이전트 정의파일에 명시된 순서대로 우선순위에 따라 구현:
- Priority 1: i18n 시스템 + 언어 토글 + Proof/Key Stats 섹션
- Priority 2: What We Do 4대 서비스 + Results 섹션
- Priority 3: Global PR Network + Why Choose Us 6개 항목
- Priority 4: Process 6단계 + Footer "HypePotions by Sentience"

## 완료 후

- 변경사항 커밋: `git add version04/ && git commit`
- 검토 후 main에 merge 여부 결정
</skill>
