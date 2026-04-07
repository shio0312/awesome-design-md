#!/usr/bin/env python3
"""
README.mdから既存サイト情報を抽出してsites.yamlを生成するスクリプト
一度だけ実行すれば良い
"""

import re
from pathlib import Path
import yaml


def parse_readme():
    """README.mdを解析してサイト情報を抽出"""
    readme_path = Path(__file__).parent / "README.md"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    sites = []
    current_category = None

    # カテゴリとサイトを抽出
    lines = content.split("\n")

    for line in lines:
        # カテゴリ（### で始まる行）
        if line.startswith("### ") and not line.startswith("### How to Use"):
            current_category = line.replace("### ", "").strip()
            continue

        # サイト情報（- [**Name**](url) - Description）
        if current_category and line.startswith("- [**"):
            # 正規表現でパース
            match = re.match(
                r'- \[\*\*(.+?)\*\*\]\((.+?)\) - (.+)',
                line
            )

            if match:
                name = match.group(1)
                github_url = match.group(2)
                description = match.group(3)

                # GitHub URLからサイト名（フォルダ名）を抽出
                # 例: https://github.com/.../tree/main/design-md/claude/
                site_match = re.search(r'/design-md/(.+?)/?$', github_url)
                if site_match:
                    folder_name = site_match.group(1)

                    # サイトのURLを推測（フォルダ名から）
                    # 多くの場合、フォルダ名がそのままドメインになる
                    site_url = f"https://{folder_name}"

                    sites.append({
                        "name": name,
                        "folder": folder_name,
                        "url": site_url,
                        "category": current_category,
                        "description": description,
                        "auto_update": True
                    })

    return sites


def generate_sites_yaml():
    """sites.yamlを生成"""
    sites = parse_readme()

    # YAML構造を作成
    sites_data = {
        "sites": sites
    }

    output_path = Path(__file__).parent / "sites.yaml"

    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(
            sites_data,
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120
        )

    print(f"✅ sites.yaml を生成しました")
    print(f"📝 {len(sites)} サイトを登録")
    print(f"📍 場所: {output_path}")
    print()
    print("⚠️  注意: URLは推測値です。各サイトの正確なURLを手動で確認・修正してください")


if __name__ == "__main__":
    generate_sites_yaml()
