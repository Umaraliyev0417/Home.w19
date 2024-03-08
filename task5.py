class Name:
	def __init__(self, fname, lname):
		self.fname = fname.capitalize()
		self.lname = lname.capitalize()
		self.fullname = self.fname + ' ' + self.lname
		self.initials = self.fname[0] + '.' + self.lname[0]

a1 = Name("john", "SMITH")
print(a1.fname) #➞ "John"
print(a1.lname) #➞ "Smith"
print(a1.fullname) #➞ "John Smith"
print(a1.initials) #➞ "J.S"