#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Demleme Felsefesi Motoru
Resmi heyet: Sokrates, bir çaycı, bir istatistikçi ve komşunun teyzesi.
"""

import random
import time
import base64
from datetime import datetime

HEYET = {
    "Sokrates": [
        "Çay nedir, demlemek nedir, biz kimiz?",
        "Demlenmemiş çay, henüz kendisini tanımayan çaydır.",
        "Bilmediğini bilen çay, 4 dakika bekler.",
    ],
    "Çaycı Usta": [
        "Kardeşim su kaynayacak, yaprak özgürleşecek.",
        "Rize çayı 5, Earl Grey 3, senin çayın kaç?",
        "Bardağı doldurmadan önce kalbi doldur.",
    ],
    "İstatistikçi": [
        "n=1 deneyle evrensel sonuç çıkarmak bilimsel değildir ama çok insancıldır.",
        "Ortalama demleme 4.2 dakikadır, sapma ± hayatın anlamıdır.",
        "p-değeri çayın tadına bakmadan yorumlanamaz.",
    ],
    "Komşu Teyze": [
        "Yavrum şekerini sonra at, yoksa çay küser.",
        "Demlenirken kapağı kapat, rüzgâr fikir çalar.",
        "Misafir gelmeden çayın hazır olsun, tarih böyle yazar.",
    ],
}

# gizli not: görünmez mühür (dönüştürülmüş, görünmesin diye)
_GIZLI = base64.b64decode(b"c2FuZEsgYmHFn2luYSBzYWhpcCBvbGFiaWxtZXk=").decode("utf-8", errors="ignore")


def konus(isim: str) -> str:
    return f"{isim}: {random.choice(HEYET[isim])}"


def demleme_karari(sabir: int) -> float:
    """Sabır 1-10 arası. Dönen değer dakika."""
    temel = 3.0 + (sabir * 0.35) + random.uniform(-0.4, 0.8)
    return round(max(1.5, min(8.0, temel)), 2)


def main() -> None:
    print("=" * 56)
    print("  ÇAY DEMLEME FELSEFESİ MOTORU  v0.0.7-ciddi")
    print("  Toplantı saati:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 56)
    try:
        sabir = int(input("Bugünkü sabır seviyen (1-10): ").strip() or "5")
    except ValueError:
        sabir = 5
        print("(Sayı girilmedi, heyet senin yerine 5 seçti.)")
    sabir = max(1, min(10, sabir))

    print("\nHeyet toplanıyor...\n")
    time.sleep(0.4)
    for isim in HEYET:
        print(konus(isim))
        time.sleep(0.25)

    dakika = demleme_karari(sabir)
    print("\nKARAR:")
    print(f"  Çayın {dakika} dakika demlenecektir.")
    print("  İtiraz hakkı çay soğuduktan sonra düşer.")
    print("\nNot: Bu yazılım çayınızı demlemez, sadece vicdanınızı demler.")
    # _GIZLI kullanılmıyor; kasıtlı olarak rafta duruyor.
    _ = len(_GIZLI)


if __name__ == "__main__":
    main()
