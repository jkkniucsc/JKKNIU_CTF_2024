## Solution for `Lost Key`
> [!NOTE]
> *A simple yet effective technique to bypass a program's verification process by performing a memory dump. <br>
> This process captures the Python memory state, potentially revealing sensitive data, like loaded passwords, that can leak due to insufficient obfuscation or protection within the program’s memory.*


1. Start by running the program to load it into memory:
  ```sh
  python lost_key.py
  ```
2. Use the following command to identify the process ID (PID):
  ```sh
  pidof python
  ```

> Such as: 
  ```sh
  $ pidof python         
  1271597
  ```
3. Since the program performs a comparison in memory, obtaining a memory dump can help retrieve the necessary key. <br> Use the following script `memdump.py` to analyze and extract data from the memory dump:
  ```python
  #https://gist.githubusercontent.com/Dbof/b9244cfc607cf2d33438826bee6f5056/raw/aa4b75ddb55a58e2007bf12e17daadb0ebebecba/memdump.py
#! /usr/bin/env python3
import sys
import re

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<process PID>', file=sys.stderr)
        exit(1)

    pid = sys.argv[1]

    # maps contains the mapping of memory of a specific project
    map_file = f"/proc/{pid}/maps"
    mem_file = f"/proc/{pid}/mem"

    # output file
    out_file = f'{pid}.dump'

    # iterate over regions
    with open(map_file, 'r') as map_f, open(mem_file, 'rb', 0) as mem_f, open(out_file, 'wb') as out_f:
        for line in map_f.readlines():  # for each mapped region
            m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
            if m.group(3) == 'r':  # readable region
                start = int(m.group(1), 16)
                end = int(m.group(2), 16)
                mem_f.seek(start)  # seek to region start
                print(hex(start), '-', hex(end))
                try:
                    chunk = mem_f.read(end - start)  # read region contents
                    out_f.write(chunk)  # dump contents to standard output
                except OSError:
                    print(hex(start), '-', hex(end), '[error,skipped]', file=sys.stderr)
                    continue
    print(f'Memory dump saved to {out_file}')
  ```
  To dump the memory of the Python process, use the following command:
  ```sh
  python memdump.py 1271597
  ```
  If the memory dump is successful, you will see a confirmation message, and the dump file will be saved in the current working directory:
  `Memory dump saved to 1271597.dump`

4. To search for the password in the memory dump, use the `strings` command followed by `grep` to filter relevant results:
  ```sh
  strings 1271597.dump | sort -u | grep pass
  ```
  The `grep` command will help you narrow down the results, making it easier to locate the password in the dump file.

5.Password: `passw0rdpassw0rdpassw0rdpassw0rdpassw0rdMySup3rs3cr37p455W0rDpassw0rdpassw0rdpassw0rdpassw0rd`


### **Flag**: `JKKNIUCTF{5L0w_D4Y!_PR4c7Ic3_D308Fu5c47i0N}`
