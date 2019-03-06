import hashlib, linecache
from datetime import datetime
from multiprocessing import Process
# title = "  ██▓███   █     █░    ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███\n"
# title += "▓██░  ██▒▓█░ █ ░█░   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒\n"
# title += "▓██░ ██▓▒▒█░ █ ░█    ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒\n"
# title += "▒██▄█▓▒ ▒░█░ █ ░█    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  \n"
# title += "▒██▒ ░  ░░░██▒██▓    ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒\n"
# title += "▒▓▒░ ░  ░░ ▓░▒ ▒     ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░\n"
# title += "░▒ ░       ▒ ░ ░       ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░\n"
# title += "░░         ░   ░     ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ "
# print(title)                                                       
def run_tests(filename, hashes):
    print("[*] Parsing passwords ... ")
    i = 1
    while linecache.getline(filename, i) != '':
        pw = linecache.getline(filename, i).rstrip("\n")
        print(pw)
        if len(hashes) == 0:
            print("[*] No hashes left in hash list! Exiting ...")
            break
        
        starttime = datetime.now()
        current_pass = pw.rstrip("\n")
        pass_hash = hashlib.md5(current_pass.encode()).hexdigest()
        if pass_hash in hashes:
            diff = ((datetime.now()-starttime).microseconds)/1000
            string = "The password for hash value %s is %s. " % (pass_hash, current_pass)
            string += "It takes the program %s sec to recover this password." % (diff)
            hashes.remove(pass_hash)
            print(string)
        linecache.clearcache()
        i += 1

if __name__ == '__main__':
    start_time = datetime.now()
    hashes = ["6f047ccaa1ed3e8e05cde1c7ebc7d958",
            "275a5602cd91a468a0e10c226a03a39c",
            "b4ba93170358df216e8648734ac2d539",
            "dc1c6ca00763a1821c5af993e0b6f60a",
            "8cd9f1b962128bd3d3ede2f5f101f4fc",
            "554532464e066aba23aee72b95f18ba2"]
    print("[*] Hashes loaded ...")

    filename = 'crackstation-human-only.txt'
    run_tests(filename, hashes)
    total_time = datetime.now() - start_time
    print("Total time running: %s" % total_time)

# blah blah