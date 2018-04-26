
class ProgressBar:

	_len = 50
	_truelen = 48
	_datatype = int
	_dataend = 100

	_LEFTD = '['
	_RIGHTD = ']'
	_PROGB = '='
	_PROGE = '>'
	_WHITE = ' '
	_ENDL = ''

	_percentage = True


	# todo: show progress ([====>] xx.xx% (a/b))
	def __init__(self, leng=50, datatype=int, dataend=100, left='[', right=']',
				progchar='=', progcharend='>', whitechar=' ', endl='', showpercentage=True):
		self._len = leng
		self._datatype = datatype
		self._dataend = datatype(dataend)
		self._LEFTD = left
		self._RIGHTD = right
		self._PROGB = progchar
		self._PROGE = progcharend
		self._WHITE = whitechar
		self._ENDL = endl
		self._percentage = showpercentage
		self._truelen = self._len - 2


	def update(self, curdata):
		s = self.__upd_str(curdata)
		if self._percentage:
			s += ' ' + self.__upd_perc(curdata)
		print(s + '\r', end=self._ENDL)


	def __upd_str(self, curdata):
		cur = self._datatype(curdata)
		perc = cur / self._dataend
		block = int(perc * self._truelen)

		s = self._LEFTD
		for i in range(1, self._truelen + 1):
			if i < block:
				s += self._PROGB
			elif i == block:
				s += self._PROGE
			else:
				s += self._WHITE
		s += self._RIGHTD
		return s


	def __upd_perc(self, curdata):
		cur = self._datatype(curdata)
		perc = cur * 100 / self._dataend

		return format(perc, '.2f') + '%'
