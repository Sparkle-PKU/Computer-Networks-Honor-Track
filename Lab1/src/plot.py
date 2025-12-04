import matplotlib.pyplot as plt

# 从txt文件读取数据
def read_floats_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # 去除空白字符并转换为float
            stripped_line = line.strip()
            if stripped_line:  # 确保不是空行
                try:
                    data.append(float(stripped_line))
                except ValueError:
                    print(f"警告: 无法将 '{stripped_line}' 转换为float，已跳过")
    return data

# 主程序
if __name__ == "__main__":
    # 替换为你的txt文件路径
    filename = 'output.txt'  
    
    try:
        # 读取数据
        data = read_floats_from_file(filename)
        
        if not data:
            print("文件为空或没有有效数据")
        else:
            # 创建折线图
            plt.figure(figsize=(10, 6))  # 设置图形大小
            plt.plot(data, marker='o', linestyle='-', color='b')  # 绘制折线图
            
            # 添加标题和标签
            plt.title('VAMF Scores', fontsize=14)
            plt.xlabel('Frame Number', fontsize=12)
            plt.ylabel('VMAF Score', fontsize=12)
            
            # 显示网格
            plt.grid(True, linestyle='--', alpha=0.7)
            
            # 显示图形
            plt.show()
            
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 未找到")
    except Exception as e:
        print(f"发生错误: {e}")