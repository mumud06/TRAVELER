import pandas as pd


def rekomendasi(filter="TAG"):
    df = pd.read_csv("dataset/Dataset Wisata 1.csv")
    data_bobot = df.groupby(filter).agg(["mean", "count"])["Ratings"].reset_index()
    m = data_bobot["count"].quantile(0.7)
    data_bobot = data_bobot[data_bobot["count"] > m]
    R = data_bobot["mean"]  # rata-rata untuk rating wisata = (Rating)
    v = data_bobot["count"]  # jumlah wisata = (Vote)
    C = data_bobot["mean"].mean()  # rata-rata vote di semua wisata
    data_bobot["Weighted Rating"] = (v / (v + m)) * R + (m / (v + m)) * C
    data_bobot = data_bobot.sort_values("Weighted Rating", ascending=False).reset_index(
        drop=True
    )
    data_bobot_final = pd.merge(data_bobot, df, on=filter)[
        ["Nama Wisata", "Lokasi", "Jenis Wisata", "Harga Tiket", "Ratings"]
    ].drop_duplicates("Jenis Wisata")
    top_10 = data_bobot_final.iloc[:15].to_dict()
    return top_10
