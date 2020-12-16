# team3project

## github 사용방법

* 레포지토리 안에 오른쪽위에 Fork를 클릭하여 링크를 딴다.
  * 이제는 자기 github 레포지토리로 이 프로젝트와 같은 이름이 생성된다.
  * fork 한후 fork한 주소를 git clone (내 remote repository URL) 하여 .git을 자신의 폴더에 생성한다.
* git remote add 별칭 (중앙 원격 저장소 URL)    // 통상 별칭은 upstream
 * 여기까지 되게되면 기본 설정은 완료

기본 설정이 완료되면 fork한 자신의 원격 저장소에 master 브랜치만 존재한다.


여기서 작업을 위해 branch를 별도로 나누어서 작업하고
때에 따라서는 나누지 않아도 무방하다.

### 주의사항!
### 맨 먼저 위에서 중앙원격 저장소 별칭을 들고 원격 저장소에 업데이트된 자료를 받아와야한다.
### git pull upstream master 로 먼저 최신정보를 받는다.

### 올리는 순서
##### 1. git add 파일 or git add . >>> .은 모두 Staged에 올린다.
##### 2. git commit -m "커밋 메세지"


* 추가적으로 branch 만들었을때
 * git checkout master <<< 로컬 저장소의 master 브랜치로 이동
 * git merge 만든브랜치명
 * git push
* 그냥 마스터에서 진행
 * git push 진행

github 사이트로 들어 와서 팀 프로젝트 저장소로 pull requests에 자신이 포크 된 저장소의
메시지와 함께 요청한다.
