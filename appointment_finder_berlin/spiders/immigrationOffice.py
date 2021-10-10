import scrapy
from scrapy.http import Response, Request
import http.client, urllib
from scrapy.utils.project import get_project_settings
import requests
import json

class BerlinImmigrationOfficeSpider(scrapy.Spider):
    name = 'immigrationOffice'

    def start_requests(self):
        url = 'https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/dd3b7824-43be-4c34-adff-7fcbddd90c59?dswid=4721&dsrid=712&st=2&v=1633871733725'

        cookies = {
            'JSESSIONID': 'N8m6rAJEuMqHFRu9H6IwUdwtpZPkOFlR1W2Jbddn.frontend',
            '31225d4d5151d978968da054bdf27710': '7c19b873a48035cca88de234d289aed8',
            'TS018ca6c6': '01d33437f9b5c14f46b8f587841e5ae9da012edb0ac7a13447f885a5aedff16af1837fc94b8c174d62c57d4d245c82f191e0c4ea16',
        }

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'Accept': '*/*',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxYYYFbsbQXM0VJI6',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
            'sec-ch-ua-platform': '"macOS"',
            'Origin': 'https://otv.verwalt-berlin.de',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/dd3b7824-43be-4c34-adff-7fcbddd90c59?dswid=4721&dsrid=712&st=2&v=1633871733725',
            'Accept-Language': 'en-US,en;q=0.9,tr;q=0.8,de;q=0.7',
            'sec-gpc': '1',
        }

        params = (
            ('dswid', '4721'),
            ('suppressRenderOnChange', 'true'),
        )

        data = {
            '------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name': '"applicationForm:managedForm"\r\n\r\napplicationForm:managedForm\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="frid"\r\n\r\nc2734a99-5b73-402b-b2e4-4f7585ff21b1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="lang"\r\n\r\nen\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="anliegen_auswahl_deutsch"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="anliegen_auswahl_andere"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="sammelfeld_konsulat"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="init_sprachauswahl"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="contrydatacsv"\r\n\r\nT\xFCrkei!-163!-nein!-163-0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="sel_staat"\r\n\r\n163\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="personenAnzahl_normal"\r\n\r\n1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dokumente"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="personenAnzahl_mit_dokument"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="personenAnzahl_ohne_dokument"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="lebnBrMitFmly"\r\n\r\n1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="fmlyMemNationality"\r\n\r\n163-0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="angehoeriger_eu_ewr"\r\n\r\n163-0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="sel_anliegensgruppe"\r\n\r\nx\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="sel_anliegenszweck"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="sel_service"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="enter_sachgebiet"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="level1"\r\n\r\n163-0-1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="level2"\r\n\r\n163-0-1-4\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="level3"\r\n\r\n163-0-1-4-324269\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="aggregatedServices"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="selectedService"\r\n\r\n163-0-1-4-324269\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="swissSelectedService"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="serviceValidationElement"\r\n\r\nAufenthaltserlaubnis  f\xFCr ein neugeborenes Kind - Erteilung (\xA7 33)\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="accId"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="TAprozessID"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dienstleistungName"\r\n\r\nAufenthaltserlaubnis  f\xFCr ein neugeborenes Kind - Erteilung (\xA7 33)\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dienstleistung"\r\n\r\n324269\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="sachgebietName"\r\n\r\nReferat E 3     Haus D, Warteraum E 3.1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="clusterId"\r\n\r\n20\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="standortId"\r\n\r\n0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="standortId1"\r\n\r\n251\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="targetVal"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_dienstleistung_ID"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="aufhenthaltnr_pflicht"\r\n\r\n0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_dienstleister"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_dienstleistung_name"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="InfoBarrierefreiheit"\r\n\r\nDer Zugang zur Einrichtung ist Rollstuhlgeeignet.Ein ausgewiesener Behindertenparkplatz ist vorhanden.Ein rollstuhlgeeigneter Aufzug ist vorhanden.Ein rollstuhlgeeignetes WC ist vorhanden.\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="OEPNVInfo"\r\n\r\nS-Bahn: S 41/42 (Westhafen) U-Bahn: U 9 (Amrumer Str.) Bus: 123, 142, M27 \r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="Leistungsname"\r\n\r\nAufenthaltserlaubnis f\xFCr im Bundesgebiet geborene Kinder - Erteilung\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="Leistungsbeschreibung"\r\n\r\nErstmalige Erteilung einer Aufenthaltserlaubnis f\xFCr ein ausl\xE4ndisches Kind, \r\n* das im Bundesgebiet geboren wird und \r\n* bei dem mindestens ein Elternteil einen g\xFCltigen Aufenthaltstitel besitzt\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="Gebuehrenrahmen"\r\n\r\n* 50,00 Euro\r\n* 22,80 Euro f\xFCr ein Kind mit t\xFCrkischer Staatsangeh\xF6rigkeit.\r\n* Geb\xFChrenfrei bei Vorlage eines aktuellen Nachweises \xFCber den Bezug von Leistungen nach SGB II, SGB XII oder nach Asylbewerberleistungsgesetz\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="benoetigteUnterlagen"\r\n\r\nPass des Kindes - Das Kind muss entweder \xFCber einen eigenen g\xFCltigen Pass verf\xFCgen oder im Pass eines Elternteils eingetragen sein.|1 aktuelles biometrisches Foto - 35mm x 45mm, Frontalaufnahme mit neutralem Gesichtsausdruck und geschlossenem Mund gerade in die Kamera blickend, heller Hintergrund (http://www.berlin.de/labo/_assets/kraftfahrzeugwesen/foto-mustertafel.pdf)|Geburtsurkunde |P\xE4sse der Eltern \r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="Besonderheiten"\r\n\r\nPers\xF6nliche Vorsprache ist erforderlich - Die Vorsprache sollte m\xF6glichst mit Termin erfolgen.|Von Amts wegen - Erteilung bei einem B\xFCrgeramt - Beide Elternteile (bei gemeinsamen Sorgerecht) oder der allein sorgeberechtigte Elternteil sind bei Geburt des Kindes im Besitz eines g\xFCltigen Aufenthaltstitels. \r\n\r\nDie Aufenthaltstitel (Aufenthaltserlaubnis, Blaue Karte-EU, Niederlassungserlaubnis, Erlaubnis zum Daueraufenthalt-EU, Aufenthaltsberechtigung oder unbefristete Aufenthaltserlaubnis) der Eltern bzw. des Elternteils m\xFCssen von der Ausl\xE4nderbeh\xF6rde Berlin / dem Landesamt f\xFCr Einwanderung erteilt worden sein. \r\n\r\nDie Aufenthaltserlaubnis f\xFCr das Kind kann dann von jedem Berliner B\xFCrgeramt erteilt werden.|Auf Antrag - Erteilung beim Landesamt f\xFCr Einwanderung - Nur ein Elternteil (bei gemeinsamen Sorgerecht) ist bei Geburt des Kindes im Besitz eines g\xFCltigen Aufenthaltstitels (siehe oben).\r\n\r\nDie Aufenthaltserlaubnis f\xFCr das Kind ist dann beim Landesamt f\xFCr Einwanderung zu beantragen.|Geburt im Bundesgebiet - Das Kind muss im Bundesgebiet geboren worden sein und gemeinsam mit den Eltern oder dem allein sorgeberechtigten Elternteil in Berlin gemeldet sein.\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="rechtlicheGrundlage"\r\n\r\n\xA7 33 Aufenthaltsgesetz - AufenthG (http://www.gesetze-im-internet.de/aufenthg_2004/__33.html)\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="Organisationsname"\r\n\r\n                LEA, Friedrich-Krause-Ufer\r\n            \r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_str"\r\n\r\nFriedrich-Krause-Ufer\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_nr"\r\n\r\n24\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_plz"\r\n\r\n13353\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_ort"\r\n\r\nBerlin\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="dl_response_error"\r\n\r\n0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="sel_staat_hidden_val"\r\n\r\n163\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="angehoeriger_eu_ewr_hidden_val"\r\n\r\n163-0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="anliegen_nr_hidden"\r\n\r\n1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="countrySelected"\r\n\r\n1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="country998"\r\n\r\n0\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="personen_anzahl_hidden_val"\r\n\r\n1\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="selectedService"\r\n\r\n163-0-1-4-324269\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="xima-9875-required"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="xfc-pp-elementslist"\r\n\r\nanliegen_auswahl_deutsch,anliegen_auswahl_andere,sammelfeld_konsulat,init_sprachauswahl,contrydatacsv,sel_staat,personenAnzahl_normal,dokumente,personenAnzahl_mit_dokument,personenAnzahl_ohne_dokument,lebnBrMitFmly,fmlyMemNationality,angehoeriger_eu_ewr,sel_anliegensgruppe,sel_anliegenszweck,sel_service,enter_sachgebiet,aggregatedServices,selectedService,swissSelectedService,level1Val,level2Val,level3Val,serviceValidationElement,accId,TAprozessID,dienstleistungName,dienstleistung,sachgebietName,clusterId,standortId,standortId1,targetVal,dl_dienstleistung_ID,aufhenthaltnr_pflicht,dl_dienstleister,dl_dienstleistung_name,InfoBarrierefreiheit,OEPNVInfo,Leistungsname,Leistungsbeschreibung,Gebuehrenrahmen,benoetigteUnterlagen,Besonderheiten,rechtlicheGrundlage,Organisationsname,dl_str,dl_nr,dl_plz,dl_ort,dl_response_error,sel_staat_hidden_val,angehoeriger_eu_ewr_hidden_val,anliegen_nr_hidden,countrySelected,country998,personen_anzahl_hidden_val,selectedService\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="error_code"\r\n\r\ngge6;:7570e60hf776d0ig0ii:efgg<gf3<8\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="clientWizardStep"\r\n\r\nMl9BbmxpZWdlbnNrbMOkcnVuZw==\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="applicationForm:managedForm:j_idt314"\r\n\r\n\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="javax.faces.ViewState"\r\n\r\n2634509714600799384:-679693269027189737\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6\r\nContent-Disposition: form-data; name="javax.faces.ClientWindow"\r\n\r\n4721\r\n------WebKitFormBoundaryxYYYFbsbQXM0VJI6--'
        }

        response = requests.post(
            'https://otv.verwalt-berlin.de/api/remote2/TerminBuchen/dd3b7824-43be-4c34-adff-7fcbddd90c59/proceed',
            headers=headers, params=params, cookies=cookies, data=data)

        if response is not None:
            self.custom_parse(response.text, url)

        yield Request(url, dont_filter=True)

    def parse(self, response):
        pass

    def custom_parse(self, text, url):
        try:
            pos = text.find('There are currently no dates available for the selected service')
            if -1 == pos:
                self.send_notification('', url)
                print("Yay")
            else:
                print("Sorry, there is no appointment :(")
                pass
            pass
        except ValueError as err:
            pass

    def send_notification(self, days, url):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": get_project_settings().get('PUSHOVER_TOKEN'),
            "user": get_project_settings().get('PUSHOVER_USER'),
            "message": "I found an empty slot(s)" +  ' ' + " ".join(days) + ' ' + url,
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()