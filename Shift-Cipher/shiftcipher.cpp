#include <iostream>
#include <string>

using namespace std;

// Fungsi untuk mengenkripsi teks menggunakan shift cipher
string shiftCipherEncrypt(string text, int shift) {
    string encryptedText = "";
    
    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        // Memproses huruf besar
        if (isupper(ch)) {
            encryptedText += char(int(ch + shift - 65) % 26 + 65);
        }
        // Memproses huruf kecil
        else if (islower(ch)) {
            encryptedText += char(int(ch + shift - 97) % 26 + 97);
        }
        // Untuk karakter selain huruf, tidak dienkripsi
        else {
            encryptedText += ch;
        }
    }
    
    return encryptedText;
}

int main() {
    string text;
    int shift;

    // Input teks plain dan nilai shift
    cout << "Masukkan teks yang akan dienkripsi: ";
    getline(cin, text);
    cout << "Masukkan nilai shift: ";
    cin >> shift;

    // Menampilkan hasil enkripsi
    string encryptedText = shiftCipherEncrypt(text, shift);
    cout << "Hasil enkripsi: " << encryptedText << endl;

    return 0;
}
