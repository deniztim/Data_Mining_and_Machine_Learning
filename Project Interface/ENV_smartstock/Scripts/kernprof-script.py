#!c:\projects\datamining\env_smartstock\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'line-profiler==2.1.2','console_scripts','kernprof'
__requires__ = 'line-profiler==2.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('line-profiler==2.1.2', 'console_scripts', 'kernprof')()
    )
