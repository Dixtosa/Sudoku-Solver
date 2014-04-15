import wx
import algorithm

def lis(s):
	k=[]
	for i in range(len(s)):
		k.append(int(s[i]))
	return k

class SolverFrame(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self,parent,id,title,pos=(100,100),size=(500,500))
		PaN=wx.Panel(self,-1)
		self.H11=wx.TextCtrl(PaN,-1,pos=(0,0),size=(50,50), style=wx.TE_MULTILINE)
		self.H12=wx.TextCtrl(PaN,-1,pos=(50,0),size=(50,50), style=wx.TE_MULTILINE)
		self.H13=wx.TextCtrl(PaN,-1,pos=(100,0),size=(50,50), style=wx.TE_MULTILINE)
		self.H21=wx.TextCtrl(PaN,-1,pos=(0,50),size=(50,50), style=wx.TE_MULTILINE)
		self.H22=wx.TextCtrl(PaN,-1,pos=(50,50),size=(50,50), style=wx.TE_MULTILINE)
		self.H23=wx.TextCtrl(PaN,-1,pos=(100,50),size=(50,50), style=wx.TE_MULTILINE)
		self.H31=wx.TextCtrl(PaN,-1,pos=(0,100),size=(50,50), style=wx.TE_MULTILINE)
		self.H32=wx.TextCtrl(PaN,-1,pos=(50,100),size=(50,50), style=wx.TE_MULTILINE)
		self.H33=wx.TextCtrl(PaN,-1,pos=(100,100),size=(50,50), style=wx.TE_MULTILINE)
		but=wx.Button(PaN,5,"solve Japanese SUDOKU!",(150,150),wx.Size(200,200))
		self.Bind(wx.EVT_BUTTON, self.solve, id=5)
	def g3t(self):
		h11=self.H11.GetValue()
		h12=self.H12.GetValue()
		h13=self.H13.GetValue()
		h21=self.H21.GetValue()
		h22=self.H22.GetValue()
		h23=self.H23.GetValue()
		h31=self.H31.GetValue()
		h32=self.H32.GetValue()
		h33=self.H33.GetValue()
		H1=h11[:3]+h12[:3]+h13[:3]
		H2=h11[4:7]+h12[4:7]+h13[4:7]
		H3=h11[8:11]+h12[8:11]+h13[8:11]
		H4=h21[:3]+h22[:3]+h23[:3]
		H5=h21[4:7]+h22[4:7]+h23[4:7]
		H6=h21[8:11]+h22[8:11]+h23[8:11]
		H7=h31[:3]+h32[:3]+h33[:3]
		H8=h31[4:7]+h32[4:7]+h33[4:7]
		H9=h31[8:11]+h32[8:11]+h33[8:11]
		LIST=[lis(H1),lis(H2),lis(H3),lis(H4),lis(H5),lis(H6),lis(H7),lis(H8),lis(H9)]
		return LIST
	def solve(self,event):
		return self.fill(algorithm.solve(self.g3t()))
	def fill(self,s):
		h1,h2,h3,h4,h5,h6,h7,h8,h9=s
		H1="".join(h1)
		H2="".join(h2)
		H3="".join(h3)
		H4="".join(h4)
		H5="".join(h5)
		H6="".join(h6)
		H7="".join(h7)
		H8="".join(h8)
		H9="".join(h9)
		print H1,H2,H3,H4,H5,H6,H7,H8,H9
		k1=H1[:3]+'\n'+H2[:3]+'\n'+H3[:3]
		k2=H1[3:6]+'\n'+H2[3:6]+'\n'+H3[3:6]
		k3=H1[6:9]+'\n'+H2[6:9]+'\n'+H3[6:9]
		k4=H4[:3]+'\n'+H5[:3]+'\n'+H6[:3]
		k5=H4[3:6]+'\n'+H5[3:6]+'\n'+H6[3:6]
		k6=H4[6:9]+'\n'+H5[6:9]+'\n'+H6[6:9]
		k7=H7[:3]+'\n'+H8[:3]+'\n'+H9[:3]
		k8=H7[3:6]+'\n'+H8[3:6]+'\n'+H9[3:6]
		k9=H7[6:9]+'\n'+H8[6:9]+'\n'+H9[6:9]
		self.H11.SetValue(k1)
		self.H12.SetValue(k2)
		self.H13.SetValue(k3)
		self.H21.SetValue(k4)
		self.H22.SetValue(k5)
		self.H23.SetValue(k6)
		self.H31.SetValue(k7)
		self.H32.SetValue(k8)
		self.H33.SetValue(k9)


app = wx.App() 
frame = SolverFrame(None, -1, "Sudoku solver")
frame.Centre()
frame.Show()
app.MainLoop()