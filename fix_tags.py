import os
import re

# 配置您的文章所在目录
directory = './content'

# 【核心修改】匹配 **纯大写字母和数字**。
# 这样能精准抓到 **S123789** 或 **BIN8888**，而完美避开 **官方注册链接** 等中文加粗词。
pattern = re.compile(r'\*\*([A-Z0-9]+)\*\*')

# 替换格式：红字 + 黄底 + 加粗
replacement = r'<span style="color:red; background-color:yellow; font-weight:bold; padding:0 4px;">\1</span>'

modified_count = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 如果找到了符合条件的邀请码
            if pattern.search(content):
                new_content = pattern.sub(replacement, content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 已成功升级黄底红字高亮: {filepath}")
                modified_count += 1

print(f"\n🎉 处理完成！共为您修改了 {modified_count} 个文件。")