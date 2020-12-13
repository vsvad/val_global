class Value:
	def __init__(self,val=None):
		self._value=val
	def get(self):
		return self._value
	def set(self,new):
		self._value=new
	def clear():
		self._value=None
def result_to_val(func,*args,**kwargs):
	return Value(func(*args,**kwargs))