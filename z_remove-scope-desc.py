from unipath import Path
import fileinput


#These are showing up on the file as its being compiled in CircleCI, not on the files at the local machine
scope = "Scope"
scope_desc = "Scope Description"



# Slate 'includes' folder

dc_index_in_gh_pages =  Path(r"./slate-ui/build/").listdir()

# The below commented path is used for testing on the local machine. You may edit the path after the r" to the
# location of Slate's 'includes' folder on your machine

#to_slate_repo_includes = Path(r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\Slate-API-Explorer-Reference\slate\source\includes").listdir()


# Update H1 Title Tag, H1 Resource Tag, and remove Authentication section from file - These updates are needed so file renders with correct font sizes in Slate UI

def removeScopeTags():
    for file in dc_index_in_gh_pages:
        if ".json" in file:            
            for line in fileinput.input(file, inplace=True):
                line = line.rstrip()
                if scope in line:
                        line = line.replace(scope, "")                                               # This will update the Resource tag from H2 to H3 - needs to be first for logic to work
                elif scope_desc in line:
                    line = line.replace(scope_desc, "")
                
                print (line)
                
                

    
        
def main():
    removeScopeTags()
    
    
    
    
main()

