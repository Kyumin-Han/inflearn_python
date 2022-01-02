# 스타크래프트 예제
# 마린 : 공격 유닛, 군인. 총을 쏨

# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크 .포를 쏨, 일반 모드 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# 유닛이 많아진다면 각각의 변수들을 각각 다르게 설정해서 유닛의 수만큼 만들어야 한다
# 클래스를 만들면 동일한 작업을 반복할 수 있다

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
        
# marin1 = Unit("마린", 40, 5)
# marin2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# marin3 = Unit("마린")
# __init__ 생성자를 구성할 때 지정해준 인자의 개수와 동일한 인자를 생성할 때도 넘겨주어야 한다

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True
# 외부에서 멤버 변수를 생성해서 만들 수 있다.

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 클래스에 비슷한 기능이 있을 때는 상속 받아서 정의 해 줄 수 있다
# 상속은 대상 클래스의 이름을 괄호안에 적어주면 된다
# 상속받은 클래스에서는 그 클래스의 생성자를 호출해주어 상속된 클래스의 멤버 변수를 사용할 수 있다
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : {1} 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 다중 상속
# 여러개의 클래스를 동시에 상속 받을 수 있다
# 상속 받을때는 여러개의 클래스를 콤마로 구분해서 지정해준다
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# 메소드 오버로딩을 통해서 다른 클래스의 메소드를 사용할 수 있게 한다
# 메소드 오버로딩의 경우 같은 이름의 메소드를 사용하고 싶은 클래스에서 재정의 하여 사용한다

# pass 는 아직 모두 정의 되진 않았지만 코드 진행에 문제가 없도록 다 정의 된 것처럼 일단 넘겨주는 키워드이다
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        # super를 사용할 때는 ()를 사용하고 인자에 self를 없이 생성한다
        super().__init__(name, hp, 0)
        self.location = location

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()