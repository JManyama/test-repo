#from unipath import Path
import os
#import shutil
import subprocess

# CircleCI will run this script first

# Widdershins Swaggerfile converter for Dev Center

# This script will run first, to convert Swagger.json files to a fresh set of Swagger.json.md files.


# Dev Center Repo -  Swagger Files for API Explorer



# swagger_v3_0 = Path (r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\api-explorer\v3-0").listdir()

# swagger_v3_1 = Path (r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\api-explorer\v3-1").listdir()

# swagger_v3_2 = Path (r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\api-explorer\v3-2").listdir()

# swagger_v4_0 = Path (r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\api-explorer\v4-0").listdir()


# All markdown files in the 'includes' folder in Slate portion of the Dev Center repo

#to_slate_repo_includes = Path(r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\Slate-API-Explorer-Reference\slate\source\includes")


# Detecting and converting the Swagger files in all sub-folders under the 'api-explorer' folder
def convertSwaggerToMarkdown():
    #cmd = 'For /R \\src\\api-explorer\\ %G IN (*.json) do widdershins "%G" -o "%G".md'
    cmd = 'For /R C:\\Users\\I860605\\Desktop\\dev-center-test\\dev-concur-test\\src\\api-explorer\\ %G IN (*.json) do widdershins "%G" -o "%G".md'
    #subprocess.call(cmd, shell=True)
    subprocess.run(cmd, shell=True)
    print("Files successfully converted to markdown")
      


def main():
    convertSwaggerToMarkdown()
    
    
main()