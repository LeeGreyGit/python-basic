# レッスン10：クラス（Class）

class Person:
    # グローバル変数（クラス変数）
    speed = 2

    # コンストラクタ（初期化メソッド）
    def __init__(self, name, width, height, pos_x, pos_y):
        self.name = name
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    # メソッド：self を使う関数
    def move(self, x, y):
        self.pos_x += x
        self.pos_y += y

# オブジェクトのインスタンスを作成
player_1 = Person('NV_0', 50, 50, 5, 10)
print(player_1.name)

# オブジェクトの属性を変更
player_1.name = 'NV_1'
print(player_1.name)

# オブジェクトのメソッドを呼び出す
player_1.move(50, 100)
print(player_1.pos_x)
print(player_1.pos_y)
print()

# レッスン11：サブクラスと継承

# Person クラスのサブクラスを作成
class Player(Person):
    
    speed = 10
    
    # サブクラスのコンストラクタで親クラスのコンストラクタを呼び出す
    def __init__(self, name, pos_x, pos_y):
        super().__init__(name, 100, 100, pos_x, pos_y)

    # メソッドのオーバーライド（他の言語でいう override）
    def move(self, y):
        # super().move(0, y) : 親クラスのメソッドを呼ぶことも可能
        self.pos_y += y  # 親を使わずに自前で値を変更

# サブクラスのインスタンスを作成
player_2 = Player('NV_2', 300, 300)

# サブクラスの属性にアクセス
print(player_2.name)

# サブクラスのメソッドにアクセス
player_2.move(10)  # Y 座標のみ移動
print(player_2.pos_x)
print(player_2.pos_y)
