# Spartacodingclub 개발일지
[9월 7일 개강1일] 1주차 10강까지 강의수강
나홀로 링크 메모장 작성
테스트용으로 링크페이지 작성/ test파일 / 댓글달기 추가
[9월 8일 개강2일] 숙제 업로드 / 1주차 숙제 나만의 쇼핑몰 페이지 만들기 완료
[9월 15일 개강 9일차] 5주차 강의 11강 완료


[9월 16일]4주차 8강 모두의 책리뷰 post 연습에서 문제가 생겼다. 
뭐가 문제인지는 몰라도 구동시키면 review_give를 읽어오지 못한다...
/ 세상에 슬랙에서 동료들의 도움으로 해결. 오타로 인한 review_give 인식오류였던듯...
+ POST,GET구문이 나뉘다보니 중복같아서 합칠 수 없을까 고민해봄
검색했더니 예제 구문있어서 따다가 실험했더니 성공!

/[9월 17일 ~18일 새벽] 뽕이 차오른닷. homework에 들어있던 원페이지 쇼핑몰 페이지에 서버, 도메인 작업해서 업로드 완료. 크읏...덕분에 gitbash에서 서버켰다 끄는건 도사가 된 기분.눈누난나

 /[9월 22일 ] 민우님팀은 아니지만 이성님 팀에 배정됐다. 왠지 고생이 눈앞에 보이는것도 같은데 기분탓이겠지.
 
 #내일배움단 #코딩프로젝트 #국비지원 #내일배움카드 #스파르타코딩클럽

/ [9월 23일 팀플젝1일차]성진이가 https 적용시켜달래서 AWS에서 개고생하다 일단 잠깐 손을 놓음. 아무리 생각해도 대상그룹 리스너 설정에서 뭘 잘못한거 같은데 대체 이걸 어떻게 설정해야하는건가. 
우선 인증서 발급 완료 되었고 https 포트에 넣고서 규칙을 어떻게 하라는건지 모르겠음. 후. 그리고 어제부터 15일 프로젝트 챌린지 시작...ㄷㄷ
한글 막 뗐는데 에세이 써오라는 너낌.

/[9월 24일 팀플젝2일차]오늘 팀프젝 회의에서 마이페이지 제작을 맡았다. 전체적인 틀을 잡는 것부터 답답해서 타 사이트를 클론코딩해본 후 참고할 예정이다. 마이페이지에는 우선 내가 쓴 글을 읽는 칸을 마련하는게 우선 순위. 헤더에는 로그아웃만 있으면 되나?? 일단 다른 사이트의 마이페이지를 좀 따서 코딩을 해보고 index.html을 만들어야겠다. 

/[9월 25일 팀플젝3일차] 성진이 한테 물어봤더니 왜 뼈대를 각자 만드냐함. 부트스트랩 안쓴댔더니 왜 레고로 성 쌓을건데 블록부터 만드는거냐 함. 나도 몰라 샛갸.....내가 어케 알아....

/[9워 26일 팀플젝4일차] 아 자바스크립트가 아니라 자바ssip크립트인가....내맘 좀 알아줘라..

/[9워 27일 팀플젝5일차] html 뼈대올리는것 부터 난관이라 썼다 지웠다 썼다 지웠다....모르는 사람이 보면 세기의 러브레터인줄 알거다. 

/[9워 28일 팀플젝6일차] 밤에 우리조 튜터가 아닌 뒷조 튜터가 갑자기 우리방에 들어왔다. https 설정 저번에 손놓은거 물어봤는데 "이렇게 물어보시면 제가 뭘 가르쳐드려야 될지 모르겠는데?" 내가 니 친구냐. 
/[9워 29일 팀플젝7일차] 로그아웃은 구현이 되는데 회원정보변경이랑 탈퇴.....무한 스크롤 해보고 싶어서 넣어봤는데 약간 망조인듯. 하 뭘 넣어줘야 만족할래.....난 쪼렙이라고 이 파일놈아....ㅜㅜ

/[10월 05일 팀플젝 13일차] * 오늘의 목표: 탈퇴, 회원정보수정 구현하기 * 토의내용 : 어떻게든 기능 최대한 구현하자 * 업무중 이슈 : 너무 많은데 뭐부터 하지. 일단 ㅊㄷㅎ튜터관련해서 선매님한테 얘기했다. 이전 스파르타 교육생들 후기에서도 그놈은 문제였던듯. 일단 할말 다해서 속이 시원하다. 그리고 로그인은 결국 민우님 깃허브 보고 따오기로 했다. 이제 그 유명한 존맛탱(jwt)을 맛보는 것인가....오늘 회의하다보니 마이페이지는 header nav 안에 넣고 회원정보수정페이지와 나의 글보기 페이지, 모든 유저 글 보기 페이지 이렇게 3페이지로 구성하는게 좋겠다는 판단이 들었다. 좋은 판단은 왜 늦게 찾아올까. 젠장. * To-do list : 로그아웃 세션 종료 및 얼럿 기능 구현,  로그인 이후 공통적용되는 헤더 모듈 분리. 8기 분들 도망쳐

/ [10월 07일 팀플젝 15일차] * 오늘의 목표: 일단 로그인 * 토의내용 : 로그인은 무엇인가, 졸립다, 다들 힘들다 * 업무중 이슈 : 다, 전부다 * To-do list : 로그인 구현노력

/ [10월 08일 팀플젝 발표날] * 다들 고생많이 하셨습니다 정말!!!!!!!! 몰라!!!!!!일단 끝낫다!!!!!!!!!!!!!!!제리야!!!!!!!!!!!!!!밥차려라!!!!!!!!!!!!!!!

/ [10월 25일 팀플젝 9일차] #내일배움단 #코딩프로젝트 #국비지원 #내일배움카드 #스파르타코딩클럽 
* 오늘의 목표: 탈퇴, 회원정보수정 구현하기 * 토의내용 : 일단 되는대로 하고 안되면 그림판으로 사기를 쳐본다 * 업무중 이슈 : 놋북이 죽었는데 뒷판을 까보니 배터리만 죽었다 다행이다. 

/[10월 28일 팀플젝 15일차] #내일배움단 #코딩프로젝트 #국비지원 #내일배움카드 #스파르타코딩클럽 
* 오늘의 목표: 노트북 살리기 * 토의내용 : 그냥 되는것만 보여주자 * 업무중 이슈 : 살아라 노트북
