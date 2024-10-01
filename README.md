STEP BY STEP
- direktori main adalah direktori dari aplikasinya
- direktori house-of-kyny adlaah direktori project

1. kita perlu membuat sebuah direktori untuk aplikasi main.
2. daftarkan main ke dalam project house-of-kyny
3. membuat direktori templates didalam direktori main yang sbeelumnya sudah kita buat, dan isi dari direktori templates adalah template yang berguna untuk menampilkan data program 
4. Buat file main.html di dalam direktori templates
5. Isi file main.html dengan informasi aplikasi, dimana isinya adalah nama aplikasinya, nama , npm, kelas.
6. membuka file models.py dalam direktori main
7. lakukan migrasi model, Setelah mengubah model, jalankan migrasi untuk memperbarui struktur database.
8. hubungkan views.py dengan template
9. Buat fungsi show_main di views.py dalam direktori main
10. modifikasi main.html 
11. routing URL main dengan membuat file urls.py dalam direktori main
12. Routing URL 'house of kyny' digunakan untuk menambahkan rute URL ke dalam urls.py project dan menghubungkannya dnegan tampilan main.
13. deploy ke PWS.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

request dari para klien -> web server environment -> menjalankan django -> permintaanya kemudian diteruskan ke views.py -> didalam views.py, django akan mencari data terkait menggunakan models.py -> Data yang ditemukan akan dikembalikan ke template HTML untuk ditampilkan kepada pengguna -> menampilkan respon para klien
![alt text](image-2.png)

fungsi git dalam pengembangan perangkat lunak
Git adalah Salah satu perangkat lunak atau tools kolaborasi coding yang sering dipakai karena mudah dan fleksibel. Jika sedang mengembangkan proyek kolaborasi untuk membuat software atau aplikasi,
git berfungsi sebagai sistem kontrol versi untuk menyimpan, mengelola, dan berbagi kode sumber secara efektif dan kolaboratif . 


mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Mudah untuk Dimengerti, karena Django dirancang untuk memudahkan pemula memahami konsep-konsep dasar pengembangan web. 
- Skalabilitas : Django kuat untuk menangani aplikasi-aplikasi berskala besar 
- Terorganisir dan Tertata: Framework ini mengadopsi pola desain Model-View-Template (MVT) yang membantu pemula memahami pemisahan tanggung jawab dalam aplikasi web.


Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena mereka berfungsi sebagai jembatan antara objek-objek dalam kode Python dan tabel-tabel dalam basis data relasional. ORM memungkinkan pengembang untuk mengelola data menggunakan konsep objek dari bahasa pemrograman, tanpa perlu menulis query SQL secara langsung untuk berinteraksi dengan basis data.



TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data delivery memastikan bahwa informasi yang tersimpan di server atau database pusat dapat diakses oleh pengguna di berbagai lokasi. Dengan data delivery, platform dapat terhubung dan berintegrasi dengan layanan lain seperti API eksternal. Ini memungkinkan data yang diperlukan dikirim dan diterima dalam format yang sesuai, sehingga mendukung kolaborasi dan interaksi yang efisien antar sistem. Data delivery memastikan bahwa komunikasi data antara berbagai komponen dan sistem dapat berlangsung dengan lancar, memfasilitasi akses yang mudah dan pengolahan informasi yang tepat.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON memiliki format penulisan yang lebih mudah dibandingkan XML, kalau JSON memakai “{}” untuk mempresentasikan objek dan array, tetapi kalau XML setiap elemen harus memakai format <tag>....pesan yang ingin disampaikan..</tag>, yang membuat format XML lebih panjang dan sulit untuk dibaca.

XML dirancang untuk situasi yang memerlukan dokumen dengan struktur yang kompleks dan terperinci, sering kali menyertakan metadata dan format yang lebih rumit. Sebaliknya, JSON lebih sering dipilih untuk aplikasi yang memerlukan komunikasi data yang cepat dan efisien, sementara XML lebih cocok digunakan ketika detail dan struktur dokumen yang rumit sangat diperlukan.


