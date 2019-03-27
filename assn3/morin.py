import hashlib
from datetime import datetime
                                                  
def run_tests(filename, hashes):
    print("[*] Parsing passwords ... ")
    f = open(filename, 'r')
    line = "x"
    for line in f:
        line = line.rstrip("\n")
        if len(hashes) == 0:
            print("[*] No hashes left in hash list! Exiting ...")
            break
        starttime = datetime.now()
        pass_hash = hashlib.md5(line.encode()).hexdigest()
        if pass_hash in hashes:
            diff = ((datetime.now()-starttime).microseconds)/1000
            string = "The password for hash value %s is %s. " % (pass_hash, line)
            string += "It takes the program %s sec to recover this password." % (diff)
            hashes.remove(pass_hash)
            print(string)
        
    if len(hashes) > 0:
        print("[*] Hashes not found ...")
        for hash in hashes:
            print("\t[*] %s" % hash)

if __name__ == '__main__':
    start_time = datetime.now()
    hashes = ["6f047ccaa1ed3e8e05cde1c7ebc7d958",
            "275a5602cd91a468a0e10c226a03a39c",
            "b4ba93170358df216e8648734ac2d539",
            "dc1c6ca00763a1821c5af993e0b6f60a",
            "8cd9f1b962128bd3d3ede2f5f101f4fc",
            "554532464e066aba23aee72b95f18ba2"]
    print("[*] Hashes loaded ...")

    filename = 'common_passwords.txt'
    run_tests(filename, hashes)
    total_time = datetime.now() - start_time
    print("Total time running: %s" % total_time)