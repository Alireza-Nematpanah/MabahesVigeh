import geopandas as gpd
import matplotlib.pyplot as plt

# بارگیری داده‌های نقشه جهان
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# فیلتر کردن نقشه آسیا
gdf_asia = gdf[gdf['continent'] == 'Asia']

# رسم نقشه
def plot_asia_highlight_iran():
    fig, ax = plt.subplots(figsize=(10, 6))
    gdf_asia.plot(ax=ax, color='lightgray', edgecolor='black')  # نقشه آسیا
    gdf_asia[gdf_asia['name'] == 'Iran'].plot(ax=ax, color='red')  # هایلایت کردن ایران
    
    plt.title("نقشه آسیا با برجسته کردن ایران", fontsize=14)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

plot_asia_highlight_iran()
