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
			selection = int(raw_input("Select an option (1-4): "))

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

		selection = int(raw_input("Select an option (1-3): "))

		if(selection == 1):
			#view account info
			userID = raw_input("Enter you user ID: ")
			print(self.queries.parse_val(self.queries.get_user(userID)))

		elif(selection == 2):
			#edit account info
			self.editAccount()

		elif(selection == 3):
			#Delete Account
			userId = raw_input("What is the user ID? ")
			self.queries.remove_user(userId)
			print("User was removed from the database")

	def plantInfo(self):
		print("")
		print("Plant Info")
		print ("1. Add plant")
		print("2. Remove plant")
		print("3. Add new watering timestamp")
		print("4. Change plant location")
		print("5. Remove plant ownership")

		selection = int(raw_input("Select an option (1-5): "))

		if(selection == 1):
			# add plant
			plantType = raw_input("What is the plant type? ")
			building = raw_input("What building is the plant in? ")
			area = raw_input("What area in the building is the plant located? ")
			plantName = raw_input("What is the name of the plant? ")

			self.queries.add_plant(plantType, building, area, plantName)

			print("Plant added")


		elif(selection == 2):
			# remove plant
			plantId = raw_input("What is the plant ID? ")

			self.queries.remove_plant(plantId)

			print("Plant removed")

		elif(selection == 3):
			# Add new watering timestamp
			userId = raw_input("Input user ID: ")
			plantId = raw_input("Input plant ID: ")
			self.queries.add_water_event(userId, plantId)
			print("Timestamp added")


		elif(selection == 4):
			# Change plant location
			plantID = raw_input("Enter the plant ID: ")
			building = raw_input("Enter the plant's building: ")
			area = raw_input("Enter the plant's area: ")
			self.queries.update_plant_location(plantID, building, area)
			print("Plant location changed")

		elif(selection == 5):
			# Remove plant ownership
			plantID = raw_input("Enter the plantID: ")
			self.queries.remove_plant_ownership(plantID)
			print("Plant ownership removed")

	def editAccount(self):
		print("")
		print("Edit Account Info")
		print("1. Change phone number")
		print("2. Change name")

		selection = int(raw_input("Select an option (1-2): "))

		if(selection == 1):
			# Change phone number
			table = "Users"
			column = "phoneNumber"
			id = raw_input("Enter your user ID: ")
			newValue = raw_input("Enter your new phone number: ")
			self.queries.update_user_info(table, column, newValue, id)
			print("Phone number has been updated")

		elif(selection == 2):
			# change name
			table = "Users"
			column = "name"
			id = raw_input("Enter your user ID: ")
			newName = "'"
			newName += raw_input("Enter your new name: ")
			newName += "'"
			self.queries.update_user_info(table, column, newName, id)


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
		print("9. Find a user's plants")
		print("10. Find plants that have never been watered")

		selection = int(raw_input("Select an option (1-10): "))

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

		elif(selection == 9):
			# find a user's plants
			pass

		elif(selection == 10):
			# find unwatered plants
			print(self.queries.parse_val(self.queries.get_dead_plants()))

if __name__ == '__main__': #runs if it's the main function being called
	Y = User()
	
	'''
	INSERT INTO WaterEvent(waterID,plantID,userID,timeWatered)
	 VALUES(1000000,157,48755,'1996-11-11 06:14:00');
	'''
