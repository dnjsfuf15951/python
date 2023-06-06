import folium
import pandas as pd

# 시/군별 인구 데이터
population_data = {
    'City': ['시/군A', '시/군B', '시/군C', '시/군D', '시/군E'],
    'Population': [550000, 400000, 620000, 350000, 480000]
}

# 데이터프레임 생성
df = pd.DataFrame(population_data)

# 색상 설정 함수
def get_color(population):
    if population > 600000:
        return 'red'
    elif population > 300000:
        return 'orange'
    elif population > 150000:
        return 'yellow'
    elif population > 100000:
        return 'green'
    elif population > 70000:
        return 'blue'
    else:
        return 'purple'

# 충청남도 지도 생성
map_center = [36.5184, 126.8009]  # 충청남도 중심 좌표
map_zoom = 9  # 지도 확대 수준
chungcheongnamdo_map = folium.Map(location=map_center, zoom_start=map_zoom, tiles='Stamen Terrain')

# 시/군별 인구 수에 따라 지도에 원 추가
for i, row in df.iterrows():
    city = row['City']
    population = row['Population']
    color = get_color(population)
    # 시/군 좌표 정보
    city_coordinates = [city_latitude, city_longitude]  # 각 시/군의 위도, 경도 좌표로 수정 필요
    # 원 추가
    folium.CircleMarker(location=city_coordinates, radius=10, color=color, fill=True, fill_color=color).add_to(chungcheongnamdo_map)

# 지도 출력
chungcheongnamdo_map.save('chungcheongnamdo_population_map.html')