import sys
import argparse

# Initiate the parser
mainparser = argparse.ArgumentParser(
		# Define programs name for help menu etc
		prog='recipebook',
		# Disable default help menu 'cause I made custom help menu, it is defined in 'gparser' -> 'description'
		add_help=False,
		argument_default=argparse.SUPPRESS,
		formatter_class=argparse.RawDescriptionHelpFormatter,
		# Override default usage message
		usage='%(prog)s [OPTIONS]... [RECIPE]',
		# Describe what the program does before the --help menu section
		description='''
		%(prog)s 0.1 is a handy command line tool
		that is inteded to be used as a cookbook, but from
		command line. Fun isn't it?
		''',
		# Description after the --help menu section
		epilog='''
		I hope that you at least get good laughs off of this program,
		but if you actually get some cooking done (which is also a good thing)
		then enjoy and have fun!
		''',
		# Arguments that start with '@' will be treated as files
		# and those files can contain arguments, that then are
		# placed as arguments
		fromfile_prefix_chars='@',
		# Add more prefix characters to the valid prefix characters list
		prefix_chars='-/',
		# Don't recognize abbreviations of long options
		allow_abbrev=False,
		)

# Override default --help option
mainparser.add_argument(
		'-h', '--help',
		action='help',
		help=argparse.SUPPRESS,
		default=argparse.SUPPRESS,
		)

# Print program version argument
mainparser.add_argument(
		'-V', '--version',
		#help='print program version',
		help=argparse.SUPPRESS,
		action='version',
		version='%(prog)s 0.1',
		)

# Choose recipe type argument
mainparser.add_argument(
		'--recipe',
		# Convert inputted value to 'str' if necessary
		type=str,
		# Available recipes to choose from
		choices=('bread', 'pizza'),
		help=argparse.SUPPRESS,
		# Require 1 argument, else raise error
		nargs=1,
		# Make this argument required
		required=True,
		)

# Define hydration level argument
mainparser.add_argument(
		'-H', '--hydration',
		# Convert inputted values to 'int' if necessary
		type=int,
		# Hydration levels to choose from
		choices=range(50, 101),
		# Suppress help 'cause gparser already prints the same help
		help=argparse.SUPPRESS,
		# Require 1 argument, else raise error
		nargs=1,
		# Make this argument requirement
		required=True,
		)

# Define portion size argument
mainparser.add_argument(
		'-S', '--size',
		# Convert inputted value to 'str' if necessary
		type=str,
		# Available parameters to choose from
		choices=('small', 's', 'medium', 'm', 'large', 'l'),
		#help='select portion size',
		help=argparse.SUPPRESS,
		# Require 1 argument, else raise error
		nargs=1,
		# Make this argument requirement
		required=True,
		)

# Define cooking time argument
mainparser.add_argument(
		'-t', '--cooking-time',
		# Convert inputted value to 'int' if necessary
		type=int,
		help=argparse.SUPPRESS,
		# Require 1 argument, else raise error
		nargs=1,
		# Make this argument requirement
		required=True,
		)

mainparser.add_argument(
		'-v', '--verbose',
		help=argparse.SUPPRESS,
		nargs='?',
		# Only accept -v or --verbose w/o arguments or with 'on' or 'off'
		choices=['on', 'off', ''],
		# If --verbose is present explicitly w/o args, then enable verbose
		const='on',
		# If --verbose isn't present don't enable verbose mode
		default='off',
		)

gparser_2 = mainparser.add_argument_group(
		title='optional arguments',
		description='''-h, --help\t\t\t\t\t\tshow this help message and exit
-V, --version\t\t\t\t\t\tprint program version and exit	
-v, --verbose\t\t\t\t\t\tprint additional message with the recipe
		''',
		)

# Create new parser for the purpose of displaying the help menu properly
gparser = mainparser.add_argument_group(
		title='recipe construction',
		description='''    --recipe=TYPE					choose recipe type
-H, --hydration=PERCENTAGE\t\tdefine water to flour ratio (50...100)
-S, --size=SIZE\t\t\t\t\tdefine portion size
-t, --cooking-time=NUMBER\t\t\tdefine time cooking should take
		''',
		)

# Custom error sub-class that for now has no use
class CustomError(Exception):
	pass

# Read arguments from the command line
args = mainparser.parse_args()

