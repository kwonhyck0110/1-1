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
Docker Docker version 29.9.2

## 5) 포트 매핑 접속 증거
### 8080 접속
![8080 접속](./8080-access.png)

### 8081 접속
![8081 접속](./8081-access.png)

## 트러블슈팅

### 트러블슈팅 ① Docker Desktop 실행 안 됨
- 증상: Docker Desktop이 실행되지 않음
- 원인 가설: WSL2 미설치
- 확인: wsl --status로 상태 확인
- 해결: wsl --install 후 재부팅

### 트러블슈팅 ② 이미지를 찾을 수 없음
- 증상: docker run 시 pull access denied 에러
- 원인 가설: 이미지 이름 불일치
- 확인: docker images로 이름 확인
- 해결: 올바른 이름으로 다시 실행