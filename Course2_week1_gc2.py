#Reading the user input using input or raw_input function and they always
#return a string even if the input was a number
dna = input("Enter a DNA seq, please:")

my_number = input("Enter your number, please:"
type(my_number)        #to know its type and it will be a string although it's a no
actual_number = int(my_number)    #Using the function int() to convert a value into an integer
typt(actual_number)

#making the output with just 3 decimal numbers 
print("The DNA seq's GC content is %5.3f %% " % gc_percent)  ## %5.3f >> this is the formating string ,,, %% >> to print the % symbol

#Other formating characters
print("%d" % 10.6)     ##Transforming 10.6 into an integer
print("%3d" % 10.6)    ##Notice the space before 10 as it prints three spaces/numbers
print("%e" % 10.6)     ##'E' notation uses power of 10
print("%s" % dna)      ##printing the output as a string
