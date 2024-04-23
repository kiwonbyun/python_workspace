import random

class TicTacToe:
    # 게임판 생성
    def __init__(self):
        self.board = []
        
    # 게임판 초기화
    def create_board(self):
        for i in range(0,3):
            row = []
            for j in range(0,3):
                row.append('*')
            self.board.append(row)
        
    # 첫 플레이어 선택
    def select_first_player(self):
        if random.randint(0,1) == 0:
            return 'X'
        else:
            return 'O'

    # 기호 표시
    def mark_spot(self, row, col, player):
        self.board[row][col] = player

    # 승리상태 확인
    def is_win(self, player):
        n= len(self.board)
        #행 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win ==True:
                return win
        #열 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win ==True:
                return win
        # 1,1 2,2 3,3대각선 확인
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win == True:
            return win
        
        win = True
        for i in range(n):
            if self.board[i][n-i-1] != player:
                win = False
                break
        if win == True:
            return win
        

        
        return False
            


    # 잔여 빈킨 여부 확인
    def is_board_full(self):
        n = len(self.board)

        for i in range(n):
            for j in range(n):
                if self.board[i][j] == "*":
                    return False
        
        return True

    # 플레이어 변경
    def next_player(self, player):
        return "X" if player == "O" else "O"

    # 현재 게임판 상태 출력
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    # 게임 시작
    def start(self):
        self.create_board()
        self.show_board()
        player = self.select_first_player()

        while True:

            if player == 'X':
                print('컴퓨터 차례입니다.')
            else:
                print('사용자 차례입니다.')

            self.show_board()

            if player == 'X':
                while True:
                    row, col = random.randint(1,3), random.randint(1,3)
                    if self.board[row-1][col-1] == '*':
                        break

                print('컴퓨터가 행 ' + str(row) + ", 열 ", str(col) + "을/를 선택했습니다." )
                print()
            else:
                row, col = list(map(int, input('선택할 빈칸의 위치를 입력하세요: ').split()))
                print('사용자가가 행 ' + str(row) + ", 열 ", str(col) + "을/를 선택했습니다." )
                print()

            if row == 0 and col == 0:
                print("게임을 종료합니다.")
                break

            self.mark_spot(row-1, col-1, player)
            self.show_board()

            if self.is_win(player) == True:
                if player =='X':
                    print("컴퓨터가 이겼습니다. 다시 도전하세요.")
                else:
                    print("사용자가 이겼습니다. 축하합니다.")
                break

            if self.is_board_full() == True:
                print("비겼습니다. 다시 시작하세요.")
                break

            player = self.next_player(player)
        
        print()
        self.show_board()


# 게임 생성
TTT = TicTacToe()

#게임 시작
TTT.start()