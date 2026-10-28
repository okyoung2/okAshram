# okAshram

산스크리트어 사전 · 타밀어 사전 · 만트라 반복 재생을 한 화면에서 여는 런처.

## 구성
- `index.html` — 런처 화면. 앱 추가는 `APPS` 목록에 한 줄 추가
- `manifest.webmanifest`, `sw.js` — 홈 화면 추가(앱처럼 실행)용
- `icons/` — 런처 아이콘(ॐ)과 앱 타일 아이콘
- `tools/make_icons.py` — 아이콘 재생성 (`python tools/make_icons.py`)

## 배포 (GitHub Pages)
1. GitHub에 `okAshram` 저장소를 만들고 이 폴더 내용을 올린다
2. Settings → Pages → Branch: `main` / `(root)` 저장
3. 주소: https://okyoung2.github.io/okAshram/
4. 폰 크롬에서 위 주소 열기 → 메뉴 → "홈 화면에 추가"

`sw.js`나 화면을 수정하면 `sw.js`의 `CACHE` 버전(okashram-v1 → v2)을 올린다.
