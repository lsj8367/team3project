# team3project

## github 사용방법
<!-- 
레포지토리 안에 오른쪽위에 Fork를 클릭하여 링크를 딴다.
이제는 자기 github 레포지토리로 이 프로젝트와 같은 이름이 생성된다.
fork 한후 fork한 주소를 git clone (내 remote repository URL) 하여 .git을 자신의 폴더에 생성한다.
git remote add 별칭 (중앙 원격 저장소 URL)    // 통상 별칭은 upstream
여기까지 되게되면 기본 설정은 완료

기본 설정이 완료되면 fork한 자신의 원격 저장소에 master 브랜치만 존재한다.


여기서 작업을 위해 branch를 별도로 나누어서 작업해야 한다.

주의사항!
다른 조원이 commit을 했을 경우가 있으니까
push를 하고싶다면 하던 작업까지 add와 commit을 하고
master 브랜치로 변경한다.
그 다음 git pull upstream master 로 먼저 최신정보를 받는다.
이 때 최신으로 받아온 master브랜치를 commit 까지 하던 branch에 먼저
git merge master 로 병합을 해준다.
그 다음 push를 해주면 된다.

올리는 순서
1. git add 파일 or git add . >>> .은 모두 Staged에 올린다.
2. git commit -m "커밋 메세지"


* 추가적으로 branch 만들었을때
 * git checkout master <<< 로컬 저장소의 master 브랜치로 이동
 * git merge 만든브랜치명
 * git push

github 사이트로 들어 와서 팀 프로젝트 저장소로 pull requests에 자신이 포크 된 저장소의
메시지와 함께 요청한다.
-->
