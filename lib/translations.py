# vim: fileencoding=utf-8

"""
Translation of almost everything.
"""

FULL_TRANSLATION = [
    "af", "be", "ca", "da", "de", "el", "et",
    "fr", "fa", "hu", "id", "it",
    "nb", "nl", "pl", "pt-br", "ro",
    "ru", "tr", "th", "uk", "vi", "zh-tw"
]

PARTIAL_TRANSLATION = [
    "az", "bg", "bs", "cy", "cs",
    "eo", "es", "fi", "ga", "hi", "hr",
    "hy", "is", "ja", "jv", "ka", "kk",
    "ko", "ky", "lt", "lv", "mk", "ml", "nl", "fy",
    "nn", "pt", "pt-br", "sk", "sl", "sr", "sr-lat",
    "sv", "sw",  "te", "uz",
    "zh", "zu", "he",
]

PROXY_LANGS = [
    "af", "az", "be", "bs", "ca",
    "cy", "el", "eo", "et", "fa",
    "fy", "he", "hr", "hu", "hy",
    "id", "is", "it", "ja", "kk",
    "lv", "mk", "nb", "nn", "ro",
    "ru", "sl", "th", "pt-br", "uk", "uz",
    "vi", "zh-tw",
]

SUPPORTED_LANGS = FULL_TRANSLATION + PARTIAL_TRANSLATION

