from my_package.config import global_config as glob 
from my_package.services.file import YAMLservice
#from importlib import reload
#reload(glob)

my_yaml = YAMLservice(root_path = glob.UC_CODE_DIR)
io = my_yaml.doRead("my_package/config/input_output.yaml")
