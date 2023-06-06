import folium
import pandas as pd

# 시/군별 인구 데이터
population_data = {
    'City': ['천안시', '공주시', '보령시', '아산시', '서산시','논산시','계룡시','당진시','금산군','부여군','서천군','청양군','홍성군','예산군','태안군'],
    'Population': [652845,106294,100908,314238,174663,118781,42735,166815,52120,66676,52072,31577,100347,79126,62628]
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
chungcheongnamdo_map = folium.Map(location=[36.5184, 126.8009], zoom_start=9)

# 시/군별 인구 수에 따라 지도에 원 추가
for i, row in df.iterrows():
    city = row['City']
    population = row['Population']
    color = get_color(population)
    # 시/군 좌표 정보를 사용하여 원 추가
    folium.CircleMarker(location=(0, 0), radius=10, color=color, fill=True, fill_color=color).add_to(chungcheongnamdo_map)

# 지도 출력
chungcheongnamdo_map