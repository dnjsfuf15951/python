# 충청남도 시/군 별 인구 수 데이터 (가상의 데이터)
population_data = {
    '천안시': 800000,
    '공주시': 200000,
    '보령시': 150000,
    '아산시': 300000,
    '서산시': 250000,
    '논산시': 180000,
    '계룡시': 100000,
    '당진시': 220000,
    '금산군': 120000,
    '부여군': 160000,
    '서천군': 140000,
    '청양군': 90000,
    '홍성군': 170000,
    '예산군': 130000,
    '태안군': 110000
}

# 시/군 별 인구 수 출력하는 함수
def print_population_by_city():
    for city, population in population_data.items():
        print(f"{city}: {population}명")

# 전체 인구 수 출력하는 함수
def print_total_population():
    total_population = sum(population_data.values())
    print(f"충청남도 전체 인구 수: {total_population}명")

# 실행 예시
print_population_by_city()
print_total_population()