3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Validasi Data Input:
Method `is_valid()` memeriksa data yang dimasukkan ke dalam form dan memastikan data tersebut sesuai dengan aturan yang ditentukan, seperti tipe data yang benar, batas maksimal panjang, format email yang tepat, dll. Jika data tersebut valid maka akan mengembalikan nilai True, sebaliknya jika data tersebut tidak valid akan mengembalikan nilai False.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

- Mengapa kita membutuhkan csrf_token saat membuat form di Django?
Karena CSRF digunakan untuk melindungi aplikasi dari serangan CSRF, dimana penyerang mencoba untuk memanipulasi para pengguna untuk melakukan tindakan yang tidak diinginkan di aplikasi web. Tetapi jika kita menambahkan CSRF token kedalam form, aplikasi tersebut dapat memastikan bahwa permintaan yang kita terima berasal dari sumber yang sah dan terpercaya.

- Apa yang terjadi jika kita tidak menambahkan csrf_token pada form Django?
Penyerang dapat mengeksploitasi sesi pengguna yang telah login untuk melakukan tindakan yang merugikan, seperti mengubah pengaturan akun atau mencuri informasi pribadi, tanpa sepengetahuan atau persetujuan pengguna.

- Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Dengan mengirimkan permintaan palsu, Penyerang dapat membuat situs web yang berbahaya dan mengirimkan pesan POST ke web yang sah. Apalagi jika aplikasi tersebut tidak menggunakan CSRF token, aplikasi dapat memproses permintaan tersebut dan dianggap seolah-olah berasal dari pengguna yang sah.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- membuat sebuah direktori templates pada direktori utama folder dan membuat berkas HTML baru bernama base.html yang berisi kerangka umum untuk halaman web.
- menambahkan isi untuk file settings.py di bagian DIRS, menambahkan extends dan block content pada file main.html dan menambahkan import uuid pada file models.py serta lakukan migrasi model
- membuat file baru dengan nama forms.py pada direktori main untuk membuat form dan isi dari form akan disimpan sebagai sebuah objek. menambahkan bebrapa import pada file views.py serta membuat fungsi yang menerima parameter request.
- mengubah fungsi show_main dengan menambahkan fungsi ProductEntry.objects.all() yang digunakan unruk mengambil seluruh objek yang tersimpan pada database.
- mengimport beberapa fungsi yang sudah kita buat tadi, lalu menambhakan path URL kedalam variabel urlpatterns dan urls.py di main. membuat file baru dengan nama create_product_entry.html pada direktori main/templates. lalu membuka main.html dan tambahkan kode {% block content %} untuk menampilkan data mood
- lalu menjalankan proyek django dengan perintah python manage.py runserver  dan bukalah website http://localhost:8000/ 
- bukalah file views.py pada direktori main, dan tambahkan import HttpResponse dan Serializer, dan buatlah fungsi baru dengan nama show_xml. Buka file urls.py pada direktori main dan tambahkan path url ke dalam urlpatterns, lalu jalankan django dan bukalah http://localhost:8000/xml/ 
- buka views.py pada direktori main, dan buat fungsi dengan nama show_json, lalu tambahkan return function berupa HttpResponse yang berisi parameter data hasil query, kemudian buka file urls.py pada direktori main dan tambahkan import fungsi yang telah dibuat, kemudian tambahkan juga path url ke dalam urlpatterns, dan jalankan projek kamu di http://localhost:8000/json/
- selanjutnya kita akan mengembalikan data berdasarkan ID dalam bentuk XML dan JSON, pertama buka view.py dan buat sebuah fungsu dengan nama show_xml_by_id dan show_json_by_id dan tambahkan nama fungsi tersebut ke dalam file urls.py , lalu tambahkan juga path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi. kemudian jalankan projek django kamu http://localhost:8000/json/[id]/ atau http://localhost:8000/xml/[id]/ 
- lalu masuk ke postman, dan masukan 4 link yang sudah dibuat tadi di bagian GET, dan setelah itu kita lakukan push ke Github dan PWS. 

