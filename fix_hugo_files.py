import os
import re

# 配置你的博客文章路径
POSTS_DIR = "./content/posts"

def fix_markdown_files(directory):
    # 1. 匹配开头没有换行的 ---
    front_matter_pattern = re.compile(r'^---([a-zA-Z])')
    
    # 2. 匹配重复拼接的币安链接
    # 查找类似 ref=BTC45/zh-CN/join?ref=BTC45 的模式
    binance_url_pattern = re.compile(r'(ref=[A-Z0-9]+)/zh-CN/join\?ref=[A-Z0-9]+')

    count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 执行修复
            new_content = front_matter_pattern.sub(r'---\n\1', content)
            new_content = binance_url_pattern.sub(r'\1', new_content)

            # 如果内容有变化，则写回文件
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 已修复: {filename}")
                count += 1

    print(f"\n🚀 搞定！共处理了 {count} 个文件。现在你可以直接 git push 了。")

if __name__ == "__main__":
    if os.path.exists(POSTS_DIR):
        fix_markdown_files(POSTS_DIR)
    else:
        print(f"❌ 找不到路径: {POSTS_DIR}，请检查脚本运行位置。")