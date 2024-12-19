import os

def rename_files_in_folder(folder_path, new_name_pattern, start_index=1):
    """
    Mengubah nama seluruh file dalam folder menjadi format image_0001_high.jpg, image_0002_high.jpg, dll.
    
    :param folder_path: Path ke folder yang berisi file yang ingin diubah namanya.
    :param new_name_pattern: Pola nama baru yang akan digunakan untuk merename file.
    :param start_index: Indeks awal untuk penomoran file (default 1).
    """
    # Memeriksa apakah folder ada
    if not os.path.exists(folder_path):
        print(f"Folder tidak ditemukan: {folder_path}")
        return

    # Mengambil semua file di dalam folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Melakukan rename untuk setiap file dalam folder
    for idx, old_filename in enumerate(files):
        # Membuat nama baru sesuai pola dengan menyertakan nomor urut yang dipadding dengan zeros
        file_extension = os.path.splitext(old_filename)[1]  # Mendapatkan ekstensi file
        new_filename = f"{new_name_pattern}_low_{str(start_index + idx).zfill(4)}{file_extension}"
        
        # Membuat path lengkap untuk file lama dan baru
        old_file_path = os.path.join(folder_path, old_filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Mengganti nama file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_filename} -> {new_filename}")

if __name__ == "__main__":
    # Tentukan folder yang berisi file yang ingin diganti namanya
    folder_path = "C:/Users/fillo/PycharmProjects/uasnih/data/low_res"  # Ganti dengan path ke folder Anda
    
    # Tentukan pola nama baru, misalnya "image"
    new_name_pattern = "image"  # Anda bisa mengganti ini sesuai keinginan
    
    # Menjalankan fungsi untuk merename file
    rename_files_in_folder(folder_path, new_name_pattern, start_index=1)
