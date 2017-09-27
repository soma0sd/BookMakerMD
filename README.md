# BookMakerMD

북메이커MD는 교재 집필에 최적화 되어 있는 마크다운 기반의 문서제작 도구입니다.

버전 0.0.1b에서는 다음의 단축 기능을 지원합니다.

* 저장(<kbd>Ctrl</kbd>+<kbd>S</kbd>)
* 불러오기(<kbd>Ctrl</kbd>+<kbd>S</kbd>)

이 프로그램이 저장하고 불러오는 파일의 확장자는 ``*.mdbk``입니다. 이 파일은 tar 형식으로 압축되어 있으며, 압축파일 관리 프로그램을 통해서 손쉽게 내용물을 열수 있습니다.


## 설치

현재 PyInstaller를 지원하지 않는 문제로 아래의 응용프로그램과 패키지를 요구합니다. (0.1.0b 이후에는 응용프로그램 형태로도 배포할 예정입니다.)

**응용프로그램**
* python 3.4 이상

**패키지**
* ``pip install PyQt5``
* ``pip install markdown``

## 실행

0.0.1b 릴리즈를 다운로드 한 뒤 ``BookMaker.zip``의 압축을 풀어 나오는 pyBookMakerMD.py를 ``python.exe``혹은 ``pythonw.exe``(추천)으로 실행합니다.

## 라이센스

GPL 3.0 라이센스를 따릅니다.
