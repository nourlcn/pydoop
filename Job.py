#encoding:utf8

class Job:
    def __init__(self,conf_instance):
        self.node_progress_kv={}
        self.progress=0
        
        #kv: hostname->tt_input_dir
        self.tt_input_dirs={}
        #same as tt_input_dirs
        self.tt_output_dirs={}		
    def get_master(self):
        pass
    def get_slave_list(self):
        slave_list=[]
        return slave_list
    def get_slave_num(self):
        return len(get_slave_list)
        
    def update_progress(self,percent,node):
        self.node_progress_kv[node]=percent        
        self.progress=()
    def get_progress(self):
		return self.progress


def test():
	job = Job()
	print job.get_progress()


test()
