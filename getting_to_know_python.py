def list_all_js_function_names(path_to_js_file):

    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
#reading into the file    

# with open('script.js') as f:
    # read_data = f.read()
    

#remember that f is closed but you stored it a variable called read_data
#you have the data now that you can work with and not the file itself
#read_data has read the file, you just have to call it


#Reading only lines
counter=0
with open('script.js') as f:
    read_datalines =f.readlines() 

for line in read_datalines:
    if counter <2:
        counter=counter+1
        print(line,end='')

#to print first two lines or specific lines then you must write a condition that will meet it    
  


