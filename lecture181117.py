import random  # 모듈 불러오기 (랜덤 선택 모듈)
# random 모듈 사용하기 http://pythonstudy.xyz/python/article/509-%EB%82%9C%EC%88%98-random

"""
모듈?

다른 프로그램에서 사용하는걸 목적으로 미리 만들어진 프로그램 코드.
여러 프로그램을 연결할때 이 모듈을 사용함.

모듈 불러올때는 import <파일 이름> 으로 하지만, 기본적으로 설치할때
같이 설치된 모듈은 import <모듈 이름>으로 불러올 수 있음.

모듈에 있는 기능은  `모듈이름.함수()`로 사용할 수 있음. 50번째줄 코드 참고.
"""

do = True  # while 문에 사용하기 위해 추가한 변수

# 가위바위보 시작 #
while(do):
    """
    첫판:       12번째 줄에서 do를 True로 설정했기 때문에 while 아래가 실행됨.
    두번째~ :   1
    """


    print('가위 바위 보 프로그램입니다.\n가위 바위 보 셋중 하나를 입력하세요.') 
    """
이스케이프 문자 

왜 중요하냐?
문자를 사용할때: " / '

문자열에서 무언가 입력했을때 생길수 있는 문제를 방지하기위해 생겼다.

\n << 엔터
\t << 탭만큼 띄움
\' << 문자열 안에서 '
\" << 문자열 안에서 "
\\ << 역슬래쉬
    """

    while(1): # 아래 무한 반복
        user_response = input() # 프로그램을 잠시 멈추고 검은창으로부터 사용자가 입력하는걸 받아옴.
        if user_response == '가위' or user_response == '바위' or user_response == '보':
            # 사용자가 가위 바위 보를 입력했을때
            break # 반복하는걸 이유불문하고 반복문 종료
        else: # 사용자가 이상한걸 입력했을때
            print('제대로 입력하세요.')
            # 다시 38번째 줄부터 시작

    comp_response = random.choice(['가위', '바위', '보'])  # 모듈 사용: 모듈이름.함수명()

    # 만약 사용자가 가위를 냈다면?
    if user_response == '가위': 
        # 가위를 냈다면 55번째줄 코드로, 다른걸 냈다면 건너뛰고 62번째줄 코드로
        if comp_response == '가위':
            print('비겼습니다.')
        elif comp_response == '바위':
            print('졌습니다.')
        elif comp_response == '보':
            print('이겼습니다.')

    # 만약 사용자가 바위를 냈다면?
    elif user_response == '바위':
        # 바위를 냈다면 55번째줄 코드로, 다른걸 냈다면 건너뛰고 72번째줄 코드로
        if comp_response == '가위':
            print('이겼습니다.')
        elif comp_response == '바위':
            print('비겼습니다.')
        elif comp_response == '보':
            print('졌습니다.')

    # 만약 사용자가 보를 냈다면?
    elif user_response == '보':
        # 바위를 냈다면 55번째줄 코드로, 다른걸 냈다면 건너뛰고 83번째줄 코드로
        # 사실 일어날 수 있는 세가지 경우가 모두 생겨서 else: 로도 가능
        if comp_response == '가위':
            print('졌습니다.')
        elif comp_response == '바위':
            print('이겼습니다.')
        elif comp_response == '보':
            print('비겼습니다.')

    # 양쪽이 낸 결과 보이기
    print('당신이 낸 승부수는 {}이고 컴퓨터가 낸 승부수는 {}입니다.'.format(user_response, comp_response))    # 문자열 포매팅 format(ting)

"""
문자열 포매팅?

문자를 합성하면서 사용
'문자열 중{}'.foramt({}에 들어갈 거리) 로 실현 가능
"""

    # 게임을 더 하시렵니까
    print('게임을 더 하시겠습니까? (y/n)')
    while(1):  # 무한반복
        response = input() # y / n 받아오기

        if response == 'y' or response == 'Y': # 대소문자를 구별해서 둘다 적어야함
            do = True  # 다시 게임을 시작하기 위해 19번째 줄 while 안에 든 내용을 참으로 설정
            break   # 무한반복 종료 

                    # 107번째줄에서 다시 19번째줄로 반복
                    # 이해를 위해 107번째 줄이라고 언급했으나, 정확히는 아님.
                    # 하지만 그냥 그런걸로 해두자.


        elif response == 'n' or response == 'N': # 대답이 N이라면?
            do = False  # 게임을 끝내기 위해 19번째 줄 while안에 든 내용을 거짓으로 설정
            break   # 무한반복 종료

        else:       # 응답이 y나 n 둘다 아니라면
            pass    # 다시 질문
                    # pass로 상황을 넘겨서 96번째 줄로 다시 돌아감.

"""
이 프로그램을 만드는 순서:

1.* 가위 바위 보의 승패를 결정할 수 있는 코드를 작성한다.
2.* 사용자로부터 가위 바위 보 선택을 받는다.
3.* 결과를 알려준다.
4. 프로그램의 실행을 알려주거나 재시작 기능 등, 몇가지 편의기능을 추가한다.
"""