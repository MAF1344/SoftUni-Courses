tournament = int(input())
money = 0
wins = 0
loses = 0

for i in range(tournament):
    daily_win = 0
    daily_lose = 0
    daily_money = 0

    while True:
        sport = input()
        if sport == 'Finish':
            break
        result = input()

        if result == 'win':
            daily_money += 20
            daily_win += 1
            wins += 1
        elif result == 'lose':
            daily_lose += 1
            loses += 1
        else:
            print('Error')

    if daily_win > daily_lose:
        daily_money += daily_money * 0.10

    money += daily_money

if wins > loses:
    money += money * 0.20
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")
