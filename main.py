# -*- coding:utf-8 -*-

import bdatacollector.pybilirating


if __name__ == '__main__':
	brating = bdatacollector.pybilirating.PyBiliRating('bangumi.csv', 'w')
	brating.startOver()
	brating.close()
