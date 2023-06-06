import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 인구 데이터가 있는 CSV 파일 경로
population_data_file = 'population_data.csv'

# 지도 데이터가 있는 SHP 파일 경로
map_file = 'chungcheongnamdo.shp'

# 인구 데이터를 저장할 딕셔너리 초기화
population_data = {}

# 인구 데이터 CSV 파일 읽기
with open(population_data_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 헤더 스킵
    for row in reader:
        city_name = row[0]
        population = int(row[1])
        population_data[city_name] = population

# 지도 데이터 로드
map_data = gpd.read_file(map_file, encoding='utf-8')

# 인구 데이터와 지도 데이터를 조인
merged_data = map_data.merge(pd.DataFrame(population_data.items(), columns=['시군명', '인구']), on='시군명')

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 8))

# 인구 수에 따라 다양한 색상으로 표시
merged_data.plot(column='인구', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# 축 제거
ax.axis('off')

# 그래프 제목 설정
plt.title('충청남도 시/군별 인구 수', fontdict={'fontsize': '18', 'fontweight' : '3'})

# 컬러바 설정
sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=merged_data['인구'].min(), vmax=merged_data['인구'].max()))
sm.set_array([])  # 더미 배열 설정
cbar = plt.colorbar(sm)
cbar.set_label('인구 수', rotation=270, labelpad=20)

# 그래프 출력
plt.show()