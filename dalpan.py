#----------------------------------------------
# Tools Admin Page Finder
# Follow me on Instagram : dalpan_id
#----------------------------------------------


import httplib
import socket
import sys

try:
    print "\t
    print "\t ____    _    _     ____   _    _   _      ___ ____   "
    print "\t|  _ \  / \  | |   |  _ \ / \  | \ | |    |_ _|  _ \  "
    print "\t| | | |/ _ \ | |   | |_) / _ \ |  \| |_____| || | | | "
    print "\t| |_| / ___ \| |___|  __/ ___ \| |\  |_____| || |_| | "
    print "\t|____/_/   \_\_____|_| /_/   \_\_| \_|    |___|____/  "
    print "\t                                                   

    print "\t Author : Dalpan     ( https://newbiengapak.com ) "
    print "\t My Team             ( http://ost-cyber.zone.id ) "
    print "\t"
    var1 = 0
    var2 = 0

    php = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/', 'usuario/',
       'administrator/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/',
       'panel-administracion/', 'instadmin/',
       'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php', 'admin/login.php',
       'admin/admin.php', 'admin/account.php',
       'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php',
       'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
       'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php', 'admin/home.php',
       'admin_area/login.html', 'admin_area/index.html',
       'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
       'admin/account.html', 'adminpanel.html', 'webadmin.html',
       'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html',
       'admin_login.html', 'panel-administracion/login.html',
       'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php',
       'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php',
       'administrator/account.php', 'administrator.php', 'admin_area/admin.html', 'pages/admin/admin-login.php',
       'admin/admin-login.php', 'admin-login.php',
       'bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html', 'admin/home.html',
       'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php',
       'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'admin/admin-login.html',
       'admin-login.html', 'controlpanel.php', 'admincontrol.php',
       'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.php',
       'adminarea/index.html', 'adminarea/admin.html',
       'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html',
       'admin/cp.html', 'cp.html', 'adminpanel.php', 'moderator.html',
       'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html',
       'administrator.html', 'login.html', 'modelsearch/login.html',
       'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
       'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
       'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.php', 'account.html',
       'controlpanel.html', 'admincontrol.html',
       'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php',
       'admin.php', 'adminarea/index.php',
       'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php', 'panel-administracion/admin.php',
       'modelsearch/index.php',
       'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php', 'admin2.php',
       'admin2/login.php', 'admin2/index.php', 'usuarios/login.php',
       'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php', 'administratorlogin.php']

    asp = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'moderator/', 'webadmin/',
       'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/',
       'memberadmin/', 'administratorlogin/', 'adm/', 'account.asp', 'admin/account.asp', 'admin/index.asp',
       'admin/login.asp', 'admin/admin.asp',
       'admin_area/admin.asp', 'admin_area/login.asp', 'admin/account.html', 'admin/index.html', 'admin/login.html',
       'admin/admin.html',
       'admin_area/admin.html', 'admin_area/login.html', 'admin_area/index.html', 'admin_area/index.asp',
       'bb-admin/index.asp', 'bb-admin/login.asp', 'bb-admin/admin.asp',
       'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html',
       'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html',
       'administrator/index.html', 'administrator/login.html', 'administrator/account.html', 'administrator.html',
       'login.html', 'modelsearch/login.html', 'moderator.html',
       'moderator/login.html', 'moderator/admin.html', 'account.html', 'controlpanel.html', 'admincontrol.html',
       'admin_login.html', 'panel-administracion/login.html',
       'admin/home.asp', 'admin/controlpanel.asp', 'admin.asp', 'pages/admin/admin-login.asp', 'admin/admin-login.asp',
       'admin-login.asp', 'admin/cp.asp', 'cp.asp',
       'administrator/account.asp', 'administrator.asp', 'acceso.asp', 'login.asp', 'modelsearch/login.asp',
       'moderator.asp', 'moderator/login.asp', 'administrator/login.asp',
       'moderator/admin.asp', 'controlpanel.asp', 'admin/account.html', 'adminpanel.html', 'webadmin.html',
       'pages/admin/admin-login.html', 'admin/admin-login.html',
       'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'user.asp', 'user.html',
       'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
       'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'adminarea/index.html',
       'adminarea/admin.html', 'adminarea/login.html',
       'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html',
       'modelsearch/admin.html', 'admin/admin_login.html',
       'admincontrol/login.html', 'adm/index.html', 'adm.html', 'admincontrol.asp', 'admin/account.asp',
       'adminpanel.asp', 'webadmin.asp', 'webadmin/index.asp',
       'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp', 'admin_login.asp',
       'panel-administracion/login.asp', 'adminLogin.asp',
       'admin/adminLogin.asp', 'home.asp', 'admin.asp', 'adminarea/index.asp', 'adminarea/admin.asp',
       'adminarea/login.asp', 'admin-login.html',
       'panel-administracion/index.asp', 'panel-administracion/admin.asp', 'modelsearch/index.asp',
       'modelsearch/admin.asp', 'administrator/index.asp',
       'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 'admin2.asp', 'admin2/login.asp',
       'admin2/index.asp', 'adm/index.asp',
       'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 'administratorlogin.asp', 'siteadmin/login.asp',
       'siteadmin/index.asp', 'siteadmin/login.html']

    js = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/', 'usuario/',
      'administrator/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/',
      'panel-administracion/', 'instadmin/',
      'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.js', 'admin/index.js', 'admin/login.js',
      'admin/admin.js', 'admin/account.js',
      'admin_area/admin.js', 'admin_area/login.js', 'siteadmin/login.js', 'siteadmin/index.js', 'siteadmin/login.html',
      'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
      'admin_area/index.js', 'bb-admin/index.js', 'bb-admin/login.js', 'bb-admin/admin.js', 'admin/home.js',
      'admin_area/login.html', 'admin_area/index.html',
      'admin/controlpanel.js', 'admin.js', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
      'admin/account.html', 'adminpanel.html', 'webadmin.html',
      'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html',
      'panel-administracion/login.html',
      'admin/cp.js', 'cp.js', 'administrator/index.js', 'administrator/login.js', 'nsw/admin/login.js',
      'webadmin/login.js', 'admin/admin_login.js', 'admin_login.js',
      'administrator/account.js', 'administrator.js', 'admin_area/admin.html', 'pages/admin/admin-login.js',
      'admin/admin-login.js', 'admin-login.js',
      'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html', 'login.js',
      'modelsearch/login.js', 'moderator.js', 'moderator/login.js',
      'moderator/admin.js', 'account.js', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html',
      'controlpanel.js', 'admincontrol.js',
      'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.js',
      'adminarea/index.html', 'adminarea/admin.html',
      'webadmin.js', 'webadmin/index.js', 'acceso.js', 'webadmin/admin.js', 'admin/controlpanel.html', 'admin.html',
      'admin/cp.html', 'cp.html', 'adminpanel.js', 'moderator.html',
      'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html',
      'administrator.html', 'login.html', 'modelsearch/login.html',
      'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
      'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
      'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.js', 'account.html',
      'controlpanel.html', 'admincontrol.html',
      'panel-administracion/login.js', 'wp-login.js', 'adminLogin.js', 'admin/adminLogin.js', 'home.js', 'admin.js',
      'adminarea/index.js',
      'adminarea/admin.js', 'adminarea/login.js', 'panel-administracion/index.js', 'panel-administracion/admin.js',
      'modelsearch/index.js',
      'modelsearch/admin.js', 'admincontrol/login.js', 'adm/admloginuser.js', 'admloginuser.js', 'admin2.js',
      'admin2/login.js', 'admin2/index.js', 'usuarios/login.js',
      'adm/index.js', 'adm.js', 'affiliate.js', 'adm_auth.js', 'memberadmin.js', 'administratorlogin.js']

    try:
        print ("Contoh : target.kalian.com")
        site = raw_input("Website yang ingin di Scan? : ")
        site = site.replace("http://", "")
        print ("\tChecking website " + site + "...")
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print "\tServer Online!!"
    except (httplib.HTTPResponse, socket.error) as Exit:
        raw_input("\t [!] Maaf.. Server Offline atau URL Tidak Valid ")
        exit()
    print "Masukkan Sumber Kode Situs :"
    print "1 PHP"
    print "2 ASP"
    print "3 JS"
    print "\nTekan angka dan ( Enter ) untuk scan tipe website\n"
    code = input("> ")

    if code == 1:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in php:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ("\n\n[+]" + host, "Halaman admin ditemukan!")
                raw_input("Tekan Enter Untuk Melanjutkan Scan\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, "Halaman admin yang ditemukan"
        print var2, "Total Halaman Yang Di Scan"
        raw_input("Selesai : Tekan Enter Untuk Keluar")

    if code == 2:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in asp:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ("\n\n[+]" + host, "Halaman admin ditemukan!")
                raw_input("Tekan Enter Untuk Melanjutkan Scan\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, "Halaman admin yang ditemukan"
        print var2, "Total Halaman Yang Di Scan"
        raw_input("Selesai : Tekan Enter Untuk Keluar")

    if code == 3:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in js:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ("\n\n[+]" + host, "Halaman admin ditemukan!")
                raw_input("Tekan Enter Untuk Melanjutkan Scan\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, "Halaman admin yang ditemukan"
        print var2, "Total Halaman Yang Di Scan"
        raw_input("Selesai : Tekan Enter Untuk Keluar")

except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Dibatalkan : Terjadi kesalahan. Periksa Pengaturan Internet"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Dibatalkan"