6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
![alt text](<Screenshot 2024-09-17 at 17.08.22-1.png>)
![alt text](<Screenshot 2024-09-17 at 17.08.34.png>)
![alt text](<Screenshot 2024-09-17 at 17.12.06.png>)
![alt text](<Screenshot 2024-09-17 at 17.12.49.png>)





Tugas 4

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect:
- Hanya menerima URL sebagai argumen.
- Mengembalikan respon HTTP dengan status 302.

redirect:
- Merupakan fungsi yang lebih fleksibel, bisa menerima URL, view Django, atau object model.
- Pada akhirnya, tetap menghasilkan HttpResponseRedirect.

2. Jelaskan cara kerja penghubungan model Product dengan User!
Hubungan antara model Product dan model User di Django dapat dibangun menggunakan ForeignKey, yang mengizinkan setiap produk terhubung dengan satu pengguna. Hal ini memungkinkan pengelolaan data yang lebih efektif dan efisien, serta satu pengguna dapat memiliki banyak produk dan dapat dengan mudah mengakses produk-produk tersebut melalui relasi yang telah dibuat.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Perbedaan : 
- authentication adalah proses memverifikasi user, hal ini harus dipenuhi agar server bisa mengklaim siapa usernya, biasanya hal ini dilakukan dengan memverifikasi username dan password, apabila dua hal tersebut sesuai dengan data yang ada pada sistem maka user tersebut dianggap sah.

- authorization : proses ini dijalankan apabila user berhasil diotentikasi. pada tahap ini, sistem akan menentukan apa yang user dapat lakukan berdasarkan hak akses yang dimilikinya. 

Saat pengguna Login : 
Pertama melakukan otentikasi yaitu dengan user memasukan username serta pssword ke sistem , kemudian melakukan verifikasi untuk memastikan bahwa identitas yang baru dimasukkan sesuai dengan identitas yang tersimpan pada sistem, selanjutnya keberhasilan otentikasi yaitu apabila identitas sesuai maka sistem mengautentikasi user, dan yang terakhir adalah otoritas yaitu sistem memeriksa izin user untuk menentukan apa yang dapat dilakukan oleh user pada sistem tersebut.

Bagaimana Django mengimplementasikan kedua kosep tersebut : 
- Otentikasi : 
Django menyediakan sistem otentikasi yang memungkinkan user untuk login dan logout dari sistem. Didasarkan pada modul "django.contrib.auth",contoh beberapa fitur yang menyediakan fitur-fitur tersebut adalah tampilan login dan logout, user, dan backend otentikasi.
- Otoritas : 
Sistem pada django yang memberikan akses kepada user, fitur-fiturnya antara lain : izin, group, dan Pemeriksaan izin 

Dengan adanya modul django.contrib.auth, Django menyediakan sistem otentikasi yang detail serta fleksibel,  dan memungkinkan pengembang untuk dengan mudah mengelola otentikasi dan izin pengguna dalam aplikasi website.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Saat pengguna berhasil login, Django akan mencatat serta membuat sesi login pengguna tersebut dan pengguna akan diberikan kode unik, kode unik tersebut akan disimpan dalam cookie. Dengan cara ini, Django dapat mengenali pengguna ketika mereka melakukan login lagi ke webnya.
Kemudian Cookies, cookies merupakan data kecil yang disimpan di browser user. APabila user mengunjungi kembali websitenya maka browser mengirimkan cookies ke server sehingga server dapat mengidentifikasi pengguna. 

Kegunaan lain dari cookies : 
- Cookies digunakan untuk melacak aktivitas user di situs web
- Selain mengingat pengguna yang telah berhasil login, cookie juga memiliki pengingatan yang membuat kita dapat memilih opsi "ingat saya" saat kita ingin login.
- Cookies dapat menyimpan preferensi pengguna.

Apakah semua cookies aman?
tidak, karena cookies dapat disalahgunakan apabila tidak dirawat/doijaga dan dikelola dengan baik,  Cookies menyimpan informasi pribadi yang harus dilindungi, dan kita harus mengatur flag secure cookies untuk memastikan bahwa cookies hanya dikirim melalui koneksi HTTPS, dimana hal ini akan mengurangi resiko penyadapan data.

