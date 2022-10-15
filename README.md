# Django 페어프로그래밍 03

## 결과물✨
- 회원가입 & 로그인

![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/74820869/195977495-0c32fbf1-3d96-40b2-9b3b-aaf4d3e65884.gif)

- 글작성/읽기/수정/삭제

![ezgif com-gif-maker (6)](https://user-images.githubusercontent.com/74820869/195977559-99094efb-83df-4178-ace6-5c583d901090.gif)

- 회원 목록 & 회원 정보 수정

![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/74820869/195978020-a039e02c-9cfb-45e8-a4fd-49f84df4015e.gif)

- 로그아웃 & 회원탈퇴

![ezgif com-gif-maker (8)](https://user-images.githubusercontent.com/74820869/195978094-5dd4c620-05c4-406a-9290-f816a3247508.gif)


## 목표📚

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- **CRUD** 구현
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)

## 요구 사항📄
### 1. 깃 설정

branch main

- 원격 저장소 생성
- 콜라보레이터 초대
- 로컬 저장소 깃 초기화
    
    ```bash
    git init
    ```
    
- 로컬 저장소 .gitignore 생성
    
    ```bash
    touch .gitigngit ore
    ```
    
- .gitignore 작성

### 2. 장고 개발환경 설정

branch setup-django 

Django 프로젝트 생성

- 가상환경 생성 & 실행
- 필요한 패키지 설치git
    
- 패키지 목록 저장
    
    ```bash
    pip freeze > requirements.txt
    ```
    
- Django 프로젝트 생성

### 3. 회원가입

branch accounts/signup

앱 App

앱 이름 : accounts

모델 Model

모델 이름 : User

- Django **AbstractUser** 모델 상속

**폼 Form**

- Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성
    
    해당 폼은 아래 필드만 출력합니다.
    
    - username
    - password1
    - password2

**기능 View**

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- CustomUserCreationForm을 활용해서 회원가입 구현

**화면 Template**

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

### 4. 로그인

branch accounts/login

**폼 Form**

로그인

- Django 내장 로그인 폼 **AuthenticationForm 활용**

**기능 View**

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

**화면 Template**

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

### 5. 회원 목록 조회

`branch` accounts/index

**기능 View**

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

**화면 Template**

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 출력
- 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동

### 6. 회원 정보 조회

`branch` accounts/detail

**기능 View**

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/

**화면 Template**

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/

### 7. 회원 정보 수정

branch accounts/update

**폼 Form**

회원 정보 수정

- Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성
    
    해당 폼은 아래 필드만 출력합니다.
    
    - first_name
    - last_name
    - email

**기능 View**

회원 정보 수정

- `POST` http://127.0.0.1:8000/accounts/update/

**화면 Template**

회원 정보 수정 페이지

- `GET` http://127.0.0.1:8000/accounts/update/

### 8. 비밀번호 수정

branch accounts/password

폼 Form
비밀번호 수정
- Django 내장 회원 수정 폼 PasswordChangeForm 사용
    
**기능 View**

비밀번호 수정

- `POST` http://127.0.0.1:8000/accounts/password/

**화면 Template**

비밀번호 수정 페이지

- `GET` http://127.0.0.1:8000/accounts/password/

### 9. 로그아웃

branch accounts/logout

**기능 View**

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

### 10. 네비게이션바

branch template/navbar

**화면 Template**

**네비게이션바**

- 리뷰 목록 페이지 이동 버튼
- 리뷰 작성 페이지 이동 버튼
- 비 로그인 유저는 작성 버튼 출력 X
- 로그인 상태에 따라 다른 화면 출력
    1. 로그인 상태
        - 로그인 한 사용자의 username 출력
            - username을 클릭하면 회원 조회 페이지로 이동
        - 로그아웃 버튼
    2. 비 로그인 상태
        - 로그인 페이지 이동 버튼
        - 회원가입 페이지 이동 버튼

### 11. 리뷰 생성

branch reviews/create

**앱 App**

앱 이름 : reviews

모델 Model

모델 이름 : Review

- 모델 필드
    
    
    | 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 리뷰 제목 |  |  |
    | content | 리뷰 내용 |  |  |
    | movie_name | 영화 이름 |  |  |
    | grade | 영화 평점 |  |  |
    | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
    | updated_at | 리뷰 수정시간 | DateTime | auto_now = True |

**기능 View**

데이터 생성

- `POST` http://127.0.0.1:8000/reviews/create/

**화면 Template**

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼

### 12. 리뷰 목록 조회

branch reviews/index

**기능 View**

데이터 목록 조회

- `POST` http://127.0.0.1:8000/reviews/

**화면 Template**

리뷰 **목록 페이지** 

- `GET` http://127.0.0.1:8000/reviews/
- 리뷰 목록 출력
- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

### 13. 리뷰 정보 조회

branch reviews/detail

**기능 View**

데이터 정보 조회

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/

**화면 Template**

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/
- 해당 리뷰 정보 출력
- 로그인한 유저와 작성자가 같으면 수정 / 삭제 가능
- 로그인한 유저와 작성자가 다르면 수정 / 삭제 불가

### 14. 리뷰 정보 수정

branch reviews/update

**기능 View**

데이터 수정

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/update/

**화면 Template**

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/update/
- 리뷰 수정 폼

### 15. 리뷰 삭제

branch reviews/delete

**기능 View**

데이터 삭제

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/delete/

## 후기💪🏻
- 로그인과 회원가입 기능 구현에서 각각의 폼에 들어가는 인자들이나 기능 함수들이 많이 헷갈렸었는데 드라이버와 네비게이터 역할을 하면서 직접 말하고 들으며 구현하니 더 잘 이해가 되었다.
- 전 날 여러명이서 브랜치로 동시 개발을 진행했었는데 충돌도 많이 나고 진행이 잘 안됐지만 오늘 한명씩 돌아가면서 브랜치를 생성/삭제하며 프로젝트를 진행하니 브랜치의 동작 과정을 더 잘 이해할 수 있었다.