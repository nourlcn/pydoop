
import sys,os
from Job import Job
from util.Configuration import Configuration

def get_job_options(argv=[]):
	if len(argv) == 0:
		return {}
	
	if len(argv) % 2 == 1:
		print "args not match"
		return {}
	
	argv_len = len(argv)
	i = 0
	result = {}
	while(i < argv_len):
		result[argv[i]]=argv[i+1]
		i = i + 2
	print result
	return result

def jt_comminicate_with_tt():
	#store tt hostname
	tt_list=[]
	tt_progress=[]
	tt_num = 0;
	
	
	
	pass

if __name__ == '__main__':
#	print "hello"
    argv = sys.argv
    #print type(argv)
    #job_options is a dict.
    if argv[0] != "jobtracker.py":
		print "Error Command Format"
    job_options = get_job_options(argv[1:])
	
	conf = Configuration(job_options)
    
    job = Job(conf)
    
    pid = os.fork()
    if pid == 0:
		jt_communicate_with_tt()
	else:
		exec_job()