#===========================================================
try:
	# Read arguments from the command line
	args = mainparser.parse_args()

	if args.verbose:
		verbose = args.verbose
		if 'on' in verbose:
			print('''
			\n======================================\n
			Note!
			If you're not going
			to invest that much time
			on baking, for example if
			you want to make bread
			from start to finish in
			just 5 hours, then you
			probably should alter the
			amount of yeast (and salt)
			in your recipe by increasing
			the amount of both of them.\n
			Why?
			Because the dough develops
			more flavour the longer it
			ferments. Also, if you plan
			on making bread in 5 hours
			and use just 1/2 tsp of yeast,
			the bread will not gain any
			volume in that time.
			So thats why!
			\n======================================
					''')
		if 'off' in verbose:
			pass

	# Save selected values into their own variables for later use (printing out the instructions)
	print('\n---Overview---\n')
	recipe = args.recipe
	print('Selected recipe \t\t\t› %s' % recipe[0])
	global hydration
	hydration = args.hydration
	print('Selected hydration level \t› %s %%' % hydration[0])
	size = args.size
	print('Selected size \t\t\t\t› %s' % size[0])
	ct = args.cooking_time
	print('Selected cooking time \t\t› %s hours' % ct[0])

	# Recipe instructions as functions here
	def small_bread(f):
		global hydration
		print('\n---Ingredients---\n')
		print('Flour\t\t\t\t\t\t› %s grams' % f)
		print('Water\t\t\t\t\t\t› %s grams' % int(hydration[0] / 100 * 300))
		print('Salt\t\t\t\t\t\t› %s grams' % int(0.02 * 300))
		print('Yeast\t\t\t\t\t\t› %s grams' % int(0.0125 * 300))

	def medium_bread(f):
		global hydration
		print('\n---Ingredients---\n')
		print('Flour\t\t\t\t\t\t› %s grams' % f)
		print('Water\t\t\t\t\t\t› %s grams' % int(hydration[0] / 100 * 370))
		print('Salt\t\t\t\t\t\t› %s grams' % int(0.02 * 370))
		print('Yeast\t\t\t\t\t\t› %s grams' % int(0.0125 * 370))

	def large_bread(f):
		global hydration
		print('\n---Ingredients---\n')
		print('Flour\t\t\t\t\t\t› %s grams' % f)
		print('Water\t\t\t\t\t\t› %s grams' % int(hydration[0] / 100 * 450))
		print('Salt\t\t\t\t\t\t› %s grams' % int(0.02 * 450))
		print('Yeast\t\t\t\t\t\t› %s grams' % int(0.0125 * 450))
	
	def small_pizza(f):
		global hydration
		print('\n---Ingredients---\n')
		print('Flour\t\t\t\t\t\t› %s grams' % f)
		print('Water\t\t\t\t\t\t› %s grams' % int(hydration[0] / 100 * 150))
		print('Salt\t\t\t\t\t\t› %s grams' % int(0.02 * 150))
		print('Yeast\t\t\t\t\t\t› %s grams' % int(0.0125 * 150))

	def medium_pizza(f):
		global hydration
		print('\n---Ingredients---\n')
		print('Flour\t\t\t\t\t\t› %s grams' % f)
		print('Water\t\t\t\t\t\t› %s grams' % int(hydration[0] / 100 * 170))
		print('Salt\t\t\t\t\t\t› %s grams' % int(0.02 * 170))
		print('Yeast\t\t\t\t\t\t› %s grams' % int(0.0125 * 170))

	def large_pizza(f):
		global hydration
		print('\n---Ingredients---\n')
		print('Flour\t\t\t\t\t\t› %s grams' % f)
		print('Water\t\t\t\t\t\t› %s grams' % int(hydration[0] / 100 * 200))
		print('Salt\t\t\t\t\t\t› %s grams' % int(0.02 * 200))
		print('Yeast\t\t\t\t\t\t› %s grams' % int(0.0125 * 200))

	# When user specifies desired recipe, save flour amounts into variable.
	# When size is then selected, use the right amount of flour from the variable
	# and pass it as an argument to the function.
	if 'bread' in recipe:
		flours_bread = [300, 370, 450]
		if 'small' in size:
			small_bread(flours_bread[0])
		if 's' in size:
			small_bread(flours_bread[0])
		if 'medium' in size:
			medium_bread(flours_bread[1])
		if 'm' in size:
			medium_bread(flours_bread[1])
		if 'large' in size:
			large_bread(flours_bread[2])
		if 'l' in size:
			large_bread(flours_bread[2])

	if 'pizza' in recipe:
		flours_pizza = [150, 170, 200]
		if 'small' in size:
			small_pizza(flours_pizza[0])
		if 's' in size:
			small_pizza(flours_pizza[0])
		if 'medium' in size:
			medium_pizza(flours_pizza[1])
		if 'm' in size:
			medium_pizza(flours_pizza[1])
		if 'large' in size:
			large_pizza(flours_pizza[2])
		if 'l' in size:
			large_pizza(flours_pizza[2])

# Consume all errors here and process them the way you want
#=================================================================
# RIGHT NOW THIS SECTION SUCKS AND IS NOT SET UP IN VERY GOOD WAY!
#=================================================================
except:
	# If no arguments are present, exit with error
	if len(sys.argv) < 2:

		# Exit and use error exit status
		sys.exit(1)
#===========================================================
