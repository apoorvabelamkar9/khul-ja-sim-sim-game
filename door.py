class Door:
	def __init__(self,num):
		self.num=num
		self.closed=True
		self.hasTreasure=False

	def __repr__(self):
		if self.hasTreasure and not self.closed:
			return f'''
				   ________________
                                   {self.treasure}O 
                                   ________________ 
                                                    '''
		if self.closed:
			return f'''
                                   ________________
                                   {self.num}  C   
                                   _________________
                                                    '''
		else:
			return f'''
			          _________________
                                  { self.num}  C   
                                  __________________
                                                    '''
			

	def putTreasure(self,t):
		self.treasure=t
		self.hasTreasure=True


	def open(self):
		self.closed=False
		