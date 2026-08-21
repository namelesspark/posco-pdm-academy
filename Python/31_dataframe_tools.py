# 데이터프레임 도구 비교 - Pandas / Polars / DuckDB
# 교수님 설명 코드 (교안 차시 코드가 아니라 도구 소개 자료)
#
# [무엇을 하나] 똑같은 작업 하나를 세 도구로 각각 짜서 문법과 특징을 비교한다.
#   작업: Electronics 만 필터 → quantity * unit_price 로 total_sales 파생 → category 별 합계
#   세 결과 모두 동일:  total_sales 1926.0 / total_qty 6
#   (Laptop 1200 + Mouse 51 + Monitor 600 + Keyboard 75)
#
# [실행 전 설치 필요]  pip install polars duckdb

import pandas as pd
import polars as pl
import duckdb

CSV = "Data/sales_data.csv"

# ==============================================================================
# [1] Pandas
# - 특징: 파이썬 데이터 분석의 표준. 행/열 인덱스 기반의 직관적인 조작.
# - 장점: 가장 넓은 생태계, 방대한 레퍼런스, scikit-learn 등과의 호환성.
# - 단점: 기본적으로 싱글 코어라 대용량에서 느리고, 메모리 복사 비용이 큼.
# ==============================================================================

# 1.1 CSV 파일 전체를 메모리로 읽어 들임
df_pd = pd.read_csv(CSV)

# 1.2 조건 필터링
# 뷰(View)와 복사본(Copy) 구분을 위해 .copy() 를 명시하는 편이 안전 (26_filtering_sorting.py 참고)
df_pd_filtered = df_pd[df_pd["category"] == "Electronics"].copy()

# 1.3 파생 컬럼 생성 (단가 * 수량)
df_pd_filtered["total_sales"] = df_pd_filtered["quantity"] * df_pd_filtered["unit_price"]

# 1.4 그룹화 및 집계
# groupby 후 인덱스로 들어간 'category' 를 일반 컬럼으로 되돌리려면 .reset_index() 필요
res_pd = (
    df_pd_filtered.groupby("category")
    .agg(total_sales=("total_sales", "sum"), total_qty=("quantity", "sum"))
    .reset_index()
)

print("--- [Pandas 결과] --- \n", res_pd)


# ==============================================================================
# [2] Polars
# - 특징: Rust 기반 초고속 데이터프레임. Apache Arrow 메모리 포맷 사용.
# - 장점: 멀티스레딩 병렬 처리, 메모리 효율 우수, 표현식 기반 파이프라인.
# - 단점: Pandas 와 문법이 달라 러닝 커브가 있고, 일부 레거시 라이브러리와 직접 호환 안 됨.
# ==============================================================================

res_pl = (
    pl.read_csv(CSV)
    # 2.1 pl.col() 표현식을 활용한 고속 벡터화 필터링
    .filter(pl.col("category") == "Electronics")
    # 2.2 with_columns(): 원본 불변성을 유지하며 새 컬럼 추가
    .with_columns((pl.col("quantity") * pl.col("unit_price")).alias("total_sales"))
    # 2.3 group_by() & agg(): 병렬 그룹 집계 (인덱스 리셋 불필요)
    .group_by("category").agg(
        pl.col("total_sales").sum().alias("total_sales"),
        pl.col("quantity").sum().alias("total_qty"),
    )
)

print("\n--- [Polars 결과] --- \n", res_pl)


# ==============================================================================
# [3] DuckDB
# - 특징: 분석용(OLAP) 임베디드 SQL 엔진.
# - 장점: 서버 설치 없이 파일/메모리에서 바로 실행, 표준 SQL 지원,
#         CSV/Parquet 를 메모리에 전부 올리지 않고 스트리밍 쿼리 가능.
# - 단점: 메서드 체이닝이 아니라 SQL 문자열 중심이라 코드 스타일이 달라짐.
# ==============================================================================

# 3.1 파일 경로를 테이블처럼 직접 쿼리 → 로딩·필터·집계를 한 번에 최적화
res_duckdb = duckdb.sql(f"""
    SELECT
        category,
        SUM(quantity * unit_price) AS total_sales,
        SUM(quantity) AS total_qty
    FROM '{CSV}'
    WHERE category = 'Electronics'
    GROUP BY category
""").df()  # 3.2 결과를 Pandas DataFrame 으로 변환해 수신

print("\n--- [DuckDB 결과] --- \n", res_duckdb)
