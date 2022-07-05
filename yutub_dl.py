import pafy

print('#'*40)
print("Audio and Video downloader From Youtube")
print("created by : Ahmad Harun")
print('#'*40)
print()

print('Jenis File: ')
print('1. Video')
print('2. Audio')

pilih_jenis = int(input('pilih jenis file: '))

if pilih_jenis == 1:
	print('Video Download From youtube!')
	data = input("link youtube: ")
	url = pafy.new(data)

	print(f"Judul: {url.title}")
	print(f"Author: {url.author}")
	print(f"Durasi: {url.duration}")
	print(f"Views: {url.viewcount}")

		# hasil = url.getbest()
		# hasil.download()

	hasil = url.getbest()
	ukuran = hasil.get_filesize()
	ukuran_view = ukuran / 1000000
	print('Ukuran File: %.1f' % ukuran_view, ' Mb')

	pilih = input("apakah ingin download video ini [y/n] ?")

	if pilih == 'y' or pilih == 'Y':
		hasil.download()
	else:
		print('Ok, thank you')

elif pilih_jenis == 2:
	print('Audio Download From Youtube')

	def mycb(total, recvd, ratio, rate, eta):
		print(recvd, ratio, eta)

	data = input('link youtube: ')
	url = pafy.new(data)

	print(f"Judul: {url.title}")
	print(f"Author: {url.author}")
	print(f"Durasi: {url.duration}")
	print(f"Views: {url.viewcount}")

	hasil = url.getbestaudio()
	ukuran = hasil.get_filesize()
	ukuran_view = ukuran / 1000000
	print('Ukuran File: %.1f' % ukuran_view, ' Mb')

	pilih = input("apakah ingin download Audio ini [y/n] ?")

	if pilih == 'y' or pilih == 'Y':
		hasil.download()
	else:
		print('Ok, thank you')

print('#'*40)
print("Audio and Video downloader From Youtube")
print("created by : Ahmad Harun")
print('#'*40)

