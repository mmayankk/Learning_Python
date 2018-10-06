import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')
def factorial(n):
	logging.debug('Start of factorial% ( )' % (n))
	total = 1
	for i in range(n + 1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
	logging.debug('End of factorial( %)' % (n))
	return total
print(factorial(8))
logging.debug('End of program')
