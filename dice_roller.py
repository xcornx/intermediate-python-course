import random

def main():
	dice_rolls = int(input('Berapa dadu? :')) 
	dice_sum = 0
	for i in range(0,dice_rolls):
		roll = random.randint(1,6)
		dice_sum += roll
		if roll == 1:
			print(f'Rolled: {roll}! Lose')
		elif roll == 6:
			print(f'Rolled: {roll}! Jackpot')
		else:
			print(f'Rolled : {roll}')
	print(f'Total: {dice_sum}')

if __name__== "__main__":
  main()