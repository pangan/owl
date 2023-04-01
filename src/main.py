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

if __name__ == '__main__':
	good()
