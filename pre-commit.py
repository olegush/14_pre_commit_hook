from subprocess import Popen, PIPE
import sys
import logging

#result_code = 1

log_filename = 'pre-commit.log'
logging.basicConfig(
        filename=log_filename,
        format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
        datefmt='%H:%M:%S',
        level=logging.WARNING
        )

#print(sys.executable)
command = [sys.executable, '/home/oleg/python/devman/14_pre_commit_hook/tests.py']
process = Popen(command, stdout=PIPE, stderr=PIPE)
#print(process)
process.wait()

#if process.returncode > 0:
logging.warning('Commit failed: {}, {}, {}, {}'.format(command, process.returncode, process.stdout, process.stderr))

exit(process.returncode)
