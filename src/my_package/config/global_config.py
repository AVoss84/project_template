import os
from pathlib import Path

#-------------------------------
# Which environment to use?
#-------------------------------
using = 'vm'                   # own virtual machine
#using = 'docker'                # Docker container

package_root = Path(__file__).parent.parent.parent.parent

## Check if required environment variables exist
## if not apply default paths from test environment:
#-----------------------------------------------------------
if using == 'vm':
    defaults = {
            "UC_CODE_DIR": str(package_root / "src"),      
            "UC_DATA_DIR": "",          # external
            "UC_DATA_PKG_DIR": "",      # internal, i.e. data folder within package                  
            "UC_DB_CONNECTION": 'postgresql://postgres...', 
            "UC_AWS_DIR" : "",
            "UC_PORT": "5000", 
            "UC_APP_CONNECTION": "127.0.0.1"
    }
else:
    defaults = {
            "UC_CODE_DIR": "/app/src/",                 
            "UC_DATA_DIR": "/app/data/",         
            "UC_DATA_PKG_DIR": "/app/src/my_package/data/",    # data folder within package
            "UC_DB_CONNECTION": 'postgresql://postgres...',
            "UC_AWS_DIR" : "",
            "UC_PORT": "5000",
            "UC_APP_CONNECTION": "0.0.0.0"    #8080
}    
#-------------------------------------------------------------------------------------------------------------------------------

for env in defaults.keys():
    if env not in os.environ:
        os.environ[env] = defaults[env]
        print(f"Environment Variable: {str(env)} has been set to default: {str(os.environ[env])}")

UC_CODE_DIR = os.environ['UC_CODE_DIR']  
UC_DATA_DIR = os.environ['UC_DATA_DIR']                 
UC_PORT = os.environ['UC_PORT']
UC_AWS_DIR = os.environ['UC_AWS_DIR']                
UC_DB_CONNECTION= os.environ['UC_DB_CONNECTION']
UC_APP_CONNECTION = os.environ['UC_APP_CONNECTION']
UC_DATA_PKG_DIR = os.environ['UC_DATA_PKG_DIR']
