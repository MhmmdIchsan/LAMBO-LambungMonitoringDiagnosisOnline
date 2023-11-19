# lambo2.py

def deteksi_penyakit_lambung(gejala_terpilih, gejala_weights):
    gejala_penyakit = {
        'Gastritis': [1, 2, 3, 4, 13],
        'Dispepsia': [1, 2, 3, 4, 5, 6, 13],
        'Kanker Lambung': [3, 4, 7, 8, 12],
        'GERD': [1, 2, 4, 9, 10, 12],
        'Gastroenteritis': [1, 4, 6, 9, 11, 12],
        'Gastroparesis': [2, 3, 4, 7, 12, 14],
        'Tukak Lambung': [3, 4, 13, 15]
    }
    
    threshold = 0.1  # Adjust this threshold based on your preference
    hasil_deteksi = []

    for penyakit, gejala in gejala_penyakit.items():
        matching_score = 0
        total_weight = 0

        for i in gejala:
            matching_score += gejala_terpilih[i - 1] * gejala_weights[i - 1]
            total_weight += gejala_weights[i - 1]

        weighted_matching_percentage = matching_score / total_weight

        if weighted_matching_percentage >= threshold:
            hasil_deteksi.append({
                'penyakit': penyakit,
                'weighted_matching_percentage': weighted_matching_percentage
            })

    return hasil_deteksi
    

def solusi_dan_obat(penyakit):
    solusi_obat = {
        'Gastritis': {'solusi': 'Hindari makanan pedas dan asam, konsumsi makanan rendah lemak.', 'obat': 'Antasida'},
        'Dispepsia': {'solusi': 'Makan secara teratur, hindari makanan pedas dan asam.', 'obat': 'Antasida'},
        'Kanker Lambung': {'solusi': 'Pengobatan kanker, operasi, kemoterapi.', 'obat': 'Sesuai resep dokter'},
        'GERD': {'solusi': 'Hindari makanan berlemak dan pedas, minum obat antasida.', 'obat': 'Antasida, Inhibitor pompa proton'},
        'Gastroenteritis': {'solusi': 'Istirahat, minum cairan elektrolit, hindari makanan berat.', 'obat': 'Antidiare, Rehidrasi'},
        'Gastroparesis': {'solusi': 'Makan dalam porsi kecil, hindari makanan tinggi serat.', 'obat': 'Obat prokinetik, Inhibitor pompa proton'},
        'Tukak Lambung': {'solusi': 'Hindari makanan pedas dan asam, konsumsi makanan rendah lemak.', 'obat': 'Antasida, Antibiotik'}
    }

    return solusi_obat.get(penyakit, {'solusi': 'Tidak ada informasi solusi yang tersedia', 'obat': 'Tidak ada informasi obat yang tersedia'})

# These are your global variables that are used in the functions above
gejala_weights = [
    1,  # Weight for symptom 1
    1,  # Weight for symptom 2
    1,  # Weight for symptom 3
    1,  # Weight for symptom 4
    1,  # Weight for symptom 5
    1,  # Weight for symptom 6
    1,  # Weight for symptom 7
    1,  # Weight for symptom 8
    1,  # Weight for symptom 9
    1,  # Weight for symptom 10
    1,  # Weight for symptom 11
    1,  # Weight for symptom 12
    1,  # Weight for symptom 13
    1,  # Weight for symptom 14
    1   # Weight for symptom 15
]

gejala_nama = [
    'Nyeri / Perih pada lambung',
    'Perut kembung',
    'Nafsu makan berkurang',
    'Mual',
    'Sembelit',
    'Diare',
    'Berat badan menurun',
    'BAB warna hitam',
    'Demam',
    'Rasa makanan kembali',
    'BAB cair',
    'Kejang perut',
    'Nyeri pada uluh hati',
    'Perasaan kenyang berlebihan',
    'Nyeri pada tukak lambung'
]

bobot_gejala = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Input from the user with error handling
gejala_terpilih = [0] * 15

# Deteksi penyakit with weighted matching
hasil_deteksi = deteksi_penyakit_lambung(gejala_terpilih, gejala_weights)

# ...

# Sort hasil_deteksi based on weighted_matching_percentage in descending order
hasil_deteksi = sorted(hasil_deteksi, key=lambda x: x['weighted_matching_percentage'], reverse=True)
# Note that the block of code that used to be here for user input has been removed.

if hasil_deteksi:
    penyakit_tertinggi = hasil_deteksi[0]  # Ambil penyakit dengan persentase tertinggi
    penyakit = penyakit_tertinggi['penyakit']
    matching_percentage = penyakit_tertinggi['weighted_matching_percentage']

    # Print summary
    print(f'Pengguna mungkin menderita: {penyakit} ({matching_percentage * 100:.2f}%)')

    # Print details for the penyakit tertinggi
    info_solusi_obat = solusi_dan_obat(penyakit)
    print(f'Detail {penyakit}: {info_solusi_obat["solusi"]}')
    print(f'Obat yang dapat digunakan: {info_solusi_obat["obat"]}')
else:
    print('Tidak ada penyakit yang terdeteksi berdasarkan gejala yang diinputkan.')