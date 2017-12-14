from Project import SQLClient
import mysql.connector
class User:
	"""
	The UI of the database
	"""
	def __init__(self):
		self.queries = SQLClient()
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
				print("")
				print("Goodbye.")
				running = False


	def userInfo(self):
		print("")
		print("User Info")
		print("1. View account info")
		print("2. Edit account info")
		print("3. Add user")
		print("4. Delete account")

		selection = int(raw_input("Select an option (1-4): "))

		if(selection == 1):
			#view account info
			print("")
			userID = raw_input("Enter your user ID: ")
			print(self.queries.parse_val(self.queries.get_user(userID)))

		elif(selection == 2):
			#edit account info
			self.editAccount()

		elif(selection == 3):
			# Add a user
			print("")
			userID = raw_input("Enter a user ID: ")
			name = raw_input("Enter your name: ")
			phone_number = raw_input("Enter your phone number: ")
			self.queries.add_user(userID, name, phone_number)
			print("User Added")

		elif(selection == 4):
			#Delete Account
			print("")
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
		print("5. Add plant ownership")
		print("6. Remove plant ownership")

		selection = int(raw_input("Select an option (1-5): "))

		if(selection == 1):
			# add plant
			print("")
			plantType = raw_input("What is the plant type? ")
			building = raw_input("What building is the plant in? ")
			area = raw_input("What area in the building is the plant located? ")
			plantName = raw_input("What is the name of the plant? ")

			self.queries.add_plant(plantType, building, area, plantName)

			print("Plant added")


		elif(selection == 2):
			# remove plant
			print("")
			plantId = raw_input("What is the plant ID? ")

			self.queries.remove_plant(plantId)

			print("Plant removed")

		elif(selection == 3):
			# Add new watering timestamp
			print("")
			userId = raw_input("Input user ID: ")
			plantId = raw_input("Input plant ID: ")
			self.queries.add_water_event(userId, plantId)
			print("Timestamp added")

		elif(selection == 4):
			# Change plant location
			print("")
			plantID = raw_input("Enter the plant ID: ")
			building = raw_input("Enter the plant's building: ")
			area = raw_input("Enter the plant's area: ")
			self.queries.update_plant_location(plantID, building, area)
			print("Plant location changed")

		elif(selection == 5):
			#Add plant ownership
			print("")
			userID = raw_input("Enter a user ID: ")
			plantID = raw_input("Enter a plant ID: ")
			if(self.queries.add_ownership(userID, plantID) == True):
				print("Ownership added")

		elif(selection == 6):
			# Remove plant ownership
			print("")
			plantID = raw_input("Enter the plantID: ")
			userID = raw_input("Enter the user ID: ")
			self.queries.remove_plant_ownership(userID, plantID)
			print("Plant ownership removed")

	def editAccount(self):
		print("")
		print("Edit Account Info")
		print("1. Change phone number")
		print("2. Change name")

		selection = int(raw_input("Select an option (1-2): "))

		if(selection == 1):
			# Change phone number
			print("")
			table = "Users"
			column = "phoneNumber"
			id = raw_input("Enter your user ID: ")
			newValue = raw_input("Enter your new phone number: ")
			self.queries.update_user_info(table, column, newValue, id)
			print("Phone number has been updated")

		elif(selection == 2):
			# change name
			print("")
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
		print("7. Find a user's past watering events within a frame of time")
		print("8. Find a user's plants")
		print("9. Find plants that have never been watered")
		print("10. Check if a plant has been watered")

		selection = int(raw_input("Select an option (1-10): "))

		if(selection == 1):
			# find plants without users
			print("")
			print("Plants without Users:")
			self.queries.plants_without_users()

		elif(selection == 2):
			# find users without plants
			print("")
			print("Users without Plants:")
			self.queries.users_without_plants()

		elif(selection == 3):
			# find users with the most amount of plants
			print("")
			print("Users with the Most Plants:")
			self.queries.users_with_most_plants()

		elif(selection == 4):
			# find the building with the most plants
			print("")
			print("Building with the most plants")
			self.queries.building_most_plants()


		elif(selection == 5):
			# find the building with the least plants
			print("")
			print("Building with the least plants")
			self.queries.building_least_plants()

		elif(selection == 6):
			# find the day with the most watering events
			print("")
			print("Day with most watering events")
			self.queries.most_watering_events()

		elif(selection == 7):
			# find a user's past watering events within a frame of time
			print("")
			userID = raw_input("What is the user ID?: ")
			begin_month = raw_input("What is the starting month?: ")
			end_month = raw_input("What is the ending month?: ")
			begin_day = raw_input("What is the starting day?: ")
			end_day = raw_input("What is the ending day?: ")
			self.queries.find_watering_events(begin_month, begin_day, end_month, end_day, userID)

		elif(selection == 8):
			# find a user's plants
			print("")
			userID = raw_input("What is the user ID?: ")
			self.queries.get_users_plants(userID)

		elif(selection == 9):
			# find unwatered plants
			print("")
			self.queries.parse_val(self.queries.get_dead_plants())

		elif(selection == 10):
			# is the plant watered?
			print("")
			plantID = raw_input("What is the plant ID?: ")
			self.queries.is_plant_watered(plantID)

if __name__ == '__main__': #runs if it's the main function being called
	Y = User()

	'''
	INSERT INTO WaterEvent(waterID,plantID,userID,timeWatered)
	 VALUES(1000000,157,48755,'1996-11-11 06:14:00');
	'''
