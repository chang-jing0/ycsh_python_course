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
position = input("輸入旗子變數")

# 檢查該棋盤格位置是否可以落子（可以放棋子在上面），
# 如果不行，顯示 '錯誤，
#此位置已經有棋子了，結束程式'，並退出程式
# TODO: 程式寫這裡
if 'cell_' + position is None:
  'cell_' + position= chess
  print(' '+cell_1 + ' | '+ cell_2 +' | '+ cell_3+' ')
  print('---+---+---')
  print(' '+cell_4 + ' | '+ cell_5 +' | '+ cell_6+' ')
  print('---+---+---')
  print(' '+cell_7 + ' | '+ cell_8 +' | '+ cell_9+' ')
else:
  print('錯誤，此位置已經有棋子了')
  sys.exit() 
