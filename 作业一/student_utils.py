def parse_student(line):
    """把一行逗号分隔的记录解析成字典。

    合法记录形如 "Alice,85"，返回 {"name": name, "score": score}。
    字段数量不对、姓名为空、成绩不是整数，或成绩不在 0〜100 时，抛出 ValueError。
    """
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(parts)}")

    name = parts[0].strip()
    score_text = parts[1].strip()
    if name == "":
        raise ValueError("姓名为空")

    try:
        score = int(score_text)
    except ValueError as exc:
        raise ValueError(f"成绩无法转换为整数：{score_text}") from exc

    if score < 0 or score > 100:
        raise ValueError(f"成绩超出 0〜100 范围：{score}")

    return {"name": name, "score": score}
