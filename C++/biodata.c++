#include <iostream>
#include <string>

using namespace std;

int main() {
    string nama, kota;
    int umur;

    cout << "Nama : ";
    getline(cin, nama);

    cout << "Umur : ";
    cin >> umur;
    cin.ignore(); // Membuang karakter '\n' yang tersisa di buffer setelah input angka

    cout << "Kota : ";
    getline(cin, kota);

    // Menampilkan output data diri
    cout << nama << ", " << umur << " tahun, dari " << kota << '\n';
    cout << "Tahun depan umur " << umur + 1 << '\n';

    return 0; // Opsional, tetapi baik untuk menandakan program selesai dengan sukses