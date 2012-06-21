# encoding:utf8

class InputFormat:
	class InputType:
		file,files,dir,dirs = range(4)
		len = 4
		
    def __init__(self, format=InputType.file):
        #self.fmt = ['file','files','dir']
        if format < InputType.len:
            self.format = format
        else:
            self.format = InputType.file
    def get_input_format(self):
        return self.format

