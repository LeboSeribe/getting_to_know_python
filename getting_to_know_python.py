import re
def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    #creating a list that will have lines with function names
    myfunctions=[]

    
    #reading into the file    
    with open('script.js') as f:
        read_datalines =f.readlines()

    
    for line in read_datalines:
        if 'function' in line:
            myfunctions.append(line)
            # print(line)
    # print(myfunctions)        

    names_list = []
    for each_item in myfunctions:

        arr = (each_item.split("()")[0]
        .split("=")[0]
        .split("(")[0]
        .split("function")[-1]
        )
        names_list.append(arr)
    return names_list
print(list_all_js_function_names('script.js'))   
  

# name_dict = {}
# name_dict['name'] = arr