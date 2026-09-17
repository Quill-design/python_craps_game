# CRAPS赌博游戏    未完成
import random
def save_money(money):
    with open('SAVE.txt','w') as f:
        f.write(str(money))

def load_money():
    try:
        with open('SAVE.txt','r') as f:
            return int(f.read())
    except(FileNotFoundError,ValueError):
        return 1000

bankroll = load_money()
while True:
    # 下注并判断是否下注》余额
    while True:
        print(f'您剩余金额为{bankroll}')
        try:
            bet = int(input('请下注：'))
        except(ValueError):
            print('下注失败')
            continue
        if bet > bankroll:
            print('您的余额不足')
            continue
        else:
            break
    # 第一次投出7，11则获胜 ，2，3，12则判负  若没有则继续投下一轮  随后投出第一次投出的数字时获胜，投出7时判负
    def roll_dice():
        return random.randint(1,7) + random.randint(1,7)
    first_roll = roll_dice()
    game_result = True
    print(f'玩家投出了{first_roll}点')
    if first_roll == 7 or first_roll == 11:
        print('玩家胜\n')
        pass
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        game_result = False
        print('庄家胜\n')
    else:
        while True:
            try_roll = roll_dice()
            print(f'玩家投出了{try_roll}')
            if try_roll == 7:
                game_result = False
                print('庄家胜\n')
                break
            elif try_roll == first_roll:
                print('玩家胜\n')
                break
            else:
                pass
    #   判断是否结束游戏
    if game_result:
        bankroll += bet
        save_money(bankroll)
    else:
        bankroll -= bet
        save_money(bankroll)
    print(f'您的余额为{bankroll}')
    if bankroll == 0:
        print('恭喜你输的一塌糊涂')
        bankroll = 1000#这里把1000存入bankroll的原因是更方便修改
        save_money(bankroll)
        break
    elif bankroll >= 5000:
        print('恭喜你赚爽了')
        bankroll = 1000#同理
        save_money(bankroll)
        break
    else:
        pass