MESSAGE = {
    'NOT_FOUND_MESSAGE': {
        'en': u"""
We were unable to find your location
so we have brought you to Oymyakon,
one of the coldest permanently inhabited locales on the planet.
""",
        'af': u"""
Ons kon nie u ligging opspoor nie
gevolglik het ons vir u na Oymyakon geneem,
een van die koudste permanent bewoonde plekke op aarde.
""",
        'be': u"""
Ваша месцазнаходжанне вызначыць не атрымалася,
таму мы пакажам вам надвор'е ў Аймяконе,
самым халодным населеным пункце на планеце.
Будзем спадзявацца, што ў вас сёння надвор'е лепей!
""",
        'bg':u"""
Не успяхме да открием вашето местоположение
така че ви доведохме в Оймякон,
едно от най-студените постоянно обитавани места на планетата.
""",
        'bs': u"""
Nismo mogli pronaći vašu lokaciju,
tako da smo te doveli do Oymyakon,
jedan od najhladnijih stalno naseljena mjesta na planeti.
Nadamo se da ćete imati bolje vreme!
""",
        'ca': u"""
Hem estat incapaços de trobar la seva ubicació,
per això l'hem portat fins Oymyakon,
un dels llocs més freds i permanentment deshabitats del planeta.
""",
        'cs': u"""
Nepodařilo se nám najít vaši polohu,
takže jsme vás přivedl do Ojmjakonu.
Je to jedno z nejchladnějších trvale obydlených míst na planetě.
Doufáme, že budete mít lepší počasí!
""",
        'cy': u"""
Ni darganfyddwyd eich lleoliad,
felly rydym wedi dod â chi i Oymyakon,
un o'r llefydd oeraf ar y blaned ble mae pobl yn dal i fyw!
""",
        'de': u"""
Wir konnten Ihren Standort nicht finden,
also haben wir Sie nach Oimjakon gebracht,
einer der kältesten dauerhaft bewohnten Orte auf dem Planeten.
Wir hoffen, dass Sie besseres Wetter haben!
""",
        'el': u"""
Δεν μπορέσαμε να βρούμε την τοποθεσία σου,
για αυτό διαλέξαμε το Οϊμιάκον για εσένα,
μία από τις πιο κρύες μόνιμα κατοικημένες περιοχές στον πλανήτη.
Ελπίζουμε να έχεις καλύτερο καιρό!
""",
        'es': u"""
No hemos logrado encontrar tu ubicación,
asi que hemos decidido enseñarte el tiempo en Oymyakon,
uno de los sitios más fríos y permanentemente deshabitados del planeta.
""",
        'fa': u"""
ما نتونستیم مکان شما رو پیدا کنیم. به همین خاطر شما رو به اویمیاکن بردیم
، یکی از سردترین مکان های روی زمین که اصلا قابل سکونت نیست!
""",
        'fi': u"""
Emme löytänyt sijaintiasi, joten toimme sinut Oimjakoniin,
yhteen maailman kylmimmistä pysyvästi asutetuista paikoista.
Toivottavasti sinulla on parempi sää!
""",
        'fr': u"""
Nous n'avons pas pu déterminer votre position,
Nous vous avons donc amenés à Oïmiakon,
l'un des endroits les plus froids habités en permanence sur la planète.
Nous espérons qu'il fait meilleur chez vous !
""",
        'hu': u"""
Nem sikerült megtalálni a pozíciódat,
így elhoztunk Ojmjakonba;
az egyik leghidegebb állandóan lakott településre a bolygón.
""",
        'hy': u"""
Ձեր գտնվելու վայրը չհաջողվեց որոշել,
այդ պատճառով մենք ձեզ կցուցադրենք եղանակը Օյմյակոնում.
երկրագնդի ամենասառը բնակավայրում։
Հույս ունենք որ ձեր եղանակը այսօր ավելի լավն է։
""",
        'id': u"""
Kami tidak dapat menemukan lokasi anda,
jadi kami membawa anda ke Oymyakon,
salah satu tempat terdingin yang selalu dihuni di planet ini!
""",
        'is': u"""
Við finnum ekki staðsetninguna þína og vísum þér þar með á Ojmjakon,
ein af köldustu byggðum jarðar.
Vonandi er betra veður hjá þér.
""",
        'it': u"""
Non siamo riusciti a trovare la sua posizione
quindi la abbiamo portato a Oymyakon,
uno dei luoghi abitualmente abitati più freddi del pianeta.
Ci auguriamo che le condizioni dove lei si trova siano migliori!
""",
        'ja': u"""
指定された場所が見つかりませんでした。
代わりにオイミャコンの天気予報を表示しています。
オイミャコンは地球上で最も寒い居住地の一つです。
""",
        'ko': u"""
지정된 장소를 찾을 수 없습니다,
대신 오이먀콘의 일기 예보를 표시합니다,
오이먀콘은 지구상에서 가장 추운 곳에 위치한 마을입니다!
""",
        'lv': u"""
Mēs nevarējām atrast jūsu atrašanās vietu tādēļ nogādājām jūs Oimjakonā,
vienā no aukstākajām apdzīvotajām vietām uz planētas.
""",
        'mk': u"""
Неможевме да ја пронајдеме вашата локација,
затоа ве однесовме во Ојмајкон,
еден од најладните трајно населени места на планетата.
""",
        'nb': u"""
Vi kunne ikke finne din lokasjon,
så her får du Ojmjakon, et av de kaldeste bebodde stedene på planeten.
Vi håper været er bedre hos deg!
""",
        'nl': u"""
Wij konden uw locatie niet vaststellen
dus hebben we u naar Ojmjakon gebracht,
één van de koudste permanent bewoonde gebieden op deze planeet.
""",
        'fy': u"""
Wy koenen jo lokaasje net fêststelle
dus wy ha jo nei Ojmjakon brocht,
ien fan de kâldste permanent bewenbere plakken op ierde.
""",
        'pt': u"""
Não conseguimos encontrar a sua localização,
então decidimos te mostrar o tempo em Oymyakon,
um dos lugares mais frios e permanentemente desabitados do planeta.
""",
        'pt-br': u"""
Não conseguimos encontrar a sua localização,
então decidimos te mostrar o tempo em Oymyakon,
um dos lugares mais frios e permanentemente desabitados do planeta.
""",
        'pl': u"""
Nie udało nam się znaleźć podanej przez Ciebie lokalizacji,
więc zabraliśmy Cię do Ojmiakonu,
jednego z najzimniejszych, stale zamieszkanych miejsc na Ziemi.
Mamy nadzieję, że u Ciebie jest cieplej!
""",
        'ro': u"""
Nu v-am putut identifica localitatea, prin urmare vă arătăm vremea din Oimiakon,
una dintre cele mai reci localități permanent locuite de pe planetă.
Sperăm că aveți vreme mai bună!
""",
        'ru': u"""
Ваше местоположение определить не удалось,
поэтому мы покажем вам погоду в Оймяконе,
самом холодном населённом пункте на планете.
Будем надеяться, что у вас сегодня погода лучше!
""",
        'sk': u"""
Nepodarilo sa nám nájsť vašu polohu,
takže sme vás priviedli do Ojmiakonu.
Je to jedno z najchladnejších trvale obývaných miest na planéte.
Dúfame, že budete mať lepšie počasie!
""",
        'sr': u"""
Нисмо успели да пронађемо Вашу локацију,
па смо Вас довели у Ојмјакон,
једно од најхладнијих стално насељених места на планети.
Надамо се да је време код Вас боље него што је то случај овде!
""",
        'sv': u"""
Vi lyckades inte hitta er plats så vi har istället tagit er till Ojmjakon,
en av planetens kallaste platser med permanent bosättning.
Vi hoppas att vädret är bättre hos dig!
""",
        'tr': u"""
Aradığınız konum bulunamadı. O yüzden sizi dünyadaki en soğuk sürekli
yerleşim yerlerinden biri olan Oymyakon'e getirdik.
Umarız sizin olduğunuz yerde havalar daha iyidir!
""",
        'te': u"""
మేము మీ స్థానాన్ని కనుగొనలేకపోయాము
కనుక మనం "ఓమాయకాన్కు" తీసుకొని వచ్చాము,
భూమిపై అత్యల్ప శాశ్వతంగా నివసించే స్థానిక ప్రదేశాలలో ఒకటి.
""",
        'th': u"""
เราไม่สามารถหาตำแหน่งของคุณได้เราจึงนำคุณไปสู่ Oymyakon หมู่บ้านที่หนาวที่สุดในโลก!
""",
        'uk': u"""
Ми не змогли визначити Ваше місцезнаходження,
тому покажемо Вам погоду в Оймяконі —
найхолоднішому населеному пункті на планеті.
Будемо сподіватися, що у Вас сьогодні погода краще!
""",
        'uz': u"""
Sizning joylashuvingizni aniqlay olmadik,
shuning uchun sizga sayyoramizning eng sovuq aholi punkti - Oymyakondagi ob-havo haqida ma'lumot beramiz.
Umid qilamizki, sizda bugungi ob-havo bundan yaxshiroq!
""",
        'zh': u"""
我们无法找到您的位置, 
当前显示奥伊米亚康(Oymyakon)，这个星球上最冷的人类定居点。
""",
        'da': u"""
Vi kunne desværre ikke finde din lokation
så vi har bragt dig til Oymyakon,
En af koldeste og helt ubolige lokationer på planeten.
""",
        'et': u"""
Me ei suutnud tuvastada teie asukohta
ning seetõttu paigutasime teid Oymyakoni,
mis on üks kõige külmemaid püsivalt asustatud paiku planeedil.
""",
        'vi': u"""
Chúng tôi không tìm thấy địa điểm của bạn
vì vậy chúng tôi đưa bạn đến Oymyakon,
một trong những nơi lạnh nhất có người sinh sống trên trái đất.
""",
        'zh-tw': u"""
我們找不到您的位置
所以我們帶您到奧伊米亞康，
這個星球上有人類定居最冷之處。
""",
    },

    'UNKNOWN_LOCATION': {
        'en': u'Unknown location',
        'af': u'Onbekende ligging',
        'be': u'Невядомае месцазнаходжанне',
        'bg': u'Неизвестно местоположение',
        'bs': u'Nepoznatoja lokacija',
        'ca': u'Ubicació desconeguda',
        'cs': u'Neznámá poloha',
        'cy': u'Lleoliad anhysbys',
        'de': u'Unbekannter Ort',
        'da': u'Ukendt lokation',
        'el': u'Άνγωστη τοποθεσία',
        'es': u'Ubicación desconocida',
        'et': u'Tundmatu asukoht',
        'fa': u'مکان نامعلوم',
        'fi': u'Tuntematon sijainti',
        'fr': u'Emplacement inconnu',
        'hu': u'Ismeretlen lokáció',
        'hy': u'Անհայտ գտնվելու վայր',
        'id': u'Lokasi tidak diketahui',
        'is': u'Óþekkt staðsetning',
        'it': u'Località sconosciuta',
        'ja': u'未知の場所です',
        'ko': u'알 수 없는 장소',
        'kk': u'',
        'lv': u'Nezināma atrašanās vieta',
        'mk': u'Непозната локација',
        'nb': u'Ukjent sted',
        'nl': u'Onbekende locatie',
        'fy': u'Ûnbekende lokaasje',
        'pl': u'Nieznana lokalizacja',
        'pt': u'Localização desconhecida',
        'pt-br': u'Localização desconhecida',
        'ro': u'Localitate necunoscută',
        'ru': u'Неизвестное местоположение',
        'sk': u'Neznáma poloha',
        'sl': u'Neznano lokacijo',
        'sr': u'Непозната локација',
        'sv': u'Okänd plats',
        'te': u'తెలియని ప్రదేశం',
        'tr': u'Bilinmeyen konum',
        'th': u'ไม่สามารถระบุตำแหน่งได้',
        'uk': u'Невідоме місце',
        'uz': u'Аникланмаган худуд',
        'zh': u'未知地点',
        'vi': u'Địa điểm không xác định',
        'zh-tw': u'未知位置',
    },

    'LOCATION': {
        'en': u'Location',
        'af': u'Ligging',
        'be': u'Месцазнаходжанне',
        'bg': u'Местоположение',
        'bs': u'Lokacija',
        'ca': u'Ubicació',
        'cs': u'Poloha',
        'cy': u'Lleoliad',
        'de': u'Ort',
        'da': u'Lokation',
        'el': u'Τοποθεσία',
        'es': u'Ubicación',
        'et': u'Asukoht',
        'fa': u'مکان',
        'fi': u'Tuntematon sijainti',
        'fr': u'Emplacement',
        'hu': u'Lokáció',
        'hy': u'Դիրք',
        'id': u'Lokasi',
        'is': u'Staðsetning',
        'it': u'Località',
        'ja': u'位置情報',
        'ko': u'위치',
        'kk': u'',
        'lv': u'Atrašanās vieta',
        'mk': u'Локација',
        'nb': u'Sted',
        'nl': u'Locatie',
        'fy': u'Lokaasje',
        'pl': u'Lokalizacja',
        'pt': u'Localização',
        'pt-br': u'Localização',
        'ro': u'Localitate',
        'ru': u'Местоположение',
        'sk': u'Poloha',
        'sl': u'Lokacijo',
        'sr': u'Локација',
        'sv': u'Plats',
        'zh': u'地点',
        'te': u'స్థానము',
        'tr': u'Konum',
        'th': u'ตำแหน่ง',
        'uk': u'Місцезнаходження',
        'vi': u'Địa điểm',
        'zh-tw': u'位置',
    },

    'CAPACITY_LIMIT_REACHED': {
        'en': u"""
Sorry, we are running out of queries to the weather service at the moment.
Here is the weather report for the default city (just to show you, how it looks like).
We will get new queries as soon as possible.
You can follow https://twitter.com/igor_chubin for the updates.
======================================================================================
""",
        'af': u"""
Verskoning, ons oorskry tans die vermoë om navrae aan die weerdiens te rig.
Hier is die weerberig van 'n voorbeeld ligging (bloot om aan u te wys hoe dit lyk).
Ons sal weereens nuwe navrae kan hanteer so gou as moontlik.
U kan vir https://twitter.com/igor_chubin volg vir opdaterings.
======================================================================================
""",
        'be': u"""
Прабачце, мы выйшлі за ліміты колькасці запытаў да службы надвор'я ў дадзены момант.
Вось прагноз надвор'я для горада па змаўчанні (толькі, каб паказаць вам, як гэта выглядае).
Мы вернемся як мага хутчэй.
Вы можаце сачыць на https://twitter.com/igor_chubin за абнаўленнямі.
======================================================================================
""",
        'bg': u"""
Съжаляваме, количеството заявки към услугата за предсказване на време е почти изчерпано.
Ето доклад за града по подразбиране (просто да видите как изглежда).
Ще осогурим допълнителни заявки максимално бързо.
Може да последвате https://twitter.com/igor_chubin за обновления.
""",
        'bs': u"""
Žao mi je, mi ponestaje upita i vremenska prognoza u ovom trenutku.
Ovdje je izvještaj o vremenu za default grada (samo da vam pokažem kako to izgleda).
Mi ćemo dobiti nove upite u najkraćem mogućem roku.
Možete pratiti https://twitter.com/igor_chubin za ažuriranja.
======================================================================================
""",
        'ca': u"""
Disculpa'ns, ens hem quedat momentàniament sense consultes al servei meteorològic.
Aquí t'oferim l'informe del temps a la ciutat per defecte (només per mostrar quin aspecte té).
Obtindrem noves consultes tan aviat com ens sigui possible.
Pots seguir https://twitter.com/igor_chubin per noves actualitzacions.
======================================================================================
""",
        'de': u"""
Entschuldigung, wir können momentan den Wetterdienst nicht erreichen.
Dafür zeigen wir Ihnen das Wetter an einem Beispielort, damit Sie sehen wie die Seite das Wetter anzeigt.
Wir werden versuchen das Problem so schnell wie möglich zu beheben.
Folgen Sie https://twitter.com/igor_chubin für Updates.
======================================================================================
""",
        'cy': u"""
Rydym yn brin o ymholiadau i'r gwasanaeth tywydd ar hyn o bryd.
Felly dyma'r adroddiad tywydd ar gyfer y ddinas ragosod (er mwyn arddangos sut mae'n edrych).
Byddwn gyda ymholiadau newydd yn fuan.
Gellir dilyn https://twitter.com/igor_chubin i gael newyddion pellach.
======================================================================================
""",
        'es': u"""
Lo siento, hemos alcanzado el límite de peticiones al servicio de previsión del tiempo en este momento.
A continuación, la previsión del tiempo para una ciudad estándar (solo para que puedas ver que aspecto tiene el informe).
Muy pronto volveremos a tener acceso a las peticiones.
Puedes seguir https://twitter.com/igor_chubin para estar al tanto de la situación.
======================================================================================
""",
        'fa': u"""
متأسفانه در حال حاضر ظرفیت ما برای درخواست به سرویس هواشناسی به اتمام رسیده.
اینجا می تونید گزارش هواشناسی برای شهر پیش فرض رو ببینید (فقط برای اینه که بهتون نشون بدیم چه شکلی هست)
ما تلاش میکنیم در اسرع وقت ظرفیت جدید به دست بیاریم.
برای دنبال کردن اخبار جدید میتونید https://twitter.com/igor_chubin رو فالو کنید.
======================================================================================
""",
        'fr': u"""
Désolé, nous avons épuisé les requêtes vers le service météo.
Voici un bulletin météo de l'emplacement par défaut (pour vous donner un aperçu).
Nous serons très bientôt en mesure de faire de nouvelles requêtes.
Vous pouvez suivre https://twitter.com/igor_chubin pour rester informé.
======================================================================================
""",
        'hu': u"""
Sajnáljuk, kifogytunk az időjárási szolgáltatásra fordított erőforrásokból.
Itt van az alapértelmezett város időjárási jelentése (hogy lásd, hogyan néz ki).
A lehető leghamarabb új erőforrásokat fogunk kapni.
A frissítésekért tekintsd meg a https://twitter.com/igor_chubin oldalt.
======================================================================================
""",
        'hy': u"""
Կներեք, այս պահին մենք գերազանցել ենք եղանակային տեսության կայանին հարցումների քանակը.
Կարող եք տեսնել տիպային եղանակը զեկուցում հիմնական քաղաքի համար (Ուղղակի որպես նմուշ):
Մենք մշտապես աշխատում ենք հարցումների քանակը բարելավելու ուղղությամբ:
Կարող եք հետևել մեզ https://twitter.com/igor_chubin թարմացումների համար.
======================================================================================
""",
        'id': u"""
Maaf, kami kehabian permintaan ke layanan cuaca saat ini.
Ini adalah laporan cuaca dari kota standar (hanya untuk menunjukkan kepada anda bagaimana tampilannya).
Kami akan mencoba permintaan baru lagi sesegera mungkin.
Anda dapat mengikuti https://twitter.com/igor_chubin untuk informasi terbaru.
======================================================================================
""",
        'it': u"""
Scusate, attualmente stiamo esaurendo le risorse a disposizione del servizio meteo.
Qui trovate il bollettino del tempo per la città di default (solo per mostrarvi come si presenta).
Potremo elaborare nuove richieste appena possibile.
Potete seguire https://twitter.com/igor_chubin per gli aggiornamenti.
======================================================================================
""",
        'ko': u"""
죄송합니다. 현재 날씨 정보를 가져오는 쿼리 요청이 한도에 도달했습니다.
대신 기본으로 설정된 도시에 대한 일기 예보를 보여드리겠습니다. (이는 단지 어떻게 보이는지 알려주기 위함입니다).
쿼리 요청이 가능한 한 빨리 이루어질 수 있도록 하겠습니다.
업데이트 소식을 원하신다면 https://twitter.com/igor_chubin 을 팔로우 해주세요.
======================================================================================
""",
        'lv': u"""
Atvainojiet, uz doto brīdi mēs esam mazliet noslogoti.
Šeit ir laika ziņas noklusējuma pilsētai (lai parādītu jums, kā izskatās izveidotais ziņojums).
Mēs atsāksim darbu cik ātri vien varēsim.
Jūs varat sekot https://twitter.com/igor_chubin lai redzētu visus jaunumus.
======================================================================================
""",
        'mk': u"""
Извинете, ни снемуваат барања за до сервисот кој ни нуди временска прогноза во моментот.
Еве една временска прогноза за град (за да видите како изгледа).
Ќе добиеме нови барања најбрзо што можеме.
Следете го https://twitter.com/igor_chubin за известувања
======================================================================================
""",
        'nb': u"""
Beklager, vi kan ikke nå værtjenesten for øyeblikket.
Her er værmeldingen for standardbyen så du får se hvordan tjenesten ser ut.
Vi vil forsøke å fikse problemet så snart som mulig.
Du kan følge https://twitter.com/igor_chubin for oppdateringer.
======================================================================================
""",
        'zh': u"""
抱歉，当前天气服务不可用。
以下显示默认城市（只对您可见）。
我们将会尽快获取新数据。
您可以通过https://twitter.com/igor_chubin 获取最新动态。
======================================================================================
""",
        'nl': u"""
Excuse, wij kunnen u op dit moment dit weerbericht niet laten zien.
Hier is het weerbericht voor de standaard stad(zodat u weet hoe het er uitziet)
Wij lossen dit probleem zo snel mogelijk op.
voor updates kunt u ons op https://twitter.com/igor_chubin volgen.
======================================================================================
""",
        'fy': u"""
Excuses, wy kinne op dit moment 't waarberjocht net sjin litte.
Hjir is 't waarberjocht foar de standaard stêd.
Wy losse dit probleem sa gau mooglik op.
Foar updates kinne jo ús op https://twitter.com/igor_chubin folgje.
======================================================================================
""",
        'pl': u"""
Bardzo nam przykro, ale chwilowo wykorzystaliśmy limit zapytań do serwisu pogodowego.
To, co widzisz jest przykładowym raportem pogodowym dla domyślnego miasta.
Postaramy się przywrócić funkcjonalność tak szybko, jak to tylko możliwe.
Możesz śledzić https://twitter.com/igor_chubin na Twitterze, aby być na bieżąco.
======================================================================================
""",
        'pt': u"""
Desculpe-nos, estamos atingindo o limite de consultas ao serviço de previsão do tempo neste momento.
Veja a seguir a previsão do tempo para uma cidade padrão (apenas para você ver que aspecto o relatório tem).
Em breve voltaremos a ter acesso às consultas.
Você pode seguir https://twitter.com/igor_chubin para acompanhar a situação.
======================================================================================
""",
        'pt-br': u"""
Desculpe-nos, atingimos o limite de consultas ao serviço de previsão do tempo neste momento.
Veja a seguir a previsão do tempo para uma cidade padrão (apenas para você ver que aspecto o relatório tem).
Em breve voltaremos a ter acesso às consultas.
Você pode seguir https://twitter.com/igor_chubin para acompanhar a situação.
======================================================================================
""",
        'ro': u"""
Ne pare rău, momentan am epuizat cererile alocate de către serviciul de prognoză meteo.
Vă arătăm prognoza meteo pentru localitatea implicită (ca exemplu, să vedeți cum arată).
Vom obține alocarea de cereri noi cât de curând posibil.
Puteți urmări https://twitter.com/igor_chubin pentru actualizări.
======================================================================================
""",
        'te': u"""
క్షమించండి, ప్రస్తుతానికి మేము వాతావరణ సేవకు ప్రశ్నలను గడుపుతున్నాం.
ఇక్కడ డిఫాల్ట్ నగరం కోసం వాతావరణ నివేదిక (కేవలం మీకు చూపించడానికి, ఇది ఎలా కనిపిస్తుంది).
సాధ్యమైనంత త్వరలో కొత్త ప్రశ్నలను పొందుతారు.
నవీకరణల కోసం https://twitter.com/igor_chubin ను మీరు అనుసరించవచ్చు.
======================================================================================
""",
        'tr': u"""
Üzgünüz, an itibariyle hava durumu servisine yapabileceğimiz sorgu limitine ulaştık.
Varsayılan şehir için hava durumu bilgisini görüyorsunuz (neye benzediğini gösterebilmek için).
Mümkün olan en kısa sürede servise yeniden sorgu yapmaya başlayacağız.
Gelişmeler için https://twitter.com/igor_chubin adresini takip edebilirsiniz.
======================================================================================
""",
        'th': u"""
ขออภัย การเรียกค้นหาระบบสภาพอากาศของเราหมดชั่วคราว
เราจึงแสดงข้อมูลของเมืองตัวอย่าง (เพื่อที่จะแสดงให้คุณเห็นว่าหน้าตาเป็นยังไง)
เราจะเรียกค้นหาใหม่โดยเร็วที่สุด
คุณสามารถติดตามการอัพเดทได้ที่ https://twitter.com/igor_chubin
======================================================================================
""",
        'da': u"""
Beklager, men vi er ved at løbe tør for forespørgsler til vejr-servicen lige nu.
Her er vejr rapporten for standard byen (bare så du ved hvordan det kan se ud).
Vi får nye forespørsler hurtigst muligt.
Du kan følge https://twitter.com/igor_chubin for at få opdateringer.
======================================================================================
""",
        'et': u"""
Vabandage, kuid hetkel on päringud ilmateenusele piiratud.
Selle asemel kuvame hetkel näidislinna ilmaprognoosi (näitamaks, kuidas see välja näeb).
Üritame probleemi lahendada niipea kui võimalik.
Jälgige https://twitter.com/igor_chubin värskenduste jaoks.
======================================================================================
""",
        'uk': u"""
Вибачте, ми перевищили максимальну кількість запитів до сервісу погоди.
Ось прогноз погоди у нашому місті (просто показати Вам як це виглядає).
Ми відновимо роботу як тільки зможемо.
Ви можете підписатися на https://twitter.com/igor_chubin для отримання новин.
======================================================================================
""",
        'vi': u"""
Xin lỗi, hiện tại chúng tôi đã hết lượt yêu cầu thông tin thời tiết.
Đây là dự báo thời tiết cho thành phố mặc định (chỉ để cho bạn thấy nó trông như thế nào).
Chung tôi sẽ có thêm lượt truy vấn sớm nhất có thể
Bạn có thể theo dõi https://twitter.com/igor_chubin để cập nhật thông tin mới nhất.
======================================================================================
""",
        'zh-tw': u"""
抱歉，目前天氣服務的查詢請求太多了。
這裡是預設城市的天氣報告（只是為您展示它的外觀）。
我們將盡快取得新的資料。
您可以追蹤 https://twitter.com/igor_chubin 以取得更新。
======================================================================================
""",
    },

    # Historical messages:
    #     'Check new Feature: \033[92mwttr.in/Moon\033[0m or \033[92mwttr.in/Moon@2016-Mar-23\033[0m to see the phase of the Moon'
    #     'New feature: \033[92mwttr.in/Rome?lang=it\033[0m or \033[92mcurl -H "Accept-Language: it" wttr.in/Rome\033[0m for the localized version. Your lang instead of "it"'

    'NEW_FEATURE': {
        'en': u'New feature: multilingual location names \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) and location search \033[92mwttr.in/~Kilimanjaro\033[0m (just add ~ before)',
        'af': u'Nuwe eienskap: veeltalige name vir liggings \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) en ligging soek \033[92mwttr.in/~Kilimanjaro\033[0m (plaas net ~ vooraan)',
        'be': u'Новыя магчымасці: назвы месц на любой мове \033[92mwttr.in/станция+Восток\033[0m (в UTF-8) i пошук месц \033[92mwttr.in/~Kilimanjaro\033[0m (трэба дадаць ~ ў пачатак)',
        'bg': u'Нова функционалност: многоезични имена на места\033[92mwttr.in/станция+Восток\033[0m (в UTF-8) и в търсенето \033[92mwttr.in/~Kilimanjaro\033[0m (добавете ~ преди)',
        'bs': u'XXXXXXXXXXXXXXXXXXXX: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[92mwttr.in/станция+Восток\033[0m (XX UTF-8) XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'ca': u'Noves funcionalitats: noms d\'ubicació multilingües \033[92mwttr.in/станция+Восток\033[0m (en UTF-8) i la ubicació de recerca \033[92mwttr.in/~Kilimanjaro\033[0m (només cal afegir ~ abans)',
        'es': u'Nuevas funcionalidades: los nombres de las ubicaciones en vários idiomas \033[92mwttr.in/станция+Восток\033[0m (em UTF-8) y la búsqueda por ubicaciones \033[92mwttr.in/~Kilimanjaro\033[0m (tan solo inserte ~ en frente)',
        'fa': u'قابلیت جدید: پشتیبانی از نام چند زبانه مکانها \033[92mwttr.in/станция+Восток\033[0m (در فرمت UTF-8) و جسجتوی مکان ها \033[92mwttr.in/~Kilimanjaro\033[0m (فقط قبل از اون ~ اضافه کنید)',
        'fr': u'Nouvelles fonctionnalités: noms d\'emplacements multilingues \033[92mwttr.in/станция+Восток\033[0m (en UTF-8) et recherche d\'emplacement \033[92mwttr.in/~Kilimanjaro\033[0m (ajouter ~ devant)',
        'mk': u'Нова функција: повеќе јазично локациски имиња \033[92mwttr.in/станция+Восток\033[0m (во UTF-8) и локациско пребарување \033[92mwttr.in/~Kilimanjaro\033[0m (just add ~ before)',
        'nb': u'Ny funksjon: flerspråklige stedsnavn \033[92mwttr.in/станция+Восток\033[0m (i UTF-8) og lokasjonssøk \033[92mwttr.in/~Kilimanjaro\033[0m (bare legg til ~ foran)',
        'nl': u'Nieuwe functie: tweetalige locatie namen \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) en locatie zoeken \033[92mwttr.in/~Kilimanjaro\033[0m (zet er gewoon een ~ voor)',
        'fy': u'Nije funksje: twatalige lokaasje nammen \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) en lokaasje sykjen \033[92mwttr.in/~Kilimanjaro\033[0m (set er gewoan in ~ foar)',
        'cy': u'Nodwedd newydd: enwau lleoliadau amlieithog \033[92mwttr.in/станция+Восток\033[0m (yn UTF-8) a chwilio am leoliad \033[92mwttr.in/~Kilimanjaro\033[0m (ychwanegwch ~ yn gyntaf)',
        'de': u'Neue Funktion: mehrsprachige Ortsnamen \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) und Ortssuche \033[92mwttr.in/~Kilimanjaro\033[0m (fügen Sie ein ~ vor dem Ort ein)',
        'hu': u'Új funkcinalitás: többnyelvű helynevek \033[92mwttr.in/станция+Восток\033[0m (UTF-8-ban) és pozíció keresés \033[92mwttr.in/~Kilimanjaro\033[0m (csak adj egy ~ jelet elé)',
        'hy': u'Փորձարկեք: տեղամասերի անունները կամայական լեզվով \033[92mwttr.in/Դիլիջան\033[0m (в UTF-8) և տեղանքի որոնում \033[92mwttr.in/~Kilimanjaro\033[0m (հարկավոր է ~ ավելացնել դիմացից)',
        'id': u'Fitur baru: nama lokasi dalam multibahasa \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) dan pencarian lokasi \033[92mwttr.in/~Kilimanjaro\033[0m (hanya tambah tanda ~ sebelumnya)',
        'it': u'Nuove funzionalità: nomi delle località multilingue \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) e ricerca della località \033[92mwttr.in/~Kilimanjaro\033[0m (basta premettere ~)',
        'ko': u'새로운 기능: 다국어로 대응된 위치 \033[92mwttr.in/서울\033[0m (UTF-8에서) 장소 검색 \033[92mwttr.in/~Kilimanjaro\033[0m (앞에 ~를 붙이세요)',
        'kk': u'',
        'lv': u'Jaunums: Daudzvalodu atrašanās vietu nosaukumi \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) un dabas objektu meklēšana \033[92mwttr.in/~Kilimanjaro\033[0m (tikai priekšā pievieno ~)',
        'mk': u'Нова функција: повеќе јазично локациски имиња \033[92mwttr.in/станция+Восток\033[0m (во UTF-8) и локациско пребарување \033[92mwttr.in/~Kilimanjaro\033[0m (just add ~ before)',
        'pl': u'Nowa funkcjonalność: wielojęzyczne nazwy lokalizacji \033[92mwttr.in/станция+Восток\033[0m (w UTF-8) i szukanie lokalizacji \033[92mwttr.in/~Kilimanjaro\033[0m (poprzedź zapytanie ~ - znakiem tyldy)',
        'pt': u'Nova funcionalidade: nomes de localidades em várias línguas \033[92mwttr.in/станция+Восток\033[0m (em UTF-8) e procura por localidades \033[92mwttr.in/~Kilimanjaro\033[0m (é só colocar ~ antes)',
        'pt-br': u'Nova funcionalidade: nomes de localidades em várias línguas \033[92mwttr.in/станция+Восток\033[0m (em UTF-8) e procura por localidades \033[92mwttr.in/~Kilimanjaro\033[0m (é só colocar ~ antes)',
        'ro': u'Funcționalitate nouă: nume de localități multilingve \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) și căutare de localități \033[92mwttr.in/~Kilimanjaro\033[0m (adăuați ~ în față)',
        'ru': u'Попробуйте: названия мест на любом языке \033[92mwttr.in/станция+Восток\033[0m (в UTF-8) и поиск мест \033[92mwttr.in/~Kilimanjaro\033[0m (нужно добавить ~ спереди)',
        'zh': u'新功能：多语言地点名称 \033[92mwttr.in/станция+Восток\033[0m (in UTF-8) 及地点搜索\033[92mwttr.in/~Kilimanjaro\033[0m （只需在名称前加~）',
        'tr': u'Yeni özellik: çok dilli konum isimleri \033[92mwttr.in/станция+Восток\033[0m (UTF-8 ile) ve konum arama \033[92mwttr.in/~Kilimanjaro\033[0m (sadece önüne ~ ekleyin)',
        'te': u'క్రొత్త లక్షణం: బహుభాషా స్థాన పేర్లు \ 033 [92mwttr.in/stancelя+Vostок\033 [0 U (UTF-8 లో) మరియు స్థానం శోధన \ 033 [92mwttr.in/~kilimanjaro\033 [0m (కేవలం ~ ముందుకి జోడించండి)',
        'th': u'ฟีเจอร์ใหม่: แสดงที่ตั้งได้หลายภาษา \033[92mwttr.in/станция+Восток\033[0m (ใน UTF-8) และการค้นหาที่ตั้ง \033[92mwttr.in/~Kilimanjaro\033[0m (เพียงเพิ่ม ~ ข้างหน้า)',
        'da': u'Ny funktion: flersprogede lokationsnavne \033[92mwttr.in/станция+Восток\033[0m (som UTF-8) og lokations søgning \033[92mwttr.in/~Kilimanjaro\033[0m (bare tilføj ~ inden)',
        'et': u'Uus funktsioon: mitmekeelsed asukohanimed \033[92mwttr.in/станция+Восток\033[0m (UTF-8 vormingus) ja asukoha otsing \033[92mwttr.in/~Kilimanjaro\033[0m (lisa ~ enne)',
        'uk': u'Спробуйте: назви місць будь-якою мовою \033[92mwttr.in/станція+Восток\033[0m (в UTF-8) та пошук місць \033[92mwttr.in/~Kilimanjaro\033[0m (потрібно додати ~ спочатку)',
        'vi': u'Chức năng mới: tên địa điểm đa ngôn ngữ \033[92mwttr.in/станция+Восток\033[0m (dùng UTF-8) và tìm kiếm địa điểm \033[92mwttr.in/~Kilimanjaro\033[0m (chỉ cần thêm ~ phía trước)',
        'zh-tw': u'新功能：多語言地點名稱 \033[92mwttr.in/станция+Восток\033[0m （使用 UTF-8 編碼）與位置搜尋 \033[92mwttr.in/~Kilimanjaro\033[0m （只要在地點前加 ~ 就可以了）',
    },

    'FOLLOW_ME': {
        'en': u'Follow \033[46m\033[30m@igor_chubin\033[0m for wttr.in updates',
        'af': u'Volg \033[46m\033[30m@igor_chubin\033[0m vir wttr.in opdaterings',
        'be': u'Сачыце за \033[46m\033[30m@igor_chubin\033[0m за навінамі wttr.in',
        'bg': u'Последвай \033[46m\033[30m@igor_chubin\033[0m за обновления свързани с wttr.in',
        'bs': u'XXXXXX \033[46m\033[30m@igor_chubin\033[0m XXXXXXXXXXXXXXXXXXX',
        'ca': u'Segueix \033[46m\033[30m@igor_chubin\033[0m per actualitzacions de wttr.in',
        'es': u'Seguir \033[46m\033[30m@igor_chubin\033[0m para recibir las novedades de wttr.in',
        'cy': u'Dilyner \033[46m\033[30m@igor_Chubin\033[0m am diweddariadau wttr.in',
        'fa': u'برای دنبال کردن خبرهای wttr.in شناسه \033[46m\033[30m@igor_chubin\033[0m رو فالو کنید.',
        'fr': u'Suivez \033[46m\033[30m@igor_Chubin\033[0m pour rester informé sur wttr.in',
        'de': u'Folgen Sie \033[46m\033[30mhttps://twitter.com/igor_chubin\033[0m für wttr.in Updates',
        'hu': u'Kövesd \033[46m\033[30m@igor_chubin\033[0m-t további wttr.in információkért',
        'hy': u'Նոր ֆիչռների համար հետևեք՝ \033[46m\033[30m@igor_chubin\033[0m',
        'id': u'Ikuti \033[46m\033[30m@igor_chubin\033[0m untuk informasi wttr.in terbaru',
        'it': u'Seguite \033[46m\033[30m@igor_chubin\033[0m per aggiornamenti a wttr.in',
        'ko': u'wttr.in의 업데이트 소식을 원하신다면 \033[46m\033[30m@igor_chubin\033[0m 을 팔로우 해주세요',
        'kk': u'',
        'lv': u'Seko \033[46m\033[30m@igor_chubin\033[0m , lai uzzinātu wttr.in jaunumus',
        'mk': u'Следете \033[46m\033[30m@igor_chubin\033[0m за wttr.in новости',
        'nb': u'Følg \033[46m\033[30m@igor_chubin\033[0m for wttr.in oppdateringer',
        'nl': u'Volg \033[46m\033[30m@igor_chubin\033[0m voor wttr.in updates',
        'fy': u'Folgje \033[46m\033[30m@igor_chubin\033[0m foar wttr.in updates',
        'pl': u'Śledź \033[46m\033[30m@igor_chubin\033[0m aby być na bieżąco z nowościami dotyczącymi wttr.in',
        'pt': u'Seguir \033[46m\033[30m@igor_chubin\033[0m para as novidades de wttr.in',
        'pt-br': u'Seguir \033[46m\033[30m@igor_chubin\033[0m para as novidades de wttr.in',
        'ro': u'Urmăriți \033[46m\033[30m@igor_chubin\033[0m pentru actualizări despre wttr.in',
        'ru': u'Все новые фичи публикуются здесь: \033[46m\033[30m@igor_chubin\033[0m',
        'zh': u'关注 \033[46m\033[30m@igor_chubin\033[0m 获取 wttr.in 动态',
        'te': u'అనుసరించండి \ 033 [46m \ 033 [30m @ igor_chubin \ 033 [wttr.in నవీకరణలను కోసం',
        'tr': u'wttr.in ile ilgili gelişmeler için \033[46m\033[30m@igor_chubin\033[0m adresini takip edin',
        'th': u'ติดตาม \033[46m\033[30m@igor_chubin\033[0m สำหรับการอัพเดท wttr.in',
        'da': u'Følg \033[46m\033[30m@igor_chubin\033[0m for at få wttr.in opdateringer',
        'et': u'Jälgi \033[46m\033[30m@igor_chubin\033[0m wttr.in uudiste tarbeks',
        'uk': u'Нові можливості wttr.in публікуються тут: \033[46m\033[30m@igor_chubin\033[0m',
        'vi': u'Theo dõi \033[46m\033[30m@igor_chubin\033[0m để cập nhật thông tin về wttr.in',
        'zh-tw': u'追蹤 \033[46m\033[30m@igor_chubin\033[0m 以取得更多 wttr.in 的動態',
    },
}

