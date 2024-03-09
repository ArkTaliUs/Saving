import os

testkey = False
textmode = False

##########

#  code  #

##########


def save(variable, filename):
	with open(filename, "w") as file:
		file.write(variable)
		if textmode == True:
			print(f"variable '{variable}' saved")
		


def load(filename):
	with open(filename, "r") as file:
		if textmode == True:
			print(f"load is success: {file.read()}")
		return file.read()



def delete(filename):
	os.remove(filename)
	if textmode == True:
		print(f"file '{filename}' deleted")


##########

#  end   #

##########





##########

#  test  #

##########


def test_a():
	save("a", "save_a.txt")
	var = load("save_a.txt")
	print(var)
	delete("save_a.txt")



if testkey != 0:
	test_a()


##########

#  end   #

##########