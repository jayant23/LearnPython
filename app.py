import ecommerce.shipping
# ecommerce.shipping.calculate_shipping()

import random

# for i in range(3):
    # print(random.randint(10,20))

members = ["John","marry","max","Mosh"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second  = random.randint(1,6)
        return first,second

dice = Dice()
print(dice.roll())

from pathlib import Path

path = Path()
# print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)

    import openpyxl as xl
    wb = xl.load_workbook("transactions.xlsx")
    Sheet = wb["Sheet1"]
    cell = Sheet["a1"]
    print(cell.value)

for row in range(1,Sheet.max_row+1):
    cell = Sheet.cell(row,1)
    print(cell.value)