CAPTION = {
    "af": u"Weer verslag vir:",
    "ar": u"ﺖﻗﺮﻳﺭ ﺡﺎﻟﺓ ﺄﻠﻄﻘﺳ",
    "az": u"Hava proqnozu:",
    "be": u"Прагноз надвор'я для:",
    "bg": u"Прогноза за времето в:",
    "bs": u"Vremenske prognoze za:",
    "ca": u"Informe del temps per a:",
    "cs": u"Předpověď počasí pro:",
    "cy": u"Adroddiad tywydd ar gyfer:",
    "da": u"Vejret i:",
    "de": u"Wetterbericht für:",
    "el": u"Πρόγνωση καιρού για:",
    "en": u"weather report for:",
    "eo": u"Veterprognozo por:",
    "es": u"El tiempo en:",
    "et": u"Ilmaprognoos:",
    "fa": u"گزارش آب و هئا برای شما:",
    "fi": u"Säätiedotus:",
    "fr": u"Prévisions météo pour:",
    "fy": u"Waarberjocht foar:",
    "ga": u"Réamhaisnéis na haimsire do:",
    "he": u":ריוואה גזמ תיזחת",
    "hr": u"Vremenska prognoza za:",
    "hu": u"Időjárás előrejelzés:",
    "hy": u"Եղանակի տեսություն:",
    "id": u"Prakiraan cuaca:",
    "it": u"Previsioni meteo:",
    "is": u"Veðurskýrsla fyrir:",
    "ja": u"天気予報：",
    "jv": u"Weather forecast for:",
    "ka": u"ამინდის პროგნოზი:",
    "kk": u"Ауа райы:",
    "ko": u"일기 예보：",
    "ky": u"Аба ырайы:",
    "lt": u"Orų prognozė:",
    "lv": u"Laika ziņas:",
    "mk": u"Прогноза за времето во:",
    "ml": u"കാലാവസ്ഥ റിപ്പോർട്ട്:",
    "nb": u"Værmelding for:",
    "nl": u"Weerbericht voor:",
    "nn": u"Vêrmelding for:",
    "pl": u"Pogoda w:",
    "pt": u"Previsão do tempo para:",
    "pt-br": u"Previsão do tempo para:",
    "ro": u"Prognoza meteo pentru:",
    "ru": u"Прогноз погоды:",
    "sk": u"Predpoveď počasia pre:",
    "sl": u"Vremenska napoved za",
    "sr": u"Временска прогноза за:",
    "sr-lat": u"Vremenska prognoza za:",
    "sv": u"Väderleksprognos för:",
    "sw": u"Ripoti ya hali ya hewa, jiji la:",
    "te": u"వాతావరణ సమాచారము:",
    "th": u"รายงานสภาพอากาศ:",
    "tr": u"Hava beklentisi:",
    "uk": u"Прогноз погоди для:",
    "uz": u"Ob-havo bashorati:",
    "vi": u"Báo cáo thời tiết:",
    "zh": u"天氣預報：",
    "zu": u"Isimo sezulu:",
    "zh-tw": u"天氣報告：",
}

def get_message(message_name, lang):
    if message_name not in MESSAGE:
        return ''
    message_dict = MESSAGE[message_name]
    return message_dict.get(lang, message_dict.get('en', ''))
