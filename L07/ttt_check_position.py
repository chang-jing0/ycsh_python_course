# 撰寫一程式，檔案名稱 ttt_check_position.py
# 定義棋盤格狀態變數 cell_1 ~ cell_9 如下，
# 提示使用者輸入棋子位置（整數 0-9 ），保存在變數 position，
# 檢查該棋盤格位置是否可以落子（可以放棋子在上面），
# 如果不行，顯示 '錯誤，此位置已經有棋子了，結束程式'，並退出程式

# 棋盤格變數：保存棋盤狀態的變數
# 變數編號對應的棋盤位置如下
#  1 | 2 | 3 
# ---+---+---
#  4 | 5 | 6 
# ---+---+---
#  7 | 8 | 9
cell_1 = ' '
cell_2 = ' '
cell_3 = 'o'
cell_4 = ' '
cell_5 = ' '
cell_6 = ' '
cell_7 = 'x'
cell_8 = 'o'
cell_9 = 'x'
# 目前棋子變數：保存目前使用的棋子
chess = 'x'

# 提示使用者輸入棋子位置（整數 0-9 ），保存在變數 position，
# TODO: 程式寫這裡
position =int(input("輸入整數0~9\n"))
# 檢查該棋盤格位置是否可以落子（可以放棋子在上面），
# 如果不行，顯示 '錯誤，
#此位置已經有棋子了，結束程式'，並退出程式
# TODO: 程式寫這裡
if position == 1 and cell_1 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()
elif position == 2 and cell_2 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()
elif position == 3 and cell_3 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()    
elif position == 4 and cell_4 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()    
elif position == 5 and cell_5 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()    
elif position == 6 and cell_6 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()    
elif position == 7 and cell_7 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()    
elif position == 8 and cell_8 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()    
if position == 9 and cell_9 != ' ':
  print('錯誤，此位置已經有棋子了')
  exit()    