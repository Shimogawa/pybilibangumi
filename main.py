# -*- coding:utf-8 -*-

import bdatacollector.pybilirating


if __name__ == '__main__':
	csv_file = open('bangumi2.csv', 'w', newline='', encoding='utf-8')
	brating = bdatacollector.pybilirating.PyBiliRating(csv_file)
	brating.startOver(1, 21)
