per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму:"))
deposit = []
for x in per_cent.values():
    x = x*money
    deposit.append(x)
deposit.sort(reverse=True)
print("Максимальная сумма, которую вы можете заработать — ", deposit[0])