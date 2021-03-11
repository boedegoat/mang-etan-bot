import random

last_quote = []
def getQuote() :
  global last_quote

  quotes = quotes_list()
  while True :
    quote = random.choice(quotes)
    last_quote.append(quote)

    if not any(last_quote.count(el) > 1 for el in last_quote) :
      if len(last_quote) >= 2 :
        last_quote.clear()
      return quote

    else :
      del last_quote[1]

def quotes_list() :
  quotes = (
  "Cantik nggak harus putih, tapi mesti perempuan.",
  "Mencintaimu itu wajar. Yang nggak wajar itu mencintai bapakmu.",
  "Rumah tangga itu rumit. Kalau sederhana itu namanya rumah makan.",
  "Secapek-capeknya kerja, lebih capek nganggur.",
  "Seberat apa pun masalahmu, jangan lupa mengeluh.",
  "Jangan membenci dirimu sendiri, karena itu tugas orang lain.",
  "Manusia menciptakan ponsel. Ponsel makin pintar. manusia tidak.",
  "Seberat apapun pekerjaan, apabila tidak dikerjakan maka akan terasa ringan.",
  "Belajarlah dari tuyul, masih kecil tapi sudah pintar cari duit.",
  "Kerja keraslah sampai tetangga berpikir rezekimu hasil dari pesugihan.",
  "Hidup itu sederhana. Goreng, angkat, lalu tiriskan.",
  "Jika Anda sudah membuat kopi, tapi masih saja mengantuk, berarti kopinya belum diminum.",
  "Jika ada orang yang menyebutmu jelek, janganlah berputus asa, belum tentu orang tersebut berkata bohong.",
  "Waktu tak dapat diputar, dijilat, apalagi dicelupin.",
  "Hidup tanpa tujuan itu ibarat orang kebelet boker tapi gak nemuin toilet",
  "Jika kamu tak mampu meyakinkan dan memukau orang dengan kepintaranmu, bingungkan dia dengan kebodohanmu",
  "Buat apa mencintai tanpa dicintai, mending cintai ususmu minum yakult tiap hari",
  "Hidup itu ibarat sungai yang mengalir, ada aja tai yang lewat.",
  )

  return quotes