Mengingat kembali user yang berhasil login melalui sesi dan cookie, memungkinkan pengolahan otentikasi yang efisien,  sehingga cookies juga mempunyai banyak kegunaan. jadi kita harus memperhatikan keamanan dan privasi saat menggunakannya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, kita membuat Fungsi dan forum registrasi.
Mengimpor UsercreationForm dan message dari django.contrib.auth ,dimana fungsi dari usercreationform adalah untuk memudahkan pembuatan formulir pendaftaran user dalam aplikasi web. Kemudian kita menambahkan fungsi registrasi, dimana fungsi ini berfungsi untuk menghasilkan formulir registrasi dan menghasilkan akun pengguna ketika di submit. Setelah itu kita membuat berkas HTML baru yang menyajikan halaman pendaftaran untuk pengguna baru. Formulir ini mengumpulkan data pendaftaran dan mengirimkannya ke server dengan aman. Melalui sistem pesan, pengguna dapat menerima umpan balik tentang status pendaftaran. kemudian kita mengimpor fungsi registrasi di views.py dan menambahkan path url kedalam urlpatterns.

Kedua, membuat fungsi Login, dengan menambahkan beberapa impor seperti authenticate, login, dan AuthenticationForm. Fungsi tersebut digunakan untuk melakukan autentikasi dan login. Kemudian kita menambah sebuah fungsi login_user di views.py dimana fungsi ini digunakan untuk melakukan login terlebih dahulu. apabila user valid, maka fungsi ini akan embaut session untuk pengguna yang berhasil login. Kemudian kita juga membuat file baru dengan nama login.html , template yang disediakan berguna untuk pengguna agar dapat masuk ke aplikasi dan menawarkan opsi untuk mendaftar jika mereka belum memiliki akun.

Ketiga, Merestriksi Akses halaman main dengan menambahkan import login_required yang berfungsi untuk mengimpor sebuah decorator yang bisa mengharuskan pengguna masuk(login) terlebih dahulu sbeleum mengakses sebuah halaman web. Kemudian menambahkan @login_required(login_url='/login') agar halaman main hanya dapat diakses oleh pengguna yang sudah login, kemudian kita menjalankan projek django dan membuka http://localhost:8000/ .

Keempat, Menggunakan data dari cookies dengan menambahkan data las login dan menampilkannya dihalaman main, lalu membuka file views.py dan mengimpor beberapa fungsi seperti import HttpResponseRedirect, reverse, dan datetime. kemudian kita menambahkan fungsionalitas cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. Kemudian pada fungsi show_main kita tambahkan 'last_login': request.COOKIES['last_login'], yang berfungsi untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan dihalaman web. Kemudian kita ubah fungsi logout_user  menjadi response.delete_cookie('last_login'), yang berfungsi untuk menghapus cookie last_login saat pengguna menekan logout. Kemudian kita menambahkan pesan yang akan ditampilkan di halaman utama yaitu sesi terakhir login, lalu jalankan projek django.

Kelima, keterangan untuk melihat cookie pada projek saya adalah saya membuka protocol localhost di chrome dan kemudian saya klik kanan pada halaman web saya, lalu saya memilih inspect dan tanda disamping Memory (>>) lalu memilih Application dan melihat cookie nya.

Keenam, Menghubungkan moodentry dengan user, dengan menambahkan import pada models.py (from django.contrib.auth.models import User)
dan menambahkan variabel dengan nama "user" yang berisi kode untuk menghubungkan satu product entry dengan satu user melalui sebauh relationship, dimana product entry pasti terasosialisasikan dengan seorang user. lalu menambahkan beberapa kepingan kode pada file views.py dengan parameter commit=false, bergna untuk mencegah django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. kemudian kita mengubah value dari product_entries dan context, gunanya kita ubah yaitu untuk menampilkan objek product__entry yang terasosiasikan dengan menyaring seluruh objek. dan kode request.user,username berfungsi untuk menampilakn username pengguna yang login. Kemudian simpan semua perubahan dan lakukan imigrasi, dan setelah itu akan ada eror yang muncul dan kita memilih angka 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat. Kemudian kita mengimoport os dan mengganti variabel DEBUG dengan kode yang telah disediakan.


