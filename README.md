# Dynamic Job Scheduling with Machine Transition Costs

Bu proje, sıralı bir üretim hattında birden fazla makinede işler gerçekleştirilirken ortaya çıkan toplam süreyi minimize etmeyi amaçlayan bir dinamik programlama uygulamasıdır. Her işin farklı makinelerde farklı tamamlanma süreleri vardır ve makineler arasında geçiş yapıldığında ek geçiş maliyetleri (örneğin taşıma süresi veya makine ayarlama süresi) oluşur.

## Problem Tanımı

- Toplam `n` iş, sırayla yapılmalıdır.
- Her iş, `m` farklı makineden birinde tamamlanabilir.
- Her işin her makinedeki işlenme süresi farklıdır.
- Makineler arasında geçiş yapılırsa geçiş maliyeti uygulanır.
- Amaç, işleri sırayla minimum toplam süreyle tamamlamaktır.

## Matris Zinciri Çarpımı ile İlişkisi

Bu problem, klasik **Matris Zinciri Çarpımı (Matrix Chain Multiplication)** problemiyle benzerlik taşır. Matris zinciri çarpımında olduğu gibi bu problemde de karar noktası, bir dizilimde işlemleri hangi sırayla ve hangi parantezleme (ya da makine) tercihiyle yapacağımızdır.

- Matris zinciri çarpımında amaç, çarpım sırasını en verimli şekilde belirlemekken;
- Bu projede amaç, işleri hangi makinelerde yapacağımızı ve makine geçişlerini en verimli şekilde seçmektir.

Bu benzerlik, problemi **dinamik programlama** yaklaşımıyla çözmek için temel oluşturur.

## Tablolama ve Hafızalama Algoritması

Bu problemde dinamik programlama tablosu `dp[i][j]` olarak tanımlanır:

- `i`: Kaçıncı işin yapıldığı (0'dan `n-1`'e kadar),
- `j`: O işin hangi makinede yapıldığı (0'dan `m-1`'e kadar),
- `dp[i][j]`: `i` numaralı işin `j` numaralı makinede yapılması durumunda, o ana kadar olan minimum toplam süreyi temsil eder.

Tablonun ilk satırı doğrudan iş sürelerinden oluşur. Sonraki her satır, önceki işin hangi makinede yapıldığına göre tüm olasılıkları dener. Her durumda geçiş maliyeti ve iş süresi toplamı hesaplanır, en küçük değer seçilir.

## Kod Açıklaması

Kodda sırasıyla şunlar yapılır:

1. Gerekli kütüphaneler (`sys`) içe aktarılır.
2. İş süreleri (`processing`) ve makine geçiş maliyetleri (`transition`) tanımlanır.
3. `dp` tablosu oluşturulur ve ilk iş için başlangıç değerleri atanır.
4. Her iş için, her makinede yapılma senaryosu değerlendirilir.
5. Önceki işin hangi makinede yapıldığına göre geçiş maliyeti + iş süresi toplanır.
6. Minimum değer bulunur ve `dp` tablosuna yazılır.
7. Son satırdaki en küçük değer, toplam minimum süredir.

## Zaman ve Uzay Karmaşıklığı

- **Zaman karmaşıklığı:** O(n × m²)
  - Her iş için (`n`), her makine (`m`) için, önceki tüm makineler (`m`) üzerinden geçilir.
- **Uzay karmaşıklığı:** O(n × m)
  - Dinamik programlama tablosu (`dp`) bu boyuttadır.

## Sonuç

Bu proje, dinamik programlama ile makineler arası geçiş maliyetlerini de dikkate alarak üretim hattındaki işleri optimal şekilde zamanlamayı hedeflemektedir. Problem, klasik matris zinciri çarpımı problemleriyle yapısal benzerlik gösterdiğinden dinamik programlama ile etkili bir şekilde çözülmüştür. Kod, açık ve öğrenmeye yönelik olarak yapılandırılmıştır.
