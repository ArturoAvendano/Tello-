import tello
import sys
from datetime import datetime
import time


def main():
    start_time = str(datetime.now())
    file_name = sys.argv[1]
    f = open(file_name, "r")
    commands = f.readlines()
    drone = tello.Tello('',8889)
    for command in commands:
        if command != '' and command != '\n':
            command = command.rstrip()

            if command.find('delay') != -1:
                sec = float(command.partition('delay')[2])
                print 'delay %s' % sec
                time.sleep(sec)
                pass
            else:
                drone.send_command(command)

    log = drone.get_log()
    def _receive_thread(self):
        """Listen to responses from the Tello.

        Runs as a thread, sets self.response to whatever the Tello last returned.

        """
        while True:
            try:
                self.response, ip = self.socket.recvfrom(3000)
                #print(self.response)
            except socket.error as exc:
                print ("Caught exception socket.error : %s" % exc)
    out = open('log/' + start_time + '.txt', 'w')
    for stat in log:
        stat.print_stats()
        strr = stat.return_stats()
        out.write(strr)

if __name__ == "__main__":
    main()

"" ""
