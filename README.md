
# Handson 4 - Docker 2 | Tubes PBO : DUNGEON FIGHTER
## Handson 4
Handson 4 ini menginstruksikan untuk membuat container terhadap proyek game yang sudah dikerjakan pada Tugas Besar PBO agar
user tidak perlu menginstall paket-paket / modul modul lagi ketika ingin menjalankan game.

## Dungeon Fighter 
Proyek ini berisikan file file esensial yang menyusun game Dungeon Fighter.
Library yang digunakan:
* pygame
* os
* sys
* pygame-widgets

UML Diagram Class Proyek dapat dilihat [disini](https://app.diagrams.net/#G1dlkLDjpyVCzWbg-prvUUIHKn4et4n6fv)

## Authors

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
- Yusuf Fadillah Ahmad; 120140245
    [@yusuffa01](https://github.com/yusuffa01)



## Running Tests (Windows)

Untuk menjalankan container ada beberapa prerequisite:
Install 3 software dibawah ini.
- Docker dekstop, dapat didownload [disini](https://docs.docker.com/desktop/windows/install/)
- VcXrv Windows X server, dapat didownload [disini](https://sourceforge.net/projects/vcxsrv/)
- PulseAudio Server, dapat didownload [disini](https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/)

1. Clone repository ini, masuk ke dalam direktori dengan perintah 'cd /path/to/file/Tugas-Besar-PBO' pada terminal
2. Jalankan docker desktop, dan lakukan build image pada terminal dengan perintah
```bash
docker build -t dungeon-fighter .
```
3. Setelah build selesai, selanjutnya setup VcXrv (X Launcher). Buka aplikasi XLauncher yang sudah diinstall


## Guide
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
    -   Game ini juga memiliki fitur pause (jeda) yang bisa dijalankan dengan menekan tombol pause (berupa ikon
        dengan dua bar vertikal) di layar atau menekan tombol 'Esc' dan Untuk resume juga dapat dilakukan dengan
        menekan tombol 'Esc' kembali ataupun dengan mengklik tombol 'Resume' pada layar
    -   Game berakhir ketika salah satu objek kehabisan healthpoints (HP = 0)
    -   Setelah game berakhir, player dapat melakukan 'try again' (kembali ke pemilihan karakter) ataupun kembali
        ke main menu
