import random as random
from sort.anime import SortAnimation

print("ソートアニメーションを描画します。")
size = int(input("ソートする配列のサイズを入力してください:"))
rand_List = list(range(size))
random.shuffle(rand_List)
sortAnimation = SortAnimation(rand_List)

while True:
    print("描画するソートを選択してください")
    print("1:バブルソート")
    print("9:処理を終了")
    sort_type = int(input("入力してください:"))
    if sort_type == 1:
        sortAnimation.bubblesort()
    elif sort_type == 9:
        print("処理を終了します。")
        break
    else:
        print("入力に誤りがあります。")
        print("もう一度入力してください。")
