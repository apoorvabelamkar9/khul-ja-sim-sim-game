from player import *
from treasure import *
from door import *

import random;
class Game:
	def __init__(self,num_doors=5):
		self.doors = [Door(i) for i in range(num_doors)]
		self.start()

	def addPlayer(self,p):
		self.player=p

	def start(self):
		name=input("enter your name: \n")
		self.addPlayer(Player(name))
		t_door=random.choice(self.doors)
		t_door.putTreasure(Treasure(100))
		print(self.doors)
		door_num = int(input('enter choice '))
		self.pickDoor(door_num)
		self.openRandomDoor()
		print(self.doors)
		user_input=input("do you want to change(y or n)\n")
		if user_input=='y':
			self.makeChange()
		self.openAllDoors()
		print(self.doors)
		msg="you win , party koda!!" if self.player.door.hasTreasure else "you lose , manig hog "
		print(msg)
		
	def pickDoor(self,door_num):
		for door in self.doors:
			if door.num==door_num:
				self.player.assignDoor(door)
				return

	def openAllDoors(self):
		for d in self.doors:
			if d.closed:
				d.open()

	def openRandomDoor(self):
		for door in self.doors:
			if door.num != self.player.door.num and not door.hasTreasure:
				door.open()
				return

	def makeChange(self):
		for d in self.doors:
			if d.num!=self.player.door.num and d.closed:
				self.player.assignDoor(d)
				return

				
		

Game()