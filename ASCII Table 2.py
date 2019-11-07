# Name: Ben Friedland
# Instructor: Ivan Mendez
# Due Date: 	

# Assignment: Ascii table - Print characters 33 - 127 of the ASCII table converted from decimal using a while and for loop (do-while for extra credit)

import time
menu = True

while menu:
	choice = eval(input("How would you like to print the ASCII conversion chart? \n"
		"1: ASCII conversion chart using a while loop \n"
		"2: ASCII conversion chart using a for loop \n"
		"3: ASCII conversion chart using a modified while loop (Do-While) \n"
		"0: Exit program: "))
	print()

	# Print the conversion with a while loop
	if choice == 1:
		start = time.time()
		print("		Decimal numbers convert to ASCII (using a while loop:) \n")

		count = 33

		while count < 127:
			print((format(count, "4d")), '=', format(chr(count), "2s"), end = '  |') # format, count, 4d - controls spacing. 4 digits of padding
			
			count += 1

			if count % 8 == 0:
				print()

		end = time.time()
		print('\n')
		print("Displayed the ASCII chart using a while loop in", format(end - start, ".2f"), "seconds.")
		print()
			
	# Print the conversion with a for loop
	elif choice == 2:
		start = time.time()
		print("		Decimal numbers convert to ASCII (using a for loop:) \n")

		for count in range(33, 127):
			print((format(count, "4d")), '=', format(chr(count), "2s"), end = '  |') # end = '' controls spacing between each number. change to ' ' for more spacing

			count += 1

			if count % 8 == 0:
				print()

		end = time.time()
		print('\n')
		print("Displayed the ASCII chart using a for loop in", format(end - start, ".2f"), "seconds.")
		print()

	# Print the conversion with a modified while loop (Do-While)
	elif choice == 3:
		start = time.time()
		print("		Decimal numbers convert to ASCII (using a modified do-while loop:) \n")

		count = 33
		do_while = True

		while do_while and count < 127:
			print((format(count, "4d")), '=', format(chr(count), "2s"), end = '  |')

			count += 1

			if count % 8 == 0:
				print()

			# if count > 127:
				# do_while = False			# Another way to end the loop after 127 cycles

		end = time.time()
		print('\n')
		print("Displayed the ASCII chart using a modified do-while loop in", format(end - start, ".2f"), "seconds.")
		print()

	elif choice == 0:
		menu = False

	else:
		print("Invalid choice. Please try again. \n")
