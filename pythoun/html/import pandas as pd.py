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
merged_data = map_data.merge(population_data, left_on='시군명', right_on='시군명', how='left')

# 인구 수에 따라 색상 결정
merged_data['Color'] = merged_data['인구'].apply(lambda x: '#f1c40f' if x < 500000 else ('#e67e22' if x < 1000000 else '#e74c3c'))

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 8))
merged_data.plot(column='Color', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# 축 제거
ax.axis('off')

# 그래프 제목 설정
plt.title('충청남도 인구 그래프', fontdict={'fontsize': '18', 'fontweight' : '3'})

# 범례 추가
legend = ax.get_legend()
legend.set_bbox_to_anchor((0.15, 0.8))

# 그래프 출력
plt.show()