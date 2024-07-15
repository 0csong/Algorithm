def solution(data, ext, val_ext, sort_by):
    # 필터링을 위한 인덱스 맵핑
    category = ["code", "date", "maximum", "remain"]
    ext_index = category.index(ext)
    
    # 필터링
    filtered_data = [d for d in data if d[ext_index] < val_ext]
    
    # 정렬을 위한 인덱스 맵핑
    sort_by_index = category.index(sort_by)
    
    # 정렬
    filtered_data.sort(key=lambda x: x[sort_by_index])
    
    return filtered_data