# Pythonの基本 Part 7
# クラスとオブジェクト
# クラスの定義、属性、メソッド
# クラスのオブジェクトインスタンスの作成

# キャラクタークラスを作成、クラスはキャラクターの設計図
class Character:
    # クラス変数
    speed = 2
    
    # コンストラクタ
    def __init__(self, name, width, height, position_x, position_y):
        self.name = name
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
    
    # メソッド（関数）を定義、selfを忘れずに
    def move(self, x, y):
        self.position_x += x
        self.position_y += y

# オブジェクトインスタンスを作成
character_1 = Character('Character_0', 50, 50, 5, 10)
character_1.name

# オブジェクトの属性を変更
character_1.name = 'Character_1'
character_1.name

# オブジェクトのメソッドを呼び出し
character_1.move(50, 100)
character_1.position_x
character_1.position_y

# Pythonの基本 Part 8
# サブクラスと継承

# キャラクタークラスのサブクラスを作成
class PlayerCharacter(Character):
    speed = 10
   
    # サブクラスのコンストラクタは親クラスを呼び出す
    def __init__(self, name, position_x, position_y): 
        super().__init__(name, 100, 100, position_x, position_y)
        
    def move(self, y):
        self.position_y += y
        
# サブクラスのインスタンスを作成
character_2 = PlayerCharacter('Character_2', 300, 300)
# サブクラスの属性にアクセス
print(character_2.name)
# サブクラスのメソッドを呼び出し
character_2.move(10)
print(character_2.position_x)
print(character_2.position_y)
