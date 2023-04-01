import time
import subprocess
import signal

all_processes = []

def run_mine():
	returncode = None
	full_command = '../../debug/.venv/bin/debin'
	child_process = subprocess.call(full_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	while returncode is None:
		time.sleep(1)
		returncode = child_process.poll()
	print(f'return code = {returncode}')

def gr_exit(*args):
	global all_processes
	for p in all_processes:
		print(f'trying to kill {p}...')
		p.terminate()

	print('Exit')
	exit(0)

def good():
	signal.signal(signal.SIGINT, gr_exit)
	global all_processes
	for a in range(17):
		full_command1 = '../../debug/.venv/bin/debin'
		child_process1 = subprocess.Popen(full_command1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		all_processes.append(child_process1)

	print(all_processes)
	while True:
		pass


def foo():
	signal.signal(signal.SIGINT, gr_exit)
	global all_processes
	bs = '../../debug/.venv/bin/'
	cms = [f'{bs}debin', f'{bs}exit_code', f'{bs}make_exception']

	for cc in cms:
		child = subprocess.Popen(cc, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		all_processes.append(child)

	print('Running')
	while True:
		time.sleep(1)
		new_pr_list = []
		for cc in all_processes:
			error_code = cc.poll()
			# output, error_code = cc.communicate()
			if error_code:
				print(f'---->>> {cc} exit: {error_code}, output = {cc.stderr.read()}')
				cc.terminate()
			else:
				new_pr_list.append(cc)
		all_processes = new_pr_list



if __name__ == '__main__':
	foo()
