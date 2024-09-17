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



