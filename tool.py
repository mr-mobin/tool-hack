import os
print"`````````````"
print "``coding`````"
print "|by|        `"
print "{MOBin.Dan} `"
print"``````````````"
print'0:{update}'
print'1:{fsociety}'
print'2:{hammer}'
print'3:{install kali}'
print'4:{PhoneSploit(hack with ip)}'
print'5:{sqlmap}'
print'6:{hack Facebook}'
print'7:{Phishing apple ID}'
print'8:{$can server(SMBGhost)}'
print'9:{hack with lnk files}'
print'10:{Brute-force}'
print'11:{install matasploit}'
print'12:{scanner}'
print'13:{hydra}'
print'14:{insta tool[vIP]}'
print'15:{ghost}{clinet hack}'
print'16:{fatrat(root)}'
print'17:{matasploit}'
x= input('enter your number:')

if x== 1:
	os.system("git clone https://github.com/Manisso/fsociety")
	os.system("cd fsociety") 
	os.system("bash install.sh")
	os.system("python2 fsociety.py")
if x== 2:
	os.system("git clone https://github.com/cyweb/hammer")
	os.system("cd hammer")
	os.system("python hammer.py")
if x== 3:
	os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter")
	os.system("./kalinethunter")
	os.system("startkali")
	os.system("wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2018.1_all.deb")
	os.system("apt install ./kali-archive-keyring_2018.1_all.deb")
if x== 4:
	os.system("git clone https://github.com/Zucccs/PhoneSploit")
	os.system("cd PhoneSploit")
	os.system("pip install colorama")
	os.system("python2 main_linux.py")
if x== 5:
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	os.system("cd sqlmap")
	os.system("python2 sqlmap.py")
if x== 6:
	os.system("git clone https://github.com/Gameye98/FBBrute")
	os.system("cd FBBrute")
	os.system("python fbbrute.py")
if x== 7:
	os.system("git clone https://github.com/JasonJerry/lockphish")
	os.system("cd lockphish")
	os.system("bash lockphish.sh")
if x== 8:
	os.system("git clone https://github.com/ollypwn/SMBGhost")
	os.system("cd SMBGhost")
	os.system("python3 scanner.py")
if x== 9:
	os.system("git clone https://github.com/thelinuxchoice/badlnk")
	os.system("cd badlnk")
	os.system("bash badlnk.sh")
if x== 10:
	os.system("git clone https://github.com/lanjelot/patator")
	os.system("cd patator")
	os.system("python patator.py")
if x== 11:
		os.system("bash <(curl -s https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh)")
if x== 12:
	os.system("git clone https://github.com/websploit/websploit.git")
	os.system("cd websploit")
	os.system("python setup.py install")
	os.system("websploit")
if x== 13:
	os.system("pkg install hydra")
	os.system("hydra")
if x== 14:
	os.system("git clone https://github.com/masokky/instagram-tools.git")
	os.system("cd instagram-tools")
	os.system("node index.js")
if x== 15:
	os.system("git clone https://github.com/entynetproject/ghost")	
	os.system("cd ghost")
	os.system("chmod +x install.sh")
	os.system("./install.sh")
	os.system("ghost")
if x== 16:
	os.system("git clone https://github.com/Screetsec/TheFatRat.git")
	os.system("cd TheFatRat")
	os.system("chmod +x setup.sh && ./setup.sh")
if x== 17:
        os.system("pkg install wget")
        os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
        os.system("chmod +x metasploit.sh")
        os.system("./metasploit.sh")
if  x== 0:
        os.system("cd ..")
	os.system("rm -rf tool-hack")
	os.system("git clone https://github.com/Mobin-Dan/tool-hack.git")
	os.system("cd tool-hack")
	os.system("python2 tool.py")


