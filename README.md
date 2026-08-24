# PyQt 계산기

PyQt5로 만든 GUI 계산기. Qt Designer로 화면을 잡고(`calculator.ui`) 파이썬에서 로드해 동작을 붙였다.

![실행 화면](docs/screenshot.png)

---

## 구성

```
calculator.ui    Qt Designer로 만든 화면 정의
calculator.py    .ui 로드 + 버튼 동작
```

화면과 로직이 분리돼 있어 배치를 바꿀 때는 Qt Designer에서 `.ui`만 수정하면 된다.

`.ui`는 스크립트 파일 위치를 기준으로 찾는다 — 어느 폴더에서 실행하든 동작한다.

```python
UI_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calculator.ui")
from_class = uic.loadUiType(UI_PATH)[0]
```

---

## 실행

```bash
pip install PyQt5
python calculator.py
```

---

## 라이선스

MIT
