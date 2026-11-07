<<<<<<< HEAD
# codyssey-1
1-1과제 나만의 작업실 꾸미기
# Docker 워크스테이션 구축 과제

## 1) 프로젝트 개요
Linux 터미널 기본 조작부터 Docker 기반 웹서버 배포,
Git/GitHub 연동까지 개발 워크스테이션 환경을 구축한다.

## 2) 실행 환경
- OS: Windows 11
- Shell: PowerShell 7.x
- Docker: (docker --version 결과)
- Git: (git version 2.56.0.windows.4 결과)

## 3) 수행 체크리스트
- [x] 터미널 기본 조작 → [logs/01-terminal.txt](./logs/01-terminal.txt)
- [x] 권한 변경 실습 → [logs/02-permission.txt](./logs/02-permission.txt)
- [x] Docker 설치/점검 → [logs/03-docker-info.txt](./logs/03-docker-info.txt)
- [x] Docker 운영 명령 → [logs/04-docker-ops.txt](./logs/04-docker-ops.txt)
- [x] Dockerfile 빌드/실행 → [logs/05-build-run.txt](./logs/05-build-run.txt)
- [x] 포트 매핑 접속 2회 → [screenshots/](./screenshots/)
- [x] 바인드 마운트 반영 → [logs/06-mount.txt](./logs/06-mount.txt)
- [x] 볼륨 영속성 → [logs/07-volume.txt](./logs/07-volume.txt)
- [x] Git/GitHub 연동 → [logs/08-git.txt](./logs/08-git.txt)

## 4) 검증 방법
### Docker 버전 확인
```bash
$ docker --version
Docker version 29.9.2, build a82e528
```

## 5) 볼륨(데이터 영속성) 구성
### 사용한 볼륨 정보
| 항목 | 값 |
|------|-----|
| 볼륨 이름 | mydata |
| 마운트 경로(컨테이너 내부) | /data |
| 테스트 이미지 | ubuntu |

### 재현 명령 (데이터 영속성 검증 절차)
```powershell
# 1. 볼륨 생성
docker volume create mydata

# 2. 볼륨을 마운트한 컨테이너 실행
docker run -d --name vol-test -v mydata:/data ubuntu sleep infinity

# 3. 볼륨에 데이터 작성
docker exec vol-test sh -c "echo hello > /data/file.txt"

# 4. 컨테이너 강제 삭제 (데이터는 볼륨에 남음)
docker rm -f vol-test

# 5. 새 컨테이너에서 같은 볼륨 재마운트
docker run -d --name vol-test2 -v mydata:/data ubuntu sleep infinity

# 6. 데이터 보존 확인 → "hello" 출력되면 성공
docker exec vol-test2 cat /data/file.txt
```

## 6) 포트 매핑 접속 증거
### 8080 접속
![8080 접속](.\screenshots\8080-access.png)

### 8081 접속
![8081 접속](.\screenshots\8081-access.png)

## 트러블슈팅

### TS-0X. git push 거부 (rejected: fetch first) + README 병합 충돌

**증상**
git push -u origin main 실행 시 아래 에러 발생:

  ! [rejected]        main -> main (fetch first)
  error: failed to push some refs to '...1-1.git'
  hint: Updates were rejected because the remote contains work that
        you do not have locally.

**원인**
- 새 원격 저장소(1-1)를 GitHub에서 README를 포함해 생성함
- 그 결과 원격에 로컬에 없는 커밋이 존재 → 로컬 이력과 불일치(diverged)
- git은 원격 내용을 덮어쓰지 않도록 push를 거부함

**해결**
1) 원격 이력을 먼저 가져와 병합 (서로 다른 이력이므로 옵션 추가)
   git pull origin main --allow-unrelated-histories

2) README.md 에서 add/add 병합 충돌 발생
   CONFLICT (add/add): Merge conflict in README.md
   → README.md 를 열어 <<<<<<< ======= >>>>>>> 표시 제거 후
     최종 내용으로 정리

3) 충돌 해결본 커밋
   git add README.md
   git commit -m "Merge: README 충돌 해결"

4) 재푸시 성공
   git push -u origin main
   → 5339517..51ddcd4  main -> main

**교훈**
- 기존 파일을 올릴 새 원격 저장소는 README/라이선스 없이
  "빈 저장소"로 생성하면 충돌을 피할 수 있다


### 트러블슈팅 2 빌드 실패: Dockerfile을 찾을 수 없음
- 증상: docker build 시 "open Dockerfile: no such file or directory"
- 원인: 잘못된 작업 디렉토리(C:\Users\user)에서 빌드함.
        Dockerfile은 프로젝트 루트(C:\codyssey_hyck)에만 존재.
- 확인: ls Dockerfile 로 현재 폴더에 파일 유무 점검
- 해결: cd C:\codyssey_hyck 로 이동 후 docker build -t my-web:1.0 . 재실행
