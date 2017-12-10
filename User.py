from Project import SQLClient
import mysql.connector
class User:
	"""
	The UI of the database
	"""
	def __init__(self):
		self.queries = SQLClient()
		self.queries.test()
		running = True
		print("Welcome!")
		while(running == True):
			print("")
			print("1. User Info")
			print("2. Plant Info")
			print("3. Advanced Options")
			print("4. Quit")
			selection = input("Select an option (1-4): ")
			
			if(selection == 1):
				self.userInfo()
				
			elif(selection == 2):
				self.plantInfo()
			
			elif(selection == 3):
				self.advancedOptions()
			
			elif(selection == 4):
				print("Goodbye.")
				running = False
				

	def userInfo(self):
		print("")
		print("User Info")
		print("1. View account info")
		print("2. Edit account info")
		print("3. Delete account")
		
		selection = input("Select an option (1-3): ")
		
		if(selection == 1):
			#view account info
			pass
			
		elif(selection == 2):
			#edit account info
			self.editAccount()
			
		elif(selection == 3):
			#Delete Account
			userId = input("What is the user ID? ")
			self.queries.remove_user(userId)
			print("User was removed from the database")

	def plantInfo(self):
		print("")
		print("Plant Info")
		print ("1. Add plant")
		print("2. Remove plant")
		print("3. Add new watering timestamp")
		print("4. Edit plant info")
		print("5. Change plant location")
		
		selection = input("Select an option (1-5): ")
		
		if(selection == 1):
			# add plant
			plantType = input("What is the plant type? ")
			building = input("What building is the plant in? ")
			area = input("What area in the building is the plant located? ")
			plantName = ("What is the name of the plant? ")
			
			self.queries.add_plant(plantType, building, area, plantName)
			
			print("Plant added")
			
		
		elif(selection == 2):
			# remove plant
			plantId = input("What is the plant ID? ")
			
			self.queries.remove_plant(plantId)
			
			print("Plant removed")
			
		elif(selection == 3):
			# Add new watering timestamp
			userId = input("input user ID: ")
			plantId = input("input plant ID: ")
			self.queries.add_water_event(userId, plantId)
			print("Timestamp added")
			
		
		elif(selection == 4):
			# Edit plant info
			pass
		
		elif(selection == 5):
			# Change plant location
			pass
			
	def editAccount(self):
		print("")
		print("1. Change phone number")
		print("2. Change name")
		print("3. Change email")
		print("4. Change password")
		
		selection = input("Select an option (1-4): ")
		
		if(selection == 1):
			# Change phone number
			pass
		
		elif(selection == 2):
			# change name
			pass
		
		elif(selection == 3):
			#change email
			pass
		
		elif(selection == 4):
			#change password
			pass
		
	def advancedOptions(self):
		print("")
		print("Advanced Options")
		print("1. Find plants without users")
		print("2. Find users without plants")
		print("3. Find users with the most amount of plants")
		print("4. Find the building with the most plants")
		print("5. Find the building with the least plants")
		print("6. Find the day with the most watering events")
		print("7. Find the week with the most watering events")
		print("8. Find a user's past watering events within a frame of time")
		
		selection = input("Select an option (1-8): ")
		
		if(selection == 1):
			# find plants without users
			pass
		
		elif(selection == 2):
			# find users without plants
			pass
		
		elif(selection == 3):
			# find users with the most amount of plants
			pass
			
		elif(selection == 4):
			# find the building with the most plants
			pass
			
		elif(selection == 5):
			# find the building with the least plants
			pass
			
		elif(selection == 6):
			# find the day with the most watering events
			pass
			
		elif(selection == 7):
			# find the week with the most watering events
			pass
			
		elif(selection == 8):
			# find a user's past watering events within a frame of time
			pass

if __name__ == '__main__': #runs if it's the main function being called
	Y = User()
	
			
			