TUGAS 5
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
inline style, karena melibatkan penerapan gaya secara langsung ke elemen HTML, dimana metode ini memeungkinkan penataan elemen tertentu dalam dokumen HTML itu sendiri, Alasan lain yaitu karena spesifik di elemen tertentu yang artinya inline style hanya memengaruhi elemen tertentu yang dianggap sebagai aturan yang spesifik dibandingkan dengan selektor lain.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Karena ini adalah metode sistem desain web yang mempunyai tujuan menghasilkan tampilan web yang terlihat baik pada seluruh perangkat seperti dekstop, tablet,mobile,dll.
Contoh aplikasi : 

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin : mengosongkan area di sekitar border(transparan)
Border : faris tepian yang membungkus konten dan paddingnya
Padding : mengosongkan area di sekitar konten (transparan)
Caranya dengan contoh yaitu : 
.element {
  margin: 20px;
  border: 2px solid black;
  padding: 15px;
}
Pada kode diatas, margin mengosongkan area di luar border, padding mengosongkan area di dalam border, dan border adalah garis di antara margin dan padding.

Jelaskan konsep flex box dan grid layout beserta kegunaannya!
flexbox : layout model satu dimensi yang dirancang mendistribusikan ruang diantara dalam satu baris atau kolom serta mempunyai kegunaan untuk mengatur elemen-elemen dalam tata letas linear.
grid layout : model dua dimensi yang memungkinkan penataan elemen dalam baris dan kolom, serta membuat struktut grid yang repsonsif dan multi-kolom. 
Keduanya digunakan untuk menciptakan tata letak responsif dan dinamis, tetapi Flexbox lebih fokus pada arah satu dimensi (baris atau kolom), sementara Grid mengelola arah dua dimensi (baris dan kolom).

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
pertama, kita menambahkan tailwind ke aplikasi dengan mengakses project Django kita, lalu membuka file base.html dan menambahkan tag <metaname="viewport>, lalu untuk menyambungkan template Django dengan tailwind, kita memanfaatkan script CDN.
Kedua, menambahkan fitur edit product pada aplikasi, dengan membuka views.py dan membuat fungsi baru serta menambahkan import pada views.py dan membuka berkas edit_mood.html serta membuka urls.py dan menambahkan beberapa import dan menambahkan path url didalam urlpatterns. Kemudian menambahkan {% url 'main:edit_product' mood_entry.pk %} untuk membangun URL.
Ktiga, menambahkan fitur Hapus mood pada aplikasi, dengan membuat fungsi dengan nama delete_mood di views.py dan membuka urls.py dan menambahkan beberapa import serta path url ke urlpatterns. Lalu membuka file main.html dan menambahkan url delete_moodnya.
Keempat, menambahkan Navigation Bar pada Aplikasi, menambahkan file navbar.html di templates yang sejajar dengan main lalu kaitkan main,html , create_product_entry.html, dan edit_product.html 
Kelima, konfigurasi static Files pada aplikasi, dengan menambahkan 'whitenoise.middleware.WhiteNoiseMiddleware' pada file settings.py dan memastikan variabel static_root , staticfiles_dirs, dan static_url dikonfigurasi.
Keenam, langkah ini adalah opsional jika kita ingin membuat gambar maka kita harus mengimpor gambar tersebut dahulu lalu memasukannya dalam folder static, dimana folder tersebut berisi folder css dan folder image. Lalu menghubungkan global.css dan script tailwind ke base.html, serta men custom styling ke global.css serta melakukan styling pada halaman login, kemudian kita membuat halaman juga di register.html lalu styling halaman home dan membuat card_product.html di folder main/templates, lalu kita styling lagi halaman create Product Entry dan styling halaman edit product.