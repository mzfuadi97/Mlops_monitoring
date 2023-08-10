# Submission 1: Machine Learning Pipeline - Churn Prediction

Username dicoding: mzfuadi97

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Churn Prediction](https://archive.ics.uci.edu/ml/datasets/bank+marketing) |
| Masalah | Masalah yang dihadapi oleh bank adalah churn atau perpindahan pelanggan. Churn merujuk pada situasi di mana pelanggan meninggalkan atau berhenti menggunakan layanan bank. Churn pelanggan dapat berdampak negatif pada pendapatan bank, citra merek, dan pertumbuhan bisnis secara keseluruhan. Oleh karena itu, penting bagi bank untuk memahami faktor-faktor yang memengaruhi churn pelanggan dan mengambil langkah-langkah untuk mengurangi tingkat churn tersebut[1] |
| Solusi machine learning | Churn yang dapat mengidentifikasi pelanggan yang memiliki kemungkinan tinggi untuk churn di masa depan, oleh karena itu akan dilakukan prediksi dengan menyesuaikan dataset. Dengan sebuah sistem prediksi penyakit gagal jantung, diharapkan para tenaga medis maupun masyarakat dapat terbantu untuk dapat mendeteksi penyakit ini lebih awal. |
| Metode pengolahan | Pada data Churn Prediction digunakan pada proyek ini terdapat dua tipe data, yaitu data kategorikal dan numerik. Metode yang digunakan untuk mengelolah data tersebut yaitu mentransformasikan data kategorikal menjadi bentuk one-hot encoding dan menormalisasikan data numerik kedalam range data yang sama. |
| Arsitektur model | Model yang dibangun cukup sederhana hanya menggunakan Dense layer dan Dropout layer sebagai hidden layer pada model neural network dan memiliki 1 output layer. |
| Metrik evaluasi | Metric yang digunakan pada model yaitu AUC, Precision, Recall, BinaryAccuracy, TruePositive, FalsePositive, TrueNegative, FalseNegative untuk mengevaluasi performa model sebuah klasifikasi|
| Performa model | Model yang dibuat menghasilkan performa yang cukup baik dalam memberikan sebuah prediksi dan dari pelatihan yang dilakukan menghasilkan binary_accuracy sebesar 94% dan val_binary_acuracy sebesar 90%, hasil seperti ini sudah cukup baik untuk sebuah sistem klasifikasi namun masih bisa ditingkatkan lagi |
| Opsi deployment | Untuk deployment, sistem ini akan dideploy menggunakan platform railway |
| Web app | [churn-prediction](https://churn-prediction-production.up.railway.app/v1/models/churn-prediction/metadata)|
| Monitoring | Monitoring pada sistem ini dilakukan menggunakan prometheus dan grafana. Disini hanya dilakukan proses monitoring untuk menampilkan request yang masuk pada sistem yang akan menamplkan status pada tiap request yang dilakukan, pada sistem ini terdapat tiga status yang ditampilkan yaitu apabila proses request pada sistem klasifikasi not found, invalid argument dan proses klasifikasi berhasil ditandakan dengan ok |
