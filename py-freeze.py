import pip


'''Getting the distribution from Pip and writing it in the requirements file.'''
with open("requirements.txt", "w") as f:
	for distribution in pip.get_installed_distributions():
		r = distribution.as_requirement()
		f.write(str(r)+ "\n")
