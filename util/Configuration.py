# encoding:utf-8

import os,sys


from InputFormat import InputFormat

class Configuration:
    def __init__(self,job_options=None):
        self.input_format = InputFormat()
        self.input_dir  = options['-input']
        self.output_dir = options['-output']
        self.mapper  = ['-mapper']
        self.reducer = ['-reducer']
        
        pass
    def set_input_format(self, input_fmt):
        self.input_format = InputFormat(input_fmt)
    def get_input_format_instance(self):
        return self.input_format
    def get_global_conf(self):
        conf_result={}
        if os.isfile('../conf/global/master'):
            pass
        if os.isfile('../conf/global/slave'):
            pass
        conf_result['master']="coffee"
        conf_result['slave']="test01"
        return conf_result
    def get_current_node_conf(self):
        pass
    def update_global_conf(self):
        pass
    def update_current_node_conf(self):
        pass
        
        
    def get_input_dir(self):
		return self.input_dir
	def get_output_dir(self):
		return self.output_dir
	def get_mapper(self):
		return self.mapper
	def get_reducer(self):
		return self.reducer

        
        
        
def test():
    c = Configuration()
    i = c.get_input_format_instance()
    print i.get_input_format()
    
    
test()

