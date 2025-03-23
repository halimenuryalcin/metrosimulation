
# Metro Rota Planlama ve Simülasyon Sistemi

Bu proje, bir metro ağı üzerinde en az aktarmalı ve en hızlı rotaları bulmak ve metro sistemini simüle etmek için geliştirilmiş bir Python uygulamasıdır. Proje, **BFS (Breadth-First Search)** ve **A\* Algoritması** kullanarak rotaları hesaplar ve kullanıcı dostu bir chatbot arayüzü sunar.

---

## 📋 İçindekiler

- [Proje Amacı](#-proje-amacı)
- [Kullanılan Teknolojiler](#-kullanılan-teknolojiler)
- [Dosyalar](#-dosyalar)
- [Kurulum](#-kurulum)
- [Nasıl Çalıştırılır?](#-nasıl-çalıştırılır)
- [Test Senaryoları](#-test-senaryoları)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 🎯 Proje Amacı


Bu proje, bir metro ağı üzerinde iki istasyon arasındaki en az aktarmalı ve en hızlı rotaları bulmayı amaçlar.Kullanıcılar, başlangıç ve hedef istasyonları belirleyerek en uygun rotayı ve bu rotanın toplam süresini öğrenebilir.Bu kısım için ilgili kod dosyası HalimeNurYALÇIN_Metro_Simulation.py'dır.
Ayrıca, metro sistemini simüle ederek rastgele gecikmeler ekler ve kullanıcıya interaktif bir chatbot arayüzü sunar.Bu kısımda yapılan eklenti ve gelişmeler ise metro_simulation.py içerisinde yer almaktadır.

---

## 🛠 Kullanılan Teknolojiler

- **Python 3.x**: Projenin temel programlama dili.
- **Veri Yapıları**:
  - `defaultdict`: Hatlar ve istasyonlar için kullanıldı.
  - `deque`: BFS algoritmasında kuyruk yapısı olarak kullanıldı.
  - `heapq`: A\* algoritmasında öncelik kuyruğu olarak kullanıldı.
- **Algoritmalar**:
  - **BFS (Breadth-First Search)**: En az aktarmalı rota bulmak için kullanıldı.
  - **A\* Algoritması**: En hızlı rota bulmak için kullanıldı.
- **Görselleştirme**:
  - `networkx`: Metro ağını görselleştirmek için kullanıldı.
  - `matplotlib`: Grafikleri çizmek için kullanıldı.

---

## 📂 Dosyalar

Proje iki ana Python dosyasından oluşmaktadır:

1. **`HalimeNurYALÇIN_Metro_Simulation.py`**:
   - Metro ağını oluşturan ve yöneten sınıfları (`MetroAgi`, `Istasyon`) içerir.
   - En az aktarmalı ve en hızlı rotaları hesaplayan fonksiyonları içerir.

2. **`metro_simulation.py`**:
   - Metro ağını simüle eden ve kullanıcıyla etkileşime geçen chatbot'u içerir.
   - Rastgele gecikmeler ekler ve rotaları görselleştirir.
not:metro_simulation dosyasında gecikme olma durumunu da gözetlemek istediğim için aynı algoritma ve fonksiyonlarla hızlı ve az aktarma yöntemlerini yapsalar da sürelerde farklılık olacaktır.
---

## 🚀 Kurulum

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. **Python'u Yükleyin**:
   - Proje Python 3.x ile uyumludur. Eğer Python yüklü değilse, [Python'un resmi sitesinden](https://www.python.org/downloads/) indirip yükleyin.

2. **Projeyi İndirin**:
   - Proje dosyalarını bilgisayarınıza indirin veya `git clone` komutuyla klonlayın:
     ```bash
     git clone https://github.com/halimenuryalcin/metrosimulation.git
     ```

3. ## 🛠 Gerekli Kütüphaneler

Projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

1. **`networkx`**:
   - Metro ağını modellemek ve görselleştirmek için kullanılır.
   - Kurulum:
     
     pip install networkx
     

2. **`matplotlib`**:
   - Metro rotalarını grafik olarak çizmek için kullanılır.
   - Kurulum:
     
     pip install matplotlib
     

3. **`typing`**:
   - Python'un standart kütüphanesidir. Ek kurulum gerektirmez.

4. **`random`**:
   - Rastgele gecikmeler eklemek için kullanılır. Python'un standart kütüphanesidir.

5. **`warnings`**:
   - Uyarıları filtrelemek için kullanılır. Python'un standart kütüphanesidir.

---

## 🖥 Nasıl Çalıştırılır?

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

### 1. **Terminali Açın**
- Proje dizinine gidin:
  
  cd /path/to/metro-rota-planlama
  

### 2. **Gerekli Kütüphaneleri Yükleyin**
- Projede kullanılan kütüphaneleri yükleyin:
 
  pip install networkx matplotlib
  

### 3. **Python Dosyasını Çalıştırın**
- `metro_rota.py` dosyasını çalıştırın:
  ```bash
  python metro_rota.py
  ```

### 4. **Chatbot'u Kullanın**
- Terminalde chatbot ile etkileşime geçin. Örnek bir etkileşim şu şekilde olacaktır:
  

## 🧪 Test Senaryoları

Projede aşağıdaki test senaryoları tanımlanmıştır:

1. **AŞTİ'den OSB'ye**:
   - En az aktarmalı rota ve en hızlı rota hesaplanır.

2. **Batıkent'ten Keçiören'e**:
   - En az aktarmalı rota ve en hızlı rota hesaplanır.

3. **Keçiören'den AŞTİ'ye**:
   - En az aktarmalı rota ve en hızlı rota hesaplanır.
---

## 📞 İletişim

Proje ile ilgili sorularınız veya önerileriniz için bana ulaşabilirsiniz:

- **E-posta**: halimenuryalcinn@gmail.com
- **GitHub**: [kullanici_adiniz](https://github.com/halimenuryalcin)


