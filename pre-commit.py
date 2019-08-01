from subprocess import Popen, PIPE
import sys
import logging


LOG_FILENAME = 'pre-commit.log'
TESTS_FILENAME = 'tests.py'


logging.basicConfig(
        filename=LOG_FILENAME,
        format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
        datefmt='%H:%M:%S',
        level=logging.WARNING
        )
command = [sys.executable, TESTS_FILENAME]
process = Popen(command, stdout=PIPE, stderr=PIPE)
output, error = process.communicate()

if process.returncode > 0:
    logging.warning('COMMIT FAILED. Command: {}, {}, {}'.format(command, output, error))
    exit(process.returncode)
