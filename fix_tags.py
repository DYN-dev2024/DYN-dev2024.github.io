import os
import re

# 配置您的文章所在目录，通常是 content 文件夹
directory = './content'

# 匹配 <b style="color:red;">内容</b>，并提取出里面的“内容”
pattern = re.compile(r'<b style="color:red;">(.*?)</b>')

# 替换格式：这里默认替换为标准 Markdown 的加粗语法 **内容**
replacement = r'**\1**'

modified_count = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            # 读取文件内容
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 检查是否包含需要替换的内容
            if pattern.search(content):
                new_content = pattern.sub(replacement, content)
                
                # 写回修改后的内容
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"已修复: {filepath}")
                modified_count += 1

print(f"\n处理完成！共修改了 {modified_count} 个文件。")