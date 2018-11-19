import ConfigParser
import os

def get_variables(varname,):
    project_path = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    filename = os.path.join(project_path, 'Configuration', 'config.ini')
    config = ConfigParser.ConfigParser()
    config.read(filename)
    variables = {}
    for section in config.sections():
        for key, value in config.items(section):
            var = "%s.%s.%s" % (varname, section, key)
            variables[var] = value
    return variables