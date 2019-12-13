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

    dict_functions={}
    counter=0
    for line in read_datalines:
        counter+=1
        if 'function' in line:
            names_list = []
            name=line.split("()")[0].split("=")[0].split("(")[0].split("function")[-1]
            dict_functions['name']=name
        
    
            starting_line = counter
            dict_functions['starting line']=starting_line
            
            

        if line.startswith('}'):
            end_line=counter
            dict_functions['end_line']=end_line 
            myfunctions.append(dict_functions) 
            dict_functions={}

    
    return myfunctions
print(list_all_js_function_names('script.js'))   
  




    

