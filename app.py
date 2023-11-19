from flask import Flask, render_template, request, redirect, url_for, session
from lambo2 import deteksi_penyakit_lambung, gejala_nama, gejala_weights, solusi_dan_obat

app = Flask(__name__)
app.secret_key = '123'  # Replace with your own secret key

# Add this line to pass the solusi_obat function to the template context
app.jinja_env.globals.update(solusi_obat=solusi_dan_obat)

@app.route('/', methods=['GET', 'POST'])
def halaman_awal():
    if request.method == 'POST':
        # Ambil nama dari form yang dikirim oleh pengguna
        nama_pengguna = request.form['nama']
        # Store it in the session
        session['nama_pengguna'] = nama_pengguna
        # Redirect pengguna ke halaman form
        return redirect(url_for('form'))
    return render_template('landing.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    # Retrieve the user's name from the session
    nama_pengguna = session.get('nama_pengguna', '')
    if request.method == 'POST':
        gejala_terpilih = [int(request.form.get(f'gejala_{i}', '0')) for i in range(15)]
        if len(gejala_terpilih) == len(gejala_weights):
            hasil_deteksi = deteksi_penyakit_lambung(gejala_terpilih, gejala_weights)
            # Now sort the results
            hasil_deteksi = sorted(hasil_deteksi, key=lambda x: x['weighted_matching_percentage'], reverse=True)
            penyakit_tertinggi = hasil_deteksi[0] if hasil_deteksi else None  # Take the top result if available
            return render_template('form.html', penyakit_tertinggi=penyakit_tertinggi, gejala_nama=gejala_nama, nama_pengguna=nama_pengguna)
        else:
            return "Error: Length of gejala_terpilih does not match gejala_weights."
        output_generated = True
    
    return render_template('form.html', penyakit_tertinggi=None, gejala_nama=gejala_nama, nama_pengguna=nama_pengguna)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False for production
