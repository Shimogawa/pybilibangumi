# -*- coding:utf-8 -*-

import bdatacollector.pybilirating


if __name__ == '__main__':
	csv_file = open('bangumi2.csv', 'a', newline='', encoding='utf-8')
	brating = bdatacollector.pybilirating.PyBiliRating('bangumi2.csv', 'a')
	brating.continueOnCsv()
