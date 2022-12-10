from flask import Flask, render_template, request
from process import preparation, generate_response
import sys

preparation()

app = Flask("Local Pride")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/destinasion")
def destination():
    return render_template("destination.html")

# Start Wisata Alam 
@app.route("/KWPLH")
def KWPLH():
    return render_template("KWPLH.html")

@app.route("/NiagaraTembinus")
def NiagaraTembinus():
    return render_template("NiagaraTembinus.html")

@app.route("/TelukKaba")
def TelukKaba():
    return render_template("TelukKaba.html")

@app.route("/AirPanas")
def AirPanas():
    return render_template("AirPanas.html")

@app.route("/AirTerjun")
def AirTerjun():
    return render_template("AirTerjun.html")

@app.route("/KersikLuway")
def KersikLuway():
    return render_template("KersikLuway.html")

@app.route("/GunungLiang")
def GunungLiang():
    return render_template("GunungLiang.html")

@app.route("/WisataSawah")
def WisataSawah():
    return render_template("WisataSawah.html")

@app.route("/TNKutai")
def TNKutai():
    return render_template("TNKutai.html")
     
@app.route("/BukitBatu")
def BukitBatu():
    return render_template("BukitBatu.html")
# End Wisata Alam              

# Start Wisata Buatan
@app.route("/WadukManggar")
def WadukManggar():
    return render_template("WadukManggar.html")

@app.route("/CIA")
def CIA():
    return render_template("CIA.html")

@app.route("/Bontang")
def Bontang():
    return render_template("Bontang.html")

@app.route("/Penangkaran")
def Penangkaran():
    return render_template("Penangkaran.html")

@app.route("/Taman")
def Taman():
    return render_template("Taman.html")

@app.route("/Garden")
def Garden():
    return render_template("Garden.html")

@app.route("/WadukPanji")
def WadukPanji():
    return render_template("WadukPanji.html")

# End Wisata Buatan

# Start Wisata Religi
@app.route("/MIC")
def MIC():
    return render_template("MIC.html")

@app.route("/Mesjid")
def Mesjid():
    return render_template("Mesjid.html")

@app.route("/MasjidJami")
def MasjidJami():
    return render_template("MasjidJami.html")

@app.route("/Gereja")
def Gereja():
    return render_template("Gereja.html")

@app.route("/ISC")
def ISC():
    return render_template("ISC.html")

@app.route("/GMS")
def GMS():
    return render_template("GMS.html")

# End Wisata Religi    


# Start Wisata Bahari
@app.route("/Lamaru")
def Lamaru():
    return render_template("Lamaru.html")

@app.route("/LabuanCermin")
def LabuanCermin():
    return render_template("LabuanCermin.html")

@app.route("/AirHemaq")
def AirHemaq():
    return render_template("AirHemaq.html")

@app.route("/PantaiSegajah")
def PantaiSegajah():
    return render_template("PantaiSengajah.html")

@app.route("/PulauGusung")
def PulauGusung():
    return render_template("PulauGusung.html")

@app.route("/PantaiTanjung")
def PantaiTanjung():
    return render_template("PantaiTanjung.html")

@app.route("/Dermaga")
def Dermaga():
    return render_template("Dermaga.html")  

@app.route("/PulauMiang")
def PulauMiang():
    return render_template("PulauMiang.html")

@app.route("/DanauSemayang")
def DanauSemayang():
    return render_template("DanauSemayang.html")  
# End Wisata Bahari   


# Start Wisata Sejarah
@app.route("/RumahDahor")
def RumahDahor():
    return render_template("RumahDahor.html")

@app.route("/Keraton")
def Keraton():
    return render_template("Keraton.html")

@app.route("/LaminTolan")
def LaminTolan():
    return render_template("LaminTolan.html")

@app.route("/MuseumSandurengas")
def MuseumSandurengas():
    return render_template("MuseumSandurengas.html")

@app.route("/Museum")
def Museum():
    return render_template("Museum.html")

@app.route("/kedaton")
def kedaton():
    return render_template("kedaton.html")

# End Wisata Sejarah       


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/get")
def get_bot_respon():
    user_input = str(request.args.get("msg"))
    result = generate_response(user_input)
    return result


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
