import matplotlib.pyplot as plt 
import sqlite3,time
import numpy as np


def plotter():
	x,y,z = None,None,None
	x_Arr=None
	with sqlite3.connect("../db.db") as conn:
		cur = conn.cursor()

		cur.execute("select x from daily")
		x = cur.fetchall()
		x_Arr = []
		
		for elems in x:
			x_Arr.append(elems[0])
		x_Arr = np.array(x_Arr)

	t = np.array(x_Arr)
	sp = np.fft.fft(np.sin(t))
	freq = np.fft.fftfreq(t.shape[-1])
	plt.plot(freq, sp.real, freq, sp.imag)
	plt.show()

plotter()