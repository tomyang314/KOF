from keycode import *


class Skill:
    @staticmethod
    def explosive_gas():
        key_press('l')

    @staticmethod
    def skill1():              # ↓ → ↓ → (j)   ←↑
        delay = 0.04
        key_down('s')
        time.sleep(delay)
        key_down('d')
        time.sleep(delay)
        key_up('s')
        time.sleep(delay)
        key_up('d')
        key_down('s')
        time.sleep(delay)
        key_down('d')
        time.sleep(delay)
        key_up('s')
        time.sleep(delay)
        key_up('d')
        # key_press('j')

    @staticmethod
    def skill2():            # ← ↓ → ← ↓ → ↓ → (j/k)   ↑
        delay = 0.04
        key_down('a')
        time.sleep(delay)
        key_down('s')
        time.sleep(delay)
        key_up('a')
        time.sleep(delay)
        key_down('d')
        time.sleep(delay)
        key_up('s')
        time.sleep(delay)
        key_up('d')
        key_down('a')
        time.sleep(delay)
        key_down('s')
        time.sleep(delay)
        key_up('a')
        time.sleep(delay)
        key_down('d')
        time.sleep(delay)
        key_up('s')
        time.sleep(delay)
        key_up('d')

    @staticmethod
    def skill3():  # ↓ → j
        delay = 0.06
        key_down('s')
        time.sleep(delay)
        key_down('d')
        time.sleep(delay)
        key_up('s')
        time.sleep(delay)
        key_up('d')
        key_press('j')


class BigSnake:
    @staticmethod
    def sunshine():        # ↓ ← j
        key_down('s')
        time.sleep(0.1)
        key_down('a')
        time.sleep(0.1)
        key_up('s')
        time.sleep(0.1)
        key_up('a')
        key_press('j')

    @staticmethod
    def black_pot_cover():    # ↓ → j
        key_down('s')
        time.sleep(0.1)
        key_down('d')
        time.sleep(0.1)
        key_up('s')
        time.sleep(0.1)
        key_up('d')
        key_press('j')

    @staticmethod
    def steal_heart():
        key_down('s')
        time.sleep(0.06)
        key_down('d')
        time.sleep(0.06)
        key_up('s')
        time.sleep(0.06)
        key_up('d')
        key_down('s')
        time.sleep(0.06)
        key_down('d')
        time.sleep(0.06)
        key_up('s')
        time.sleep(0.06)
        key_up('d')
        key_press('j')


class K9999:
    @staticmethod
    def explosive_gas():
        Skill.explosive_gas()

    @staticmethod
    def crescent():
        Skill.skill2()
        key_down('j')
        time.sleep(0.2)
        key_up('j')

    @staticmethod
    def gun():
        Skill.skill2()
        key_down('k')
        time.sleep(0.2)
        key_up('k')

    @staticmethod
    def centipede_hand():
        Skill.skill1()
        key_down('o')
        time.sleep(0.3)
        key_up('o')
        # key_press('o')

    @staticmethod
    def grand():
        Skill.skill3()




