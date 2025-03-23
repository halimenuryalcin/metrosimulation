import random
from typing import List, Optional
import matplotlib.pyplot as plt
import networkx as nx
from HalimeNurYALÇIN_Metro_Simulation import MetroAgi, Istasyon
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

def gecikme_ekle(metro_ag: MetroAgi):
    """Bazı hatlara rastgele gecikmeler ekler."""
    for istasyon in metro_ag.istasyonlar.values():
        for i, (komsu, sure) in enumerate(istasyon.komsular):
            if random.random() < 0.2:  # %20 ihtimalle gecikme ekle
                yeni_sure = sure + random.randint(2, 10)
                istasyon.komsular[i] = (komsu, yeni_sure)
    print("📢 Rastgele gecikmeler eklendi!")


def rota_ciz(rota: List['Istasyon']):

    # Hat renklerini tanımla
    hat_renkleri = {
        'Kırmızı Hat': '#f73d3d',
        'Mavi Hat': '#87e5fe',
        'Turuncu Hat': '#faa223',
    }

    # Grafik için bir yönlü grafik oluştur
    G = nx.DiGraph()

    # İstasyonları ekle
    for istasyon in rota:
        G.add_node(istasyon.ad, hat=istasyon.hat)

    for i in range(len(rota) - 1):
        istasyon1 = rota[i]
        istasyon2 = rota[i + 1]
        #print(f"{istasyon1.ad} -> {istasyon2.ad}: Komsular = {istasyon1.komsular}")
        sure = next((sure for komsu, sure in istasyon1.komsular if komsu == istasyon2), None)
        if sure is None:
            print(f"Hata: {istasyon1.ad} ile {istasyon2.ad} arasında bağlantı bulunamadı.")
        else:
            print(f"Sure: {sure}")
            G.add_edge(istasyon1.ad, istasyon2.ad, sure=sure)
    # Grafik düzeni
    pos = nx.spring_layout(G)  # İstasyonlar arasındaki mesafeyi düzenler
    plt.figure(figsize=(10, 8))

    # İstasyonların renklerini hatlara göre belirle
    node_colors = [hat_renkleri[G.nodes[istasyon]['hat']] for istasyon in G.nodes]

    # İstasyonları ve bağlantıları çiz
    nx.draw(G, pos, with_labels=True, node_size=4000, node_color=node_colors, font_size=12, font_weight='normal', edge_color='gray')
    # Bağlantıların üzerindeki süreleri ekle
    sure_bilgileri = nx.get_edge_attributes(G, 'sure')
    edge_labels = {k: f"{v} dakika" for k, v in sure_bilgileri.items()}

    # Aktarma istasyonlarını belirlemek (aynı isme sahip istasyonların bağlantılarında "Aktarma" yazsın)
    baglantilar = list(G.edges())
    for baglanti in baglantilar:
        kaynak, hedef = baglanti
        # Eğer kaynak ve hedef aynı isme sahipse, bu bir aktarma bağlantısıdır
        if kaynak == hedef:
            edge_labels[baglanti] += " (Aktarma)"
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    # Başlık ekle
    plt.title("Metro Rota Haritası", fontsize=15)
    plt.axis('off')  # Eksenleri gizle
    plt.show()




def istasyon_id_bul(istasyon_ad: str, metro: MetroAgi) -> Optional[str]:
    """İstasyon adı ile id'yi bulur (boşlukları temizler, büyük/küçük harf duyarsız)."""
    istasyon_ad = istasyon_ad.strip().lower()  # Küçük harfe çevir ve boşlukları temizle
    for istasyon in metro.istasyonlar.values():
        if istasyon.ad.strip().lower() == istasyon_ad:
            return istasyon.idx
    return None



def chatbot(metro: MetroAgi):
    """Kullanıcıyla terminal üzerinden etkileşime giren chatbot."""
    gecikme_ekle(metro)

    def istasyon_gecerli_mi(istasyon_adi):
        """Girilen istasyonun geçerli olup olmadığını kontrol eder."""
        # Girdiyi temizle: baştaki ve sondaki boşlukları kaldır, küçük harfe çevir
        istasyon_adi = istasyon_adi.strip().lower()

        # Türkçe karakterleri dikkate alarak eşleştirme yap
        for istasyon in metro.istasyonlar.values():
            if istasyon.ad.lower() == istasyon_adi:
                return True
        return False

    # Kullanıcıdan başlangıç istasyonunu al
    while True:
        print("\n👋 Merhaba! Gideceğiniz istasyonu söyleyin:")
        hedef = input("> ").strip().title()
        if istasyon_gecerli_mi(hedef):
            break
        else:
            print("❌ Geçersiz istasyon! Lütfen geçerli bir istasyon adı girin.")

    # Kullanıcıdan başlangıç noktasını al
    while True:
        print("Nereden kalkıyorsunuz?")
        baslangic = input("> ").strip().title()
        if istasyon_gecerli_mi(baslangic):
            break
        else:
            print("❌ Geçersiz istasyon! Lütfen geçerli bir istasyon adı girin.")

    # Kullanıcıdan rota tercihini al
    print("\n🎯 Rota tercihinizi seçin: (hızlı / az aktarma / yürüyüş)")
    print("Seçenekler hakkında daha fazla bilgi almak için 'yardım' yazabilirsiniz.")
    mod = input("> ").strip().lower()

    if mod == "yardım":
        print("\n**Rota Tercihleri:**")
        print("1. **Hızlı**: En hızlı güzergahı seçer.")
        print("2. **Az Aktarma**: Aktarmalı hatlar arasında en az aktarma ile geçiş sağlar.")
        return

    # İstasyon ID'lerini bulma
    baslangic_id = istasyon_id_bul(baslangic, metro)
    hedef_id = istasyon_id_bul(hedef, metro)

    if not baslangic_id or not hedef_id:
        print("❌ İstasyonları bulamadım. Lütfen geçerli bir istasyon adı girin.")
        return

    # Rota seçimini yapma
    if mod == "hızlı":
        rota = metro.en_hizli_rota_bul(baslangic_id, hedef_id)
    elif mod == "az aktarma":
        rota = metro.en_az_aktarma_bul(baslangic_id, hedef_id)
    else:
        print("❌ Geçersiz seçim! Lütfen 'hızlı', 'az aktarma' veya 'yürüyüş' seçeneklerinden birini seçin.")
        return

    if rota:
        istasyonlar, sure = rota if isinstance(rota, tuple) else (rota, None)
        print(f"\n🚆 **Önerilen rota** ({sure} dk): " + " -> ".join(i.ad for i in istasyonlar))
        rota_ciz(istasyonlar)
    else:
        print("❌ Üzgünüm, uygun rota bulunamadı.")


if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    chatbot(metro)
