# 🏆 Tubes PBO dan Handson 4 SO
## Daftar Konten
### [👨🏽‍💻 Tubes PBO : Dungeon Fighter](#tubes)
### [🖋 Cara Bermain](#guide)
### [⚓ UML Class Digram Proyek](#UML)
### [💻 Handson 4 - Docker 2](#handson)
### [🚀 Cara Menjalankan Container (Windows)](#container)
### [🎥 Video Demo Container](#Demo)
### [💂🏼‍♀️💂🏼 Anggota Kelompok](#angkel)
    

<a name="tubes" />

## 👨🏽‍💻 Tubes PBO : DUNGEON FIGHTER
### Game Dungeon Fighter
Proyek ini berisikan file file esensial yang menyusun game Dungeon Fighter.
Library yang digunakan:
* pygame
* os
* sys
* pygame-widgets

<a name="UML" />

### ⚓ UML Class Digram Proyek
UML Diagram Class Proyek dapat dilihat [disini](https://app.diagrams.net/#G1dlkLDjpyVCzWbg-prvUUIHKn4et4n6fv) (Belum final)

<a name="guide" />

### 🖋 Cara Bermain
-   Game memiliki 3 menu saat dijalankan, yaitu start, guide dan exit
-   Guide akan menampilkan window (jendela) yang berisi petunjuk permainan
-   Exit akan menghentikan program / game.
-   Menu Start akan memulai permainan
-   Setelah memulai player akan diarahkan pada character selection
-   Setelah memilih karakter dan lawan, player dapat memilih arena dan difficulty
-   Player dapat menggunakan basic attack, dan skill untuk memberikan damage kepada lawan.
    Player memiliki indikator yang berupa bar energi dibawah bar healthpoint
    Penggunaan skill membutuhkan 2 energi yang didapat dari setiap selesai melakukan attack normal
-   Monster juga memiliki mekanisme khusus yaitu buff, buff ini memiliki indikator dibawah healthpoints
    Buff akan dipicu setiap 4 turn monster.
-   Game ini juga memiliki fitur pause (jeda) yang bisa dijalankan dengan menekan tombol pause (berupa ikon dengan dua bar vertikal) di layar atau menekan tombol <b><i>Esc</b></i> dan Untuk resume juga dapat dilakukan dengan menekan tombol <b><i>Esc</b></i> kembali ataupun dengan mengklik tombol <b><i>Resume</b></i> pada layar
-   Game berakhir ketika salah satu objek kehabisan healthpoints (HP = 0)
-   Setelah game berakhir, player dapat melakukan <b><i>try again</b></i> (kembali ke pemilihan karakter) ataupun kembali ke main menu
 
<a name="angkel" />

## 💂🏼‍♀️💂🏼 Anggota Kelompok

- Ardhito Saputra; 120140003 -
    [@Ardhito12014003](https://github.com/Ardhito120140003)
- M. Fida Raditya; 120140037 -
    [@pusingbro01](https://github.com/pusingbro)
- Nabila Muthia Putri; 120140023 -
    [@nalskii](https://github.com/nalskii)
- Revan Fauzi Algifari; 120140049 -
    [@handshakers01](https://github.com/handshakers01) dan
    [@120140049](https://github.com/120140049)
- Sinta Dwi Putri; 120140033 -
    [@Sintadwiputri](https://github.com/Sintadwiputri)
- Yusuf Fadillah Ahmad; 120140245
    [@yusuffa01](https://github.com/yusuffa01)
    
<a name="handson"/>

## 💻 Handson 4 - Docker 2
### Game Dungeon Fighter
Handson 4 ini menginstruksikan untuk membuat container terhadap proyek game yang sudah dikerjakan
pada Tugas Besar PBO agar user tidak perlu menginstall paket-paket / modul modul lagi ketika ingin
menjalankan game. Game yang kami kembangkan adalah turn-based pve fighting game yang kami beri nama Dungeon Fighter. Goal dari permainan ini adlaah untuk saling mengalahkan satu sama lain.
Note: Untuk penjalanan container sejauh ini hanya bisa kami lakukan di windows, karena saat mencoba di linux terdapat error "X Error of failed request: BadValue... " yang membuat container force closed.

<a name="container"/>

### 🚀 Cara Menjalankan Container (Windows)

Untuk menjalankan container ada beberapa prerequisite:
Install 3 software dibawah ini.
- Docker dekstop, dapat didownload [disini](https://docs.docker.com/desktop/windows/install/)
- VcXsrv Windows X server, dapat didownload [disini](https://sourceforge.net/projects/vcxsrv/)
- PulseAudio Server, dapat didownload [disini](https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/)

1. Clone repository ini, masuk ke dalam direktori dengan perintah 'cd /pathtofile/Tugas-Besar-PBO' pada terminal
2. Jalankan docker desktop, dan lakukan build image pada terminal dengan perintah
   ```bash
   docker build -t dungeon-fighter .
   ```
3. Sambil menunggu build selesai, selanjutnya setup VcXsrv (X Launcher). Buka aplikasi XLauncher yang sudah diinstall. Pada window awal pilih Multiple Windows dengan display number -1 > next > Start no client > next > centang disable access control > next > finish. Atau juga dapat dilakukan dengan membuka file konfigurasi Xlauncher yang ada di repository ini yaitu file 'Docker.xlaunch'.
4. Konfigurasi file ~/pulseaudio/etc/default.pa dengan menambahkan line:
   ```bash
   load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1
   ```
5. Selanjutnya masih pada folde yang sama, edit file daemon.conf dengan menambahkan line:
   ```bash
   exit-idle-time = -1
   ```
6. Setelah itu pindah satu folder diatasnya dan masuk ke dalam folder bin. Jalankan pulseaudio.exe, jika muncul pesan seperti 'pulsecore/core-util.c: secure directory...' berarti pulseaudio server sudah berhasil dijalankan.
7. Setelah build Selesai jalankan container dengan perintah:
   ```bash
   docker run --rm dungeon-fighter
   ```
8. Container sudah berjalan dan game sudah dapat dimainkan

<a name="Demo" />

### 🎥 Video Demo Container
Untuk link video demonstrasi kontainer dapat diakses di halaman youtube dengan mengklik thumbnail dibawah <br />
<p align="center">
    <a href link="https://youtu.be/YCheHXCA2Hc/"><img src="https://img.youtube.com/vi/YCheHXCA2Hc/sddefault.jpg"/></a>
<p>
