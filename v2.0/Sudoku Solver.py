import wx
import algorithm
import random
import itertools

indices = itertools.product(range(3), range(3))

class SolverFrame(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self,parent,id,title,pos=(100,100),size=(500,500))
		PaN=wx.Panel(self, -1)
		
		for h, v in indices:
			self.H[h][v] = wx.TextCtrl(PaN, -1, pos=(50 * v, 50 * h), size=(50,50), style=wx.TE_MULTILINE)
		but=wx.Button(PaN,5,"Solve Sudoku!",(15, 150))
		but=wx.Button(PaN,6,"generate randomly",(15, 250))
		self.Bind(wx.EVT_BUTTON, self.solve, id = 5)
		self.Bind(wx.EVT_BUTTON, self.generate, id = 6)
	def getMatrix(self):
		matrix = []
		for i in range(9):matrix += [[]]
		
		for i, j in indices:
			curBox = self.H[i][j].GetValue().split()
			for ii, jj in indices:
				matrix[3 * i + ii][3 * j + jj] = curBox[ii][jj]
		return matrix

	def solve(self,event):
		matrix = algorithm.solve(self.getMatrix())
		#if fail: somethin xD else:
		self.fill(matrix)
	def generate(self, event):
		for i, j in indices:
			self.H[i][j].SetValue(self.generate3x3())
	def generate3x3(self):
		permutation = range(1, 10)
		random.shuffle(permutation)
		return "\n".join([permutation[i::3] for i in range(3)])
	def fill(self, matrix):
		for i, j in indices:
			box = ""
			for ii in range(3):
				for jj in range(3):
					box += matrix[3 * i + ii][3 * j + jj]
				box += "\n"
			self.H[i][j] = box


app = wx.App() 
frame = SolverFrame(None, -1, "Sudoku solver")
frame.Centre()
frame.Show()
app.MainLoop()